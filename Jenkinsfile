
pipeline {
  agent any
  options {
    skipStagesAfterUnstable()
  }
  stages {
  environment {
      HOME_DIR="/home/jkulante"
      VENV_PATH="${HOME_DIR}/Documents/django-async-project/virtenv"
      PYTHON_INTERPRETER="${VENV_PATH}/bin/python3"

   }
     stage('Build') {
        steps {
             sh "cd /home/jkulante/Documents/django-async-project/"
             echo "activation complete !"
        }
     }
     stage('Test') {
       steps {
          sh "${PYTHON_INTERPRETER} manage.py test"
       }
     }
     stage('deploy') {
       steps {
         echo "This is the deployment"
       }
     }
  }
}