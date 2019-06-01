from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
	# login
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]
		if username and password:
			try:
				#user = User.objects.filter(Q(username=username)|Q(email=email)).get()
				auth = authenticate(username=username, password=password)
				if auth is not None and auth.is_active:
					login(request, auth)
					print(auth)
					return redirect("/")
			except User.DoesNotExist:
				messages.error(request, "Invalid Username or Password")
	return render(request, "login.html", {})

def logout_view(request):
	logout(request)
	return redirect("/")