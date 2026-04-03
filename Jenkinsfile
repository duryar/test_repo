pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/duryar/test_repo.git'
            }
        }

        stage('Run Python Script') {
            steps {
                sh 'python test_python.txt'
            }
        }
    }
}