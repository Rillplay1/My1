# Удаляет старые результаты
if (Test-Path "reports/allure-results") {
    Remove-Item "reports/allure-results" -Recurse -Force
}

# Удаляет старый отчёт
if (Test-Path "reports/allure-report") {
    Remove-Item "reports/allure-report" -Recurse -Force
}

# Запускает тесты (pytest сам знает, куда класть отчёт — благодаря pytest.ini)
pytest

# Генерирует новый отчёт
allure generate reports/allure-results --clean -o reports/allure-report

# Открывает отчёт
allure open reports/allure-report