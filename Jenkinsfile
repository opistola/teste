pipeline {
  agent any
  stages {
    stage('Prepare env') {
      steps {
        sh 'PATH="/usr/local/bin:$PATH"'
      }
    },
    stage('Tests') {
      steps {
        sh '/usr/bin/python3 -m pytest tests/'
      }
    }
  }
}