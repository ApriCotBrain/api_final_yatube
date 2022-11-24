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

Примеры для запросов API:

```
GET  api/v1/posts/
POST api/v1/posts/
GET api/v1/posts/{id}/
PUT api/v1/posts/{id}/
PATCH api/v1/posts/{id}/
```