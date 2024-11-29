# Bulti-in Database Functions

## Aggregate or Column Functions
- **INPUT**: Collection of values 
- **OUTPUT**: Single value
- Examples: **SUM()**, **MIN()**, **MAX()**, **AVG()**
---
### SUM
```sql
sum(COLUMN_NAME)
```
> Returns the sum of all the values in a column
---
### MIN / MAX
```sql
SELECT MAX(COLUMN_NAME) FROM TABLE_NAME
```
> **MAX()**: Return the MAXIMUN value
> **MIN()**: Return the MINIMUM value
---
### AVERAGE
```sql
SELECT AVG(COLUMN_NAME0) FROM TABLE_NAME
```
> Returns the average or mean of a column
---

# Scalar and String Functions
- **Scalar**: Perform operations on every input value
- Examples: **ROUND()**, **LENGTH()**, **UCASE**, **LCASE**
**ROUND()**: Round the number to the nearest integer
**LENGHT()**: Retrive the lenght of each value
**UCASE**: UPPERCASE
**LCASE**: LOWERCASE 
 