from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from main.send_email import pyMail, USER
from main.article.models import Article, Tag

ADMIN_MAIl = "email@example.com"

def home_view(request):
    articles = Article.objects.filter(is_active=True, state=Article.APPROVED)[:20]
    return render(request, "content/home.html", dict(articles=articles))

def contact_view(request):
    if request.POST:
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        pyMail(subject=subject, from_mail=USER, maillist=[email, ADMIN_MAIl], message=message)
        messages.success(request, 'Your message has been sent successfully!')
        return redirect(reverse("contact_view"))
    return render(request, "content/contact.html", {})

def about_view(request):
    return render(request, "content/about.html", {})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, "content/article_detail.html", dict(article=article))