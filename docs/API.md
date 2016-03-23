# API /api/

The REST API provides programmatic access to read and write LOTube data.<br>
Responses are available in both JSON and XML formats (append the desired format 
at the end).

URL example:

`/api/users.json`

## Users

### GET users

Returns a collection of users.

```json
    {
     "page_info": {
        "total_results": 100,
        "results_page": 100
     },
     "items": [
        { 
          "id": 1,
          "username": "tommy33",
          "first_name": "Tommy",
          "last_name": "Sun",
          "created_at": "2016-03-23T10:37:04.873Z",
          "last_login": "2016-03-23T10:37:04.873Z",
          "is_staff": false,
          "is_active": true
        }
     ]
    }
```

### GET users/:username
```json
    {
     "id": 1,
     "username": "tommy33",
     "first_name": "Tommy",
     "last_name": "Sun",
     "created_at": "2016-03-23T10:37:04.873Z",
     "last_login": "2016-03-23T10:37:04.873Z"
    }
```
