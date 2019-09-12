# An Interview Questions for Python Junior/Senior Developer

### Q1. What is the difference between list and tuples (Say two difference)?
| List 								 		| Tuples 															 |
|-------------------------------------------|--------------------------------------------------------------------|
|Lists are mutable i.e they can be edited.  | Tuples are immutable (tuples are lists which can’t be edited).     |
|Lists are slower than tuples.              | Tuples are faster than list. 										 |
|Syntax: `list_1 = [10, ‘Chelsea’, 20]`     | Syntax: `tup_1 = (10, ‘Chelsea’ , 20)`                             |

### Q2. What are the key features of Python (Say two features)?
* Python is an interpreted language. That means that, unlike languages like C and its variants, Python does not need to be compiled before it is run. Other interpreted languages include PHP and Ruby.
* Python is dynamically typed, this means that you don’t need to state the types of variables when you declare them or anything like that. You can do things like `x=111` and then `x="I'm a string"` without error
* Python is well suited to object orientated programming in that it allows the definition of classes along with composition and inheritance. Python does not have access specifiers (like C++’s public, private), the justification for this point is given as “we are all adults here”
* In Python, functions are first-class objects. This means that they can be assigned to variables, returned from other functions and passed into functions. Classes are also first class objects
* Writing Python code is quick but running it is often slower than compiled languages. Fortunately，Python allows the inclusion of C based extensions so bottlenecks can be optimized away and often are. The numpy package is a good example of this, it’s really quite quick because a lot of the number crunching it does isn’t actually done by Python
* Python finds use in many spheres – web applications, automation, scientific modelling, big data applications and many more. It’s also often used as “glue” code to get other languages and components to play nice.

### Explain what Flask is and its benefits (Say two benefits)?
Flask is a web microframework for Python based on “Werkzeug, Jinja2 and good intentions” BSD license. Werkzeug and Jinja2 are two of its dependencies. This means it will have little to no dependencies on external libraries.  It makes the framework light while there is a little dependency to update and fewer security bugs.

A session basically allows you to remember information from one request to another. In a flask, a session uses a signed cookie so the user can look at the session contents and modify. The user can modify the session if only it has the secret key Flask.secret_key.

### Q4. What does this mean: `*args`, `**kwargs`? And why would we use it?
We use `*args` when we aren’t sure how many arguments are going to be passed to a function, or if we want to pass a stored list or tuple of arguments to a function. `**kwargs` is used when we don’t know how many keyword arguments will be passed to a function, or it can be used to pass the values of a dictionary as keyword arguments. The identifiers args and kwargs are a convention, you could also use `*bob` and `**billy` but that would not be wise.

### Q5. What is lambda in Python?
It is a single expression anonymous function often used as inline function.

### Q6. Explain how can you make a Python Script executable on Unix?
To make a Python Script executable on Unix, you have two things to do:
* Script file's mode must be executable by converting file mode `chmod +x filename.py`.
* The first line must begin with # like `#!/usr/bin/python`.

### Q7. how to extract distinct list from  [1, 2, 2, 4, 9, 9] ?
```python
list(set([1, 2, 4, 9]))
```