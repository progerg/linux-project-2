### Задание 2 - Взаимодействующие приложения в Docker

- необходимо реализовать многоконтейнерное приложение (не используя docker compose)
- отдельные контейнеры должны взаимодействовать между собой через файловую систему или сеть
- в отчёт необходимо добавить код приложений, команды на запуск контейнеров и ссылку на образ (hub.docker.com/...)

##### Решение
У меня 2 контейнера: один создает веб-сервер, второй обрабатывает данные. 
Обработчик (processor) отправляет запрос на сервер, узнает состояние сервера. После этого обрабатывает данные и пишет в логи.
"Server is healthy" - если сервер здоров
"Server is not healthy" - если сервер не здоров

##### Если нужно сбилдить самому
Тут два образа, один для веб-сервера, второй для обработчика данных.
```bash
docker build -t my-web-server web
docker build -t my-data-processor processor

docker tag my-web-server yourusername/my-web-server
docker tag my-data-processor yourusername/my-data-processor

docker push yourusername/my-web-server
docker push yourusername/my-data-processor
```

##### Запуск с моих образов из Docker Hub
```bash
docker network create my-network

docker run -d --name web-server --network my-network progerg/my-web-server
docker run -d --name data-processor --network my-network progerg/my-data-processor
```

Ссылки на сами образы:
https://hub.docker.com/repository/docker/progerg/my-data-processor/general
https://hub.docker.com/repository/docker/progerg/my-web-server/general