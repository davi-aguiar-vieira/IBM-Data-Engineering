# Database Concepts and Examples

This document covers essential database concepts, including **views**, **stored procedures**, and **ACID transactions**, with examples to illustrate their use.

---

## 1. Views

### What is a View?
A **view** is a dynamic mechanism for presenting data from one or more tables. It simplifies complex queries and improves readability.

### Syntax for Creating a View
```sql
CREATE VIEW <view_name> (column_alias_1, column_alias_2, ...)
AS 
SELECT <column_1>, <column_2>, ...
FROM <table_name>
WHERE <predicate>;
```

### Benefits of Views
- Simplify data access for users.
- Abstract complex queries for better readability.
- Improve security by limiting direct access to tables.

---

## 2. Stored Procedures

### What is a Stored Procedure?
A **stored procedure** is a set of SQL statements that are stored and executed on the database server. Stored procedures reduce network traffic and execution time by encapsulating SQL logic.

### Benefits of Stored Procedures
- **Reusability**: Write once, use multiple times.
- **Maintainability**: Centralized logic simplifies updates.
- **Security**: Control access and permissions.
- **Performance**: Precompiled execution reduces overhead.

### Example: Simple Stored Procedure
```sql
CREATE PROCEDURE SelectAllCustomers()
BEGIN
    SELECT * FROM Customers;
END;
```
To execute this stored procedure:
```sql
CALL SelectAllCustomers();
```

### Example: Stored Procedure with Parameters
```sql
CREATE PROCEDURE SelectCustomerByID(IN customerID INT)
BEGIN
    SELECT * FROM Customers WHERE CustomerID = customerID;
END;
```
To execute this stored procedure with a parameter:
```sql
CALL SelectCustomerByID(1);
```

---

## 3. ACID Transactions

### What is an ACID Transaction?
An **ACID transaction** is one where all SQL statements must complete successfully, or none at all. ACID ensures reliability through the following properties:

### The Four ACID Properties

1. **Atomicity**
   - Ensures that all operations in a transaction are completed successfully. If any operation fails, the transaction is rolled back.
   - **Example**: If debiting one account fails during a bank transfer, the credit operation is also rolled back.

2. **Consistency**
   - Guarantees that a transaction transitions the database from one valid state to another, maintaining database invariants (e.g., foreign keys, constraints).
   - **Example**: A banking transaction ensures the total balance remains consistent.

3. **Isolation**
   - Ensures that transactions execute independently, preventing interference from concurrent transactions.
   - **Example**: Intermediate states of a transaction are not visible to others.

4. **Durability**
   - Once a transaction is committed, its changes are permanently stored, even in the event of a system failure.
   - **Example**: After committing a bank transfer, the updates persist despite a server crash.

---

### Example: Banking Transaction in SQL

#### Scenario
Transfer $100 from `Account A` (ID: 1) to `Account B` (ID: 2).

#### SQL Code
```sql
-- Start the transaction
BEGIN TRANSACTION;

-- Step 1: Deduct $100 from Account A
UPDATE accounts
SET balance = balance - 100
WHERE account_id = 1;

-- Step 2: Add $100 to Account B
UPDATE accounts
SET balance = balance + 100
WHERE account_id = 2;

-- Step 3: Commit or Rollback
-- If no errors occurred, commit the transaction
IF @@ERROR = 0
BEGIN
    COMMIT TRANSACTION;
END
ELSE
BEGIN
    -- Rollback in case of an error
    ROLLBACK TRANSACTION;
END;
```

### How ACID Properties Are Ensured
1. **Atomicity**: Both `UPDATE` statements succeed or fail as a unit. If one fails, the transaction rolls back.
2. **Consistency**: The total balance across accounts remains unchanged.
3. **Isolation**: Other transactions cannot access intermediate states.
4. **Durability**: Once committed, the changes are permanent.

---

### Summary
- **Views** provide simplified and secure ways to access data.
- **Stored Procedures** encapsulate reusable SQL logic, improving performance and maintainability.
- **ACID Transactions** ensure database reliability through Atomicity, Consistency, Isolation, and Durability.