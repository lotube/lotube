# API /api/v2/

The REST API provides programmatic access to read and write LOTube data.<br>
Responses are available in both JSON and XML formats (append the desired format
at the end).

URL example:

`/api/v2/users.json`

## Table of Contents

- [Users](#users)
- [Videos](#videos)

## Users

### GET users

Returns a collection of users.

```json
    {
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
    {
    "id": 1,
    "href": "http://127.0.0.1:8000/api/v2/users/1.json",
    "username": "admin",
    "first_name": "administrator",
    "last_name": "administrator",
    "date_joined": "2016-05-08T08:30:56.096132Z",
    "last_login": "2016-05-10T09:51:00.708211Z",
    "is_staff": true,
    "is_active": true
    }
    }
```

### GET users/:username

If exists, it returns the user details of the :username provided.

```json
    {
    "id": 1,
    "href": "http://127.0.0.1:8000/api/v2/users/1.json",
    "username": "admin",
    "first_name": "administrator",
    "last_name": "administrator",
    "date_joined": "2016-05-08T08:30:56.096132Z",
    "last_login": "2016-05-10T09:51:00.708211Z",
    "is_staff": true,
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
    "count": 4,
    "next": null,
    "previous": null,
    "results": [
    {
    "id": 2,
    "id_source": "2",
    "source": "lotube",
    "user": "http://127.0.0.1:8000/api/v2/users/2",
    "href": "http://127.0.0.1:8000/api/v2/videos/2.json",
    "title": "liketsl",
    "description": "Video testing",
    "duration": 65,
    "created": "2016-05-08T09:34:10.702075Z",
    "modified": "2016-05-08T09:34:10.702104Z",
    "filename": "1.flv",
   "thumbnail": {
        "height": 0,
        "width": 0,
        "url": "http://www.example.com/thumbnail.jpg",
   },
    "analytics": "http://127.0.0.1:8000/api/v2/videos/2/analytics",
    "tags": [
        "python"
    ],
    "comments": "http://127.0.0.1:8000/api/v2/videos/2/comments"
    }
    }
```

### GET videos/:id

If exists, it returns the video details of the provided video :id.

See [GET videos](#get-videos)

```json
   {
   "id": 5,
   "id_source": "7",
   "source": "lotube",
   "user": "http://127.0.0.1:8000/api/v2/users/3",
   "href": "http://127.0.0.1:8000/api/v2/videos/5.json",
   "title": "Lions video",
   "description": "lion video",
   "duration": 56,
   "created": "2016-05-16T12:16:35.449889Z",
   "modified": "2016-05-16T12:17:16.255752Z",
   "filename": "1.flv",
   "thumbnail": {
        "height": 0,
        "width": 0,
        "url": "http://www.example.com/thumbnail.jpg",
   },
   "analytics": "http://127.0.0.1:8000/api/v2/videos/5/analytics",
   "tags": [
       {
       "python"
       }
   ],
   "comments":"http://127.0.0.1:8000/api/v2/videos/5/comments"
   }
```

### GET videos/user/:username

Returns a collection of videos uploaded by the provided User :username.

See [GET videos](#get-videos)

```json
    {
    "count": 4,
    "next": null,
    "previous": null,
    "results": [
    {
    "id": 2,
    "id_source": "2",
    "source": "lotube",
    "user": "http://127.0.0.1:8000/api/v2/users/2",
    "href": "http://127.0.0.1:8000/api/v2/videos/2.json",
    "title": "liketsl",
    "description": "Video testing",
    "duration": 65,
    "created": "2016-05-08T09:34:10.702075Z",
    "modified": "2016-05-08T09:34:10.702104Z",
    "filename": "1.flv",
    "thumbnail": {
        "height": 0,
        "width": 0,
        "url": "http://www.example.com/thumbnail.jpg",
    },
    "analytics": "http://127.0.0.1:8000/api/v2/videos/2/analytics",
    "tags": [
        "python"
    ],
    "comments": "http://127.0.0.1:8000/api/v2/videos/2/comments"
    }
    }
```

### GET videos/tags

Returns a collection of all tags.

See [GET videos](#get-videos)

```json
    {
    "count": 5,
    "next": null,
    "previous": null,
    "results": [
        {
          "python"
        }
    ]
    }
```

### GET videos/tags/:coma_separated_tags

Returns a collection of videos containing at least one of the following
:coma_separated_tags.

See [GET videos](#get-videos)

```json
    {
      "python"
    }
```

### GET videos/:id/analytics

Returns video analytics (such as views) of provided Video :id.

```json
    {
    "views": 0,
    "unique_views": 0,
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
       "count": 1,
       "next": null,
       "previous": null,
       "results": [
           {
           "id": 20,
           "href": "http://127.0.0.1:8000/api/v2/videos/6/comments/20",
           "user": "http://127.0.0.1:8000/api/v2/users/3",
           "video": 6,
           "created": "2016-05-16T14:59:30.631150Z",
           "modified": "2016-05-16T14:59:30.631174Z",
           "content": "testing"
           }
       ]
   }
```

### GET videos/:id/comments/:comment_id

If exists, it returns the comment details of the video :id.

```json
    {
    "id": 20,
    "href": "http://127.0.0.1:8000/api/v2/videos/6/comments/20",
    "user": "http://127.0.0.1:8000/api/v2/users/3",
    "video": 6,
    "created": "2016-05-16T14:59:30.631150Z",
    "modified": "2016-05-16T14:59:30.631174Z",
    "content": "testing"
    }
```
