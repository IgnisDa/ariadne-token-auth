from django.http import JsonResponse
from django_tokens.decorators import login_required


@login_required
def test_view(request):
    return JsonResponse({"message": "The view worked successfully!", "status": True})
