from django.contrib import admin
from django.urls import path, include

from theme.views import change_theme

default_patterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("agenda", include("schedule.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]

config_patterns = [
    path("switch-theme/", change_theme, name="change-theme"),
    path("__reload__/", include("django_browser_reload.urls")),
]


urlpatterns = default_patterns + config_patterns
