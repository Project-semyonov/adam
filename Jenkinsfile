pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building docker image..'
                sh "docker build -t semyonov/test_python ."
                //Next step is to push this image to semyonov docker-hub repo
                //Jenkins will require credentials to get into this repo
                docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                //push("${env.BUILD_NUMBER}")
                //app.push("latest")
                sh "docker push semyonov/test_python:latest"
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh "docker run semyonov/test_python"
            }
        }
    }
}
