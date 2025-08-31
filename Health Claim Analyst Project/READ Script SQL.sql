-#¿Qué diagnósticos son los más costosos?  
SELECT diagnosis,SUM(cost) as Total_cost
FROM claims
GROUP BY diagnosis
ORDER BY Total_cost DESC
LIMIT 10;

-#¿Existen diferencias entre regiones? 
#Average cost by region
SELECT region,round(AVG(cost),2) as Average_cost_region
FROM claims
GROUP BY region
ORDER BY Average_cost_region  DESC;

-#total cost by region
SELECT region,count(claim_id),round(SUM(cost),2) as Total_costo_region
FROM claims
GROUP BY region
ORDER BY Total_costo_region DESC;

-¿Cómo varía el costo por día de hospitalización?  
SELECT strftime('%w', admission_date) AS day_of_week,
ROUND(AVG(cost_per_day), 2) AS avg_cost_per_day,
COUNT(*) AS claims
FROM claims
GROUP BY day_of_week
ORDER BY day_of_week;

- ¿Qué grupos de edad concentran más gasto?  
SELECT age_band, SUM(cost) AS TOTAL_COST
FROM claims
GROUP BY age_band
ORDER BY TOTAL_COST DESC;

- Total promedio de gastos
SELECT Round(SUM(cost), 2) as Total_cost, Round(Avg(cost), 2) As Average_cost
FROM claims;

- Promedio de días de hospitalización
SELECT Round(Avg(los_days), 0) as Average_days
FROM claims;

- costo promedio por dia
SELECT Round(Avg(los_days), 0) as Average_days
FROM claims;

- Costo total por día
SELECT
    strftime ('%w', admission_date) AS day_of_week,
    ROUND(sum(cost_per_day), 2) AS cost_per_day,
    COUNT(*) AS claims
FROM claims
GROUP BY
    day_of_week
ORDER BY day_of_week;
