pipeline {
  agent { label "jenkins-node1" }
  stages {
    stage("PrepareEnv") {
      steps {
        sh """
              echo ${SHELL}
              [ -d venv ] && rm -rf venv
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
          echo "which python3"
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