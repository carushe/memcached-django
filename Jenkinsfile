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

             sh "source virtualenv/bin/activate"

          echo 'activation complete !'
        }
     }
     stage('Test') {
       steps {
         sh 'python manage test'
       }
     }
     stage('deploy') {
       steps {
         echo 'This is the deployment'
       }
     }
  }
}