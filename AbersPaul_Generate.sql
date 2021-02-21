DROP DATABASE IF EXISTS FAKE_AMAZON;
CREATE DATABASE FAKE_AMAZON;
USE FAKE_AMAZON;


CREATE TABLE COMPANY (
    id int  NOT NULL AUTO_INCREMENT,
    cname varchar(255) NOT NULL,
    address varchar(255),
    country_code varchar(64)  NOT NULL,
    CONSTRAINT UNIQUE (cname),
    CONSTRAINT company_pk PRIMARY KEY (id)
);

INSERT INTO COMPANY (cname, address, country_code) VALUES ('Electron','Sante Fe, NM','United States');
INSERT INTO COMPANY (cname, address, country_code) VALUES ('Intensity','New York NY','United States');
INSERT INTO COMPANY (cname, address, country_code) VALUES ('Danke','Munich','Germany');
INSERT INTO COMPANY (cname, address, country_code) VALUES ('Voules Vouz','Place de Italie, Paris','France');


CREATE TABLE USER (
    id int  NOT NULL AUTO_INCREMENT,
    firstname varchar(32) NOT NULL,
    lastname varchar(32) NOT NULL,
    address varchar(255)  NOT NULL,
    CONSTRAINT user_pk PRIMARY KEY  (id)
);

INSERT INTO USER (firstname, lastname, address) VALUES ('Jennifer','Smith','Austin, TX');
INSERT INTO USER (firstname, lastname, address) VALUES ('Adam',' Smith','Glasgow, Scotland');
INSERT INTO USER (firstname, lastname, address) VALUES ('Pierangelo','Pirlo','Firenze, Italy');
INSERT INTO USER (firstname, lastname, address) VALUES ('Tim','Nguyen','Hanoi, Vietnam');

CREATE TABLE PRODUCT (
    id int  NOT NULL AUTO_INCREMENT,
    product_name varchar(128) NOT NULL,
    category int NOT NULL DEFAULT 4,
    company_id int NOT NULL,
    price float NOT NULL,
    FOREIGN KEY (company_id) REFERENCES COMPANY(id),
    CONSTRAINT product_pk PRIMARY KEY  (id)
);

INSERT INTO PRODUCT (product_name, category, company_id, price) VALUES ('Awesome Phone',1,1,754.75);
INSERT INTO PRODUCT (product_name, category, company_id, price) VALUES ('Knock Off Phone',1,2,354.23);
INSERT INTO PRODUCT (product_name, category, company_id, price) VALUES ('Jeans',2,3,24.99);
INSERT INTO PRODUCT (product_name, category, company_id, price) VALUES ('Silver Cutlery', 3, 4, 250.0);
INSERT INTO PRODUCT (product_name, company_id, price) VALUES ('Juggling Clubs', 4, 12.50);

CREATE TABLE PRODUCT_TYPES (
    category int NOT NULL,
    category_name varchar(32) NOT NULL,
    CONSTRAINT product_types_pk PRIMARY KEY (category)
);

INSERT INTO PRODUCT_TYPES (category, category_name) VALUES (1, 'Phone');
INSERT INTO PRODUCT_TYPES (category, category_name) VALUES (2, 'Clothing');
INSERT INTO PRODUCT_TYPES (category, category_name) VALUES (3, 'Home');
INSERT INTO PRODUCT_TYPES (category, category_name) VALUES (4, 'Miscellaneous');

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
    id int  NOT NULL AUTO_INCREMENT,
    user_id int NOT NULL,
    product_id int NOT NULL,
    quantity int NOT NULL,
    transact_date date NOT NULL,
    FOREIGN KEY (user_id) REFERENCES USER(id),
    FOREIGN KEY (product_id) REFERENCES PRODUCT(id),
    CONSTRAINT transaction_pk PRIMARY KEY  (id)
);

INSERT INTO TRANSACTIONS (user_id, product_id, quantity, transact_date) VALUES (1,1,1, '2021-02-15');
INSERT INTO TRANSACTIONS (user_id, product_id, quantity, transact_date) VALUES (2,1,2,'2021-02-13');
INSERT INTO TRANSACTIONS (user_id, product_id, quantity, transact_date) VALUES (2,3,4,'2021-02-11');
INSERT INTO TRANSACTIONS (user_id, product_id, quantity, transact_date) VALUES (4,4,1,'2021-02-09');
