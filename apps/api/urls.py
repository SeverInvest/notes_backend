from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from apps.api.views import ResultViewSet

users_urls = [
    path("login/", views.obtain_auth_token, name="user-login"),
    # path("me/", MeView.as_view(), name="user-me"),
]

router = DefaultRouter()
router.register('results', ResultViewSet)

urlpatterns = [
    path('users/', include(users_urls)),
    path('', include(router.urls)),
]
