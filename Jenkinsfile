pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Python Data Validation') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                python app/check_data.py
                '''
            }
        }

        stage('Run Selenium TestNG Tests') {
            steps {
                sh '''
                cd tests/selenium
                mvn test
                '''
            }
        }

    }
}