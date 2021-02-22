from ariadne_token_auth.decorators import login_required
from django.http import JsonResponse


@login_required
def test_view(request):
    return JsonResponse({"message": "The view worked successfully!", "status": True})
