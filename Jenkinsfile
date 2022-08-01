node {
  stage('SCM') {
    checkout scm
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'SonarQube Scanner';
    withSonarQubeEnv(installationName: 'SonarQube') {
      sh "sonar-scanner -Dsonar.projectKey=way-web"
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
}
