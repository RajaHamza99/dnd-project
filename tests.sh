#! /bin/bash

. /home/rajahamza104/dnd-project/venv/bin/activate
pytest ./service_one --cov ./service_one/
pytest ./service_two --cov ./service_two/
pytest ./service_three --cov ./service_three/
