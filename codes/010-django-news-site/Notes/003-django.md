# Small Notes

### For Models:

1. QuerySet (it's a model list as django featured)
2. QuerySet<ModelName> e.g QuerySet<User>, QuerySet<Post>, QuerySet<Group>

### Django User has 3 main roles:

1. `is_superuser` for administration (admin)
2. `is_staff` as middle user or editor or moderator
3. `is_active` as lowest level of user e.g customer/student

These take boolean value `True / False`.

### Why detailed view used slug:

* /post/hello-news/ this highly recommended for **SEO friendly** (e.g google search engine)
* /post/43/ this is not recommended


### In Django for translation and datetime format we have:

* for translation you may use **i18n** tag in HTML templates
* for datetime formatting based on Geolocation (Istanbul/Europ) 24.02.2019 (NYC) 2019/24/02 (London) 2019/02/24 here we use **i10n**

### In view in Django we have request parameter:

1. this is usefull to check GET/POST incoming parameters from HTML Form.
2. this is good to make sure this request if authenticated or not.
3. in request we have request.GET/request.POST as dictionary called (QueryDict)