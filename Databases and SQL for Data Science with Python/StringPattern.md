# String patterns

To find records that match a specific pattern in SQL, you can use the `LIKE` operator. Here is a general example:

```sql
SELECT *
FROM employees
WHERE first_name LIKE 'J%';
```

In this example, the query selects all records from the `employees` table where the `first_name` starts with the letter 'J'. The `%` wildcard character represents zero or more characters.

# Range
To filter records based on a range of values, you can use comparison operators such as `>=` and `<=`. Here is an example:

```sql
SELECT *
FROM employees
WHERE salary BETWEEN 50000 AND 100000;
```

In this example, the query selects all records from the `employees` table where the `salary` is between 50,000 and 100,000 inclusive.

# IN
To filter records based on a set of values, you can use the `IN` operator. Here is an example:

```sql
SELECT *
FROM employees
WHERE country IN ('BRA', 'USA');
```

In this example, the query selects all records from the `employees` table where the `country` is either 'BRA' (Brazil) or 'USA' (United States).