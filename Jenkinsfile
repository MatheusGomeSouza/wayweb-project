pipeline {
    agent any
    
    stages{
        stage('Build') {
            steps {
                git branch: 'develop', credentialsId: 'git_credentials', url: 'https://github.com/MatheusGomeSouza/wayweb-project.git'
                sh 'sleep 10'
                sh 'echo "Docker Image validation"'
                sh 'echo "Build Validation"'
            }
        }
        stage('Test') {
            steps {
                sh 'sleep 10'
                sh 'echo "Unit Test .."'
                sh 'echo "Smoke Test .."'
            }
        }
        stage('CodeCoverage') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh "${scannerHome}/bin/sonar-scanner"
                }
            }
        }
        stage('Deploy') {
            steps {
                sh 'sleep 10'
                sh 'echo "Connecting EC2.."'
                sh 'echo "Deploying .."'
            }
        }
    }
}
