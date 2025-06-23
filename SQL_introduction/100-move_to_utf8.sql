-- Modify charset of selected column
USE hbtn_0c_0;

ALTER TABLE
    first_table
MODIFY
    COLUMN name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci