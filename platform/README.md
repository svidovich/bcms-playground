# Starting the Test Platform

You should have docker-compose installed.

Run

```shell
docker compose -f test.docker-compose.yaml build
docker compose -f test.docker-compose.yaml up
```

The service should be running but incomplete. Get an interactive shell:

```shell
docker exec -it  platform-api-1 /bin/bash
# You are now inside the running API container
python3 manage.py migrate
```
