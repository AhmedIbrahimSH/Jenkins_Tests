pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                // Replace this with your build commands
                echo "hello word"
            }
        }
        // Additional stages like 'Test', 'Deploy', etc. can be added here
    }
    post {
        failure {
            script {
                def gitCommit = sh(script: 'git rev-parse HEAD', returnStdout: true).trim()
                echo "Failed at commit: ${gitCommit}"
                // Additional failure handling
            }
        }
    }
}
