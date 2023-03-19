SELECT * FROM Employees;
SELECT * FROM Employees WHERE first_name = 'David';
SELECT * FROM Employees WHERE department_id IN (20, 30);
SELECT * FROM Employees WHERE department_id IN (50, 80) AND commission_pct IS NOT NULL;
SELECT * FROM Employees WHERE hire_date LIKE '%-01';
SELECT * FROM Employees WHERE hire_date LIKE '2008-%';
SELECT CONCAT('Tomorrow is ', DATE_FORMAT(DATE_ADD(NOW(), INTERVAL 1 DAY), '%D day of %M')) AS tomorrow_date FROM DUAL;
SELECT CONCAT(DATE_FORMAT(hire_date, '%D of %M, %Y')) AS hire_date_format FROM Employees;
SELECT CONCAT('$ ', FORMAT((salary * 1.2), 2)) AS increased_salary FROM Employees;
SELECT * FROM Employees WHERE hire_date BETWEEN '2007-02-01' AND '2007-02-28';
SELECT NOW(), DATE_ADD(NOW(), INTERVAL 1 SECOND), DATE_ADD(NOW(), INTERVAL 1 MINUTE), DATE_ADD(NOW(), INTERVAL 1 HOUR), DATE_ADD(NOW(), INTERVAL 1 DAY), DATE_ADD(NOW(), INTERVAL 1 MONTH), DATE_ADD(NOW(), INTERVAL 1 YEAR) FROM DUAL;
SELECT CONCAT(CASE WHEN commission_pct IS NULL THEN 'No' ELSE 'Yes' END) AS has_bonus FROM Employees;
