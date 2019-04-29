pipeline {
  agent none
  stages {
    agent { label 'jenkins-node1' }
    stage('Prepare env') {
      steps {
        sh 'virtualenv venv'
        sh 'source venv/bin/activate'
        sh 'pip3 install -r requirements.txt'
      }
    }
    stage('Tests') {
      agent { label 'jenkins-node1' }
      steps {
        sh 'pytest tests/'
      }
    }
  }
}