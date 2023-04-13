pipeline {
  agent any
  stages {
    stage('stage') {
      steps {
        sh '''pipeline {

    agent any

 

    stages {

        stage(\'Dev\') {

            steps {

                script {

                    def generateDummyData = load \'path/to/your/python/file.py\'

                    def data = generateDummyData(\'Dev\', 0.8) // 80% success rate

                    if (data != null) {

                        echo "Dev data: ${data}"

                    } else {

                        error "Dev stage failed"

                    }

                }

            }

        }

        stage(\'Qa\') {

            steps {

                script {

                    def generateDummyData = load \'path/to/your/python/file.py\'

                    def data = generateDummyData(\'Qa\', 0.5) // 50% success rate

                    if (data != null) {

                        echo "Qa data: ${data}"

                    } else {

                        error "Qa stage failed"

                    }

                }

            }

        }

        stage(\'Uat\') {

            steps {

                script {

                    def generateDummyData = load \'path/to/your/python/file.py\'

                    def data = generateDummyData(\'Uat\', 0.2) // 20% success rate

                    if (data != null) {

                        echo "Uat data: ${data}"

                    } else {

                        error "Uat stage failed"

                    }

                }

            }

        }

        stage(\'Prod\') {

            steps {

                script {

                    def generateDummyData = load \'path/to/your/python/file.py\'

                    def data = generateDummyData(\'Prod\', 1.0) // always succeeds

                    echo "Prod data: ${data}"

                }

            }

        }

    }

}'''
        }
      }

    }
  }