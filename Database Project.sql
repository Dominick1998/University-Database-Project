/* 
Univerity Database Project 
Database Concepts
Dominick Ferro 
DDL Commands 11/9/2021
*/

create database University;
use University;

CREATE TABLE PROFESSOR(
	/*Professor ID, Primary Key cannot contain NULL*/
    Pid INT NOT NULL PRIMARY KEY,

    Rank VARCHAR(10),
	/*Professor Name*/
    PName VARCHAR(50),
	/*Professor Office*/
    POffice VARCHAR(50),
    /*Professor Phone*/
	PPhone VARCHAR(15),
	/*Department Code*/
    DCode CHAR(5)

);

CREATE TABLE COLLEGE(
	/*College Name*/
    CName VARCHAR(50),
	/*College Office*/
    COffice VARCHAR(50),
	/*College Phone*/
    Cphone VARCHAR(15),

    deanId INT,

    FOREIGN KEY(deanID) REFERENCES PROFESSOR(id)

);

CREATE TABLE DEPARTMENT(
	/*Department Code*/
    Dcode VARCHAR(5) NOT NULL PRIMARY KEY,
	/*Department Name*/
    DName VARCHAR(50) UNIQUE,
	/*Department Office*/
    DOffice VARCHAR(50),
	/*Department Phone*/
    Dphone VARCHAR(15),
	/*Chair Name*/
    CName VARCHAR(50),
	/*Department Chair ID*/
    ChairID INT,
	/*Chair Start Date*/
    CStartDate DATE,

    FOREIGN KEY (CName) REFERENCES COLLEGE(CName),

    FOREIGN KEY (ChairID) REFERENCES PROFESSOR(id)

);

CREATE TABLE COURSE(
	/*Course Code*/
    CCode CHAR(6) NOT NULL PRIMARY KEY,

    Credits INT,
	/*Course Name*/
    CoName VARCHAR(50) UNIQUE,

    Level INT,
	/*Course Description*/
    CDesc VARCHAR(100),
	/*Department Code*/
    DCode CHAR(5),

    FOREIGN KEY(DCode) REFERENCES DEPARTMENT(DCode)
);

CREATE TABLE SECTION(

    SecId INT NOT NULL PRIMARY KEY,

    SecNo INT,
	/*Course Building*/
    CRoomBldg VARCHAR(20),
	/*Course Room Number*/
    CRoomRoomNo VARCHAR(20),

    DaysInTime VARCHAR(50),
	/*Course Code*/
	CCode CHAR(6),
	/*Professor ID*/
    PId INT,

    FOREIGN KEY(PID) REFERENCES PROFESSOR(id),

    FOREIGN KEY(CCode) REFERENCES COURSE(CCode)

);

CREATE TABLE STUDENT(
	/*Student ID*/
    SId INT NOT NULL PRIMARY KEY,
	/*First, Middle, and Last Names*/
    FName VARCHAR(50),
    MName VARCHAR(5),
    LName VARCHAR(50),
	/*Date of Birth*/
    DOB DATE,
	/*Address*/
    Addr VARCHAR(50),

    Phone VARCHAR(15),

    Major VARCHAR(10),
	/*Department Code*/
    DCode VARCHAR(5),

    FOREIGN KEY (DCode) REFERENCES DEPARTMENT(DCode)

);

CREATE TABLE TAKES(
	/*Student ID*/
    SId INT,
	/*Section ID*/
    SecId INT,

    Grade CHAR(1),

    FOREIGN KEY (SId) REFERENCES STUDENT(SId),

    FOREIGN KEY (SecId) REFERENCES SECTION(SecId)

);

ALTER TABLE PROFESSOR 
ADD FOREIGN KEY(DCode)
REFERENCES DEPARTMENT(DCode);