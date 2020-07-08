pipeline{
        agent any
        stages{
            stage('Install docker and docker-compose'){
                steps{
                    sh "docker: curl https://get.docker.com | sudo bash"
                    sh "sudo curl -L 'https://github.com/docker/compose/releases/download/\${version}/docker-compose-\$(uname -s)-\$(uname -m)' -o /usr/local/bin/docker-compose"
                    sh "sudo chmod +x /usr/local/bin/docker-compose"
                }
            }
                stage('Deploy application'){
                        steps{
                                sh "cd dnd-project"
                                sh "docker-compose build"
                                sh "docker-compose push"
                                sh "docker stack deploy --compose-file docker-compose.yaml dnd"
                        }
        }    
}
}


