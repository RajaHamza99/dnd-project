pipeline{
        agent any
        stages{
            stage('Install Docker using ansible'){
                steps{
                        sh "sudo su - rajahamza104 && ansible-playbook -i inventory playbook.yaml"
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


