pipeline {
  agent any
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