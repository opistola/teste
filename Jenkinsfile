pipeline {
  agent { label "jenkins-node1" }
  stages {
    stage("PrepareEnv") {
      steps {
        sh """
              echo ${SHELL}
              [ -d venv ] && rm -rf venv
              virtualenv venv
              export PATH=${VIRTUAL_ENV}/bin:${PATH}
              pip install --upgrade pip
              pip install -r requirements.txt
              make clean
          """
      }
    }
    stage("Tests") {
      steps {
        sh """
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