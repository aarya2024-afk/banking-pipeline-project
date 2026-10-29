pipeline {
    agent any

    environment {
        DOCKER_HUB_USER = 'aarya120924'
        IMAGE_NAME = 'banking-app'
        REGISTRY_CREDENTIALS_ID = 'docker-hub-credentials'
    }

    stages {
        stage('Source Code Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Automated Tests') {
            steps {
                sh 'pytest test_app.py'
            }
        }

        stage('Build and Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://docker.io', "${REGISTRY_CREDENTIALS_ID}") {
                        def customImage = docker.build("${DOCKER_HUB_USER}/${IMAGE_NAME}:${BUILD_NUMBER}")
                        customImage.push()
                    }
                }
            }
        }

        stage('Configure Kubernetes Manifest') {
            steps {
                sh """
                    SED_EXPR="s|DOCKERHUB_USERNAME/banking-app:TAG_PLACEHOLDER|${DOCKER_HUB_USER}/${IMAGE_NAME}:${BUILD_NUMBER}|g"
                    sed -i "\$SED_EXPR" k8s/deployment.yaml
                """
            }
        }

        stage('Deployment to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/deployment.yaml'
            }
        }
    }
}
