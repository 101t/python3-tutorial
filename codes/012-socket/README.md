# Socket with Python

## Required

    Python 3.6 or later.

## Content

1. Echo Client and Server
2. Multi-Connection Client and Server
3. Advanced Application Client and Server

### Echo Client and Server

In Terminal (server):
```
python server.py
```

In Another Terminal (client):
```
python client.py
```

### Multi-Connection Client and Server

In Terminal (server):
```
python server.py 0.0.0.0 5000
```

In Another Terminal (client):
```
python client.py 0.0.0.0 5000 3
```

### Advanced Application Client and Server

In Terminal (server):
```
python app-server.py 0.0.0.0 5000
```

In Another Terminal (client):
```
python app-client.py 0.0.0.0 5000 search morpheus

python app-client.py 0.0.0.0 5000 search 🐶

python app-client.py 0.0.0.0 5000 binary 😃
```

## Contribute

[Socket with Real Python](https://realpython.com/python-sockets/)
[Source Code](https://github.com/realpython/materials/tree/master/python-sockets-tutorial)