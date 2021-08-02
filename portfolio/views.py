from django.shortcuts import render
from django.urls import reverse

from portfolio.models import Projects, Skills


def home_page(request):
    context = {"skills": [], "about_us": "blablabla"}
    return render(request, "portfolio/home_page.html", context=context)
