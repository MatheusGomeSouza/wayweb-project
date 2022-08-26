node {
  stage('SCM') {
    checkout scm
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'SonarQube Scanner';
    withSonarQubeEnv(installationName: 'SonarQube') {
      sh "pwd"
      sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=way-web -Dsonar.host.url=http://192.168.56.1:9000 -Dsonar.login=squ_0a9408dc20c57dd0eceec761ee74cde738712a65 -Dsonar.exclusions=wayweb/settings.py"
      waitForQualityGate abortPipeline: true
    }
  }
}
