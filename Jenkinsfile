pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'python calculator.py'
                stash(name: 'compiled-results', includes: 'sources/*.py*')
            }
        }
    }
}
