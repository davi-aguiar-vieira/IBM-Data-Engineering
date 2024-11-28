# Sorting results sets
To sort the results of a query, you can use the `ORDER BY` clause. This clause allows you to specify the column by which you want to sort the results, and you can also specify whether you want the results in ascending (`ASC`) or descending (`DESC`) order.

### Syntax
```sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1 [ASC|DESC], column2 [ASC|DESC], ...;
```

### Example
Suppose you have a table called `employees` with the following columns: `id`, `name`, and `salary`. To get a list of employees sorted by their salary in descending order, you would use the following query:

```sql
SELECT id, name, salary
FROM employees
ORDER BY salary DESC;
```

If you want to sort by multiple columns, for example, by `salary` in descending order and then by `name` in ascending order, you can do so like this:

```sql
SELECT id, name, salary
FROM employees
ORDER BY salary DESC, name ASC;
```
---
# GROUP BY clause

The `GROUP BY` clause is used in SQL to arrange identical data into groups. This is particularly useful when you want to aggregate data, such as calculating sums, averages, counts, etc., for each group of data.

### Syntax

```sql
SELECT column_name(s), aggregate_function(column_name)
FROM table_name
WHERE condition
GROUP BY column_name(s);
```
---
# HAVING clause

The `HAVING` clause is used in SQL to filter records that work on aggregated data. It is similar to the `WHERE` clause, but `WHERE` cannot be used with aggregate functions. `HAVING` was added to SQL because the `WHERE` keyword could not be used with aggregate functions.

### Syntax

```sql
SELECT column_name(s), aggregate_function(column_name)
FROM table_name
WHERE condition
GROUP BY column_name(s)
HAVING condition;
```

### Example

```sql
SELECT department, COUNT(employee_id) AS num_employees
FROM employees
GROUP BY department
HAVING COUNT(employee_id) > 10;
```

In this example, the `HAVING` clause filters the results to include only departments with more than 10 employees.