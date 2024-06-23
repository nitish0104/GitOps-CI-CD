pipeline {
    
    agent {
        label 'Kubernetes'
    }
    
    environment {
        IMAGE_TAG = "${BUILD_NUMBER}"
        registryCredential = "${Docker}"
        GITHUB_TOKEN = "${Github}"
    }
    
    stages {
        
        stage('Checkout Code') {
            steps {
                script {
                    // Checkout source code (TODO app) from the repository
                    git credentialsId: 'Github', 
                        url: 'https://github.com/nitish0104/GitOps-CI-CD.git'
                        branch: 'master'
                }
            }
        }

        stage('Build Docker'){
            steps{
                script{
                        sh '''
                        echo 'Buid Docker Image'
                        sudo docker build -t nitish0104/todo:${BUILD_NUMBER} .
                        echo 'Docker Build Completed'
                        '''
                    }
            }
        }

        stage('Push Docker image to dockerHub'){
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

        
        stage("CI Done"){
            steps{
                echo "Done CI pipeline Done"
            }
            
        }
        stage("CD "){
            steps{
                echo "CD  pipeline Start "
            }
            
        }
        stage('Checkout K8S manifest SCM'){
            steps {
                git credentialsId: 'Github', 
                url: 'https://github.com/nitish0104/GitOps-Mainfest-Repo.git',
                branch: 'master'
            }
        }
        
        
        stage('Update K8S manifest & push to Repo'){
            steps {
                script{
                    withCredentials([usernamePassword(credentialsId: 'Github', passwordVariable: 'GITHUB_TOKEN', usernameVariable: 'nitish0104')]) {
                        sh '''
                        cat Deploy.yaml
                        sed -i "s|11|${BUILD_NUMBER}|g" Deploy.yaml
                        cat Deploy.yaml
                        git config --global user.email "nitishdalvi1@gmail.com"
                        git config --global user.name "nitish0104"
                        echo "git configuration done"
                        git remote set-url origin https://nitish0104:${GITHUB_TOKEN}@github.com/nitish0104/GitOps-Mainfest-Repo.git
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
