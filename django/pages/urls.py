from django.urls import path

from .views import HomePageView, ByTagView, ArticleView, AboutView, manage_articles

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("tags/<int:pk>/", ByTagView.as_view(), name="by_tag"),
    path("article/<int:pk>/", ArticleView.as_view(), name="article"),
    path("article/add/", manage_articles, name="article-add"),
    path("about", AboutView.as_view(), name="about"),
]
