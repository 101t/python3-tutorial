### Welcome to Flask Project

Make sure `virtualenv` installed on your computer by:

```bash
sudo apt install python3-pip
pip install virtualenv --user
```

Installing Project on Unix (Linux/MacOS)

```bash
cd 009-flask-config/

virtualenv -p python3 env

source env/bin/activate

pip install -r requirements.pip

```

Then copy `Sample.env` to `.env`
```bash
cp -rf Sample.env .env
```

Then we need to export `GLOABL VARIABLE` to configure class

```bash
export APP_SETTINGS="config.DevelopmentConfig"

echo $APP_SETTINGS
```

To run this application

```bash
python app.py
```