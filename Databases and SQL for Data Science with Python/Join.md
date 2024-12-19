# Joins

### Inner join
An inner join returns only the rows that have matching values in both tables.

### Left (Outer) Join
A left join returns all rows from the left table, and the matched rows from the right table. If no match is found, NULL values are returned for columns from the right table.

### Right (Outer) Join
A right join returns all rows from the right table, and the matched rows from the left table. If no match is found, NULL values are returned for columns from the left table.

### Full (Outer) Join
A full join returns all rows when there is a match in either left or right table. If there is no match, the result is NULL on the side that does not have a match.

### Syntax

#### Inner Join
```sql
SELECT columns
FROM table1
INNER JOIN table2
ON table1.column = table2.column;
```

#### Left Join
```sql
SELECT columns
FROM table1
LEFT JOIN table2
ON table1.column = table2.column;
```

#### Right Join
```sql
SELECT columns
FROM table1
RIGHT JOIN table2
ON table1.column = table2.column;
```

#### Full Join
```sql
SELECT columns
FROM table1
FULL OUTER JOIN table2
ON table1.column = table2.column;
```