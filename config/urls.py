"""Waitress URL Configuration"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path(
        route='',
        view=csrf_exempt(GraphQLView.as_view(graphiql=settings.DEBUG)),
        name='graphql'
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
