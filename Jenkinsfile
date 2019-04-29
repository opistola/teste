pipeline {
  agent any
  stages {
    stage('Tests') {
      steps {
        sh '/usr/bin/python3 -m pytest tests/'
      }
    }
  }
}