from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Post

from core.utils import get_query, paginate

import json

def home_view(request):
	posts = Post.objects.filter(is_active=True)
	search = request.GET.get("search")
	if search:
		entry_query = get_query(search, ("title",))
		posts = posts.filter(entry_query)
	posts = paginate(posts, per_page=24, page=request.GET.get("page", 1))
	return render(request, "home.html", dict(posts=posts))

def post_detail(request, slug):
	post = get_object_or_404(Post, slug=slug)
	return render(request, "post_detail.html", dict(post=post))

def about_view(request):
	return render(request, "about.html")

def sample_api(request):
	dicts = {
		"name": "Jade",
		"age": 24,
	}
	return HttpResponse(json.dumps(dicts), content_type="application/json", status=404)