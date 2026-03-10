CREATE DATABASE covid_analysis;
USE covid_analysis;

CREATE TABLE covid_data (
    date DATE,
    country VARCHAR(100),
    confirmed INT,
    deaths INT,
    recovered INT,
    active INT
);
//total cases country wise

SELECT country, SUM(confirmed) AS total_confirmed
FROM covid_data
GROUP BY country
ORDER BY total_confirmed DESC;

SELECT country, SUM(deaths) AS total_deaths
FROM covid_data
GROUP BY country
ORDER BY total_deaths DESC
LIMIT 5;

SELECT date, SUM(confirmed) AS daily_cases
FROM covid_data
GROUP BY date
ORDER BY date;