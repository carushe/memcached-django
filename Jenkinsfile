#!/usr/bin/env groovy

pipeline {
  agent any
  options {
    skipStagesAfterUnstable()
  }
  stages {
     stage('Build') {
        steps {
             sh "cd /home/jkulante/Documents/django-async-project/"
             echo "activation complete !"
        }
     }
     stage('Test') {
       steps {
         sh "$PYTHON_INTERPRETER manage test"
       }
     }
     stage('deploy') {
       steps {
         echo "This is the deployment"
       }
     }
  }
}