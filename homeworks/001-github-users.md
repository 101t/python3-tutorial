# Github Users Homework

Enter username then get response as json from github using github public api then save it into JSON file

```
users/
├── 101t.json
├── ahmet.json
├── cd.json
└── fatih.json
```
### How it works?

1. wrint response in json file into directory `users/`
2. reading file and print it in screen
3. this app should be interactive CLI using `input()` and `print()` functions

### Required knowledges:

1. requests should be installed
2. file read/write `open()`.
3. Github public api.

### Description:
* Create **CLI interactive application** using Python3 that using `input()` and `print()`.
* User can enter Github username then App will return user information as JSON format then will save this response into file under folder called `users/`, also user can browse saved file by typing username.