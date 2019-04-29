pipeline {
  agent any
  stages {
    stage('Tests') {
      steps {
        sh 'python3 -m pytest tests/'
      }
    }
  }
}