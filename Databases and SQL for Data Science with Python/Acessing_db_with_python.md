# Concepts of the Python DB API

## Connection Objects
- Database connections
- Manage transactions

## Cursor Objects
- Database Queries
- Scroll through result set
- Retrieve results

---

### Connection methods
- `.cursor()`
- `.commit()`
- `.rollback()`
- `.close()`

```PYTHON
from dbmodule import connect

# Create connection object
Connection = connect('database_name', 'username', 'pswd')

# Create a cursor object
Cursor = connection.cursor()

# Run queries
Cursor.execute('SELECT * FROM table_name')
Results = cursor.cursor.fetchall()

# Free resources
Cursor.close()
Connection.close()
```