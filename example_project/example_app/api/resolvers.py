from ariadne import MutationType, QueryType
from ariadne_token_auth.decorators import login_required_ariadne

query = QueryType()
mutation = MutationType()


@query.field("testQuery")
@login_required_ariadne
def test_query(self, info, *args, **kwargs):
    return "The view worked successfully!"
