from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import TextTestimonial, Tag
from django.forms import ModelForm


class ArticleCreate(ModelForm):
    class Meta:
        model = TextTestimonial
        fields = ["text", "author_gender", "author_age", "tags"]


class HomePageView(ListView):
    template_name = "pages/home.html"
    model = TextTestimonial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        context["ArticleCreate"] = ArticleCreate
        return context

    def get_queryset(self):
        filter_val = self.request.GET.get("date")
        if not filter_val:
            return self.model.objects.all()
        else:
            return self.model.objects.filter(creation_date=filter_val)


class ArticleView(DetailView):
    model = TextTestimonial


class ByTagView(ListView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = get_object_or_404(Tag, pk=self.kwargs["pk"])
        context["tags"] = Tag.objects.all()
        return context

    def get_queryset(self):
        return TextTestimonial.objects.filter(tags__pk=self.kwargs["pk"])


def manage_articles(request):
    if request.method == "POST":
        form = ArticleCreate(request.POST)
        if form.data["text"]:
            form.save()
    return redirect("home")
