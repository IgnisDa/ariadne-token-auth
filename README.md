# ariadne-token-auth

A django app to implement token based authentication in projects which use
[ariadne](https://ariadnegraphql.org/).

## Summary

- [ariadne-token-auth](#ariadne-token-auth)
  - [Summary](#summary)
    - [Installing](#installing)
  - [Using the package](#using-the-package)
    - [Settings](#settings)
    - [Schema](#schema)
  - [Running the tests](#running-the-tests)
    - [Break down into end to end tests](#break-down-into-end-to-end-tests)
    - [And coding style tests](#and-coding-style-tests)
  - [Contributing](#contributing)
  - [Versioning](#versioning)
  - [Authors](#authors)
  - [License](#license)
  - [Acknowledgements](#acknowledgements)
  - [Others](#others)

### Installing

The package is live on [PyPI](https://pypi.org/project/ariadne-token-auth/) and can be
installed using `pip`

```bash
pip install ariadne-token-auth
```

Or using [poetry](https://python-poetry.org/)

```bash
poetry add ariadne-token-auth
```

## Using the package

**NOTE**: You can have a look at the [example project](./example_project) for a fully
working project. [Habitrac](https://github.com/IgnisDa/habitrac) is also a production
website which uses this package to implement authentication.

### Settings

Include the `AuthTokenMiddleware` in your `MIDDLEWARE` settings.

```python
MIDDLEWARE = [
    # Other middleware
    "ariadne_token_auth.middleware.AuthTokenMiddleware",
]
```

Include the `AuthTokenBackend` in your `BACKENDS` settings.

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
    'ariadne_token_auth
]
```

### Schema

Hello

## Running the tests

The tests for this package have been written using
[pytest](https://docs.pytest.org/en/stable/). You can run them using the following command

```bash
pytest
```

### Break down into end to end tests

Explain what these tests test and why

    Give an example

### And coding style tests

Explain what these tests test and why

    Give an example

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
