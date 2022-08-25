node {
  stage('SCM') {
    checkout scm
    load '$JENKINS_HOME/Variables.txt'
    echo '${PROJECT_KEY}'
    echo '${HOST_URL}'
}
  stage('SonarQube Analysis') {
    def scannerHome = tool 'SonarQube Scanner';
    withSonarQubeEnv(installationName: 'SonarQube') {
      sh "pwd"
      sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=way-web -Dsonar.host.url=http://192.168.56.1:9000 -Dsonar.login=squ_0a9408dc20c57dd0eceec761ee74cde738712a65"
    }
  }
}
