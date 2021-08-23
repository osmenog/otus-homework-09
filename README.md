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
newman run otus-09.postman_collection.json
```
