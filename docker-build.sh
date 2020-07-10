#! /bin/bash
export SECRET_KEY=apogjmnaiopdgn
export DB_USER=hamza
export DB_PASS=hamza2
docker-compose build
docker-compose push
scp docker-compose.yaml jenkins@dnd-manager/home/jenkins/
ssh jenkins@dnd-manager docker stack deploy --compose-file docker-compose.yaml dnd
