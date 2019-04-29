pipeline {
  agent any
  stages {
    stage('Tests') {
      steps {
        sh 'PATH="/usr/local/bin:$PATH"'
        sh 'python3 -m pytest tests/'
      }
    }
  }
}