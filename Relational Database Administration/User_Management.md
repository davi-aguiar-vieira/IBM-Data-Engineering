# User Management and Access Control in PostgreSQL

## Creating Roles with Different Privileges

### 1. Creating a Read-Only Role
```sql
CREATE ROLE read_only;
```
- This command creates a new role called `read_only`. A role in PostgreSQL can be a user or a group of users with specific privileges.

```sql
GRANT CONNECT ON DATABASE my_database TO read_only;
```
- Grants the `read_only` role permission to connect to the specified database.

```sql
GRANT USAGE ON SCHEMA my_schema TO read_only;
```
- Allows the `read_only` role to access objects in the specified schema without modifying them.

```sql
GRANT SELECT ON ALL TABLES IN SCHEMA my_schema TO read_only;
```
- Grants read-only access (SELECT) to all tables within the schema.

### 2. Creating a Read-Write Role
```sql
CREATE ROLE read_write;
```
- Creates a role called `read_write`, which will have additional privileges beyond reading data.

```sql
GRANT CONNECT ON DATABASE my_database TO read_write;
```
- Allows the `read_write` role to connect to the database.

```sql
GRANT USAGE ON SCHEMA my_schema TO read_write;
```
- Grants access to the schema, allowing interaction with objects inside it.

```sql
GRANT SELECT, INSERT, DELETE, UPDATE ON ALL TABLES IN SCHEMA my_schema TO read_write;
```
- Provides full data modification privileges (read, insert, update, and delete) on all tables in the schema.

## Creating Users and Assigning Roles

```sql
CREATE USER my_user WITH PASSWORD 'secure_password';
```
- Creates a new user with a specified password.

```sql
GRANT read_only TO my_user;
```
- Assigns the `read_only` role to the user, inheriting all associated privileges.

## Checking Assigned Roles
```sql
\du
```
- Lists all roles and their attributes, including which roles have been granted to which users.

## Revoking Privileges

```sql
REVOKE SELECT ON my_table FROM my_user;
```
- Removes the SELECT permission from the specified table for the user.

```sql
REVOKE read_only FROM my_user;
```
- Removes the `read_only` role from the user, stripping away all associated privileges.

## Notes:
- When granting permissions, it is best practice to assign privileges to roles instead of directly to users.
- New tables created in a schema will **not** automatically inherit privileges unless `GRANT ... ON ALL TABLES` is used. Consider using `ALTER DEFAULT PRIVILEGES` for consistency.


