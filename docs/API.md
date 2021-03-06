# API /api/v1/

The REST API provides programmatic access to read and write LOTube data.<br>
Responses are available in both JSON and XML formats (append the desired format 
at the end).

URL example:

`/api/v1/users.json`

## Table of Contents

- [Users](#users)
- [Videos](#videos)

## Users

### GET users

Returns a collection of users.

```json
    {
     "type": "user_list",
     "page_info": {
        "total_results": 1,
        "results_page": 10,
        "page": 1
     },
     "links": {
        "self": "http://127.0.0.1/api/v1/users.json?page=1",
        "first": "http://127.0.0.1/api/v1/users.json?page=1",
        "previous": "",
        "next": "",
        "last": "http://127.0.0.1/api/v1/users.json?page=1"
     },
     "items": [
        {
          "type": "user",
          "id": 1,
          "href": "http://127.0.0.1/api/v1/users/tommy33.json",
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

If exists, it returns the user details of the :username provided.

```json
    {
      "type": "user",
      "id": 1,
      "href": "http://127.0.0.1/api/v1/users/tommy33.json",
      "username": "tommy33",
      "first_name": "Tommy",
      "last_name": "Sun",
      "created_at": "2016-03-23T10:37:04.873Z",
      "last_login": "2016-03-23T10:37:04.873Z",
      "is_staff": false,
      "is_active": true
    }
```

## Videos

### GET videos

**id**: LOTube unique identifier.

**id_source**: LOTube identifier if `source="lotube"`, else source's unique 
identifier.

Other data such as user, title or description will be relative to the source.

#### Params

_Optional parameters_

**user**: Published by user (i.e. admin)

**title**: Video title contains (i.e. hello)

**tags**: Video has tags (coma separated values) (i.e. games,fps)

#### Sample

```json
    {
     "type": "video_list",
     "page_info": {
        "total_results": 1,
        "results_page": 10,
        "page": 1
     },
     "links": {
        "self": "http://127.0.0.1/api/v1/videos.json?page=1",
        "first": "http://127.0.0.1/api/v1/videos.json?page=1",
        "previous": "",
        "next": "",
        "last": "http://127.0.0.1/api/v1/videos.json?page=1"
     },
     "items": [
        {
          "type": "video",
          "id": {
            "id": 1,
            "id_source": 1
          },
          "href": "http://127.0.0.1/api/v1/videos/1.json",
          "source": "lotube",
          "user": "tommy33",
          "title": "Hello world",
          "description": "My hello world video",
          "duration" : 10,
          "created_at": "2016-03-23T10:37:04.873Z",
          "modified_at": "2016-03-23T10:37:04.873Z",
          "filename": "1.flv",
          "thumbnail": {
            "height": 0,
            "width": 0,
            "url": "http://www.example.com/thumbnail.jpg"
          },
          "tags": [
            "python"
          ]
        }
     ]
    }
```

### GET videos/:id

If exists, it returns the video details of the provided video :id.

See [GET videos](#get-videos)

```json
    {
      "type": "video",
      "id": {
        "id": 1,
        "id_source": 1
      },
      "href": "http://127.0.0.1/api/v1/videos/1.json",
      "source": "lotube",
      "user": "tommy33",
      "title": "Hello world",
      "description": "My hello world video",
      "duration" : 10,
      "created_at": "2016-03-23T10:37:04.873Z",
      "modified_at": "2016-03-23T10:37:04.873Z",
      "filename": "1.flv",
      "thumbnail": {
        "height": 0,
        "width": 0,
        "url": "http://www.example.com/thumbnail.jpg"
      },
      "tags": [
        "python"
      ]
    }
```

### GET videos/user/:username

Returns a collection of videos uploaded by the provided User :username.

See [GET videos](#get-videos)

```json
    {
     "type": "video_list",
     "page_info": {
        "total_results": 1,
        "results_page": 10,
        "page": 1
     },
     "links": {
        "self": "http://127.0.0.1/api/v1/videos/user/tommy33.json?page=1",
        "first": "http://127.0.0.1/api/v1/videos/user/tommy33.json?page=1",
        "previous": "",
        "next": "",
        "last": "http://127.0.0.1/api/v1/videos/user/tommy33.json?page=1"
     },
     "items": [
        {
          "type": "video",
          "id": {
            "id": 1,
            "id_source": 1
          },
          "href": "http://127.0.0.1/api/v1/videos/1.json",
          "source": "lotube",
          "user": "tommy33",
          "title": "Hello world",
          "description": "My hello world video",
          "duration" : 10,
          "created_at": "2016-03-23T10:37:04.873Z",
          "modified_at": "2016-03-23T10:37:04.873Z",
          "filename": "1.flv",
          "thumbnail": {
            "height": 0,
            "width": 0,
            "url": "http://www.example.com/thumbnail.jpg"
          },
          "tags": [
            "python"
          ]
        }
     ]
    }
```

### GET videos/tags

Returns a collection of all tags.

See [GET videos](#get-videos)

```json
    {
     "type": "tag_list",
     "page_info": {
        "total_results": 2,
        "results_page": 10,
        "page": 1
     },
     "links": {
        "self": "http://127.0.0.1/api/v1/videos/tags.json?page=1",
        "first": "http://127.0.0.1/api/v1/videos/tags.json?page=1",
        "previous": "",
        "next": "",
        "last": "http://127.0.0.1/api/v1/videos/tags.json?page=1"
     },
     "items": ["python", "django"]
    }
```

### GET videos/tags/:coma_separated_tags

Returns a collection of videos containing at least one of the following
:coma_separated_tags.

See [GET videos](#get-videos)

```json
    {
     "type": "video_list",
     "page_info": {
        "total_results": 1,
        "results_page": 10,
        "page": 1
     },
     "links": {
        "self": "http://127.0.0.1/api/v1/videos/tags/python.json?page=1",
        "first": "http://127.0.0.1/api/v1/videos/tags/python.json?page=1",
        "previous": "",
        "next": "",
        "last": "http://127.0.0.1/api/v1/videos/tags/python.json?page=1"
     },
     "items": [
        {
          "type": "video",
          "id": {
            "id": 1,
            "id_source": 1
          },
          "href": "http://127.0.0.1/api/v1/videos/1.json",
          "source": "lotube",
          "user": "tommy33",
          "title": "Hello world",
          "description": "My hello world video",
          "duration" : 10,
          "created_at": "2016-03-23T10:37:04.873Z",
          "modified_at": "2016-03-23T10:37:04.873Z",
          "filename": "1.flv",
          "thumbnail": {
            "height": 0,
            "width": 0,
            "url": "http://www.example.com/thumbnail.jpg"
          },
          "tags": [
            "python"
          ]
        }
     ]
    }
```

### GET videos/:id/analytics

Returns video analytics (such as views) of provided Video :id.

```json
    {
      "type": "video_analytic",
      "href": "http://127.0.0.1/api/v1/videos/1/rating.json",
      "video_id": 1,
      "views": {
        "total_views": 1,
        "unique_views": 1
      },
      "shares": 0
    }
```

### GET videos/:id/rating

Returns video rating of the provided Video :id.

```json
    {
      "type": "video_rating",
      "href": "http://127.0.0.1/api/v1/videos/1/rating.json",
      "video_id": 1,
      "upvotes": 0,
      "downvotes": 0
    }
```

### GET videos/:id/comments

Returns a collection of comments of the provided Video :id.

**id**: LOTube unique identifier of the comment

**id_source**: LOTube identifier of the comment if `source="lotube"`,
else source's unique identifier.

```json
    {
     "type": "comment_list",
     "page_info": {
        "total_results": 1,
        "results_page": 10,
        "page": 1
     },
     "links": {
        "self": "http://127.0.0.1/api/v1/videos/1/comments.json?page=1",
        "first": "http://127.0.0.1/api/v1/videos/1/comments.json?page=1",
        "previous": "",
        "next": "",
        "last": "http://127.0.0.1/api/v1/videos/1/comments.json?page=1"
     },
     "items": [
        {
          "type": "comment",
          "video_id": 1,
          "id": 1,
          "href": "http://127.0.0.1/api/v1/videos/1/comments/1.json",
          "user": "tommy33",
          "content": "I like my own video!",
          "created_at": "2016-03-23T10:37:04.873Z",
          "modified_at": "2016-03-23T10:37:04.873Z",
          "is_removed": false
        }
     ]
    }
```

### GET videos/:id/comments/:comment_id

If exists, it returns the comment details of the video :id.

```json
    {
      "type": "comment",
      "video_id": 1,
      "id": 1,
      "href": "http://127.0.0.1/api/v1/videos/1/comments/1.json",
      "user": "tommy33",
      "content": "I like my own video!",
      "created_at": "2016-03-23T10:37:04.873Z",
      "modified_at": "2016-03-23T10:37:04.873Z",
      "is_removed": false
    }
```
