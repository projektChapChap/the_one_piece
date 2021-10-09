from django.urls import path
from .views import PostViews

urlpatterns = [
    path('v1/', PostViews.as_view()),
    path('v1/<slug:tarehe>', PostViews.as_view())
]