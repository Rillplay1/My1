if (Test-Path "allure-report") {
    Remove-Item "allure-report" -Recurse -Force
}

allure generate allure-results --clean -o allure-report

allure open allure-report