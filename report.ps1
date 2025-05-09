if (Test-Path "reports/allure-report") {
    Remove-Item "reports/allure-report" -Recurse -Force
}

allure generate reports/allure-results --clean -o reports/allure-report

allure open reports/allure-report