#! /bin/bash

. /home/rajahamza104/dnd-project/venv/bin/activate

pwd
cd /home/jenkins/.jenkins/workspace/dnd-app/service_one
pwd
ls
pytest --cov ./application
pwd
ls

pytest ./service_two --cov ./service_two/
pytest ./service_three --cov ./service_three/
