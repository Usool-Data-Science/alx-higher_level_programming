-- creates hbtn_0d_2 and user_0d_2 (Database and user) respectively
-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create user
USE hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_02@localhost IDENTIFIED by 'user_0d_2_pwd';
-- grant SELECT privileges only to the user.
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
