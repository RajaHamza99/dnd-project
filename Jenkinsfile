pipeline{
        agent any
        stages{
	    stage ('Test application'){
		steps{
			sh "bash tests.sh"
		} 
	}
            stage('Install Docker using ansible'){
                steps{
                        sh "bash execute-ansible.sh"
                }
            }
                stage('Deploy application'){
                        steps{
                                sh "bash docker-build.sh"

                        }
        }    
}
}


