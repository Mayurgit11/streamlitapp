pipeline {
    agent any
    stages {
        stage('checkout code'){
            git url:'https://github.com/Mayurgit11/streamlitapp.git',branch:'main'
        }
    }
}