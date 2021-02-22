from ariadne.contrib.django.views import GraphQLView
from django.contrib import admin
from django.urls import include, path

from example_project.api.graphql_config import schema

urlpatterns = [
    path("admin/", admin.site.urls),
    path("graphql/", GraphQLView.as_view(schema=schema), name="graphql"),
    path("", include("example_app.urls")),
]
