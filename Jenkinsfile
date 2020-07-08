pipeline{
        agent any
        stages{
            stage('Install docker and docker-compose'){
                steps{
                        sh "bash install-docker.sh"
                }
            }
                stage('Deploy application'){
                        steps{
                                sh "export SECRET_KEY=apmgdipandg"
                                sh "docker-compose build"
                                sh "docker-compose push"
                                sh "docker stack deploy --compose-file docker-compose.yaml dnd"
                        }
        }    
}
}


