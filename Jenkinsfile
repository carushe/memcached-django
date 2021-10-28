#!/usr/bin/env groovy

pipeline {
  agent any
  options {
    skipStagesAfterUnstable()
  }
  stages {
     stage('Build') {
        steps {
          dir("${env.WORKSPACE}") {
              sh "pwd"
          }

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