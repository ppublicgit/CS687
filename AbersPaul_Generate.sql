-- tables
-- Table: call
CREATE TABLE COMPANY (
    id int  NOT NULL,
    cname varchar(255) NOT NULL,
    address varchar(255),
    country_code varchar(3)  NOT NULL,
    CONSTRAINT UNIQUE (id),
    CONSTRAINT UNIQUE (cname),
    CONSTRAINT company_pk PRIMARY KEY (id)
);

CREATE TABLE USER (
    id int  NOT NULL,
    firstname varchar(32) NOT NULL,
    lastname varchar(32) NOT NULL,
    address varchar(255)  NOT NULL,
    CONSTRAINT user_pk PRIMARY KEY  (id)
);

CREATE TABLE PRODUCT (
    id int  NOT NULL,
    product_name varchar(128) NOT NULL,
    category int,
    company_id int NOT NULL,
    price float NOT NULL,
    FOREIGN KEY (company_id) REFERENCES COMPANY(id),
    CONSTRAINT product_pk PRIMARY KEY  (id)
);

CREATE TABLE SUPPORT (
    company_id int  NOT NULL,
    contact_name varchar(128),
    contact_email varchar(128),
    contact_phone int,
    FOREIGN KEY (company_id) REFERENCES COMPANY(id),
    CONSTRAINT support_pk PRIMARY KEY (company_id)
);

CREATE TABLE TRANSACTIONS (
    id int  NOT NULL,
    company_id int NOT NULL,
    user_id int NOT NULL,
    product_id int NOT NULL,
    quantity int NOT NULL,
    transact_date date NOT NULL,
    FOREIGN KEY (company_id) REFERENCES COMPANY(id),
    FOREIGN KEY (user_id) REFERENCES USER(id),
    FOREIGN KEY (product_id) REFERENCES PRODUCT(id),
    CONSTRAINT transaction_pk PRIMARY KEY  (id)
);

CREATE TABLE RET (
    id int  NOT NULL,
    transaction_id int NOT NULL,
    quantity int NOT NULL CHECK (quantity < TRANSACTIONS(quantity),
    return_date date NOT NULL,
    FOREIGN KEY (transaction_id) REFERENCES TRANSACTIONS(id),
    CONSTRAINT UNIQUE (id),
    CONSTRAINT return_pk PRIMARY KEY  (id)
);
