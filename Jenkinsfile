pipeline{
        agent any
        stages{
            stage('Install Docker using ansible'){
                steps{
                        sh "bash execute-ansible.sh"
                }
            }
                stage('Deploy application'){
                        steps{
                                sh "export SECRET_KEY=apdgmaidopgnauod"
                                sh "export DB_USER=hamza"
                                sh "export DB_PASS=hamza2"
                                sh "docker-compose build && docker-compose push"
                                sh "export SECRET_KEY=apigdnadipgnda && docker stack deploy --compose-file docker-compose.yaml dnd"
                        }
        }    
}
}


