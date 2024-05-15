# University Database Project

## Overview
This project defines a database schema for a university management system. It includes tables and relationships to store information about professors, colleges, departments, courses, sections, students, and the courses taken by students. Additionally, a Python script for managing student information is provided.

## Features
- **Tables**: PROFESSOR, COLLEGE, DEPARTMENT, COURSE, SECTION, STUDENT, TAKES
- **Relationships**: Proper foreign key constraints to ensure referential integrity between tables
- **Primary Keys**: Defined for unique identification of records
- **Foreign Keys**: Defined for establishing relationships between tables
- **Python Script**: Manage student information with functionalities to add, delete, modify, query, and save student data.

## File Description
- `university_db.sql`: The SQL file containing the Data Definition Language (DDL) commands to create the database schema.
- `student_db.py`: The Python script for managing student information.

## How to Run
### SQL Database
1. Ensure you have a MySQL server running.
2. Open a MySQL command line or a database management tool (e.g., MySQL Workbench).
3. Execute the commands in the `university_db.sql` file:
   ```sh
   source /path/to/university_db.sql
   ```
4. The script will create the `University` database and all the necessary tables.

### Python Script
1. Ensure you have Python installed.
2. Run the `student_db.py` script:
   ```sh
   python student_db.py
   ```
3. Follow the prompts in the console to use the student management features.

## Schema Details

### PROFESSOR
```sql
CREATE TABLE PROFESSOR(
    Pid INT NOT NULL PRIMARY KEY,
    Rank VARCHAR(10),
    PName VARCHAR(50),
    POffice VARCHAR(50),
    PPhone VARCHAR(15),
    DCode CHAR(5)
);
```

### COLLEGE
```sql
CREATE TABLE COLLEGE(
    CName VARCHAR(50),
    COffice VARCHAR(50),
    Cphone VARCHAR(15),
    deanId INT,
    FOREIGN KEY(deanID) REFERENCES PROFESSOR(Pid)
);
```

### DEPARTMENT
```sql
CREATE TABLE DEPARTMENT(
    Dcode VARCHAR(5) NOT NULL PRIMARY KEY,
    DName VARCHAR(50) UNIQUE,
    DOffice VARCHAR(50),
    Dphone VARCHAR(15),
    CName VARCHAR(50),
    ChairID INT,
    CStartDate DATE,
    FOREIGN KEY (CName) REFERENCES COLLEGE(CName),
    FOREIGN KEY (ChairID) REFERENCES PROFESSOR(Pid)
);
```

### COURSE
```sql
CREATE TABLE COURSE(
    CCode CHAR(6) NOT NULL PRIMARY KEY,
    Credits INT,
    CoName VARCHAR(50) UNIQUE,
    Level INT,
    CDesc VARCHAR(100),
    DCode CHAR(5),
    FOREIGN KEY(DCode) REFERENCES DEPARTMENT(DCode)
);
```

### SECTION
```sql
CREATE TABLE SECTION(
    SecId INT NOT NULL PRIMARY KEY,
    SecNo INT,
    CRoomBldg VARCHAR(20),
    CRoomRoomNo VARCHAR(20),
    DaysInTime VARCHAR(50),
    CCode CHAR(6),
    PId INT,
    FOREIGN KEY(PId) REFERENCES PROFESSOR(Pid),
    FOREIGN KEY(CCode) REFERENCES COURSE(CCode)
);
```

### STUDENT
```sql
CREATE TABLE STUDENT(
    SId INT NOT NULL PRIMARY KEY,
    FName VARCHAR(50),
    MName VARCHAR(5),
    LName VARCHAR(50),
    DOB DATE,
    Addr VARCHAR(50),
    Phone VARCHAR(15),
    Major VARCHAR(10),
    DCode VARCHAR(5),
    FOREIGN KEY (DCode) REFERENCES DEPARTMENT(DCode)
);
```

### TAKES
```sql
CREATE TABLE TAKES(
    SId INT,
    SecId INT,
    Grade CHAR(1),
    FOREIGN KEY (SId) REFERENCES STUDENT(SId),
    FOREIGN KEY (SecId) REFERENCES SECTION(SecId)
);
```

### Additional Constraints
```sql
ALTER TABLE PROFESSOR 
ADD FOREIGN KEY(DCode)
REFERENCES DEPARTMENT(DCode);
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author
**Dominick Ferro**

## Date
November 9, 2021

---
