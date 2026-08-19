@echo off

call .QAvenv\Scripts\activate.bat

echo ==============================
echo remove last report data
echo ==============================


if exist allure-results (
    rmdir /s /q allure-results
)



echo ==============================
echo Running Pytest Tests
echo ==============================

pytest -m blocker

echo.
echo ==============================
echo Opening Allure Report
echo ==============================

allure serve allure-results