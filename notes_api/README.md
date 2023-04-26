
```
docker build -t my-django-app . --no-cache

docker run -it -p 8000:8000 my-django-app
```

> 0.0.0.0:8000/api/notes
> 0.0.0.0:8000/api/notes/1
```
curl -X POST -H "Content-Type: application/json" -d '{"title": "Sample Note", "content": "This is a sample note."}' http://localhost:8000/api/notes/

# specific one
curl -X GET http://localhost:8000/api/notes/2/
```