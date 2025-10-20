pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'puttaumadevi/ticket-system'
        DOCKER_CREDENTIALS = 'Docker-hub-credentials'
        APP_PORT = '5000'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'master', url: 'https://github.com/PuttaUmadevi/DevOps_assignment_2-CI-CD-automation-.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "🚀 Building Docker image: ${DOCKER_IMAGE}:${env.BUILD_NUMBER}"
                    dockerImage = docker.build("${DOCKER_IMAGE}:${env.BUILD_NUMBER}")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('', "${DOCKER_CREDENTIALS}") {
                        dockerImage.push("${env.BUILD_NUMBER}")
                        dockerImage.push('latest')
                    }
                }
            }
        }

        stage('Deploy Locally') {
            steps {
                script {
                    sh 'docker stop ticket-system-app || true'
                    sh 'docker rm ticket-system-app || true'
                    sh "docker run -d -p ${APP_PORT}:${APP_PORT} --name ticket-system-app ${DOCKER_IMAGE}:${env.BUILD_NUMBER}"
                    echo "✅ App deployed locally at: http://localhost:${APP_PORT}"
                }
            }
        }
    }

    post {
        success {
            echo "🎉 Pipeline succeeded! Image pushed and running."
        }
        failure {
            echo "❌ Pipeline failed — check logs."
        }
    }
}
