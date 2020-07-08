#! /bin/bash
echo "installing docker"
curl https://get.docker.com | sudo bash
echo "install docker-compose"
sudo curl -L 'https://github.com/docker/compose/releases/download/\${version}/docker-compose-\$(uname -s)-\$(uname -m)' -o /usr/local/bin/docker-compose
echo "making docker-compose executable"
sudo chmod +x /usr/local/bin/docker-compose
