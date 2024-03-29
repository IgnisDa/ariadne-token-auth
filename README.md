# ariadne-token-auth

A django app to implement token based authentication in projects which use
[ariadne](https://ariadnegraphql.org/).

## Summary

- [ariadne-token-auth](#ariadne-token-auth)
  - [Summary](#summary)
    - [Installing](#installing)
  - [Using the package](#using-the-package)
    - [Example Project](#example-project)
    - [Setup](#setup)
    - [Migrations](#migrations)
    - [Schema](#schema)
    - [Protecting Views](#protecting-views)
    - [Configuration](#configuration)
    - [Bonus](#bonus)
  - [Contributing](#contributing)
  - [Versioning](#versioning)
  - [Authors](#authors)
  - [License](#license)
  - [Acknowledgements](#acknowledgements)
  - [Others](#others)

### Installing

The package can be downloaded from [PyPI](https://pypi.org/project/ariadne-token-auth/) or
[github](https://github.com/IgnisDa/ariadne-token-auth) repository.

```bash
pip install ariadne-token-auth
```

Or using [poetry](https://python-poetry.org/)

```bash
poetry add ariadne-token-auth
```

## Using the package

### Example Project

You can have a look at the [example project](./example_project) for a fully
working project. [Habitrac](https://github.com/IgnisDa/habitrac) is also a production
website which uses this package to implement authentication.

### Setup

Include the `AuthTokenMiddleware` in your `MIDDLEWARE` settings.

```python
MIDDLEWARE = [
    # Other middleware
    "ariadne_token_auth.middleware.AuthTokenMiddleware",
]
```

Include the `AuthTokenBackend` in your `AUTHENTICATION_BACKENDS` settings.

```python
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "ariadne_token_auth.backends.AuthTokenBackend",
)
```

Finally add `ariadne_token_auth` to your `INSTALLED_APPS`.

```python
INSTALLED_APPS = [
    # other apps
    'ariadne_token_auth',
]
```

### Migrations

Next, run `python manage.py migrate` to commit the auth-token model to your database.

### Schema

Add the relevant mutations to your GraphQL schema.

```python
from ariadne import MutationType, make_executable_schema
from ariadne_token_auth.api import resolvers

auth_mutation = MutationType()

auth_mutation.set_field("getAuthToken", resolvers.get_auth_token)
auth_mutation.set_field("deleteAuthToken", resolvers.delete_auth_token)
type_defs = """
  type Mutation {
    getAuthToken(identifier: String!, password: String!): AuthTokenPayload!
    deleteAuthToken(token: String!): DeleteTokenPayload!
}
"""

schema = make_executable_schema([type_defs, resolvers.type_defs], auth_mutation)
```

- `getAuthToken` to authenticate an existing user and obtain a corresponding token. The
  resolver uses the user model's `USERNAME_FIELD` which by default is `username`. However
  it will work with other `USERNAME_FIELD`s just fine, for example when the default user
  identifier is `email` instead of `username`. The [example project](#example-project) does
  this by defining a
  [custom user model](https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#specifying-a-custom-user-model).

  ```graphql
  mutation getAuthToken($identifier: String!, $password: String!) {
    getAuthToken(identifier: $identifier, password: $password) {
      error
      auth {
        token
      }
    }
  }
  ```

  If authentication is successful, you can obtain the auth-token from
  `response.data.getAuthToken.auth.token`, and if it is unsuccessful, errors will
  be present in `response.data.getAuthToken.error`.

- `deleteAuthToken` to delete a logged in user using the above token.

  ```graphql
  mutation deleteAuthToken($token: String!) {
    deleteAuthToken(token: $token) {
      status
      error
    }
  }
  ```

  If the token was correct and deletion was successful, the value of
  `response.data.deleteAuthToken.status` will be set to `true` (or it's equivalent in your
  frontend language). Otherwise, the error will be present in
  `response.data.deleteAuthToken.error` and `response.data.deleteAuthToken.status` will be
  set to `false`.

### Protecting Views

You can use the `login_required` decorator to protect your graphql queries from
non-authenticated users.

```python
from ariadne import QueryType
from ariadne_token_auth.decorators import login_required

@query.field("testQuery")
@login_required
def test_query(self, info, *args, **kwargs):
    return {"user": info.context.get("request").user}
```

### Configuration

Settings specific to ariadne-token-auth are stored in the `ARIADNE_TOKEN_AUTH` dictionary
in `settings.py` file. The defaults can be seen in [utils.py](./ariadne_token_auth/utils.py)
file. They can be configured as follows:

```python
# settings.py
ARIADNE_TOKEN_AUTH = {
    'TOKEN_NAME': 'myBearer', # case insensitive
    'TOKEN_LENGTH': 15
}
```

With the above settings, you will have to send requests in the following fashion (example
uses `curl`, but the basic premise stays the same).

```bash
curl 'http://127.0.0.1:8000/graphql/' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: myBearer 8496fda8dedad2235921693717c8dc' \
      --data-binary '{"query":"query {\n  testQuery {\n    user\n  }\n}"}'
```

### Bonus

You can find a very easy way to add your `*.graphql` files to the django auto-reloader
[here](https://github.com/IgnisDa/ariadne-token-auth/blob/main/example_project/example_app/apps.py#L6).

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code
of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions
available, see the [tags on this
repository](https://github.com/PurpleBooth/a-good-readme-template/tags).

## Authors

See also the list of [contributors](contributors.md) who participated in this project.

## License

This project is licensed under the
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) - see the
[LICENSE.md](LICENSE.md) file for details

## Acknowledgements

1. **django-token**: Model definitions, middleware and authentication backends adapted from
   [django-tokens](https://github.com/jasonbeverage/django-token) package.
2. **ariadne-jwt**: Exceptions, and decorators adapted from
   [ariadne-jwt](https://github.com/Usama0121/ariadne-jwt) package.

## Others

Project bootstrapped using [cookiecutter](https://github.com/IgnisDa/project-cookiecutter)
by IgnisDa.
