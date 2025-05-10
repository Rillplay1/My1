if (Test-Path "reports/allure-report")
#Проверяет существует ли папка reports/allure-report
{Remove-Item "reports/allure-report" -Recurse -Force}
#Если существует то удаляет её полностью. Это делается, чтобы перед генирацией нового отчёта очистить старый

allure generate reports/allure-results --clean -o reports/allure-report
#Команда allure generate собирает отчёт на основе данных, которые находятся в папке reports/allure-results.
# Ключ --clean — очищает перед этим папку назначения, на всякий случай.
# -o reports/allure-report — говорит Allure: "Создай новый отчёт в папке reports/allure-report".

allure open reports/allure-report
#Открывает сгенирированый allure отчёт в браузере