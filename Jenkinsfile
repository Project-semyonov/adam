pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building docker image..'
                sh "docker build -t semyonov/test_python ."
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
