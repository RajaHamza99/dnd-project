pipeline{
        agent any
        stages{
            stage('Install Docker using ansible'){
                steps{
                        sh "ansible-playbook -i inventory Ansible/playbook.yaml"
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


