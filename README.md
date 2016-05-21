# lotube

## Requeriments

- Python 2.7.5

## Installation

### Source code
 
```
git clone https://github.com/lotube/lotube
```

### Install dependencies

There is currently no production specific version, thereby you should install
 the developers requirements.

```
pip install -r requirements.txt
```

#### Developers

```
pip install -r requirements_dev.txt
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