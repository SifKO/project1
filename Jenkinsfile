#!groovy

properties([disableConcurrentBuilds()])

pipeline {
    agent any
    triggers {
        pollSCM('* * * * *')
        }

    options {
        buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10'))
        timestamps()
    }

    stages {
        stage("Pull code") {
            steps {
                    sh '''
                        ssh admin@34.207.229.44 "
                        (cd project1 && git pull) || (git clone https://github.com/SifKO/project1.git \
                        && cd project1 \
                        &&python -m venv .venv)
                        "
                    '''
            }
        }
        stage("Install requirements") {
            steps {
                    sh '''
                        ssh admin@34.207.229.44 "
                        cd project1
                        source .venv/bin/activate
                        pip install -r req.txt
                        "
                    '''
            }
        }

        stage("Restart services") {
            steps {
                    sh '''
                        ssh admin@34.207.229.44 "
                        sudo systemctl restart myflaskapp
                        "
                    '''
            }
        }
    }
}