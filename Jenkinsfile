pipeline {
  agent any

  stages {
    stage('Exécution du script') {
      steps {
        echo "Exécution du script Python"
        sh 'python3 code.py'
      }
    }

    stage('Tests unitaires') {
      steps {
        echo "Tests avec unittest"
        sh 'python3 -m unittest test_code.py'
      }
    }
  }

  post {
    failure {
      emailext(
        to: 'cv.04@laposte.net',
        subject: "❌ ECHEC : ${env.JOB_NAME} #${env.BUILD_NUMBER}",
        body: """
Bonjour,

Le build ${env.JOB_NAME} #${env.BUILD_NUMBER} a échoué.

🔗 Voir les logs ici : ${env.BUILD_URL}
"""
      )
    }
  }
}
