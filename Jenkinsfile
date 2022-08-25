node {
  environment {
    DISABLE_AUTH = 'true'
    DB_ENGINE    = 'sqlite'
  }
  stage('SCM') {
    checkout scm
    echo "Database engine is ${DB_ENGINE}"
    echo "DISABLE_AUTH is ${DISABLE_AUTH}"
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'SonarQube Scanner';
    withSonarQubeEnv(installationName: 'SonarQube') {
      sh "pwd"
      sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=way-web -Dsonar.host.url=http://192.168.56.1:9000 -Dsonar.login=squ_0a9408dc20c57dd0eceec761ee74cde738712a65"
    }
  }
}
