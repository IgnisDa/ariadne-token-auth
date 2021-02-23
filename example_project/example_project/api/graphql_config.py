import glob

from ariadne import (
    load_schema_from_path,
    make_executable_schema,
    snake_case_fallback_resolvers,
)
from django.conf import settings
from example_app.api import resolvers as example_app_resolvers

# assuming all our schema is defined in files which match the following pattern,
# we can use python `glob` to import these files dynamically, so that we don't have
# to specify each file here specifically.
type_defs = [
    load_schema_from_path(f)
    for f in glob.glob(str(settings.BASE_DIR / "*" / "api" / "schema" / "*.graphql"))
]
type_defs.extend(example_app_resolvers.auth_type_definitions)

schema = make_executable_schema(
    type_defs,
    [
        example_app_resolvers.query,
        example_app_resolvers.mutation,
        example_app_resolvers.auth_mutation,
    ],
    snake_case_fallback_resolvers,
)
