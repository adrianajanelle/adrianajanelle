
SQL Libreria Master!
-- =====================================
-- 📘 SQL FUNCTIONS CHEATSHEET
-- =====================================

-- 🔹 AGGREGATE FUNCTIONS
-- Estas se usan con GROUP BY para resumir datos

SELECT 
    COUNT(*) AS total_filas,         -- Cuenta el total de filas
    SUM(salary) AS total_sueldos,    -- Suma total de un campo numérico
    AVG(age) AS edad_promedio,       -- Calcula el promedio
    MIN(age) AS edad_menor,          -- Valor mínimo
    MAX(age) AS edad_mayor           -- Valor máximo
FROM empleados;

-- 🔹 STRING FUNCTIONS
-- Manipulan texto o cadenas (strings)

SELECT 
    UPPER(nombre) AS mayuscula,      -- Convierte a mayúsculas
    LOWER(nombre) AS minuscula,      -- Convierte a minúsculas
    LENGTH(nombre) AS largo,         -- Cuenta caracteres
    TRIM(nombre) AS limpio,          -- Elimina espacios al principio/final
    SUBSTRING(nombre, 1, 3) AS abreviatura -- Extrae parte del string
FROM empleados;

-- 🔹 DATE FUNCTIONS
-- Trabajan con fechas

SELECT 
    CURRENT_DATE AS hoy,              -- Fecha de hoy
    CURRENT_TIMESTAMP AS fecha_hora,  -- Fecha y hora actual
    EXTRACT(YEAR FROM fecha_nac) AS año, -- Extrae año de una fecha
    DATE_PART('month', fecha_nac) AS mes  -- Extrae mes
FROM empleados;

-- 🔹 MATH FUNCTIONS
-- Operaciones matemáticas básicas

SELECT 
    ROUND(sueldo, 2) AS sueldo_redondeado,  -- Redondea con 2 decimales
    CEIL(sueldo) AS techo,                  -- Redondea hacia arriba
    FLOOR(sueldo) AS piso,                  -- Redondea hacia abajo
    ABS(balance) AS valor_absoluto          -- Convierte negativo a positivo
FROM finanzas;

-- 🔹 CONDITIONAL FUNCTION
-- Devuelve valores basados en una condición

SELECT 
    nombre,
    CASE 
        WHEN edad < 18 THEN 'Menor'
        WHEN edad BETWEEN 18 AND 64 THEN 'Adulto'
        ELSE 'Senior'
    END AS categoria_edad
FROM empleados;

-- 🔹 NULL FUNCTIONS
-- Trabajan con valores nulos

SELECT 
    COALESCE(correo, 'No disponible') AS correo_seguro, -- Devuelve valor alterno si es NULL
    NULLIF(departamento, '') AS depto_valido            -- Devuelve NULL si ambos son iguales
FROM empleados;

-- 🔹 CONVERSION FUNCTIONS
-- Convierten tipos de datos

SELECT 
    CAST(sueldo AS VARCHAR) AS sueldo_texto,
    CONVERT(DATE, fecha_hora) AS solo_fecha
FROM pagos;

-- 🔹 BONUS: FILTRADO Y AGRUPACIÓN

-- WHERE: filtra antes de agrupar
-- HAVING: filtra después de agrupar

SELECT departamento, COUNT(*) AS total
FROM empleados
WHERE activo = true
GROUP BY departamento
HAVING COUNT(*) > 5;


