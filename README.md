### О проекте:
API сервис для социальной сети

### Возможности:
* Создание постов
* Подписка на интересных авторов
* Комментарии

### Технологии:
* Python 3.8
* Django 2.2
* Django REST Framework 3.12
* Postman

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/ApriCotBrain/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Документация:
После запуска на localhost доступна [документация](http://127.0.0.1:8000/redoc/).

## Примеры:
### Получение токена:
POST: http://127.0.0.1:8000/api/v1/jwt/create/
```
{
    "username": "string",
    "password": "string"
}
```
RESPONSE:
```
{
    "refresh": "string",
    "access": "string"
}
```
Для добавления/изменения данных через API необходимо добавить в header к запросу параметр <br>
'Authorization' со значением 'Bearer ACCESS_TOKEN'.

### Получение постов (с офсетом и ограничением по количеству):
##### GET: http://127.0.0.1:8000/api/v1/posts/?offset=300&limit=100 
##### RESPONSE:
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2022-11-24T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
 ```

##### RESPONSE (при запросе без параметров offset и limit):
```

[
    {
        "id": 1,
        "author": "alex",
        "text": "alex post",
        "pub_date": "2022-11-24T12:19:43.288654Z",
        "image": null,
        "group": null
    }
]
```
### Создание поста:
POST:  http://127.0.0.1:8000/api/v1/posts/

```
{
  "text": "string",
  "image": "string", 
  "group": 0
}

```
RESPONSE:
```
{
  "id": 0,
  "author": "string",`
  "text": "string",
  "pub_date": "2022-11-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
### Подписаться на автора (только для авторизованных пользователей):

POST:  http://127.0.0.1:8000/api/v1/follow/

```
{
  "following": "string_username"
}
```

##### RESPONSE:
```
{
  "user": "string",
  "following": "string"
}
```