import random
from django.shortcuts import render
from django.views.generic import TemplateView


def random_number():
    return random.randint(1, 100) + random.randint(100, 200)


def home(request):
    number = random_number()
    return render(request, "home.html", {"number": number})


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["number"] = random_number()
        return context
