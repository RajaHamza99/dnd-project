#! /bin/bash
export SECRET_KEY=apogjmnaiopdgn
export DB_USER=hamza
export DB_PASS=hamza2
docker-compose build
docker-compose push
docker stack deploy --compose-file docker-compose.yaml dnd
