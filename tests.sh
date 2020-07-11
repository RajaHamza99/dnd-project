#! /bin/bash

. /home/rajahamza104/dnd-project/venv/bin/activate

echo pwd
cd /home/jenkins/.jenkins/workspace/dnd-app/service_one
echo pwd
ls
pytest ./service_one --cov ./service_one/
echo pwd
ls

pytest ./service_two --cov ./service_two/
pytest ./service_three --cov ./service_three/
