pipeline {
    agent any

    stages {
        stage('Git Checkout') {
            steps {
                git branch: 'main', changelog: false, credentialsId: 'bde67af4-884c-41e5-b485-f98be783d24a', poll: false, url: 'https://github.com/Hiba-Abdul-Jameel/CICD.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'd4f525b1-568d-4c2e-8948-e6dec7087cb3', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
                    }
                    sh 'docker rmi hibajameel/sampleapp:latest | true'
                    sh 'docker build -t hibajameel/sampleapp:latest .'
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                // Push the Docker image to Docker Hub
                sh 'docker push hibajameel/sampleapp:latest'
            }
        }
        stage('Deploy the Container') {
            steps {
                // Push the Docker image to Docker Hub
                sh 'docker stop sampleapp | true'
                sh 'docker rm sampleapp | true'
                sh 'docker run -dp 80:80 --name sampleapp hibajameel/sampleapp'
            }
        }
        stage('Test') {
            steps {
                // Activate Python virtual environment and execute the test script
                sh 'source /snap/core18/2812/usr/lib/python3.6/venv/bin/activate && python3 /var/lib/jenkins/workspace/AutoBuild/test_html.py'
            }
        }
    }
}
