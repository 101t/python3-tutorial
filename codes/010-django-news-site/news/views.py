from django.shortcuts import render, HttpResponse

import json
# Create your views here.

def news_view(request):
	return HttpResponse("<h3>Hello News</h3>")

def news_api(request):
	dicts = {
		"name": "Mohammed",
		"age": 24,
	}
	return HttpResponse(json.dumps(dicts), content_type="application/json", status=404)