pipeline {
    
    agent any 
    
    environment {
        IMAGE_TAG = "${BUILD_NUMBER}"
        registryCredential = 'Docker-jenkins'
        GIT_REPO_URL = 'https://github.com/nitish0104/ToDo-mainfest-repo.git'
        GIT_CREDENTIAL_ID = 'jenkins-github'
        GIT_TOKEN = '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'  // Replace with the token you generated
        GIT_EMAIL = 'nitishdalvi1@gmail.com'
        GIT_NAME = 'nitish0104'
    }
    
    stages {
        
        stage('Checkout Code') {
            steps {
                script {
                    // Checkout source code (TODO app) from the repository
                    git credentialsId: 'jenkins-github', 
                        url: 'https://github.com/nitish0104/TODO-CI-CD.git'
                        branch: 'master'
                }
            }
        }

        stage('Build Docker'){
            steps{
                script{
                        sh '''
                        echo 'Buid Docker Image'
                        docker build -t nitish0104/todo:${BUILD_NUMBER} .
                        echo 'Docker Build Completed'
                        '''
                    }
            }
        }

        stage('Push the artifacts'){
           steps{
                script{
                    docker.withRegistry('', registryCredential) {
                        sh '''
                        echo 'Logging into Docker'
                        docker login
                        echo 'Push to Docker  Repo'
                        docker push nitish0104/todo:${BUILD_NUMBER}
                        '''
                    }
                }
            }
        }

        
        stage("Done"){
            steps{
                echo "Done CI pipeline Done"
            }
            
        }
        
        stage('Checkout K8S manifest SCM'){
            steps {
                git credentialsId: 'jenkins-github', 
                url: 'https://github.com/nitish0104/ToDo-mainfest-repo.git',
                branch: 'master'
            }
        }
        stage("Done2"){
            steps{
                echo "Done CD pipeline"
            }
            
        }
        
        stage('Update K8S manifest & push to Repo'){
            steps {
                script{
                    // Configure Git identity
                    sh "git config --global user.email '${GIT_EMAIL}'"
                    sh "git config --global user.name '${GIT_NAME}'"

                    // Clone repository
                    sh "git clone -b master https://${GIT_TOKEN}@${GIT_REPO_URL} myrepo"
                    dir('myrepo') {
                        // Update Deploy.yaml
                        sh '''
                        cat Deploy.yaml
                        sed -i "s|9|${BUILD_NUMBER}|g" Deploy.yaml
                        cat Deploy.yaml
                        '''

                        // Configure Git credentials
                        sh "git config credential.helper 'store --file=.git/credentials'"
                        sh "echo 'https://${GIT_USERNAME}:${GIT_TOKEN}@${GIT_REPO_URL}' > .git/credentials"

                        // Commit and push changes
                        sh '''
                        git add Deploy.yaml
                        git commit -m "Updated the Deploy yaml | Jenkins Pipeline"
                        git remote -v
                        git push origin master
                        '''
                    }
                }

            }
        }
    }
}