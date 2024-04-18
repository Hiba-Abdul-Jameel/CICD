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
        stage('Test HTML with Selenium') {
            steps {
                // Install required packages (e.g., Chrome WebDriver)
                sh 'apt-get update'
                sh 'apt-get install -y chromium-browser chromium-chromedriver'

                // Run Selenium test
                sh 'pip install selenium'
                sh '''
                    python <<EOF
                    from selenium import webdriver

                    options = webdriver.ChromeOptions()
                    options.add_argument("--no-sandbox")
                    options.add_argument("--disable-dev-shm-usage")
                    options.binary_location = "/usr/bin/chromium-browser"

                    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=options)
                    driver.get("file:///path/to/your/repo/test.html") // Replace with the actual path to your HTML file in the repo

                    assert "Welcome to My Test Page" in driver.title
                    assert "This is a paragraph of text." in driver.page_source

                    driver.quit()
                    EOF
                '''
            }
        }
    }
}
