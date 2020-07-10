#! /bin/bash
docker-compose build
docker-compose push
ssh jenkins@dnd-manager
export SECRET_KEY=apogjmnaiopdgn
export DB_USER=hamza
export DB_PASS=hamza2
docker stack deploy --compose-file docker-compose.yaml dnd
