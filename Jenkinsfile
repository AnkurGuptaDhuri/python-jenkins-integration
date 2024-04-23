pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
                print("hello world")
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/AnkurGuptaDhuri/python-jenkins-integration']])
            }
        }
        stage('Build Python'){
            steps{
                git branch: 'main', url: 'https://github.com/AnkurGuptaDhuri/python-jenkins-integration'
                sh 'python3 calc.py'
            }
        }
        stage('testing'){
            steps{
                sh 'python3 -m unittest -v test.py'
            }
        }
        
    }
}