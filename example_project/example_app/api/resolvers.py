from ariadne import MutationType, QueryType
from ariadne_token_auth.api import resolvers
from ariadne_token_auth.decorators import login_required

query = QueryType()
mutation = MutationType()

auth_mutation = MutationType()

auth_mutation.set_field("getAuthToken", resolvers.get_auth_token)
auth_mutation.set_field("deleteAuthToken", resolvers.delete_auth_token)

auth_type_definitions = [
    resolvers.type_defs,
]


@query.field("testQuery")
@login_required
def test_query(self, info, *args, **kwargs):
    return {"user": info.context.get("request").user}


@mutation.field("testMutation")
@login_required
def test_mutation(self, info, *args, **kwargs):
    return {"user": info.context.get("request").user}
