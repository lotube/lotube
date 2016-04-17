# lotube

## Requeriments

- Python 2.7.5
- Ruby _(will be used in upcoming versions)_

## Installation

### Source code
 
```
git clone https://github.com/lotube/lotube
```

### Install dependencies

```
pip install -r requirements.txt
```

The following will also be used in upcoming versions:

```
gem install sass
```

## How to run

### Environment variables

**TOKEN_YOUTUBE**: Youtube token key for the Crawler

### Create superuser(s)

```
cd lotube/;
python manage.py createsuperuser;
```

### Start the website

By default it will start in development mode 
(will be changed in upcoming versions):

```
cd lotube/;
python manage.py migrate;
python manage.py runserver;
```

Check it out at [127.0.0.1:8000](http://127.0.0.1:8000).