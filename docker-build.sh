#! /bin/bash
docker-compose build
docker-compose push
scp docker-compose.yaml jenkins@dnd-manager:/home/rajahamza104/dnd-project/docker-compose.yaml
ssh jenkins@dnd-manager << EOF
cd /home/rajahamza104/dnd-project
env SECRET_KEY=${SECRET_KEY} env DB_USER=${DB_USER} env DB_PASS=${DB_PASS} docker stack deploy --compose-file docker-compose.yaml dnd
EOF
