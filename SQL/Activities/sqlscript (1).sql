REM   Script: Session 01
REM   SQL Basic features CREATE, INSERT, SELECT

CREATE TABLE Customers(cust_id int PRIMARY KEY, cust_name varchar(32), cust_location varchar(10));

INSERT INTO Customers VALUES(1, 'Alpha', 'Hyderabad');

INSERT INTO Customers(cust_id, cust_name) VALUES(2, 'Beta');

SELECT * FROM Customers;

CREATE TABLE salesman(salesman_id int, salesman_name varchar2(20), salesman_city varchar2(20), commission int);

INSERT INTO salesman VALUES (5001, 'James Hoog', 'New York', 15);

INSERT INTO salesman VALUES (5002, 'Nail Knite', 'Paris', 13);

INSERT INTO salesman VALUES (5005, 'Pit Alex', 'London', 11);

INSERT INTO salesman VALUES (5006, 'McLyon', 'Paris', 14);

INSERT INTO salesman VALUES (5007, 'Paul Adam', 'Rome', 13);

INSERT INTO salesman VALUES (5003, 'Lauson Hen', 'San Jose', 12);

SELECT salesman_id, salesman_city from salesman;

SELECT * from salesman WHERE salesman_city = 'Paris';

SELECT salesman_id, commission FROM salesman WHERE salesman_name = 'Paul Adam';

