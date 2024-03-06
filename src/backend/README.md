# Start

1. Create env
```
python -m venv env
```

2. Start env
```
. .\env\Scripts\activate
```

3. Start env
```
pip install -r .\requirements.dev.txt
```

4. migrate
```
python manage.py migrate 
```

5. Create super user
```
python manage.py createsuperuser
```

6. Start server
```
python manage.py runserver
```

## Routes
- [Дока](http://127.0.0.1:8000/api/v1/docs/)
- [Админка](http://127.0.0.1:8000/admin/)
- [Точка входа в api](http://127.0.0.1:8000/api/v1/)
