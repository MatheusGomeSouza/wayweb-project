node {
  stage('SCM') {
    checkout scm
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'SonarQube Scanner';
    withSonarQubeEnv(installationName: 'SonarQube') {
      sh "pwd"
      sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=way-web -Dsonar.host.url=http://192.168.56.1:9000 -Dsonar.login=157a9a741dc7b56f86826d3d8b6c61676881d0a0 -Dsonar.exclusions=wayweb/settings.py -Dsonar.sources=."
    }
    sleep 10 // seconds
    def qualityGate = waitForQualityGate() 
      if (qualityGate.status != 'OK') {
        error "O código não está de acordo com as regras do Sonar: ${qualityGate.status}"
    }
  }
}
