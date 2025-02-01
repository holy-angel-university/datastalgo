from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.tasks.views import TasksViewSet, RegisterView
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r"api/v1/tasks", TasksViewSet, basename="tasks")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/register/", RegisterView.as_view(), name="register"),
    path("api/v1/login/", obtain_auth_token, name="login"),
    path("", include(router.urls)),
]
