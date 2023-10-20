-- LOAD DATA INFILE "./temperatures.sql" INTO temperatures



--curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/temperatures.sql" -s | mysql -uroot -p hbtn_0c_0
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
