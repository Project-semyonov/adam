pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building docker image..'
                sh "docker build -t semyonov4360/test_python ."
    /*          Next step is to push this image to semyonov docker-hub repo
                //Jenkins will require credentials to get into this repo

                withCredentials([[$class: 'UsernamePasswordMultiBinding',
                credentialsId: 'docker-hub-credentials',
                usernameVariable: 'DOCKER_HUB_USER',
                passwordVariable: 'DOCKER_HUB_PASSWORD']]) 
                {
                    sh "docker login -u ${DOCKER_HUB_USER} -p ${DOCKER_HUB_PASSWORD}"
                }

                //**Now push to semyonov4360 repo
                sh "docker push semyonov4360/test_python"
                
    */
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh "python3 -m unittest Test.py"
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh "docker run semyonov4360/test_python"
            }
        }
    }
}
