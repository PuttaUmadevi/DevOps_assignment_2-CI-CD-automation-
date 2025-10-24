pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'puttaumadevi/ticket-system'
        DOCKER_CREDENTIALS = credentials('docker-hub-credentials')   //created in jenkins
        APP_PORT = '5000'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/PuttaUmadevi/DevOps_assignment_2-CI-CD-automation-.git'
                bat 'echo  Code checked out successfully.'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    bat """
                    echo 🚀 Building Docker image: ${DOCKER_IMAGE}:${env.BUILD_NUMBER}
                    docker build -t ${DOCKER_IMAGE}:${env.BUILD_NUMBER} .
                    docker tag ${DOCKER_IMAGE}:${env.BUILD_NUMBER} ${DOCKER_IMAGE}:latest
                    """
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    bat """
                    docker login -u ${DOCKER_CREDENTIALS_USR} -p ${DOCKER_CREDENTIALS_PSW}
                    docker push ${DOCKER_IMAGE}:${env.BUILD_NUMBER}
                    docker push ${DOCKER_IMAGE}:latest
                    docker logout
                    """
                }
            }
        }

        stage('Deploy Locally (Optional)') {
            steps {
                script {
                    bat """
                    docker stop ticket-system-app || echo Container not running
                    docker rm ticket-system-app || echo Container not found
                    docker run -d -p ${APP_PORT}:${APP_PORT} --name ticket-system-app ${DOCKER_IMAGE}:${env.BUILD_NUMBER}
                    echo  Application deployed locally at http://localhost:${APP_PORT}
                    """
                }
            }
        }
    }

    post {
        success {
            bat 'echo  Jenkins Pipeline succeeded! Image built, pushed, and deployed.'
        }
        failure {
            bat 'echo  Jenkins Pipeline failed! Check the console output for errors.'
        }
    }
}
