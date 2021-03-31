pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'oabuoun/calculator'
                }
            }
            steps {
                sh 'python calculator.py'
                stash(name: 'compiled-results', includes: 'sources/*.py*')
            }
        }
    }
}
