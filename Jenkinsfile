node {
  stage('SCM') {
    checkout scm
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'SonarQube Scanner';
    withSonarQubeEnv(installationName: 'SonarQube') {
      sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=gerenciadorprojeto-back -Dsonar.host.url=http://192.168.56.1:9000 -Dsonar.login=9e25125cd2c7897ba6ced991e52cc606f90cbe32"
    }
  }
}
