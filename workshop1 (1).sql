-- kill other connections
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'week1_workshop' AND pid <> pg_backend_pid();
-- (re)create the database
DROP DATABASE IF EXISTS week1_workshop;
CREATE DATABASE week1_workshop;
-- connect via psql
\c week1_workshop

-- database configuration
SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET default_tablespace = '';
SET default_with_oids = false;


---
--- CREATE tables
---

CREATE TABLE products (
    id SERIAL,
    name TEXT NOT NULL,
    discontinued BOOLEAN NOT NULL,
    supplier_id INT,
    category_id INT,
    PRIMARY KEY (id)
);


CREATE TABLE categories (
    id SERIAL,
    name TEXT UNIQUE NOT NULL,
    description TEXT,
    picture TEXT,
    PRIMARY KEY (id)
);

-- TODO create more tables here...

-- Task 1

CREATE TABLE suppliers (
    id SERIAL,
    supplier_id INT NOT NULL,
    PRIMARY KEY(id)
);

-- Task 2

CREATE TABLE customers (
    id SERIAL,
    company_name TEXT NOT NULL,
    PRIMARY KEY(id)
);


-- task 3
CREATE TABLE employees (
    id SERIAL,
    first_name TEXT NOT NULL,
    last_name text NOT NULL,
    PRIMARY KEY(id)

);

---- task 4

CREATE TABLE orders (
    id SERIAL,
    date date,
    customer_id int not NULL,
    employee_id int,
    PRIMARY KEY(id)
);

--- task 5
CREATE TABLE orders_products (
    product_id int NOT NULL,
    order_id int NOT NULL,
    quantity int Not Null,
    discount numeric Not Null,
    PRIMARY KEY(product_id,order_id)
);

---Task 6
CREATE TABLE territories (
    id int  NOT NULL,
    description text Not Null,
    PRIMARY KEY (id)
);

--task 7
CREATE TABLE employees_territories (
    employee_id int NOT NULL,
    territory_id int NOT NULL,
    PRIMARY KEY(employee_id,territory_id)
);

--ttask 8
CREATE TABLE Offices(
    id SERIAL,
    address_line text NOT Null,
    PRIMARY KEY(id),
    territory_id int Not Null
);

---TASK 9

CREATE  TABLE us_states (
    id int NOT NULL,
    name text Not Null,
    abbreviation character(2) Not Null,
    PRIMARY KEY(id)
);


--- Add foreign key constraints
---




-- PRODUCTS

ALTER TABLE products
ADD CONSTRAINT fk_products_categories 
FOREIGN KEY (category_id) 
REFERENCES categories (id);

--task 10

ALTER TABLE products
ADD CONSTRAINT fk_orders_customers
FOREIGN KEY (customer_id) 
REFERENCES employee_id (id);

--task 11 

ALTER TABLE products
ADD CONSTRAINT fk_products_suppliers
FOREIGN KEY (supplier_id) 
REFERENCES suppliers (id);

---task 12
ALTER TABLE orders
ADD CONSTRAINT fk_orders_customers
FOREIGN KEY (customers_id) 
REFERENCES customers (id);

---task 13
ALTER TABLE employees_territories
add CONSTRAINT fk_employees_territories_employees
FOREIGN KEY (employee_id)
REFERENCES employees (id);

---task 14
alter table Offices
add CONSTRAINT fk_Offices_territories
FOREIGN KEY (territory_id)
REFERENCES territories (id);





-- TODO create more constraints here...


