# otus-homework-09
Для запуска можно вызвать команду:
```
skaffold run --tail
```
или развернуть при помощи helm (предварительно создав namespace командой `kubectl create namespace otus`):
```
helm install otus ./k8s/user_service -n otus
```

После развертывания приложения можно запустить postman тесты командой:
```
newman run otus-06.postman_collection.json
```


while 1; do ab -n 50 -c 5 http://arch.homework/ ; sleep 3; done

while 1; do curl http://arch.homework/handle500 ; sleep 10; done