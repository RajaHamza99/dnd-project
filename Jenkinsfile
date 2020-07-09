pipeline{
        agent any
        stages{
            stage('Install Docker using ansible'){
                steps{
                        sh "install-jenkins.sh"
                }
            }
                stage('Deploy application'){
                        steps{
                                sh "export SECRET_KEY=apmgdipandg"
                                sh "docker-compose build"
                                sh "docker stack deploy --compose-file docker-compose.yaml dnd"
                        }
        }    
}
}


