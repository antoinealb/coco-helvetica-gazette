from django.urls import path

from .views import HomePageView, ByTagView, ArticleView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("tags/<int:pk>/", ByTagView.as_view(), name="by_tag"),
    path("article/<int:pk>/", ArticleView.as_view(), name="article"),
]
