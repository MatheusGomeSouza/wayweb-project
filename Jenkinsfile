node {
  
  environment{
    PROJECT_KEY="way-web"
    HOST_URL="http://192.168.56.1:9000"
    LOGIN="squ_0a9408dc20c57dd0eceec761ee74cde738712a65"
    EXCLUSIONS="wayweb/settings.py"
  }
  
  stage('SCM') {
    checkout scm
    load 'Variables.txt'
    echo '${PROJECT_KEY}'
    echo '${HOST_URL}'
}
  stage('SonarQube Analysis') {
    def scannerHome = tool 'SonarQube Scanner';
    withSonarQubeEnv(installationName: 'SonarQube') {
      sh "pwd"
      sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=$PROJECT_KEY -Dsonar.host.url=$HOST_URL -Dsonar.login=$LOGIN"
    }
  }
}
