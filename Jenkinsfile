pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/duryar/test_repo.git'
            }
        }

        stage('Run Python Script') {
            steps {
                sh 'python test_python.txt'
            }
        }
    }
}