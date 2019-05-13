from django.shortcuts import render, HttpResponse

from .models import Post

import json

def home_view(request):
	posts = Post.objects.filter(is_active=True)
	return render(request, "home.html", dict(posts=posts))

def sample_api(request):
	dicts = {
		"name": "Jade",
		"age": 24,
	}
	return HttpResponse(json.dumps(dicts), content_type="application/json", status=404)