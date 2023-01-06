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

  CREATE TABLE Creators (
  CID int NOT NULL,
  PRIMARY KEY (CID));



   CREATE TABLE Resources (
  Resource_ID int NOT NULL AUTO_INCREMENT,
  Description varchar(1000) ,
  Title varchar(32) ,
  Creator_ID int NOT NULL,
  PRIMARY KEY (Resource_ID),
  FOREIGN KEY (Creator_ID) REFERENCES Creators (CID)
);



CREATE TABLE Books (
  BID int NOT NULL AUTO_INCREMENT,
  Resource_ID int NOT NULL,
  Publisher varchar(32) ,
  Date_of_publishing date ,
  Language varchar(15),
  PRIMARY KEY (BID),
FOREIGN KEY (Resource_ID) REFERENCES Resources (Resource_ID));


CREATE TABLE Authors (
  Author_ID int NOT NULL AUTO_INCREMENT,
  CID int not NULL,
  Name varchar(32) ,
  Gender varchar(10) ,
  Date_of_birth date ,
  PRIMARY KEY (Author_ID),
FOREIGN KEY (CID) REFERENCES Creators (CID));


CREATE TABLE Collectives (
  Collective_ID int NOT NULL AUTO_INCREMENT,
  CID int not NULL,
  Name varchar(32) ,
  Date_of_birth date  ,
  PRIMARY KEY (Collective_ID),
FOREIGN KEY (CID) REFERENCES Creators (CID));

CREATE TABLE Articles (
  AID int NOT NULL AUTO_INCREMENT,
  Resource_ID int NOT NULL,
  Publisher varchar(32) ,
  Language varchar(15) ,
  Container_text varchar(32) ,
  Date_of_publishing date ,

  PRIMARY KEY (AID),
FOREIGN KEY (Resource_ID) REFERENCES Resources (Resource_ID));

CREATE TABLE Essays (
  EID int NOT NULL AUTO_INCREMENT,
  Resource_ID int NOT NULL,
  Publisher varchar(32) ,
  Language varchar(15) ,
  Container_text varchar(32) ,
  Date_of_publishing date ,

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

insert into Creators values (1);
