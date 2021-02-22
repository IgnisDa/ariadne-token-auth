import glob

from ariadne import (
    load_schema_from_path,
    make_executable_schema,
    snake_case_fallback_resolvers,
)
from django.conf import settings
from example_app.api import resolvers as example_app_resolvers

type_defs = [
    load_schema_from_path(f)
    for f in glob.glob(str(settings.BASE_DIR / "*" / "api" / "schema" / "*.graphql"))
]
schema = make_executable_schema(
    type_defs,
    [example_app_resolvers.query, example_app_resolvers.mutation],
    snake_case_fallback_resolvers,
)
