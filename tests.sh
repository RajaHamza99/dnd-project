#! /bin/bash




. /home/rajahamza104/dnd-project/venv/bin/activate

cd /home/jenkins/.jenkins/workspace/dnd-app/service_one
pytest --cov ./application

cd /home/jenkins/.jenkins/workspace/dnd-app/service_two
pytest --cov ./application

cd /home/jenkins/.jenkins/workspace/dnd-app/service_three
pytest --cov ./application

cd /home/jenkins/.jenkins/workspace/dnd-app/service_four
pytest --cov ./application 