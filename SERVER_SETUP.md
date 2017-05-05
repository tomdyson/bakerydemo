# Server set up

Ubuntu 17.04

- sudo apt-get install nginx
- sudo apt-get install python-pip
- git clone https://github.com/tomdyson/entity-tagging-demo.git
- cd entity-tagging-demo
- pip install -r requirements/base.txt
- cp bakerydemo/settings/local.py.example bakerydemo/settings/local.py
- echo "DJANGO_SETTINGS_MODULE=bakerydemo.settings.local" > .env
- ./manage.py migrate