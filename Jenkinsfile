pipeline {
    
    agent any 
    
    environment {
        IMAGE_TAG = "${BUILD_NUMBER}"
        registryCredential = 'Docker-jenkins'
        GITHUB_TOKEN = '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'
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
                    withCredentials([usernamePassword(credentialsId: 'jenkins-github', passwordVariable: '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', usernameVariable: 'nitish0104')]) {
                        sh '''
                        cat Deploy.yaml
                        sed -i "s|9|${BUILD_NUMBER}|g" Deploy.yaml
                        cat Deploy.yaml
                        git config --global user.email "nitishdalvi1@gmail.com"
                        git config --global user.name "nitish0104"
                        echo "git configuration done"
                        git remote set-url origin https://nitish0104:${GITHUB_TOKEN}@github.com/nitish0104/ToDo-mainfest-repo.git
                        git add Deploy.yaml
                        git commit -m 'Updated the Deploy yaml | Jenkins Pipeline'
                        git push origin HEAD:master
                        '''                        
                    }
                }
            }
        }
    }
}