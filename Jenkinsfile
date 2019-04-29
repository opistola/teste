pipeline {
  agent { label "jenkins-node1" }
  stages {
    stage("PrepareEnv") {
      steps {
        sh """
              if [ -d venv ]; then
                rm -rf venv;
              fi
              virtualenv venv
              pip3 install -r requirements.txt
          """
      }
    }
    stage("Tests") {
      steps {
        sh """
          . venv/bin/activate
          pytest tests/
        """
      }
    }
    stage ('Cleanup') {
            steps {
                sh 'rm -rf venv'
            }
    }
  }
}