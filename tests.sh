#! /bin/bash




. /home/rajahamza104/dnd-project/venv/bin/activate

cd /home/jenkins/.jenkins/workspace/dnd-app/service_one
pytest --cov ./application

cd /home/jenkins/.jenkins/workspace/dnd-app/service_two
pytest ./service_two --cov ./service_two/

cd /home/jenkins/.jenkins/workspace/dnd-app/service_three
pytest ./service_three --cov ./service_three/
