# example-project

This is a small project which uses
[ariadne-token-auth](https://github.com/IgnisDa/ariadne-token-auth) for authentication.

The main resolver is in [resolvers.py](./example_app/api/resolvers.py). The
graphql configuration is in [graphql_config.py](./example_project/api/graphql_config.py).
The schema is defined in [root.graphql](./example_project/api/schema/root.graphql) and
[types.graphql](./example_app/api/schema/types.graphql). Custom user model is defined
in [models.py](./example_app/models.py) and it's corresponding
[manager](https://docs.djangoproject.com/en/3.1/topics/db/managers/) is defined in
[managers.py](./example_app/managers.py)
