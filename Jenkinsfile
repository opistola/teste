pipeline {
  agent { label 'jenkins-node1' }
  stages {
    stage('Prepare env') {
      steps {
        sh 'virtualenv venv'
        sh 'source venv/bin/activate'
        sh 'pip3 install -r requirements.txt'
      }
    }
    stage('Tests') {
      steps {
        sh 'pytest tests/'
      }
    }
  }
}