# Python Backend Development with FastAPI & MySQL
### A Complete Beginner-to-Industry Study Guide (DBMS → SQL → SQLAlchemy → FastAPI)

*Written like a textbook + bootcamp. Assumes: you know Python basics. Assumes: you know nothing about databases or SQLAlchemy yet.*

---

## Table of Contents

1. DBMS Basics
2. MySQL Basics
3. Tables
4. Constraints
5. CRUD SQL
6. CRUD Mapping (SQL → REST)
7. SQLAlchemy ORM
8. SQLAlchemy Architecture
9. SQLAlchemy Setup
10. SQLAlchemy Models
11. FastAPI + SQLAlchemy
12. CRUD Using SQLAlchemy
13. Old Project vs New Project
14. Project Structure
15. Complete Request Flow
16. Industry Best Practices
17. Interview Questions
18. Revision Notes
19. Cheat Sheet
20. Practice Zone (SQL / SQLAlchemy / FastAPI questions + Projects)

---

# SECTION 1 — DBMS Basics

## 1.1 What is Data

**Definition:** Data is raw, unprocessed facts — numbers, text, dates — that have no meaning by themselves until organized.

**Why this concept exists:** Every software system, at its core, exists to store and move data. Before we can talk about databases, we need to be precise about what we're storing.

**Real-world analogy:** A single word scribbled on a sticky note ("Rahul", "23", "Delhi") is data — meaningless alone. Put it into a form ("Name: Rahul, Age: 23, City: Delhi") and it becomes information.

**Examples:**
- `"Rahul"` → data
- `23` → data
- `"rahul@email.com"` → data

**Important notes:** Data becomes **information** when it is structured and given context. A database's job is to store data so it can reliably become information again on demand.

---

## 1.2 What is a Database

**Definition:** A database is an organized, persistent collection of related data, stored electronically, that can be efficiently accessed, managed, and updated.

**Why this concept exists:** Storing data in flat files (`.txt`, `.csv`) works for tiny amounts of data, but breaks down fast: no consistency guarantees, no concurrent access control, no fast lookup, no relationships between data. Databases solve all of this.

**Real-world analogy:** A library. Books (data) are not thrown in a pile — they are catalogued, shelved by section, indexed by title/author, and a librarian (the DBMS) controls who can add, remove, or borrow books.

**Internal working (conceptual):**
- Data is stored on disk in files, but organized into structured units (tables, pages, blocks).
- An index (like a library catalog) allows the system to jump straight to relevant data instead of scanning everything.

**Common beginner mistakes:**
- Confusing "database" with "table" (a database is a *container* of tables).
- Thinking a `.csv` file is a database — it's just a file; there's no engine managing consistency, concurrency, or indexing.

**Summary:** A database = organized data + rules for storing/retrieving it reliably.

---

## 1.3 What is DBMS

**Definition:** DBMS (Database Management System) is the software layer that creates, manages, and controls access to databases. Examples: MySQL, PostgreSQL, Oracle, SQL Server, SQLite, MongoDB.

**Why this concept exists:** Someone has to actually enforce the rules — prevent two users from corrupting the same row at once, enforce that an email column can't be duplicated, recover data after a crash, optimize how a query runs. That "someone" is the DBMS engine.

**Real-world analogy:** The database is the library's books and shelves. The DBMS is the librarian + the entire management system: check-in/check-out rules, security guards at the door, the reservation system.

**Internal working:**
```
Application (FastAPI) 
      ↓  SQL query
   DBMS Engine (MySQL Server)
      ↓
 Query Parser → Optimizer → Executor
      ↓
   Storage Engine (reads/writes disk pages)
```

**Types of DBMS:**
| Type | Example | Data Model |
|---|---|---|
| Relational (RDBMS) | MySQL, PostgreSQL | Tables with rows/columns |
| NoSQL - Document | MongoDB | JSON-like documents |
| NoSQL - Key-Value | Redis | Key → Value pairs |
| NoSQL - Graph | Neo4j | Nodes + edges |

**Interview questions:**
- Q: What is the difference between Database and DBMS?
  A: Database = the actual stored data. DBMS = the software that manages that data (create, read, update, delete, secure, back up).
- Q: Name popular RDBMS software.
  A: MySQL, PostgreSQL, Oracle, SQL Server, SQLite.

---

## 1.4 Advantages of DBMS

1. **Data Redundancy Control** — one central source of truth instead of duplicated files.
2. **Data Consistency** — constraints prevent contradictory data.
3. **Concurrent Access** — many users/apps can safely read/write at once (via locking/transactions).
4. **Security** — user permissions, roles, encryption.
5. **Backup & Recovery** — built-in crash recovery.
6. **Data Integrity** — constraints (PRIMARY KEY, FOREIGN KEY, etc.) guarantee valid relationships.
7. **Fast retrieval** — indexing enables sub-second lookups even on millions of rows.

**Without a DBMS (raw files) you would have to hand-write:** locking logic, indexing, crash recovery, validation, and concurrency control yourself — the exact reason DBMS software exists.

---

## 1.5 Types of Databases

| Type | Structure | Best For | Example |
|---|---|---|---|
| Relational | Tables, rows, columns, strict schema | Structured data with relationships (banking, e-commerce) | MySQL, PostgreSQL |
| NoSQL Document | JSON/BSON documents | Flexible/evolving schema (content, catalogs) | MongoDB |
| Key-Value | Simple key → value | Caching, sessions | Redis |
| Graph | Nodes + relationships | Social networks, recommendations | Neo4j |
| Columnar | Column-oriented storage | Analytics/big data | Cassandra, BigQuery |

---

## 1.6 Relational Database

**Definition:** A relational database organizes data into **tables** (relations), where each table has rows (records) and columns (attributes), and tables can be linked to each other via keys.

**Why this concept exists:** Real-world data has *relationships* — a Student takes many Courses, an Order belongs to a Customer. Relational databases model these connections directly and enforce them with rules (foreign keys), instead of leaving it to application code to keep things consistent.

**Real-world analogy:** Think of a school. One table lists "Students," another lists "Courses," and a third table (StudentCourses) says which student is enrolled in which course — instead of copy-pasting course details into every student record.

**Internal working:** Relational engines store each table's rows typically as separate disk pages, use indexes (usually B-trees) for fast lookup by key, and use a query optimizer to decide *how* to execute a SQL statement (e.g., which index to use).

**Diagram:**
```
[Students]              [Enrollments]            [Courses]
id | name        id | student_id | course_id      id | title
1  | Aisha  <---     1  |     1      |    10   --->  10  | DBMS
2  | Rohan  <---     2  |     2      |    10   --->  
```

**Common beginner mistakes:**
- Storing repeated data in one giant table instead of splitting into related tables (this is what "normalization," covered implicitly through constraints, aims to prevent).

**Interview questions:**
- Q: Why not just use one giant table for everything?
  A: It causes data duplication, wasted storage, and inconsistency when the same fact (e.g. a course name) is updated in some rows but not others. Splitting into related tables with foreign keys avoids that.

---

## 1.7 Database vs Table

| Aspect | Database | Table |
|---|---|---|
| Definition | A container holding many related tables | A structured grid of rows & columns inside a database |
| Analogy | A whole filing cabinet | One drawer/folder inside it |
| SQL | `CREATE DATABASE school;` | `CREATE TABLE students (...);` |
| Contains | Tables, views, users, permissions | Rows (records) and columns (fields) |

**Practice question:** If you were building an e-commerce app, name 4 tables you'd expect inside your `ecommerce` database.
*(Answer hint: customers, products, orders, order_items)*

---

# SECTION 2 — MySQL Basics

## 2.1 CREATE DATABASE

**Definition:** Creates a new, empty database (a named container for tables) inside the MySQL server.

**Why it exists:** You must have a database to hold tables — MySQL can host many independent databases on one server (e.g., `school`, `shop`, `blog` all on the same server, fully isolated from each other).

**Syntax:**
```sql
CREATE DATABASE database_name;
CREATE DATABASE IF NOT EXISTS database_name;
```

**Keyword explanation:**
- `CREATE DATABASE` → the command itself.
- `IF NOT EXISTS` → prevents an error if the database already exists; MySQL silently skips creation instead of throwing "database exists" error.

**Examples:**
```sql
CREATE DATABASE school;
CREATE DATABASE IF NOT EXISTS school;
```

**Common beginner mistakes:**
- Forgetting `IF NOT EXISTS` and re-running a setup script → causes an error on second run.
- Using spaces or special characters in database names without backticks (`` `my db` ``) — avoid this entirely, use underscores instead (`my_db`).

**Best practices:** Use lowercase, snake_case names (`school_db`, not `SchoolDB` or `School Db`), since MySQL identifier case-sensitivity depends on the OS (case-sensitive on Linux, not on Windows) — consistency avoids bugs when moving servers.

---

## 2.2 DROP DATABASE

**Definition:** Permanently deletes a database and **everything inside it** — all tables, all data, irreversibly (no "recycle bin").

**Syntax:**
```sql
DROP DATABASE database_name;
DROP DATABASE IF EXISTS database_name;
```

**Why it exists:** Cleanup — remove test/staging databases, or fully reset an environment.

**Important notes:** There is no undo. In real production systems, `DROP DATABASE` is almost never run directly by a developer — it's gated behind backups, approvals, and staging environments.

**Common beginner mistakes:**
- Running `DROP DATABASE` on the wrong environment (production instead of local) — always double check which database you're connected to first with `SELECT DATABASE();`.

---

## 2.3 USE DATABASE

**Definition:** Selects which database the current session's subsequent commands should apply to.

**Syntax:**
```sql
USE database_name;
```

**Why it exists:** A single MySQL server can host many databases at once; `USE` tells the client "from now on, unqualified table names refer to *this* database."

**Example:**
```sql
USE school;
SELECT * FROM students;   -- refers to school.students
```

**Common beginner mistakes:** Forgetting to run `USE` and getting "No database selected" errors, or accidentally being inside the wrong database and modifying the wrong tables.

**Best practice:** In application code (Python, FastAPI), the database name is specified in the connection URL itself, so you rarely type `USE` manually outside the MySQL shell.

---

## 2.4 SHOW DATABASES

**Definition:** Lists every database that currently exists on the connected MySQL server.

**Syntax:**
```sql
SHOW DATABASES;
```

**Example output:**
```
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql               |
| performance_schema |
| school              |
+--------------------+
```

**Important notes:** `information_schema`, `mysql`, `performance_schema`, `sys` are built-in system databases MySQL creates automatically — never delete them.

**Interview questions:**
- Q: What's the difference between `USE db;` and `CREATE DATABASE db;`?
  A: `CREATE DATABASE` makes a new one; `USE` just switches your active session to an existing one.

**Mini assignment:** Open a MySQL shell (or Workbench) and: create a database `practice_db`, list all databases to confirm it exists, switch into it, then drop it and confirm it's gone.

---

# SECTION 3 — Tables

## 3.1 CREATE TABLE

**Definition:** Defines a new table — its name, columns, each column's data type, and constraints — inside the currently selected database.

**Why it exists:** A database needs a *schema* (structure) before it can store any rows. `CREATE TABLE` is how you declare that structure up front.

**Real-world analogy:** Designing a paper form before anyone fills it out — you decide the fields ("Name", "Age", "Email") and their type (text box vs number box) before collecting data.

**Syntax:**
```sql
CREATE TABLE table_name (
    column1 datatype constraints,
    column2 datatype constraints,
    ...
);
```

**Example:**
```sql
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT,
    email VARCHAR(150) UNIQUE
);
```

**Line-by-line explanation:**
- `id INT PRIMARY KEY AUTO_INCREMENT` → a whole number column that uniquely identifies each row and auto-generates itself (1, 2, 3, ...).
- `name VARCHAR(100) NOT NULL` → a text column, max 100 characters, that cannot be left empty.
- `age INT` → a whole-number column, optional (nullable by default).
- `email VARCHAR(150) UNIQUE` → text column, max 150 chars, no two rows may share the same value.

**Common beginner mistakes:**
- Forgetting a `PRIMARY KEY` — every table should have one to uniquely identify rows.
- Making every column `VARCHAR(255)` by habit instead of choosing the right type/length.

**Best practices:** Name tables in plural, lowercase, snake_case (`students`, `order_items`). Always define a primary key.

---

## 3.2 DROP TABLE

**Definition:** Permanently deletes a table and all its data and structure.

**Syntax:**
```sql
DROP TABLE table_name;
DROP TABLE IF EXISTS table_name;
```

**Important notes:** Unlike `DELETE FROM table`, which removes rows but keeps the table, `DROP TABLE` removes the table definition itself. No undo.

---

## 3.3 ALTER TABLE

**Definition:** Modifies the structure of an existing table — add/remove/rename columns, change data types, add/drop constraints — without losing existing data.

**Syntax:**
```sql
ALTER TABLE table_name ADD COLUMN column_name datatype;
ALTER TABLE table_name DROP COLUMN column_name;
ALTER TABLE table_name MODIFY COLUMN column_name new_datatype;
ALTER TABLE table_name RENAME COLUMN old_name TO new_name;
```

**Examples:**
```sql
ALTER TABLE students ADD COLUMN phone VARCHAR(15);
ALTER TABLE students DROP COLUMN phone;
ALTER TABLE students MODIFY COLUMN age SMALLINT;
ALTER TABLE students RENAME COLUMN name TO full_name;
```

**Why it exists:** Requirements change after launch — you rarely design the "perfect" schema on day one. `ALTER TABLE` lets the schema evolve without destroying data.

**Common beginner mistakes:** Running `ALTER TABLE` directly on a production database with huge tables during peak hours — large alters can lock the table and cause downtime; in real jobs this is done via migration tools (e.g., Alembic for SQLAlchemy) during low-traffic windows.

---

## 3.4 SHOW TABLES / DESC TABLE

**Definition:**
- `SHOW TABLES;` → lists all tables in the currently selected database.
- `DESC table_name;` (or `DESCRIBE`) → shows a table's column names, types, nullability, keys, and defaults.

**Example:**
```sql
SHOW TABLES;
DESC students;
```

**Example DESC output:**
```
+-------+--------------+------+-----+---------+----------------+
| Field | Type         | Null | Key | Default | Extra          |
+-------+--------------+------+-----+---------+----------------+
| id    | int          | NO   | PRI | NULL    | auto_increment |
| name  | varchar(100) | NO   |     | NULL    |                |
| age   | int          | YES  |     | NULL    |                |
| email | varchar(150) | YES  | UNI | NULL    |                |
+-------+--------------+------+-----+---------+----------------+
```

---

## 3.5 Rows, Columns, Records, Fields, Schema

| Term | Definition | Analogy |
|---|---|---|
| **Column** | A named attribute/property that every row has (e.g., `name`) | A field on a paper form |
| **Row / Record** | One complete entry in the table (all column values for one entity) | One filled-out form |
| **Field** | The intersection of a specific row and a specific column — one value | One filled-in box on the form |
| **Schema** | The overall structure definition: tables, columns, types, constraints, relationships | The blueprint of the entire filing system |

**Note:** "Row" and "Record" are used interchangeably. Same with "Column" and "Field" in casual speech — but strictly, *field* refers to a single value, while *column* refers to the whole vertical attribute.

**Interview questions:**
- Q: What's the difference between schema and table?
  A: Schema is the overall design (could include many tables, relationships, constraints). A table is one specific structure within that schema.

**Mini assignment:** Create a `books` table with columns `id`, `title`, `author`, `price`, `published_year`. Then use `DESC books;` to verify the structure. Add a `stock_quantity` column using `ALTER TABLE`.

---

# SECTION 4 — Constraints

Constraints are rules attached to columns that the database engine *enforces automatically* — they exist so that invalid data can never be inserted, no matter what application code does (or forgets to do).

## 4.1 PRIMARY KEY

**Definition:** A column (or combination of columns) that uniquely identifies each row in a table. Cannot be NULL, and cannot repeat.

**Why it exists:** Every table needs a reliable, unique way to reference exactly one row — for updates, deletes, and for other tables to link to it (foreign keys).

**Syntax:**
```sql
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    ...
);
```

**Internal working:** MySQL automatically builds a unique index (usually a B-tree) on the primary key, making lookups by ID extremely fast (O(log n) instead of scanning every row).

**Common beginner mistakes:** Using a "natural" column like `email` or `name` as the primary key instead of a dedicated auto-incrementing `id` — natural values can change (a user updates their email) and that breaks every table linking to it via foreign key.

---

## 4.2 FOREIGN KEY

**Definition:** A column that references the primary key of another table, enforcing that its value must exist in that other table (referential integrity).

**Why it exists:** To physically enforce relationships between tables — you cannot insert an order for a `customer_id` that doesn't exist in the `customers` table.

**Syntax:**
```sql
CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);
```

**Real-world analogy:** A library card number written on a borrowing slip must correspond to an actual, existing library member — you can't write down a fake member number.

**Common beginner mistakes:**
- Forgetting to create the referenced table first (foreign keys need the parent table to already exist).
- Trying to delete a parent row (e.g., a customer) while child rows (orders) still reference it — MySQL blocks this unless you define `ON DELETE CASCADE` or similar.

**Best practice:** Decide `ON DELETE` behavior explicitly:
```sql
FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE;
```

---

## 4.3 UNIQUE

**Definition:** Ensures no two rows can have the same value in that column (but unlike PRIMARY KEY, a UNIQUE column *can* be NULL, and a table can have multiple UNIQUE columns).

**Syntax:**
```sql
email VARCHAR(150) UNIQUE
```

**Why it exists:** Some columns must never repeat even though they aren't the primary identifier — e.g., email, username, phone number.

---

## 4.4 NOT NULL

**Definition:** Forces a column to always have a value — `NULL` (empty/unknown) is not allowed.

**Syntax:**
```sql
name VARCHAR(100) NOT NULL
```

**Why it exists:** Some fields are mandatory by business logic (you can't have a student with no name). Enforcing this at the database level means *no* code path, anywhere, can accidentally skip it.

---

## 4.5 DEFAULT

**Definition:** Provides an automatic value for a column when no value is explicitly given during insert.

**Syntax:**
```sql
status VARCHAR(20) DEFAULT 'active',
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
```

**Why it exists:** Reduces repetitive application code and guarantees a sane fallback (e.g., every new order is `'pending'` unless stated otherwise).

---

## 4.6 CHECK

**Definition:** Enforces a custom boolean condition that every row must satisfy.

**Syntax:**
```sql
age INT CHECK (age >= 0),
price DECIMAL(10,2) CHECK (price > 0)
```

**Why it exists:** Some rules aren't about uniqueness or nullability but about *valid ranges/logic* — e.g., age can't be negative, price must be positive.

**Note:** Older MySQL versions (< 8.0.16) silently ignored `CHECK` constraints; modern MySQL (8.0.16+) enforces them properly.

---

## Constraints Summary Table

| Constraint | Purpose | Can repeat? | Can be NULL? |
|---|---|---|---|
| PRIMARY KEY | Unique row identifier | No | No |
| FOREIGN KEY | Enforces valid reference to another table | Yes | Depends on column |
| UNIQUE | No duplicate values | No | Yes (once) |
| NOT NULL | Value is mandatory | Yes | No |
| DEFAULT | Auto-fills missing value | Yes | N/A |
| CHECK | Enforces custom condition | Yes | Depends |

**Interview questions:**
- Q: Can a table have more than one PRIMARY KEY?
  A: No — only one primary key per table (though it can be a composite key spanning multiple columns).
- Q: Difference between UNIQUE and PRIMARY KEY?
  A: PRIMARY KEY = unique + not null + exactly one per table (and typically used for foreign key references). UNIQUE = unique but nullable, and a table can have several UNIQUE columns.
- Q: What happens if you try to insert a row violating a FOREIGN KEY?
  A: MySQL rejects the insert with a constraint violation error.

**Mini assignment:** Design two related tables: `authors` (id, name) and `books` (id, title, author_id FK → authors.id, price CHECK > 0). Try inserting a book with a non-existent `author_id` and observe the error.

---

# SECTION 5 — CRUD SQL

CRUD = **C**reate, **R**ead, **U**pdate, **D**elete — the four fundamental operations on data, in every application ever built.

## 5.1 INSERT (Create)

**Definition:** Adds one or more new rows into a table.

**Syntax:**
```sql
INSERT INTO table_name (col1, col2, col3) VALUES (val1, val2, val3);
INSERT INTO table_name (col1, col2) VALUES (v1a, v2a), (v1b, v2b);  -- multi-row
```

**Examples:**
```sql
INSERT INTO students (name, age, email) VALUES ('Aisha', 20, 'aisha@mail.com');

INSERT INTO students (name, age, email) VALUES
  ('Rohan', 22, 'rohan@mail.com'),
  ('Priya', 21, 'priya@mail.com');
```

**Common beginner mistakes:**
- Omitting column names (`INSERT INTO students VALUES (...)`) — fragile, breaks silently if table structure changes order.
- Forgetting quotes around string/date values.

---

## 5.2 SELECT (Read)

**Definition:** Retrieves rows from one or more tables.

**Syntax:**
```sql
SELECT column1, column2 FROM table_name WHERE condition;
SELECT * FROM table_name;
```

**Examples:**
```sql
SELECT * FROM students;
SELECT name, age FROM students WHERE age > 21;
```

---

## 5.3 UPDATE

**Definition:** Modifies existing rows that match a condition.

**Syntax:**
```sql
UPDATE table_name SET column1 = value1 WHERE condition;
```

**Example:**
```sql
UPDATE students SET age = 23 WHERE id = 1;
```

**⚠️ Critical warning:** Omitting `WHERE` updates **every row in the table**:
```sql
UPDATE students SET age = 23;   -- updates ALL students! Dangerous.
```

---

## 5.4 DELETE

**Definition:** Removes rows matching a condition (table structure remains).

**Syntax:**
```sql
DELETE FROM table_name WHERE condition;
```

**Example:**
```sql
DELETE FROM students WHERE id = 5;
```

**⚠️ Same danger:** `DELETE FROM students;` (no WHERE) deletes every row.

**Best practice:** In production apps, always run a `SELECT ... WHERE ...` with the same condition *first* to confirm exactly which rows will be affected, before running `UPDATE`/`DELETE`.

---

## 5.5 WHERE

**Definition:** Filters rows — only rows for which the condition evaluates true are affected/returned.

**Syntax & operators:**
```sql
SELECT * FROM students WHERE age > 20;
SELECT * FROM students WHERE age >= 20 AND city = 'Delhi';
SELECT * FROM students WHERE city = 'Delhi' OR city = 'Mumbai';
SELECT * FROM students WHERE age BETWEEN 18 AND 25;
SELECT * FROM students WHERE city IN ('Delhi', 'Mumbai');
SELECT * FROM students WHERE email IS NULL;
```

## 5.6 ORDER BY

**Definition:** Sorts the result set.

**Syntax:**
```sql
SELECT * FROM students ORDER BY age ASC;   -- ascending (default)
SELECT * FROM students ORDER BY age DESC;  -- descending
SELECT * FROM students ORDER BY city ASC, age DESC;  -- multi-column
```

## 5.7 LIMIT

**Definition:** Restricts how many rows are returned — essential for pagination.

**Syntax:**
```sql
SELECT * FROM students LIMIT 10;             -- first 10 rows
SELECT * FROM students LIMIT 10 OFFSET 20;   -- rows 21-30 ("page 3" of size 10)
```

**Real-world use:** Every "Load More" button or paginated API list (`GET /students?page=2`) is implemented with `LIMIT`/`OFFSET` under the hood.

## 5.8 LIKE (Pattern Matching)

**Definition:** Filters text columns using wildcard pattern matching.

**Wildcards:**
- `%` → matches **any number of characters** (including zero).
- `_` → matches **exactly one character**.

**Examples:**
```sql
SELECT * FROM students WHERE name LIKE 'A%';     -- starts with A
SELECT * FROM students WHERE name LIKE '%a';     -- ends with a
SELECT * FROM students WHERE name LIKE '%an%';   -- contains "an" anywhere
SELECT * FROM students WHERE name LIKE 'A___';   -- starts with A, exactly 4 chars total
SELECT * FROM students WHERE email LIKE '%@gmail.com';  -- gmail users
```

**Common beginner mistakes:**
- Using `=` instead of `LIKE` for partial matches (`name = 'A%'` looks for the literal string "A%", not a pattern).
- Forgetting `LIKE` is case-insensitive by default in MySQL (depends on collation) — don't rely on it for case-sensitive matching.

**Interview questions:**
- Q: What's the difference between `WHERE age = 20` and `WHERE age LIKE 20`?
  A: For plain equality, use `=`. `LIKE` is meant for string pattern matching; using it on numbers usually still works but is semantically wrong and unclear.
- Q: How would you find all emails from Yahoo?
  A: `SELECT * FROM students WHERE email LIKE '%@yahoo.com';`

**Mini assignment:** Using a `students` table: (1) insert 5 rows, (2) select all students older than 20 sorted by name, (3) find students whose name contains "an", (4) get only the 2nd page of 2 results per page.

---

# SECTION 6 — CRUD Mapping (SQL ↔ REST API)

## 6.1 Why This Mapping Matters

**Definition:** REST APIs expose CRUD operations over HTTP using specific HTTP methods, each of which conventionally maps to one SQL operation.

**Why it exists:** REST is a *convention* for making backend behavior predictable — any client (mobile app, frontend, another service) knows that `POST /students` creates something and `DELETE /students/5` removes something, without reading custom documentation for every single endpoint.

## 6.2 The Mapping Table

| HTTP Method | REST Meaning | SQL Operation | Example URL |
|---|---|---|---|
| `POST` | Create a new resource | `INSERT` | `POST /students` |
| `GET` | Read/fetch resource(s) | `SELECT` | `GET /students`, `GET /students/5` |
| `PUT` | Replace a resource entirely | `UPDATE` (full) | `PUT /students/5` |
| `PATCH` | Partially update a resource | `UPDATE` (partial) | `PATCH /students/5` |
| `DELETE` | Remove a resource | `DELETE` | `DELETE /students/5` |

## 6.3 FastAPI Examples (Conceptual — Raw, Pre-SQLAlchemy)

```python
from fastapi import FastAPI
app = FastAPI()

@app.post("/students")
def create_student(student: dict):
    # conceptually → INSERT INTO students (...) VALUES (...)
    ...

@app.get("/students")
def get_students():
    # conceptually → SELECT * FROM students
    ...

@app.get("/students/{student_id}")
def get_student(student_id: int):
    # conceptually → SELECT * FROM students WHERE id = student_id
    ...

@app.put("/students/{student_id}")
def update_student(student_id: int, student: dict):
    # conceptually → UPDATE students SET ... WHERE id = student_id
    ...

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    # conceptually → DELETE FROM students WHERE id = student_id
    ...
```

**Important notes:** `PUT` is technically supposed to replace the *entire* resource (every field), while `PATCH` updates only the fields sent. In practice, many APIs (including ones you'll see in real jobs) use `PUT` loosely for "update," but interview answers should know the technical distinction.

**Interview questions:**
- Q: Why not just use `GET` for everything?
  A: HTTP methods carry semantic meaning that browsers, caches, proxies, and API gateways rely on — e.g., `GET` requests are assumed to be safe/side-effect-free and are cacheable; using `GET` to delete data would violate that and could cause data loss (e.g., a web crawler following a "delete" link).
- Q: What's the difference between PUT and PATCH?
  A: PUT conceptually replaces the whole resource; PATCH updates only the given fields.

**Mini assignment:** Sketch (on paper) the 5 REST endpoints you'd need for a `books` resource, and write the SQL statement each one would conceptually trigger.

---

# SECTION 7 — SQLAlchemy ORM

## 7.1 What is ORM

**Definition:** ORM (Object-Relational Mapping) is a technique — and SQLAlchemy is a *library* implementing it — that lets you interact with a relational database using Python objects and methods instead of writing raw SQL strings.

**Why this concept exists:** Python code deals in objects (`student.name`, `student.age`). SQL deals in rows and columns inside tables. Someone has to translate between the two worlds every single time you touch the database. Doing that translation *by hand*, in every function, for years, across a large codebase, is repetitive and error-prone. ORM automates the translation.

**Real-world analogy:** Think of ORM as a professional translator sitting between you (speaking Python) and the database (speaking SQL). You say "give me the student named Aisha" in Python; the translator converts it to `SELECT * FROM students WHERE name = 'Aisha'`, runs it, and hands you back a Python object.

## 7.2 Problems Without ORM (Raw SQL in App Code)

```python
import pymysql
conn = pymysql.connect(host="localhost", user="root", password="pass", db="school")
cursor = conn.cursor()
cursor.execute("SELECT * FROM students WHERE age > %s", (20,))
rows = cursor.fetchall()
# rows is a list of raw tuples: [(1, 'Aisha', 20, 'aisha@mail.com'), ...]
# you must manually know which index is which column!
```

Problems this reveals:
1. **No type safety** — `rows[0][1]` could be name, or could be something else if the table changes; nothing warns you.
2. **SQL injection risk** — if you carelessly build queries with string formatting (`f"...{age}"`) instead of parameters, attackers can inject malicious SQL.
3. **Repetition** — every single query repeats connection/cursor/execute/fetch boilerplate.
4. **Database lock-in** — raw SQL syntax differs slightly between MySQL, PostgreSQL, SQLite; switching databases means rewriting queries.
5. **Hard to maintain** — a change to a table's columns means hunting through every raw SQL string in the codebase.

## 7.3 Advantages of ORM

- Work with Python objects/classes (`Student`) instead of raw tuples.
- Automatic protection against SQL injection (parameters handled safely).
- Database-agnostic — swap MySQL for PostgreSQL with minimal code change.
- Auto-generates SQL, reducing boilerplate.
- Integrates naturally with type hints and validation (great fit with FastAPI + Pydantic).
- Relationship handling (`student.courses`) instead of manual JOINs everywhere.

## 7.4 Disadvantages of ORM

- Learning curve — you must understand what SQL is being generated underneath, or you'll write inefficient queries without realizing it.
- Can hide performance costs (e.g., the "N+1 query problem" where a loop silently fires hundreds of small queries).
- Extremely complex queries are sometimes easier and faster to write in raw SQL.
- Slight performance overhead vs. hand-tuned raw SQL (usually negligible for typical apps).

## 7.5 How ORM Converts Python → SQL

**Diagram:**
```
Python (your code)                    SQLAlchemy                      MySQL
-------------------                    -----------                     -----
db.query(Student)                       builds a Select object    ->   SELECT * FROM students;
   .filter(Student.age > 20)            adds WHERE clause          ->     WHERE age > 20;
   .all()                               compiles + executes SQL    ->   (runs on the server)
                                         maps result rows back
                                         into Student Python objects
```

**Step by step internal working:**
1. You call ORM methods (`.query()`, `.filter()`, `.add()`) on Python objects.
2. SQLAlchemy's **Query/Expression layer** builds an internal representation of the SQL statement (not a raw string yet).
3. The **SQL compiler** translates that representation into the correct dialect of SQL for your specific database (MySQL syntax, in our case).
4. The **DBAPI driver** (`pymysql`) sends that SQL string over a network connection to the MySQL server.
5. MySQL executes it and returns raw rows.
6. SQLAlchemy's **ORM layer** maps each raw row back into an instance of your Python class (e.g., a `Student` object with `.name`, `.age` attributes).

**Interview questions:**
- Q: What problem does ORM solve?
  A: It removes the need to hand-write raw SQL strings and manually map rows to Python objects, while protecting against SQL injection and reducing database-specific code.
- Q: Is ORM always faster than raw SQL?
  A: No — raw, hand-tuned SQL can be faster for complex queries; ORM trades a bit of performance for developer productivity, safety, and maintainability.
- Q: What is the "N+1 query problem"?
  A: A performance bug pattern where fetching a list of parent objects, then accessing a related field on each in a loop, causes one query for the list plus N additional queries (one per item) instead of a single efficient JOIN.

**Summary:** ORM = a translation and mapping layer between Python objects and SQL, giving you safety and productivity at a small performance cost you must stay aware of.

---

# SECTION 8 — SQLAlchemy Architecture

## 8.1 The Big Picture

```
   Your Code
      │
      ▼
   Session   ──── the "workspace" where you stage changes (add/query/commit)
      │
      ▼
   Engine    ──── manages the actual DB connection pool + knows the SQL dialect
      │
      ▼
   Model (mapped class)  ──── Python class describing a table's shape
      │
      ▼
   Query / Statement  ──── the generated SQL
      │
      ▼
   MySQL Database
```

## 8.2 Engine

**Definition:** The `Engine` is the starting point of any SQLAlchemy application — it represents the core interface to the database: it knows the connection string, manages a pool of reusable connections, and knows which SQL dialect to generate (MySQL vs PostgreSQL syntax, etc).

**Why it exists:** Opening a brand-new network connection to MySQL for every single query would be extremely slow. The Engine manages a **connection pool** — a set of already-open connections that get reused, dramatically improving performance.

**Analogy:** The Engine is like a call center's phone-line pool — instead of dialing a brand-new phone line for every customer call, a set of lines stays open and gets reused as calls come and go.

**Created once, per application**, typically in `database.py`:
```python
from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://user:password@localhost/school")
```

## 8.3 Session

**Definition:** A `Session` is a temporary "workspace" or transaction scope tied to the Engine — it tracks Python objects you've loaded or created, and translates your `.add()`, `.query()`, `.commit()` calls into actual SQL, executed through a connection borrowed from the Engine's pool.

**Why it exists:** Real work happens in units called *transactions* — a sequence of operations that should either all succeed or all fail together (atomicity). The Session is where that unit of work is tracked before being finalized (`commit()`) or discarded (`rollback()`).

**Analogy:** The Session is like a shopping cart at a store. You add items (`session.add(student)`), browse more, maybe remove something — nothing is final until you "check out" (`session.commit()`). If you walk away without checking out (`rollback()`), nothing happened.

**Created per-request** in a web app (this is critical — a Session should NOT be shared across unrelated requests):
```python
from sqlalchemy.orm import sessionmaker
SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()
```

## 8.4 Model

**Definition:** A Model is a Python class (usually inheriting from a `Base` declarative class) whose attributes are mapped to a specific table's columns. One model class = one table (typically).

**Why it exists:** This is the actual "mapping" in Object-Relational Mapping — it's the dictionary that tells SQLAlchemy: "this Python class corresponds to this SQL table, and each of its attributes corresponds to this specific column, with this specific type."

```python
class Student(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
```

## 8.5 Query

**Definition:** A Query (or, in modern SQLAlchemy 2.0 style, a `select()` statement) represents a *request for data* — built up via chained method calls — that gets compiled into SQL and executed through the Session.

```python
db.query(Student).filter(Student.age > 20).all()
# or, SQLAlchemy 2.0 style:
from sqlalchemy import select
db.execute(select(Student).where(Student.age > 20)).scalars().all()
```

## 8.6 How They All Connect — Full Picture

| Layer | Role | Created |
|---|---|---|
| Engine | Knows how to talk to MySQL; manages connection pool | Once, at app startup |
| Session | A working transaction scope for one unit of work | Once per request |
| Model | Python class mapped to a table | Once, at model-definition time |
| Query | A specific data request, run through a Session | Every time you need data |

**Common beginner mistakes:**
- Creating a new `Engine` on every request (extremely wasteful — defeats the whole purpose of connection pooling).
- Sharing one global `Session` across multiple unrelated requests (causes data leaking between users' requests and threading bugs).

**Interview questions:**
- Q: What's the difference between Engine and Session?
  A: The Engine is the low-level, long-lived connection manager to the database (created once). The Session is a short-lived transactional workspace built on top of the Engine, created fresh per unit of work (e.g., per HTTP request).
- Q: Why is a new Session created per request in FastAPI?
  A: To keep each request's transaction isolated — so one user's uncommitted changes or query cache never leaks into another user's request, and so each request cleanly closes its DB resources when done.

**Mini assignment:** Draw the Engine → Session → Model → Query diagram from memory and explain each arrow in one sentence.

---

# SECTION 9 — SQLAlchemy Setup

## 9.1 Installing Dependencies

```bash
pip install sqlalchemy
pip install pymysql
```

**Why both?** SQLAlchemy itself is database-agnostic — it doesn't know how to actually talk MySQL's wire protocol. `pymysql` is the **DBAPI driver**: the low-level library that actually opens a TCP connection to MySQL and speaks its protocol. SQLAlchemy sits on top of it and generates the SQL; `pymysql` sends it.

## 9.2 DATABASE_URL

**Definition:** A single connection string encoding everything needed to connect: dialect, driver, credentials, host, port, and database name.

**Syntax:**
```
dialect+driver://username:password@host:port/database_name
```

**Example:**
```python
DATABASE_URL = "mysql+pymysql://root:mypassword@localhost:3306/school"
```

**Breaking it down:**
- `mysql` → the SQL dialect (MySQL syntax rules).
- `pymysql` → the driver used to physically connect.
- `root:mypassword` → username and password.
- `localhost:3306` → host and port (3306 is MySQL's default port).
- `school` → the database name to connect into (equivalent to running `USE school;`).

**Best practice:** Never hardcode credentials in source code. Load them from environment variables:
```python
import os
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:pass@localhost/school")
```

## 9.3 create_engine()

```python
from sqlalchemy import create_engine
engine = create_engine(DATABASE_URL, echo=True)
```

**Explanation of arguments:**
- `DATABASE_URL` → tells the engine what/where to connect to.
- `echo=True` → logs every generated SQL statement to the console — extremely useful while learning/debugging, turned off in production.

## 9.4 SessionLocal

```python
from sqlalchemy.orm import sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```

**Explanation:**
- `sessionmaker(...)` → a *factory* — it doesn't create a session itself, it creates a *class/callable* that produces new Session objects on demand (`SessionLocal()`).
- `autocommit=False` → changes are NOT saved automatically; you must call `.commit()` explicitly (this is the safe, standard setting).
- `autoflush=False` → SQLAlchemy won't automatically push pending changes to the DB before every query (you control flushing/committing explicitly).
- `bind=engine` → ties this session factory to our specific Engine/database.

## 9.5 DeclarativeBase

```python
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
```

**Definition:** `Base` is the parent class that all your ORM models inherit from. It's what lets SQLAlchemy track every model class you define and know they all belong to the same metadata/schema.

**Why it exists:** SQLAlchemy needs a central registry of "here are all the tables the app knows about" — that registry lives on `Base.metadata`, automatically populated as soon as any class inherits from `Base`.

## 9.6 metadata.create_all()

```python
Base.metadata.create_all(bind=engine)
```

**Definition:** Looks at every model class that inherited from `Base`, and issues `CREATE TABLE IF NOT EXISTS ...` for each one that doesn't already exist in the connected database.

**Important notes:**
- It does **not** alter existing tables if you change a model's columns later (that's what migration tools like Alembic exist for — `create_all()` is fine for early learning/small apps, but real production systems use proper migrations).
- It's usually called once, at application startup.

## 9.7 Putting It All Together — `database.py`

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "mysql+pymysql://root:password@localhost/school"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass
```

**Common beginner mistakes:**
- Forgetting to actually call `Base.metadata.create_all(engine)` anywhere → tables never get created and you get "table doesn't exist" errors.
- Mixing up `Session` (the class-like factory `SessionLocal`) with an actual session *instance* (`SessionLocal()`).

**Interview questions:**
- Q: Why do we need both SQLAlchemy and PyMySQL installed?
  A: SQLAlchemy generates SQL and manages the ORM layer, but it needs an actual driver (PyMySQL) to physically communicate with the MySQL server over the network.
- Q: What does `echo=True` do, and should it be used in production?
  A: It logs every SQL statement generated — great for learning/debugging, but should be turned off (or routed to proper structured logging) in production because of noise and minor overhead.

**Mini assignment:** Write your own `database.py` from scratch (without looking) for a database called `shop`, then verify with `echo=True` that a simple query prints SQL to your console.

---

# SECTION 10 — SQLAlchemy Models

## 10.1 Defining a Model

**Definition:** A model is a Python class, inheriting from `Base`, whose class-level attributes describe a table's columns using `mapped_column()` and Python type hints via `Mapped[...]`.

**Syntax (modern SQLAlchemy 2.0 style):**
```python
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class StudentDB(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=True)
    email: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
```

## 10.2 Keyword-by-Keyword Explanation

- **`class StudentDB(Base)`** → declares a new ORM model. Inheriting from `Base` registers this class in SQLAlchemy's metadata so `create_all()` knows about it. (Note: naming it `StudentDB`, not just `Student`, is a common convention to visually distinguish the *database* model from the *Pydantic* schema class used for request/response validation — they look similar but serve very different jobs, see Section 16.)
- **`__tablename__ = "students"`** → the literal name of the SQL table this class maps to. Without this, SQLAlchemy has no idea what table you mean.
- **`Mapped[int]`** → a type-hint wrapper telling SQLAlchemy (and your IDE) that this attribute will hold a Python `int` once loaded from the database.
- **`mapped_column(...)`** → the actual column definition — this is where you specify the SQL type and constraints.
- **`Integer` / `String(100)`** → SQLAlchemy's own type classes representing SQL `INT` and `VARCHAR(100)` respectively. Using `String(100)` (with length) matters for MySQL specifically — MySQL requires a length for `VARCHAR`.
- **`primary_key=True`** → marks this column as the table's primary key.
- **`autoincrement=True`** → tells the database to auto-generate this value (1, 2, 3, ...) — maps to MySQL's `AUTO_INCREMENT`.
- **`nullable=False`** → equivalent to SQL's `NOT NULL`.
- **`nullable=True`** (or omitted, often default) → column is optional.
- **`unique=True`** → equivalent to SQL's `UNIQUE` constraint.

## 10.3 How This Model Maps to SQL

`StudentDB` above is functionally identical to running:
```sql
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    email VARCHAR(150) NOT NULL UNIQUE
);
```

**Diagram:**
```
Python Model (StudentDB)              SQL Table (students)
------------------------              ---------------------
id: Mapped[int] (PK, autoincr) <-->   id INT AUTO_INCREMENT PRIMARY KEY
name: Mapped[str] (not null)   <-->   name VARCHAR(100) NOT NULL
age: Mapped[int] (nullable)    <-->   age INT
email: Mapped[str] (unique)    <-->   email VARCHAR(150) UNIQUE NOT NULL
```

## 10.4 Common Column Types

| SQLAlchemy Type | MySQL Equivalent | Python Type |
|---|---|---|
| `Integer` | `INT` | `int` |
| `String(n)` | `VARCHAR(n)` | `str` |
| `Text` | `TEXT` | `str` |
| `Boolean` | `TINYINT(1)` | `bool` |
| `Float` | `FLOAT` | `float` |
| `Numeric(10,2)` | `DECIMAL(10,2)` | `decimal.Decimal` |
| `DateTime` | `DATETIME` | `datetime.datetime` |
| `Date` | `DATE` | `datetime.date` |

**Common beginner mistakes:**
- Using `String` without a length on MySQL — MySQL's `VARCHAR` requires a max length; this raises an error.
- Confusing the Pydantic schema class (used by FastAPI for request/response bodies) with the SQLAlchemy model class (used to talk to the database) — they are separate classes with separate purposes even when they look similar.
- Forgetting `nullable=False` on required fields, silently allowing `NULL` where business logic requires a value.

**Interview questions:**
- Q: What does `Mapped[int]` actually do vs `mapped_column(Integer)`?
  A: `Mapped[int]` is the Python-level type annotation for static typing/IDE support; `mapped_column(Integer, ...)` is the actual runtime column definition (SQL type + constraints). Together they fully describe the attribute.
- Q: Why must `String` specify a length for MySQL but not necessarily for PostgreSQL?
  A: MySQL's `VARCHAR` type requires a maximum length at table-creation time; PostgreSQL's `VARCHAR`/`TEXT` types are more flexible about unspecified lengths.

**Mini assignment:** Define a `ProductDB` model with `id`, `name` (required, max 120 chars), `price` (Numeric, required, must conceptually be > 0 — note the CHECK enforcement piece is covered separately at the DB level), and `in_stock` (Boolean, default True).

---

# SECTION 11 — FastAPI + SQLAlchemy

## 11.1 How FastAPI Talks to MySQL — The Big Picture

FastAPI itself has *zero* built-in database logic. It's purely an HTTP framework. The database connection is entirely handled by SQLAlchemy, which FastAPI calls into through a clean pattern called **Dependency Injection**.

```
HTTP Request
     │
     ▼
FastAPI route function
     │  (needs a database session)
     ▼
Depends(get_db)  ───►  yields a Session  ───►  route uses it  ───►  session closes automatically
     │
     ▼
SQLAlchemy Session → Engine → MySQL
```

## 11.2 `get_db()` and `yield`

```python
from database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

**Line-by-line:**
- `db = SessionLocal()` → creates a brand-new Session for this specific request.
- `yield db` → hands that session to whichever route function requested it — execution *pauses* here until the route function finishes.
- `finally: db.close()` → guarantees the session is closed and its connection returned to the pool, **even if the route raised an exception**.

**Why `yield` instead of `return`?** A generator function using `yield` lets FastAPI run code *both before and after* the route handles the request — `yield` is the pause point where the route "borrows" the resource; whatever comes after `yield` runs automatically once the route is done, guaranteeing cleanup. `return` would give up the session immediately with no chance to close it afterward.

## 11.3 Depends

```python
from fastapi import Depends

@app.get("/students")
def read_students(db: Session = Depends(get_db)):
    ...
```

**Definition:** `Depends(get_db)` tells FastAPI: "before running this route, call `get_db()`, and inject whatever it yields as the `db` parameter."

**Why it exists — Dependency Injection:** Instead of every route function manually creating and closing its own session (repetitive, easy to forget cleanup), FastAPI centralizes that logic in one reusable function and *injects* the result wherever needed. This is the industry-standard pattern called **Dependency Injection** — the route doesn't create its own dependencies, they are provided ("injected") from outside.

## 11.4 The Request Lifecycle (Session Scope)

1. A request hits `GET /students`.
2. FastAPI sees the route needs `db: Session = Depends(get_db)`.
3. FastAPI calls `get_db()`, which creates a new `Session` and yields it.
4. The route function runs, using `db` to query MySQL.
5. The route returns its response.
6. FastAPI resumes `get_db()` after the `yield`, running `db.close()`.
7. The connection returns to the Engine's pool, ready for the next request.

**Real-world analogy:** Think of `get_db` as a hotel front desk. Each guest (request) is handed a room key (`Session`) when they check in, uses the room during their stay (the route function's logic), and the key is automatically returned to the front desk (`db.close()`) the moment they check out — regardless of whether their stay went smoothly or something went wrong.

**Common beginner mistakes:**
- Creating a *global* `Session` shared across all requests instead of one per request via `Depends(get_db)` — causes data leaking between unrelated requests and severe concurrency bugs.
- Forgetting the `finally: db.close()` — leaks connections until the pool exhausts and the app grinds to a halt.

**Interview questions:**
- Q: Why does `get_db()` use `yield` instead of `return`?
  A: `yield` allows code to run *after* the route completes (closing the session), which a plain `return` cannot do — FastAPI's dependency system specifically supports generator-based dependencies for this setup/teardown pattern.
- Q: What is Dependency Injection, and why does FastAPI use it for the database?
  A: It's a design pattern where a function/class receives (is "injected with") the resources it needs from an external provider, rather than creating them itself — for the DB, it centralizes session creation/cleanup in one place, keeps route functions clean and testable, and guarantees consistent resource management across the whole app.

**Mini assignment:** Write `get_db()` from memory, then write a route `GET /ping-db` that opens a session via `Depends(get_db)` and executes a trivial query (e.g., counting rows in `students`) to confirm the wiring works end to end.

---

# SECTION 12 — CRUD Using SQLAlchemy

For all examples below, assume:
```python
from sqlalchemy.orm import Session
from sqlalchemy import or_
from models import StudentDB
```

## 12.1 Create

```python
def create_student(db: Session, name: str, age: int, email: str):
    new_student = StudentDB(name=name, age=age, email=email)
    db.add(new_student)      # stage the new object
    db.commit()              # write it to MySQL permanently
    db.refresh(new_student)  # reload it (to get the auto-generated id)
    return new_student
```

**Keyword explanation:**
- `db.add(obj)` → stages a new Python object to be inserted; nothing is sent to MySQL yet.
- `db.commit()` → flushes all staged changes as SQL (here, an `INSERT`) and permanently saves the transaction.
- `db.refresh(obj)` → re-fetches the object's current state from the database — necessary because `id` (and any server-side defaults) don't exist on the Python object until MySQL generates them during the INSERT.

**SQL generated behind the scenes:**
```sql
INSERT INTO students (name, age, email) VALUES ('Aisha', 20, 'aisha@mail.com');
```

## 12.2 Read

```python
def get_all_students(db: Session):
    return db.query(StudentDB).all()

def get_student_by_id(db: Session, student_id: int):
    return db.query(StudentDB).filter(StudentDB.id == student_id).first()

def search_students_by_name(db: Session, keyword: str):
    return db.query(StudentDB).filter(StudentDB.name.ilike(f"%{keyword}%")).all()

def count_students(db: Session):
    return db.query(StudentDB).count()
```

**Keyword explanation:**
- `db.query(Model)` → begins building a SELECT statement against that model's table.
- `.filter(condition)` → adds a WHERE clause.
- `.all()` → executes and returns every matching row as a list of model instances.
- `.first()` → executes and returns only the first matching row (or `None`), generating `LIMIT 1` under the hood.
- `.ilike(pattern)` → case-**insensitive** LIKE (MySQL's default `LIKE` is often already case-insensitive depending on collation, but `ilike` makes the intent explicit and is portable across databases).
- `.count()` → generates a `SELECT COUNT(*) ...` instead of pulling all rows just to count them in Python (much more efficient).

**SQL generated:**
```sql
SELECT * FROM students;
SELECT * FROM students WHERE id = 3 LIMIT 1;
SELECT * FROM students WHERE name LIKE '%an%';
SELECT COUNT(*) FROM students;
```

## 12.3 Update

```python
def update_student(db: Session, student_id: int, new_age: int):
    student = db.query(StudentDB).filter(StudentDB.id == student_id).first()
    if student:
        student.age = new_age   # just change the Python attribute
        db.commit()             # SQLAlchemy detects the change and generates UPDATE
    return student
```

**Internal working:** SQLAlchemy's Session keeps a live "identity map" tracking every object it has loaded — when you mutate an attribute on a tracked object, the Session marks it "dirty." On `commit()`, it automatically generates and runs an `UPDATE` only for the changed columns.

**SQL generated:**
```sql
UPDATE students SET age = 23 WHERE id = 3;
```

## 12.4 Delete

```python
def delete_student(db: Session, student_id: int):
    student = db.query(StudentDB).filter(StudentDB.id == student_id).first()
    if student:
        db.delete(student)
        db.commit()
    return student
```

**SQL generated:**
```sql
DELETE FROM students WHERE id = 3;
```

## 12.5 Combining Filters — `or_()`

```python
from sqlalchemy import or_

def search_flexible(db: Session, keyword: str):
    return db.query(StudentDB).filter(
        or_(StudentDB.name.ilike(f"%{keyword}%"), StudentDB.email.ilike(f"%{keyword}%"))
    ).all()
```

**SQL generated:**
```sql
SELECT * FROM students WHERE name LIKE '%raj%' OR email LIKE '%raj%';
```

## 12.6 Summary Table — Python Call → SQL

| SQLAlchemy Call | Generated SQL Concept |
|---|---|
| `db.add(obj)` + `db.commit()` | `INSERT INTO ...` |
| `db.query(Model).all()` | `SELECT * FROM ...` |
| `.filter(Model.x == y)` | `WHERE x = y` |
| `.filter(Model.x.ilike('%y%'))` | `WHERE x LIKE '%y%'` |
| `or_(a, b)` | `WHERE (a OR b)` |
| `.first()` | `... LIMIT 1` |
| `.count()` | `SELECT COUNT(*) FROM ...` |
| attribute mutation + `commit()` | `UPDATE ... SET ... WHERE ...` |
| `db.delete(obj)` + `commit()` | `DELETE FROM ... WHERE ...` |

**Common beginner mistakes:**
- Calling `db.commit()` after every single line inside a loop instead of once at the end (hurts performance and can cause inconsistent partial states).
- Forgetting `db.refresh()` after `add()`+`commit()` and then trying to access the auto-generated `id` — it may not be populated on the Python object yet without a refresh (behavior can also depend on engine settings).
- Using `.all()` and counting in Python (`len(query.all())`) instead of `.count()` — wastes memory and time on large tables.

**Best practices:**
- Wrap multi-step operations in a single transaction (one `commit()` at the end), so either everything succeeds or everything rolls back together.
- Always check `if student:` before using a `.first()` result — it can be `None`.

**Interview questions:**
- Q: What is the "dirty" state in a Session?
  A: When you change an attribute on an object the Session already tracks, SQLAlchemy marks it as "dirty" — pending an UPDATE the next time you flush/commit.
- Q: Why use `.count()` instead of `len(query.all())`?
  A: `.count()` runs an efficient `SELECT COUNT(*)` on the database server; `.all()` pulls every full row into memory just to measure the list length in Python — far more wasteful, especially on large tables.

**Mini assignment:** Implement full CRUD functions for a `ProductDB` model (create, get all, get by id, update price, delete, search by name).

---

# SECTION 13 — Old Project vs New Project

## 13.1 The "Old" In-Memory Approach

```python
students = []

@app.post("/students")
def create_student(student: dict):
    students.append(student)
    return student

@app.get("/students")
def get_students():
    return students

@app.delete("/students/{index}")
def delete_student(index: int):
    students.pop(index)
    return {"deleted": True}
```

**Problems:**
- **Data disappears** every time the server restarts — it's just a Python list living in RAM.
- **No concurrency safety** — two simultaneous requests modifying the list can corrupt state (race conditions).
- **No querying power** — filtering/searching means writing manual `for` loops over the entire list every time.
- **No relationships** — impossible to cleanly represent "this student belongs to this course."
- **Doesn't scale** — can't run multiple server instances (each would have its own separate, inconsistent list).

## 13.2 The "New" SQLAlchemy + MySQL Approach

```python
@app.post("/students")
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = StudentDB(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
```

**Why it's better:**

| Aspect | Old (in-memory list) | New (SQLAlchemy + MySQL) |
|---|---|---|
| Persistence | Lost on restart | Permanently stored on disk |
| Concurrency | Unsafe, race conditions | Handled by the DB engine's transactions/locking |
| Querying | Manual Python loops | Indexed SQL queries (`filter`, `ilike`, `count`) |
| Relationships | Not practical | Foreign keys, joins |
| Scaling to multiple servers | Impossible (separate memory per instance) | All instances share the same MySQL database |
| Data integrity | None (any value can be appended) | Enforced constraints (NOT NULL, UNIQUE, CHECK, FK) |

**Interview questions:**
- Q: Why is storing data in a Python list a bad idea for a real API?
  A: It's not persistent (lost on restart), not safe under concurrent access, doesn't scale across multiple server processes, and has none of the integrity guarantees a database provides.

**Mini assignment:** Take your earlier in-memory `students` list CRUD project and rewrite every route to use `StudentDB` + a MySQL-backed session, one route at a time, testing after each conversion.

---

# SECTION 14 — Project Structure

## 14.1 Why Split Into Multiple Files

**Why this concept exists:** Cramming database setup, table definitions, and route logic into one giant `main.py` works for a 10-minute demo but becomes unmanageable within days on any real project. Splitting responsibilities makes code easier to navigate, test, and reuse.

## 14.2 Recommended Structure

```
project/
├── database.py     # Engine, SessionLocal, Base, get_db()
├── models.py        # SQLAlchemy ORM model classes (tables)
├── schemas.py       # Pydantic classes (request/response validation shapes)
├── main.py          # FastAPI app + route definitions
```

## 14.3 Responsibility of Each File

**`database.py`** — "How do we connect?"
- Creates the `Engine` (one time, using the `DATABASE_URL`).
- Creates `SessionLocal` (the session factory).
- Defines `Base` (the declarative base all models inherit from).
- Defines `get_db()` (the dependency used by routes).

**`models.py`** — "What does our data look like in the database?"
- Contains SQLAlchemy ORM classes (`StudentDB`, `CourseDB`, ...), each mapped to a table, imported from `database.Base`.

**`schemas.py`** — "What shape of data do we accept/return over HTTP?"
- Contains Pydantic classes (`StudentCreate`, `StudentResponse`, ...) used purely for request validation and response serialization — **not** tied to the database directly.

**`main.py`** — "What can clients actually do?"
- Creates the `FastAPI()` app instance.
- Defines routes (`@app.post`, `@app.get`, ...), each using `Depends(get_db)` and the model/schema classes from the other files.

**Diagram:**
```
main.py  ──imports──►  models.py  ──imports──►  database.py (Base, engine)
   │                                                    ▲
   └──imports──►  schemas.py                            │
                                                get_db() used by main.py routes
```

**Common beginner mistakes:**
- Defining Pydantic schemas and SQLAlchemy models in the same file/class — conflates two very different responsibilities (validation vs persistence) and makes the code harder to reason about.
- Importing `main.py` from `models.py` (circular imports) — dependencies should flow one direction: `main.py` → `models.py`/`schemas.py` → `database.py`.

**Interview questions:**
- Q: Why keep Pydantic schemas separate from SQLAlchemy models even though they can look nearly identical?
  A: They serve fundamentally different jobs — Pydantic schemas validate/serialize data at the HTTP boundary (and can intentionally expose a *subset* or reshaped version of the data), while SQLAlchemy models define the actual database structure and persistence behavior. Merging them tightly couples your API contract to your database schema, which becomes painful as the two need to evolve independently (e.g., hiding a password field from API responses while still storing it in the DB).

**Mini assignment:** Take a single-file FastAPI+SQLAlchemy prototype and split it into `database.py`, `models.py`, `schemas.py`, `main.py`, verifying it still runs identically after the split.

---

# SECTION 15 — Complete Request Flow: `POST /students`

Walking through **every single step** that happens when a client calls `POST /students` with a JSON body like `{"name": "Aisha", "age": 20, "email": "aisha@mail.com"}`.

```
 1. Client
     │  sends HTTP POST /students with JSON body
     ▼
 2. FastAPI (Uvicorn/ASGI layer)
     │  receives the raw request, routes it to the matching function
     ▼
 3. Pydantic Validation (schemas.StudentCreate)
     │  parses & validates JSON → checks types, required fields
     │  ✗ if invalid → FastAPI immediately returns HTTP 422 (never reaches your code)
     ▼
 4. Route function runs
     │  db: Session = Depends(get_db)  → a fresh Session is created
     ▼
 5. Your code builds a StudentDB instance
     │  db_student = StudentDB(**student.dict())
     ▼
 6. SQLAlchemy Session
     │  db.add(db_student)   → stages the object (nothing sent yet)
     │  db.commit()          → SQLAlchemy compiles an INSERT statement
     ▼
 7. Engine
     │  borrows a connection from the pool, sends compiled SQL via PyMySQL driver
     ▼
 8. MySQL Server
     │  executes INSERT INTO students (...) VALUES (...)
     │  enforces constraints (NOT NULL, UNIQUE, etc.) — rejects if violated
     │  generates the auto-increment id
     ▼
 9. Result flows back up
     │  db.refresh(db_student)  → re-fetches the row, populating db_student.id
     ▼
10. Route function returns db_student
     │  FastAPI serializes it through your response_model (Pydantic) → JSON
     ▼
11. Response
     │  HTTP 201/200 with JSON body sent back to Client
```

**Important notes at each junction:**
- Step 3 is why FastAPI + Pydantic is powerful: bad data (wrong types, missing fields) is rejected *before* touching the database at all.
- Step 6-8 is exactly where "ORM → SQL → MySQL" from Section 7.5 happens in a real request.
- Step 9 is why `refresh()` matters — the client expects the newly created `id` back in the response, and only MySQL knows what that id is.
- If any step from 6-8 raises an exception (e.g., a UNIQUE violation because the email already exists), and you haven't handled it, FastAPI returns a 500 error — production code should catch this and return a clean 400/409 instead (see Section 16).

**Interview questions:**
- Q: At what point in the request lifecycle does invalid input get rejected, and why does that matter?
  A: During Pydantic validation (step 3), before any database code runs — this protects the database from ever seeing malformed data and gives the client a fast, precise 422 error instead of a confusing failure deep in the database layer.
- Q: Why is `db.refresh()` necessary before returning the created object?
  A: Because the primary key (and any DB-generated defaults) don't exist on the Python object until the database assigns them during the INSERT — refresh reloads the object with those generated values.

**Mini assignment:** Draw this entire flow from memory for `DELETE /students/{id}` instead, noting what changes (e.g., no Pydantic *request* body needed, but a check that the student exists before deleting).

---

# SECTION 16 — Industry Best Practices

## 16.1 Why Response Models Matter

```python
@app.post("/students", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    ...
```

**Why:** Without `response_model`, FastAPI would try to serialize the raw SQLAlchemy object directly, which can leak internal-only fields (e.g., a hashed password column) and doesn't give you control over the exact shape/documentation of your API's output. `response_model` acts as an explicit *contract* — only the fields it defines get sent to the client, regardless of what extra attributes the database object carries.

## 16.2 Why Duplicate Checks Are Important

```python
existing = db.query(StudentDB).filter(StudentDB.email == student.email).first()
if existing:
    raise HTTPException(status_code=400, detail="Email already registered")
```

**Why:** Relying solely on the database's `UNIQUE` constraint to catch duplicates means the failure surfaces as an ugly low-level database exception (potentially a 500 error) instead of a clean, predictable API error message. Checking proactively in application code gives clients a clear, actionable 400 response.

## 16.3 Why `commit()` Is Needed

Without `commit()`, all your changes exist only inside the Session's pending transaction — nothing is durably saved in MySQL, and everything vanishes on rollback or disconnect. `commit()` is the explicit boundary that says "this unit of work is complete and correct — make it permanent."

## 16.4 Why `refresh()` Is Used

As covered in Section 15 — auto-generated values (primary keys, server-side defaults, `CURRENT_TIMESTAMP` columns) don't exist on your Python object until the database creates the row. `refresh()` re-syncs the Python object with what the database actually stored.

## 16.5 Why ORM Models Differ From Pydantic Models

| | SQLAlchemy Model (`StudentDB`) | Pydantic Schema (`StudentCreate`/`StudentResponse`) |
|---|---|---|
| Purpose | Represents a database table | Validates/serializes HTTP request & response data |
| Lives in | `models.py` | `schemas.py` |
| Tied to | The actual database structure | The public API contract |
| Can hide fields? | No — has every DB column | Yes — can expose a subset (e.g., hide `password_hash`) |
| Changes when... | The table structure changes | The API contract changes |

Keeping them separate lets your database schema evolve independently of what you choose to expose publicly — a very common real-world need (e.g., storing a `password_hash` column that should never appear in any API response).

## 16.6 Additional Best Practices

- **Never commit secrets** (DB passwords) into source code — use environment variables / `.env` files (with `.env` in `.gitignore`).
- **Use connection pooling settings deliberately** (`pool_size`, `max_overflow`) for production traffic levels.
- **Handle exceptions around commits** — wrap in try/except and call `db.rollback()` on failure, so a partial/broken transaction never lingers.
- **Use Alembic for schema migrations** in any real project — `create_all()` is fine for prototypes only.
- **Paginate list endpoints** (`LIMIT`/`OFFSET` or cursor-based) — never return an entire table unbounded.
- **Log meaningful errors**, not raw stack traces, to clients.
- **Validate at the boundary** — let Pydantic reject bad input before it ever reaches the database layer.

**Interview questions:**
- Q: What should happen if `db.commit()` fails partway through a multi-step operation?
  A: The exception should be caught, `db.rollback()` called to undo any partial changes, and a clean error should be returned to the client — the database should never be left in an inconsistent halfway state.
- Q: Why not just return the raw SQLAlchemy model object directly from a FastAPI route?
  A: `response_model` lets you explicitly control and document exactly what shape of data leaves your API, hiding internal-only fields and decoupling your public contract from your internal table structure.

**Mini assignment:** Add a try/except with rollback around your `create_student` endpoint, and add a duplicate-email check that returns a 400 with a clear message.

---

# SECTION 17 — Interview Questions (100+ Beginner-to-Intermediate, with Answers)

## A. DBMS & SQL Fundamentals (1–20)

1. **What is a database?** An organized, persistent collection of related data managed by a DBMS.
2. **What is a DBMS?** Software that creates, manages, and secures access to databases (e.g., MySQL).
3. **What is RDBMS?** A DBMS that organizes data into related tables using rows/columns (e.g., MySQL, PostgreSQL).
4. **Difference between DBMS and RDBMS?** RDBMS enforces the relational model (tables, keys, relationships); generic DBMS doesn't require this (e.g., some NoSQL stores).
5. **What is a primary key?** A column (or set of columns) uniquely identifying each row; cannot be NULL or duplicated.
6. **What is a foreign key?** A column referencing another table's primary key, enforcing referential integrity.
7. **Difference between PRIMARY KEY and UNIQUE?** Primary key: one per table, never NULL. Unique: multiple allowed per table, can be NULL once.
8. **What is normalization?** The process of organizing tables to reduce data redundancy and improve integrity by splitting data into related tables.
9. **What is a composite key?** A primary key made of two or more columns together.
10. **What does `NOT NULL` do?** Forces a column to always have a value.
11. **What does `DEFAULT` do?** Auto-fills a column with a specified value if none is provided on insert.
12. **What is a `CHECK` constraint?** Enforces a custom boolean condition on column values (e.g., `price > 0`).
13. **Difference between `DELETE`, `DROP`, and `TRUNCATE`?** `DELETE` removes rows (can use WHERE, logged, can rollback within a transaction); `DROP` removes the entire table/database structure; `TRUNCATE` quickly removes all rows but keeps the table structure (typically not row-by-row logged).
14. **What does the `%` wildcard do in LIKE?** Matches zero or more characters.
15. **What does the `_` wildcard do in LIKE?** Matches exactly one character.
16. **What is the purpose of `ORDER BY`?** Sorts query results by one or more columns.
17. **What does `LIMIT`/`OFFSET` do?** Restricts the number of returned rows and skips a number of rows — used for pagination.
18. **What happens if you omit `WHERE` in an UPDATE/DELETE?** Every row in the table is affected.
19. **What is a JOIN, conceptually?** An operation that combines rows from two or more tables based on a related column.
20. **What is an index?** A data structure (often a B-tree) that speeds up lookups on a column at the cost of extra storage and slightly slower writes.

## B. Tables & Constraints (21–35)

21. **What does `AUTO_INCREMENT` do in MySQL?** Automatically generates the next integer value for a column (commonly the primary key) on each insert.
22. **What is `ALTER TABLE` used for?** Changing an existing table's structure (add/drop/rename/modify columns) without losing data.
23. **What's the difference between `VARCHAR` and `TEXT`?** `VARCHAR(n)` has a defined max length and is typically more efficient for shorter, indexed text; `TEXT` is for larger, variable-length text and has different indexing limitations.
24. **What is referential integrity?** The guarantee that a foreign key value always points to an existing row in the referenced table.
25. **What happens on `ON DELETE CASCADE`?** Deleting a parent row automatically deletes all its dependent child rows.
26. **Can a foreign key be NULL?** Yes, unless it's also marked `NOT NULL` — a NULL foreign key means "no relationship" for that row.
27. **What is `DESC table_name` used for?** Shows a table's structure: columns, types, nullability, keys, defaults.
28. **Difference between a schema and a table?** Schema is the whole structural blueprint (possibly multiple tables and relationships); a table is one specific structure within it.
29. **Why avoid natural keys (like email) as primary keys?** Natural values can change; a primary key referenced by foreign keys elsewhere shouldn't need to change.
30. **What's the purpose of `UNIQUE` combined with `NOT NULL`?** Guarantees the column always has a value and that value never repeats — common for things like usernames.
31. **What is a self-referencing foreign key?** A foreign key in a table that references the same table's primary key (e.g., an `employees` table with a `manager_id` pointing to another employee).
32. **What is a many-to-many relationship, and how is it modeled?** A relationship where many rows in table A relate to many rows in table B — modeled with a junction/association table holding foreign keys to both.
33. **What is cascading update vs cascading delete?** Cascading update propagates a primary key change to all referencing foreign keys; cascading delete propagates row deletion to dependent rows.
34. **Why specify a length for VARCHAR in MySQL?** MySQL requires a maximum length for VARCHAR columns at creation time.
35. **What is a surrogate key?** An artificial key (like an auto-incrementing `id`) with no business meaning, used purely to uniquely identify rows.

## C. SQLAlchemy & ORM (36–65)

36. **What is ORM?** A technique/library mapping Python objects/classes to database tables, letting you use Python instead of raw SQL.
37. **What problem does ORM solve?** Removes repetitive raw-SQL boilerplate, adds SQL-injection protection, and improves database portability and maintainability.
38. **What is the SQLAlchemy Engine?** The core interface managing the DB connection pool and SQL dialect.
39. **What is the SQLAlchemy Session?** A transactional workspace tracking objects and translating ORM operations into SQL for one unit of work.
40. **Difference between Engine and Session?** Engine is long-lived and connection-pool-focused; Session is short-lived, created per unit of work (e.g., per request).
41. **What is `Base` (DeclarativeBase)?** The parent class all ORM models inherit from, registering them in SQLAlchemy's metadata.
42. **What does `Base.metadata.create_all(engine)` do?** Creates tables for every registered model that doesn't already exist in the database.
43. **Does `create_all()` alter existing tables?** No — it only creates missing tables; schema changes need a migration tool like Alembic.
44. **What does `mapped_column()` do?** Defines an actual database column (type + constraints) for a model attribute.
45. **What is `Mapped[int]` for?** A type-hint annotation telling SQLAlchemy/your IDE what Python type this column maps to.
46. **What does `nullable=False` correspond to in SQL?** `NOT NULL`.
47. **What does `unique=True` correspond to in SQL?** `UNIQUE`.
48. **What does `db.add()` do?** Stages a new object to be inserted; nothing is sent to the database yet.
49. **What does `db.commit()` do?** Executes and permanently saves all pending changes as a transaction.
50. **What does `db.refresh()` do, and why is it needed?** Reloads an object's state from the database — needed to populate auto-generated values like the primary key after an insert.
51. **What does `db.query(Model).filter(...)` generate?** A `SELECT ... WHERE ...` SQL statement.
52. **Difference between `.all()` and `.first()`?** `.all()` returns every matching row as a list; `.first()` returns only the first match (or `None`), generating `LIMIT 1`.
53. **What does `.count()` do, and why prefer it over `len(query.all())`?** Generates an efficient `SELECT COUNT(*)`; `len(query.all())` wastefully loads every full row just to measure the list.
54. **What does `.ilike()` do?** Performs a case-insensitive LIKE pattern match.
55. **What does `or_()` do?** Combines multiple filter conditions with SQL `OR`.
56. **How does SQLAlchemy generate an UPDATE?** By tracking attribute mutations on already-loaded objects ("dirty" objects) and issuing an UPDATE for changed columns on commit.
57. **How do you delete a row with SQLAlchemy?** `db.delete(obj)` followed by `db.commit()`.
58. **What is the N+1 query problem?** A performance issue where fetching a list, then accessing a related attribute per item in a loop, triggers one query per item instead of a single efficient join/batch query.
59. **What is lazy loading vs eager loading?** Lazy loading fetches related data only when accessed (can cause N+1 issues); eager loading fetches related data upfront in the same or a combined query.
60. **Is SQLAlchemy always faster than raw SQL?** No — hand-tuned raw SQL can outperform ORM-generated SQL for complex queries; ORM trades some performance for productivity and safety.
61. **What is a connection pool, and why does it matter?** A set of reused, already-open database connections managed by the Engine — avoids the cost of opening a fresh TCP connection for every query.
62. **What is `autoflush`, and what does setting it to False mean?** Controls whether SQLAlchemy automatically pushes pending changes to the DB before running a query; `False` means you control flush/commit timing explicitly.
63. **Why is the ORM model class often named differently from the Pydantic schema (e.g., `StudentDB` vs `Student`)?** To visually and structurally distinguish the database-mapped class from the API validation/serialization class, even though their fields may look similar.
64. **What happens if you mutate an object's attribute but never call `commit()`?** The change stays only in memory/in the Session's pending state — it is never written to the database.
65. **Can one SQLAlchemy model map to more than one table?** Not directly in the standard pattern — one model class typically maps to exactly one table (though advanced patterns like joined-table inheritance exist).

## D. FastAPI Integration (66–85)

66. **What is Dependency Injection in FastAPI?** A pattern where a route receives ("is injected with") resources like a DB session from an external provider function via `Depends()`, rather than creating them itself.
67. **What does `Depends(get_db)` do?** Tells FastAPI to call `get_db()` before running the route and pass whatever it yields into the route's parameter.
68. **Why does `get_db()` use `yield` instead of `return`?** `yield` lets code run both before (session creation) and after (session closing) the route executes — enabling guaranteed cleanup via `finally`.
69. **What does `db.close()` in the `finally` block guarantee?** The session's connection is released back to the pool even if the route raised an exception.
70. **Why create a new Session per request instead of one global Session?** To keep each request's transaction and object tracking isolated — prevents data/state leaking between unrelated concurrent requests.
71. **What is `response_model` for?** Explicitly defines and restricts the shape of data returned to the client, hiding internal-only fields regardless of what the underlying object contains.
72. **Why use Pydantic for request validation?** It automatically parses and validates incoming JSON against declared types/constraints, rejecting malformed requests (HTTP 422) before your code or the database ever sees them.
73. **What HTTP status code does FastAPI return automatically on failed Pydantic validation?** 422 Unprocessable Entity.
74. **Map `POST`, `GET`, `PUT`, `PATCH`, `DELETE` to SQL operations.** POST→INSERT, GET→SELECT, PUT/PATCH→UPDATE, DELETE→DELETE.
75. **Difference between PUT and PATCH?** PUT conceptually replaces the entire resource; PATCH updates only specified fields.
76. **What happens if a route function raises an unhandled exception during a DB operation?** FastAPI returns a 500 Internal Server Error by default; production code should catch specific errors (e.g., constraint violations) and return a clean 4xx response instead.
77. **Why should you check for duplicates in code even when a UNIQUE constraint exists?** To return a clean, predictable API error (e.g., 400) instead of letting an ugly low-level database exception surface as a 500 error.
78. **What is the typical recommended project structure for a FastAPI+SQLAlchemy app?** `database.py` (engine/session/base), `models.py` (ORM models), `schemas.py` (Pydantic schemas), `main.py` (routes).
79. **Why separate Pydantic schemas from SQLAlchemy models?** They serve different purposes — API contract/validation vs actual database structure — and need to evolve independently.
80. **What's the danger of returning a raw SQLAlchemy object directly without a response_model?** It can leak internal-only fields (e.g., password hashes) and gives you no control over exactly what shape of data is exposed publicly.
81. **How does pagination typically get implemented in a FastAPI list endpoint?** Using query parameters (e.g., `skip`, `limit`) mapped to SQL's `LIMIT`/`OFFSET`.
82. **What does `db.rollback()` do, and when should you call it?** Reverts all uncommitted changes in the current transaction — call it when an exception occurs partway through a multi-step operation, to avoid leaving a half-completed state.
83. **Why avoid hardcoding the database URL/credentials in source code?** Security risk (secrets exposed in version control) and inflexibility across environments (dev/staging/prod) — use environment variables instead.
84. **What tool is typically used for schema migrations in real SQLAlchemy projects (instead of `create_all()`)?** Alembic.
85. **Why is it important to test the full request lifecycle (validation → DB → response) rather than just the SQL query in isolation?** Because bugs commonly occur at the boundaries — e.g., a valid query might still return data in a shape that breaks the response_model, or invalid input might slip past a loosely defined schema.

## E. Conceptual / Comparison (86–100+)

86. **Why is storing app data in a Python list a bad idea for production?** Not persistent, not concurrency-safe, doesn't scale across multiple server instances, and lacks database integrity guarantees.
87. **What's the main advantage of MySQL over storing data in flat CSV/JSON files?** Concurrency control, indexing for fast queries, constraints for data integrity, transactions, and built-in backup/recovery.
88. **What is a transaction?** A sequence of database operations treated as a single atomic unit — either all succeed (commit) or none do (rollback).
89. **What does ACID stand for (high-level)?** Atomicity, Consistency, Isolation, Durability — the guarantees a reliable transactional database provides.
90. **Why might you choose NoSQL (e.g., MongoDB) over MySQL for some projects?** When the schema is highly flexible/evolving, or the data model doesn't naturally fit rows/columns/relationships (e.g., deeply nested, variable documents).
91. **What is database connection pooling, conceptually?** Reusing a fixed set of already-open database connections across many requests instead of opening/closing a new one each time.
92. **Why is indexing a trade-off, not a free win?** Indexes speed up reads but add overhead to writes (every insert/update must also update the index) and consume extra storage.
93. **What's the risk of running `ALTER TABLE` directly on a huge production table during peak hours?** It can lock the table and cause downtime or severe slowdowns for live traffic.
94. **What's the difference between a logical delete (soft delete) and a physical delete?** Logical delete marks a row as inactive/deleted via a flag (e.g., `is_deleted=True`) without removing it; physical delete (`DELETE FROM`) permanently removes the row.
95. **Why might a real system prefer soft deletes?** Preserves historical data for auditing/recovery, and avoids breaking foreign key relationships that still reference the "deleted" row.
96. **What is the main difference between `session.query()` (legacy style) and `session.execute(select(...))` (2.0 style) in modern SQLAlchemy?** Both ultimately build and run SQL; the 2.0 `select()` style is the more explicit, forward-looking API aligned with SQLAlchemy's newer core expression language, while `.query()` is the older ORM-specific convenience API.
97. **Why does FastAPI pair so naturally with SQLAlchemy and Pydantic?** FastAPI handles HTTP + validation (via Pydantic), SQLAlchemy handles persistence — each layer has one clear job, and Depends() cleanly wires them together per request.
98. **What's a realistic first debugging step if a FastAPI+SQLAlchemy app raises "table doesn't exist"?** Confirm `Base.metadata.create_all(engine)` was actually called, and that the model was imported before that call (otherwise SQLAlchemy never registered it).
99. **What's a realistic first debugging step if inserts succeed but the returned `id` is `None`?** Confirm `db.refresh(obj)` was called after `db.commit()`.
100. **What's the benefit of `echo=True` on the Engine during development?** Prints every generated SQL statement, helping you verify the ORM is producing the SQL you expect.
101. **Why does splitting a monolithic `main.py` into `database.py`/`models.py`/`schemas.py`/`main.py` matter as a project grows?** Keeps responsibilities isolated, making the codebase easier to navigate, test, and extend without one file becoming an unmanageable mess.
102. **What's the difference between `IN` and multiple `OR` conditions in SQL, and are they equivalent?** `WHERE city IN ('Delhi','Mumbai')` is functionally equivalent to `WHERE city='Delhi' OR city='Mumbai'` but more concise and often easier for the optimizer to reason about.

**Mini assignment:** Without looking at the answers, write out your own answers to questions 40, 58, 66, 76, and 94 — these five test the concepts most commonly probed in real interviews.

---

# SECTION 18 — Revision Notes (Condensed)

- **Data** → raw facts. **Database** → organized, persistent collection of data. **DBMS** → software managing databases (MySQL, PostgreSQL, etc.).
- **Relational DB** → tables + rows + columns + relationships enforced via keys.
- **Database** = container of **tables**. **Table** = rows (records) + columns (fields). **Schema** = the whole structural blueprint.
- **Constraints**: PRIMARY KEY (unique + not null, one per table), FOREIGN KEY (valid reference to another table), UNIQUE (no dupes, nullable), NOT NULL (mandatory), DEFAULT (auto-fill), CHECK (custom rule).
- **CRUD SQL**: INSERT (create), SELECT (read), UPDATE (modify — always use WHERE!), DELETE (remove — always use WHERE!). Filter with WHERE, sort with ORDER BY, paginate with LIMIT/OFFSET, pattern-match with LIKE (`%`=any chars, `_`=one char).
- **REST ↔ SQL**: POST→INSERT, GET→SELECT, PUT/PATCH→UPDATE, DELETE→DELETE.
- **ORM** = Python objects ↔ SQL translation layer. Solves: repetition, injection risk, DB lock-in, hard maintenance. Costs: learning curve, hidden performance traps (N+1).
- **SQLAlchemy architecture**: Engine (connection pool + dialect, created once) → Session (per-request transactional workspace) → Model (Python class = table) → Query (generates SQL).
- **Setup**: `create_engine(DATABASE_URL)` → `sessionmaker(bind=engine)` → `DeclarativeBase` (`Base`) → `Base.metadata.create_all(engine)`.
- **Models**: `Mapped[type]` + `mapped_column(SQLType, constraints...)`, `__tablename__` required.
- **FastAPI + SQLAlchemy**: `get_db()` (a generator using `yield`) + `Depends(get_db)` = Dependency Injection giving each request its own Session, always closed in `finally`.
- **CRUD in SQLAlchemy**: `add()`+`commit()`+`refresh()` = Create. `query().filter().all()/.first()/.count()` = Read. Mutate attribute + `commit()` = Update. `delete()`+`commit()` = Delete.
- **Project structure**: `database.py` (connection), `models.py` (tables), `schemas.py` (API contract), `main.py` (routes).
- **Request lifecycle**: Client → FastAPI → Pydantic validation → Route → SQLAlchemy Session → Engine → MySQL → refresh → response_model serialization → Client.
- **Best practices**: use `response_model`, check duplicates explicitly, always `commit()`/`rollback()` deliberately, `refresh()` after insert, keep ORM models and Pydantic schemas separate, never hardcode secrets, paginate lists, use Alembic for real migrations.

---

# SECTION 19 — One-Page Cheat Sheet

## SQL
```sql
CREATE DATABASE db_name;
DROP DATABASE db_name;
USE db_name;
SHOW DATABASES;
SHOW TABLES;
DESC table_name;

CREATE TABLE t (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(150) UNIQUE,
  age INT CHECK (age >= 0),
  status VARCHAR(20) DEFAULT 'active'
);
ALTER TABLE t ADD COLUMN phone VARCHAR(15);
ALTER TABLE t DROP COLUMN phone;
ALTER TABLE t MODIFY COLUMN age SMALLINT;
DROP TABLE t;

INSERT INTO t (name, email) VALUES ('Aisha', 'a@mail.com');
SELECT * FROM t WHERE age > 20 ORDER BY age DESC LIMIT 10 OFFSET 0;
SELECT * FROM t WHERE name LIKE 'A%' AND city IN ('Delhi','Mumbai');
UPDATE t SET age = 23 WHERE id = 1;
DELETE FROM t WHERE id = 1;
```

## SQLAlchemy Setup (`database.py`)
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "mysql+pymysql://user:pass@localhost/db_name"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase): pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

## SQLAlchemy Model (`models.py`)
```python
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class StudentDB(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
```

## SQLAlchemy CRUD
```python
db.add(obj); db.commit(); db.refresh(obj)                     # Create
db.query(Model).all()                                         # Read all
db.query(Model).filter(Model.id == id).first()                 # Read one
db.query(Model).filter(Model.name.ilike(f"%{kw}%")).all()      # Search
db.query(Model).count()                                        # Count
obj.attr = new_val; db.commit()                                 # Update
db.delete(obj); db.commit()                                     # Delete
```

## FastAPI Wiring (`main.py`)
```python
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, Base, engine
from models import StudentDB
from schemas import StudentCreate, StudentResponse

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.post("/students", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    if db.query(StudentDB).filter(StudentDB.email == student.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    db_student = StudentDB(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
```

## REST ↔ SQL Quick Map
| HTTP | SQL |
|---|---|
| POST | INSERT |
| GET | SELECT |
| PUT/PATCH | UPDATE |
| DELETE | DELETE |

---

# SECTION 20 — Practice Zone

## 20.1 — 30 SQL Practice Questions

*(Assume a `students(id, name, age, city, email)` table and a `courses(id, title, fee)` table unless stated otherwise.)*

1. Create a `students` table with an auto-incrementing primary key, required name, and unique email.
2. Insert 5 students in a single statement.
3. Select all students older than 21.
4. Select only the `name` and `city` columns for all students.
5. Select students from 'Delhi' OR 'Mumbai' using `IN`.
6. Select students whose name starts with "S".
7. Select students whose email ends with "@gmail.com".
8. Select students whose name contains exactly 5 characters using `_`.
9. Sort students by age descending, then name ascending.
10. Get the 2nd page of results, 5 per page.
11. Count how many students are from each city (requires `GROUP BY`, a natural extension).
12. Update a specific student's city by id.
13. Update all students in 'Pune' to 'Mumbai' (be careful with WHERE!).
14. Delete a student by id.
15. Delete all students older than 100 (data cleanup scenario).
16. Add a `phone` column to `students` using `ALTER TABLE`.
17. Remove the `phone` column.
18. Create a `courses` table with `id`, `title`, `fee CHECK (fee > 0)`.
19. Create an `enrollments` junction table linking `students` and `courses` via foreign keys.
20. Insert an enrollment row, then try inserting one with an invalid `student_id` and observe the error.
21. Write a query to find students NOT enrolled in any course (conceptual JOIN/anti-join).
22. Find the average age of all students.
23. Find the oldest student's name.
24. Find students whose age is between 18 and 25 using `BETWEEN`.
25. Find students with a NULL email.
26. Rename the `students` table's `name` column to `full_name`.
27. Show the full structure of the `students` table.
28. List every database on the server.
29. Drop the `enrollments` table safely (`IF EXISTS`).
30. Design (on paper) constraints for a `products` table: unique SKU, required name, price > 0, default stock 0.

## 20.2 — 30 SQLAlchemy Practice Questions

1. Define a `CourseDB` model with `id`, `title` (required), `fee` (Numeric).
2. Define a `StudentDB` model with a unique `email` and nullable `age`.
3. Create the Engine and SessionLocal for a database called `academy`.
4. Write `get_db()` from memory without checking notes.
5. Create a new student using `add()`/`commit()`/`refresh()`.
6. Fetch all students using `.query().all()`.
7. Fetch one student by id using `.filter().first()`.
8. Search students by partial name using `.ilike()`.
9. Count all students using `.count()` instead of `len(.all())`.
10. Update a student's age and commit the change.
11. Delete a student by id, checking it exists first.
12. Combine two filter conditions using `or_()`.
13. Combine two filter conditions using `and_()` (research this — same import location as `or_`).
14. Write a query with both `.filter()` and `.order_by()`.
15. Write a query with `.limit()` and `.offset()` for pagination.
16. Add a `CourseDB` foreign key `category_id` referencing a `CategoryDB` model.
17. Explain (in writing) what SQL is generated by `db.query(StudentDB).filter(StudentDB.age > 20).all()`.
18. Explain what happens if you forget `db.commit()` after `db.add()`.
19. Explain what happens if you forget `db.refresh()` after creating a row and then access `.id`.
20. Write a function that returns the count of students in a given city.
21. Write a function that raises a clean error if creating a student with a duplicate email.
22. Wrap a multi-step create-then-update operation in a single try/except with rollback on failure.
23. Explain the difference between `.first()` and `.all()[0]`, including what happens if there are zero results.
24. Model a many-to-many relationship between `StudentDB` and `CourseDB` via an association table.
25. Write a query using `.count()` combined with a `.filter()` condition.
26. Explain what "dirty" means in the context of a Session object.
27. Explain why `echo=True` is useful and where you'd turn it off.
28. Explain the purpose of `autoflush=False`.
29. Explain why a new Session should be created per request instead of reused globally.
30. Design the full model layer (models.py) for a `library` app: `BookDB`, `AuthorDB`, `BorrowRecordDB`.

## 20.3 — 20 FastAPI Practice Questions

1. Create a FastAPI app with a single `GET /` route returning `{"status": "ok"}`.
2. Add a `POST /students` route accepting a Pydantic `StudentCreate` schema.
3. Add `Depends(get_db)` to that route and use it to insert a row.
4. Add a `GET /students` route returning all students with `response_model=list[StudentResponse]`.
5. Add a `GET /students/{id}` route, returning 404 if not found.
6. Add a `PUT /students/{id}` route that updates a student's fields.
7. Add a `DELETE /students/{id}` route.
8. Add pagination query parameters (`skip`, `limit`) to the `GET /students` route.
9. Add a duplicate-email check that raises `HTTPException(400, ...)`.
10. Explain, in your own words, why `get_db()` uses `yield`.
11. Add a search endpoint `GET /students/search?keyword=...` using `.ilike()`.
12. Add response models that hide an internal `password_hash` field from a `UserDB` model.
13. Wrap a route's database logic in try/except with rollback on error.
14. Explain what status code is returned automatically on invalid Pydantic input, and why.
15. Explain the difference between a path parameter and a query parameter with an example of each.
16. Build a `PATCH /students/{id}` route that updates only provided fields (partial update).
17. Add a `GET /courses/{id}/students` route demonstrating a relationship query.
18. Explain what would go wrong if `Base.metadata.create_all()` is never called.
19. Explain what would happen (concurrency-wise) if a single global Session were shared across all routes.
20. Design the full route file (`main.py`) for a small "Library" API: books, authors, borrow/return endpoints.

## 20.4 — 10 Mini Projects

1. **Student Directory API** — CRUD for students with a unique-email check.
2. **Book Catalog API** — CRUD for books with title search (`ilike`) and price filtering.
3. **Todo List API** — tasks with a `completed` boolean and `PATCH` toggle endpoint.
4. **Contact Book API** — contacts with unique phone numbers and city-based search.
5. **Movie Ratings API** — movies + ratings (one-to-many), average-rating query.
6. **Simple Blog API** — posts with `title`, `content`, `published` boolean, filter by published status.
7. **Employee Directory API** — employees with a self-referencing `manager_id` foreign key.
8. **Product Inventory API** — products with `stock_quantity`, a CHECK constraint on price, low-stock filter endpoint.
9. **Event RSVP API** — events + attendees (many-to-many via an association table).
10. **Feedback Collector API** — feedback entries with a rating (CHECK 1–5) and free-text comment.

## 20.5 — 5 Major Projects

1. **School Management System** — students, courses, enrollments (many-to-many), teachers, grades. Full CRUD, search, pagination, duplicate checks, and relationship-based endpoints (e.g., "all students in course X").
2. **E-Commerce Backend** — customers, products (with stock + price CHECK), orders, order_items (many-to-many with quantity), basic order-total calculation, and status transitions (`pending → shipped → delivered`).
3. **Library Management System** — books, authors (one-to-many), members, borrow_records (many-to-many with due dates), overdue-detection query, and availability tracking.
4. **Hospital Appointment System** — doctors, patients, appointments (many-to-many with a specific date/time), department relationships, and conflict-detection logic (no double-booking a doctor's slot).
5. **Job Portal Backend** — companies, job_postings (one-to-many), applicants, applications (many-to-many with a status field), search/filter by job title/location, and a duplicate-application check.

**How to use this Practice Zone:** Work top-down — SQL questions first (build real comfort with raw SQL before trusting the ORM's abstraction over it), then SQLAlchemy questions (map every concept back to the SQL you already know), then FastAPI questions (wire it all into a real HTTP API), then attempt at least 3 mini projects before tackling one major project end-to-end.

---

*End of notes. This guide is meant to be revisited — re-read Section 18 (Revision Notes) and Section 19 (Cheat Sheet) before interviews, and treat Section 20 as your hands-on lab.*
