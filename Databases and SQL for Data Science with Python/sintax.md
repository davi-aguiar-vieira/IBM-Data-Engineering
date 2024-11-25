## Some syntax examples for Data Manipulation Language (DML)

### - Syntax of **INSERT** statement
```SQL
INSERT INTO table_name (column1, column2, ... )
VALUES (value1, value2, ... );
```

### - Syntax of **UPDATE** statement
```SQL
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

### - Syntax of **DELETE** statement
```SQL
DELETE FROM table_name
WHERE condition;
```
---
## Some syntax examples for Data Definition Language (DDL)

### - Syntax of **ALTER TABLE** statement
#### Add column
```SQL
ALTER TABLE table_name
ADD column_name data_type;
```

```SQL
ALTER TABLE table_name
ADD COLUMN column_name data_type;
```
#### Modify data type
```SQL
ALTER TABLE table_name
MODIFY column_name data_type;
```
#### Remove column
```SQL
ALTER TABLE table_name
DROP COLUMN column_name;
```

### - Syntax of **TRUNCATE** statement
#### Delete all the rows in a table
```SQL
TRUNCATE TABLE table_name;
```
