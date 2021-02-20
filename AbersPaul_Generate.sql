DROP DATABASE IF EXISTS FAKE_AMAZON;
CREATE DATABASE FAKE_AMAZON;
USE FAKE_AMAZON;
-- tables
-- Table: call
CREATE TABLE COMPANY (
    id int  NOT NULL,
    cname varchar(255) NOT NULL,
    address varchar(255),
    country_code varchar(64)  NOT NULL,
    CONSTRAINT UNIQUE (cname),
    CONSTRAINT company_pk PRIMARY KEY (id)
);

INSERT INTO COMPANY (id, cname, address, country_code) VALUES (1,'Electron','Sante Fe, NM','United States');
INSERT INTO COMPANY (id, cname, address, country_code) VALUES (2,'Intensity','New York NY','United States');
INSERT INTO COMPANY (id, cname, address, country_code) VALUES (3,'Danke','Munich','Germany');
INSERT INTO COMPANY (id, cname, address, country_code) VALUES (4,'Voules Vouz','Place de Italie, Paris','France');


CREATE TABLE USER (
    id int  NOT NULL,
    firstname varchar(32) NOT NULL,
    lastname varchar(32) NOT NULL,
    address varchar(255)  NOT NULL,
    CONSTRAINT user_pk PRIMARY KEY  (id)
);

INSERT INTO USER (id, firstname, lastname, address) VALUES (1,'Jennifer','Smith','Austin, TX');
INSERT INTO USER (id, firstname, lastname, address) VALUES (2,'Adam',' Smith','Glasgow, Scotland');
INSERT INTO USER (id, firstname, lastname, address) VALUES (3,'Pierangelo','Pirlo','Firenze, Italy');
INSERT INTO USER (id, firstname, lastname, address) VALUES (4,'Tim','Nguyen','Hanoi, Vietnam');

CREATE TABLE PRODUCT (
    id int  NOT NULL,
    product_name varchar(128) NOT NULL,
    category int NOT NULL,
    company_id int NOT NULL,
    price float NOT NULL,
    valid boolean NOT NULL,
    FOREIGN KEY (company_id) REFERENCES COMPANY(id),
    CONSTRAINT product_pk PRIMARY KEY  (id)
);

INSERT INTO PRODUCT (id, product_name, category, company_id, price, valid) VALUES (1,'Awesome Phone',1,1,754.75,true);
INSERT INTO PRODUCT (id, product_name, category, company_id, price, valid) VALUES (2,'Knock Off Phone',1,2,354.23,true);
INSERT INTO PRODUCT (id, product_name, category, company_id, price, valid) VALUES (3,'Jeans',2,3,24.99,true);
INSERT INTO PRODUCT (id, product_name, category, company_id, price, valid) VALUES (4,'Silver Cutlery', 3, 4, 250.0, true);
-- FOREIGN KEY (category) REFERENCES PRODUCT(category),
CREATE TABLE PRODUCT_TYPES (
    category int NOT NULL,
    category_name varchar(32) NOT NULL,
    CONSTRAINT product_types_pk PRIMARY KEY (category)
);

INSERT INTO PRODUCT_TYPES (category, category_name) VALUES (1, 'Phone');
INSERT INTO PRODUCT_TYPES (category, category_name) VALUES (2, 'Clothing');
INSERT INTO PRODUCT_TYPES (category, category_name) VALUES (3, 'Home');

CREATE TABLE SUPPORT (
    company_id int  NOT NULL,
    contact_name varchar(128),
    contact_email varchar(128),
    contact_phone bigint,
    FOREIGN KEY (company_id) REFERENCES COMPANY(id),
    CONSTRAINT support_pk PRIMARY KEY (company_id)
);

INSERT INTO SUPPORT (company_id, contact_name, contact_email) VALUES (1, 'Support Team', 'support@electron.com');
INSERT INTO SUPPORT (company_id, contact_name, contact_email, contact_phone) VALUES (2,'Anderson Silva', 'anderson.silva@intensity.com',9213242949);
INSERT INTO SUPPORT (company_id, contact_name, contact_phone) VALUES (3,'Craig Doyle', 2943842929);
INSERT INTO SUPPORT (company_id, contact_name, contact_email) VALUES (4,'Susan Dowling','susan@gmail.com');


CREATE TABLE TRANSACTIONS (
    id int  NOT NULL,
    user_id int NOT NULL,
    product_id int NOT NULL,
    quantity int NOT NULL,
    transact_date date NOT NULL,
    FOREIGN KEY (user_id) REFERENCES USER(id),
    FOREIGN KEY (product_id) REFERENCES PRODUCT(id),
    CONSTRAINT transaction_pk PRIMARY KEY  (id)
);

INSERT INTO TRANSACTIONS (id, user_id, product_id, quantity, transact_date) VALUES (1,1,1,1, '2021-02-15 15:24:00');
INSERT INTO TRANSACTIONS (id,  user_id, product_id, quantity, transact_date) VALUES (2,2,1,2,'2021-02-13 11:36:12');
INSERT INTO TRANSACTIONS (id, user_id, product_id, quantity, transact_date) VALUES (3,2,3,4,'2021-02-11 20:45:07');
INSERT INTO TRANSACTIONS (id, user_id, product_id, quantity, transact_date) VALUES (4,4,4,1,'2021-02-09 06:12:12');

CREATE TABLE RET (
    id int  NOT NULL,
    transaction_id int NOT NULL,
    quantity int NOT NULL ,
    return_date date NOT NULL,
    FOREIGN KEY (transaction_id) REFERENCES TRANSACTIONS(id),
    CONSTRAINT UNIQUE (id),
    CONSTRAINT return_pk PRIMARY KEY  (id)
);

INSERT INTO RET (id, transaction_id, quantity, return_date) VALUES (1, 2, 1, '2021-02-19 15:24:00');
INSERT INTO RET (id, transaction_id, quantity, return_date) VALUES (2, 4, 1, '2021-02-20 15:24:00');
INSERT INTO RET (id, transaction_id, quantity, return_date) VALUES (3, 3, 3, '2021-02-24 15:24:00');
INSERT INTO RET (id, transaction_id, quantity, return_date) VALUES (4, 1, 1, '2021-02-28 15:24:00');
