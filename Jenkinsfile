pipeline {
    
    agent {
        label 'Kubernetes'
    }
    
    environment {
        TAG = "${BUILD_NUMBER}"
        DOCKER_CREDENTIALS_ID = 'Docker'
        IMAGE_NAME = 'nitish0104/todo'
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

        stage('Build') {
            steps {
                script {
                    // Build the Docker image
                    docker.build("${IMAGE_NAME}:${TAG}")
                }
            }
        }

        stage('Push') {
            steps {
                script {
                    // Log in to Docker Hub
                    docker.withRegistry('https://index.docker.io/v1/', DOCKER_CREDENTIALS_ID) {
                        // Push the Docker image to the repository
                        docker.image("${IMAGE_NAME}:${TAG}").push()
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
