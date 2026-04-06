pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/duryar/test_repo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'sudo docker build -t flask-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker rm -f flask-app || true
                docker run -d -p 5000:5000 --name flask-app flask-app
                '''
            }
        }

    }
}