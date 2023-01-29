use library;

drop database IF EXISTS library;
CREATE DATABASE library;
use library;

CREATE TABLE Borrowers (
  Borrower_ID int NOT NULL AUTO_INCREMENT,
  Phone_number varchar(15) ,
  Name varchar(32) ,
  Date_of_birth date ,
  Address varchar(32) ,
  PRIMARY KEY (Borrower_ID));

CREATE TABLE Creators ( # It turns out this is needed to enforce Creator_ID uniqueness
  Creator_ID int NOT NULL,
  PRIMARY KEY (Creator_ID));

  CREATE TABLE Resources (
  Resource_ID int NOT NULL AUTO_INCREMENT,
  Description varchar(1000) ,
  Title varchar(32) ,
  Creator_ID int NOT NULL,
  PRIMARY KEY (Resource_ID),
  FOREIGN KEY (Creator_ID) REFERENCES Creators (Creator_ID));

CREATE TABLE Books (
  Book_ID int NOT NULL AUTO_INCREMENT,
  Resource_ID int NOT NULL,
  Publisher varchar(32) ,
  Year_of_publication year,
  Language varchar(15),
  PRIMARY KEY (Book_ID),
FOREIGN KEY (Resource_ID) REFERENCES Resources (Resource_ID));

CREATE TABLE Authors (
  Author_ID int NOT NULL AUTO_INCREMENT,
  Creator_ID int not NULL,
  Name varchar(32) ,
  Gender varchar(10) ,
  Date_of_birth date ,
  PRIMARY KEY (Author_ID),
FOREIGN KEY (Creator_ID) REFERENCES Creators (Creator_ID));


CREATE TABLE Collectives (
  Collective_ID int NOT NULL AUTO_INCREMENT,
  Creator_ID int not NULL,
  Name varchar(32) ,
  Date_of_formation date  ,
  PRIMARY KEY (Collective_ID),
FOREIGN KEY (Creator_ID) REFERENCES Creators (Creator_ID));

CREATE TABLE Articles (
  AID int NOT NULL AUTO_INCREMENT,
  Resource_ID int NOT NULL,
  Publisher varchar(32) ,
  Language varchar(15) ,
  Container_text varchar(32) ,
  Date_of_publication date ,

  PRIMARY KEY (AID),
FOREIGN KEY (Resource_ID) REFERENCES Resources (Resource_ID));

CREATE TABLE Essays (
  EID int NOT NULL AUTO_INCREMENT,
  Resource_ID int NOT NULL,
  Publisher varchar(32) ,
  Language varchar(15) ,
  Container_text varchar(32) ,
  Date_of_publication date ,

  PRIMARY KEY (EID),
FOREIGN KEY (Resource_ID) REFERENCES Resources (Resource_ID));



CREATE TABLE Periodicals (
  PID int NOT NULL AUTO_INCREMENT,
  Name varchar(32) ,
  Publisher varchar(32) ,
  Language varchar(15) ,
  Date_of_running date ,
  PRIMARY KEY (PID)
);


CREATE TABLE Issue (
  IID int NOT NULL AUTO_INCREMENT,
  Resource_ID int NOT NULL,
  Title varchar(32) ,
  Date_of_Issue date ,
  PID int default NULL,
  PRIMARY KEY (IID),
  FOREIGN KEY (PID) REFERENCES Periodicals (PID),
FOREIGN KEY (Resource_ID) REFERENCES Resources (Resource_ID));

  CREATE TABLE Borrowing (
  Borrower_ID int NOT NULL,
  Resource_ID int NOT NULL,
  Borrow_date date NOT NULL,
  Must_return_date date NOT NULL,
  FOREIGN KEY (Borrower_ID) REFERENCES Borrowers (Borrower_ID),
  FOREIGN KEY (Resource_ID) REFERENCES Resources (Resource_ID),
  PRIMARY KEY (Borrower_ID,Resource_ID,Borrow_date));

  CREATE TABLE Borrowed (
  Borrower_ID int NOT NULL,
  Resource_ID int NOT NULL,
  Borrow_date date NOT NULL,
  Return_date date NOT NULL,
  FOREIGN KEY (Borrower_ID) REFERENCES Borrowers (Borrower_ID),
  FOREIGN KEY (Resource_ID) REFERENCES Resources (Resource_ID),
  PRIMARY KEY (Borrower_ID,Resource_ID,Borrow_date));

INSERT INTO Creators VALUES (1);
INSERT INTO Authors (Creator_ID, Name, Gender, Date_of_birth)
VALUES (1, 'Toni Morrison', 'Female', '1931-02-18');
INSERT INTO Resources (Resource_ID, Description, Title, Creator_ID)
VALUES (1, 'A novel about a slave', 'Beloved', 1);
INSERT INTO Books (Book_ID, Resource_ID, Publisher, Year_of_publication, Language)
Values (1, 1, 'Alfred A. Knopf', '1987', 'English');
