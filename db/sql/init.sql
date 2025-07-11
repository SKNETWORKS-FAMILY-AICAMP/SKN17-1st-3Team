create user ohgiraffers@'%' identified by 'ohgiraffers';

create database menudb;
create database employeedb;
create database cardb;

show databases;

grant all privileges on menudb.* to ohgiraffers@'%';
grant all privileges on employeedb.* to ohgiraffers@'%';
grant all privileges on cardb.* to ohgiraffers@'%';

show grants for ohgiraffers@'%';