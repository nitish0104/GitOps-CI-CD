pipeline {
    
    agent any 
    
    environment {
        IMAGE_TAG = "${BUILD_NUMBER}"
        DOCKER_HUB_CREDENTIALS = credentials('Docker') // Use the ID you set in Jenkins
        // K8S_MANIFESTS_REPO_CRED_ID = 'github'
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

        stage('Push the artifacts') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'DOCKER_HUB_CREDENTIALS', passwordVariable: 'Nitish@2002', usernameVariable: 'nitish0104')]) {
                        sh '''
                        echo 'Push to Repo'
                        echo 'Debug: Checking Docker Version'
                        docker version
                        docker login -u nitish0104 -p Nitish@2002
                        docker push nitish0104/todo:${BUILD_NUMBER}
                        echo 'Docker Push Completed'
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
                git credentialsId: 'github', 
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
                    withCredentials([usernamePassword(credentialsId: 'jenkins-github', passwordVariable: 'Shradha@2002#', usernameVariable: 'nitish0104')]) {
                        sh '''
                        cat Deploy.yaml
                        sed -i '' "s/v1/${BUILD_NUMBER}/g" Deploy.yaml
                        cat Deploy.yaml
                        git add Deploy.yaml
                        git commit -m 'Updated the Deploy yaml | Jenkins Pipeline'
                        git remote -v
                        git push https://github.com/nitish0104/ToDo-mainfest-repo.git HEAD:master
                        '''                        
                    }
                }
            }
        }
    }
}