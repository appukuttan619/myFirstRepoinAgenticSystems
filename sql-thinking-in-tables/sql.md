# Understanding Relational Databases in AI Systems

## 1. Why Databases Are Important in AI Systems

Databases store and manage structured data that AI systems use for training, analysis, and decision-making.

### Why they are important
- Efficient storage of large datasets
- Fast data retrieval using queries
- Data consistency and reliability
- Scalability for growing systems

### Examples of stored data
| AI Application | Data Stored |
|---|---|
| Recommendation systems | User activity, product views |
| Fraud detection | Transaction records |
| Chatbots | Conversation history |
| Healthcare AI | Patient data |

### Example

| User_ID | Name | Age |
|---|---|---|
| 101 | Amit | 25 |
| 102 | Sara | 30 |

Structured storage helps AI systems easily analyze and retrieve data.

---

# 2. Relational Database Mental Model

A relational database organizes data into **tables, rows, and columns**.

### Tables
A **table** represents a single entity (e.g., Employees).

| Employee_ID | Name | Department |
|---|---|---|
| 1 | Rahul | IT |
| 2 | Neha | HR |

### Rows
A **row** represents one record.

Example:  
`1, Rahul, IT` → One employee.

### Columns
A **column** represents an attribute of the entity.

Examples:
- Name
- Department
- Salary

### Why one entity per table
It prevents duplication and keeps data organized.

Example:

**Customers Table**

| Customer_ID | Name |

**Orders Table**

| Order_ID | Customer_ID |

---

# 3. Primary Key

A **primary key** uniquely identifies each record in a table.

Example:

| Employee_ID | Name |
|---|---|
| 1 | Rahul |
| 2 | Neha |

Here `Employee_ID` is the primary key.

### Rules
- Must be **unique**
- Cannot be **NULL**

### Importance
- Identifies records uniquely
- Prevents duplicates
- Helps link tables together

---

# 4. Database Schema

A **schema** is the structure or blueprint of a database.

It defines:
- Table names
- Column names
- Data types
- Keys and relationships

Example schema:

**Employees Table**

| Column | Type |
|---|---|
| Employee_ID | INT |
| Name | VARCHAR |
| Department | VARCHAR |

Schemas ensure the database structure stays consistent.

---

# 5. Relationships Between Tables

Tables connect using **foreign keys**.

A **foreign key** references the primary key of another table.

Example:

**Users Table**

| User_ID | Name |
|---|---|
| 1 | Amit |
| 2 | Sara |

**Orders Table**

| Order_ID | User_ID |
|---|---|
| 101 | 1 |
| 102 | 2 |

Here `User_ID` in the Orders table is a **foreign key**.

### Why relationships matter
- Connect related data
- Avoid duplication
- Maintain data integrity