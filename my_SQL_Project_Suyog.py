

import mysql.connector as sqlcon

db = sqlcon.connect(host = "localhost", user = "root", passwd = "system", database = 'essentials')

cur = db.cursor()

cur.execute("update mobile set model_number = 2020 where sname = 'Nokia'")
cur.execute("select * from mobile")

for i in cur:
	print(i)

cur.close()
db.commit()

# SQL Statements

'''

create database essentials;
drop database essentials;

show databases;
use essentials;
show tables;
create table mobile(model_number int, model_name varchar(30), year_of_manufacture int);
desc mobile;

insert into mobile values(1100, 'Nokia', 2021);
insert into mobile values(1750, 'Samsung', 2022);

select * from mobile;

update mobile set model_number = 2021 where model_name = 'Nokia';

set SQL_SAFE_UPDATES = 1;

drop table mobile;

'''