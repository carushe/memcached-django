#!/usr/bin/env groovy

pipeline {
  agent any
  options {
    skipStagesAfterUnstable()
  }
  stages {
     stage('Build') {
        steps {
             sh """
                 PATH=$WORKSPACE/venv/bin:/usr/local/bin:$PATH
                 if [! -d "venv" ]; then
                    python3 -m venv venv
                 fi
                 . venv/bin/activate
                 pip install -r requirements.txt --download-cached=/tmp/$JOB_NAME
                """
             echo "activation complete !"
        }
     }
     stage('Test') {
       steps {
         sh """. venv/bin/activate && python3 manage.py test
            """
       }
     }
     stage('deploy') {
       steps {
         echo "This is the deployment"
       }
     }
  }
}