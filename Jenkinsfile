pipeline{
        agent any
        stages{
            stage('Pull Repo'){
                steps{
                    sh "git clone https://github.com/RajaHamza99/dnd-project.git"
                    sh "git checkout development2"
                }
            }
            stage('Install docker and docker-compose'){
                steps{
                    sh "docker: curl https://get.docker.com | sudo bash"
                    sh "sudo curl -L 'https://github.com/docker/compose/releases/download/\${version}/docker-compose-\$(uname -s)-\$(uname -m)' -o /usr/local/bin/docker-compose"
                    sh "sudo chmod +x /usr/local/bin/docker-compose"
                }
            }
                stage('Deploy application'){
                        steps{
                                sh "docker-compose down"
                                sh "docker-compose build"
                                sh "docker-compose push"
                                sh "docker stack deploy --compose-file docker-compose.yaml dnd"
                        }
        }    
}
}
