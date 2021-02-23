from ariadne.contrib.django.views import GraphQLView
from django.contrib import admin
from django.urls import path

from example_project.api.graphql_config import schema

urlpatterns = [
    path("admin/", admin.site.urls),
    path("graphql/", GraphQLView.as_view(schema=schema), name="graphql"),
]
