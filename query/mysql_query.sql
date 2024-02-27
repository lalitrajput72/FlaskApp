CREATE TABLE users(
    id int NOT NULL AUTO_INCREMENT,
    name varchar(100),
    password varchar(100),
    email varchar(100),
    role_id INT,
    PRIMARY KEY (id),
    FOREIGN KEY (role_id) REFERENCES role(id)
    ON DELETE NO ACTION
    ON UPDATE CASCADE
);
-- insert into users table
insert into users values(1, "Test1", "password1", "test@mail.com", 1)
insert into users values(2, "Test2", "password2", "tj@mail.com", 2);
insert into users values(3, "Test3", "password3", "ah@mail.com", 3);
insert into users values(4, "Test4", "password4", "kk@mail.com", 4);
insert into users values(5, "Test5", "password5", "sv@mail.com", 2);

-- create role table
CREATE TABLE role (
id int NOT NULL AUTO_INCREMENT,
title varchar(45) NOT NULL,
PRIMARY KEY (id));

-- insert into role table
insert into role values(1, "superadmin");
insert into role values(2, "admin");
insert into role values(3, "user");
insert into role values(4, "guest");


-- create endpoint table
CREATE TABLE endpoints (
id int NOT NULL AUTO_INCREMENT,
endpoint varchar(255),
methods varchar(20),
PRIMARY KEY (id));

-- insert into endpoint table
insert into endpoints values(1, "/users/get", "GET");

-- create accessability table
create table accessability(
        id INT not Null AUTO_INCREMENT,
        endpoint_id int not null,
        roles LONGTEXT,
        PRIMARY KEY (id),
        FOREIGN KEY (endpoint_id) REFERENCES endpoints(id)
        ON DELETE NO ACTION
        ON UPDATE CASCADE
)
-- insert into accessability table
insert into accessability values(1, 1, "[1,2]")

-- create view
create view access_endpoint_view as
select endpoints.endpoint, accessability.roles
from endpoints join accessability
where endpoints.id = accessability.endpoint_id

-- Create employee table for employee crud operation

CREATE TABLE employee (
id int NOT NULL AUTO_INCREMENT,
name varchar(45) NOT NULL,
email varchar(50) NOT NULL,
age int, PRIMARY KEY (id));