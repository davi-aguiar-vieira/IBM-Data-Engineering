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