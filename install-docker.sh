#! /bin/bash
curl https://get.docker.com | sudo bash
sudo curl -L 'https://github.com/docker/compose/releases/download/\${version}/docker-compose-\$(uname -s)-\$(uname -m)' -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
