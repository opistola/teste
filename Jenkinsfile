pipeline {
  agent { label "jenkins-node1" }
  stages {
    stage("PrepareEnv") {
      steps {
        sh """
              echo ${SHELL}
              if [ -d venv ]; then rm -rf venv fi
              virtualenv venv
              pip3 install --user --no-warn-script-location -r requirements.txt
          """
      }
    }
    stage("Tests") {
      steps {
        sh """
          echo ${SHELL}
          source venv/bin/activate
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