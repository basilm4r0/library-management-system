use library;

drop database IF EXISTS library;
CREATE DATABASE library;
use library;

CREATE TABLE Borrowers (
  Borrower_ID int NOT NULL AUTO_INCREMENT,
  Phone_number varchar(32) NOT NULL,
  First_Name varchar(32) NOT NULL,
  Last_Name varchar(32) NOT NULL,
  Date_of_birth varchar(32) NOT NULL,
  Address varchar(64) NOT NULL,
  PRIMARY KEY (Borrower_ID));

create table Users (
  User_ID int NOT NULL AUTO_INCREMENT,
  Borrower_ID int not null,
  Email varchar(50)not null,
  Password varchar(32)not null,
  primary key (User_ID),
  foreign key (Borrower_ID) REFERENCES Borrowers (Borrower_ID));

CREATE TABLE Creators (
  Creator_ID int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (Creator_ID));

CREATE Table Categories (
  Category_ID int NOT NULL AUTO_INCREMENT,
  Category_Name varchar(32),
  PRIMARY KEY (Category_ID));

CREATE TABLE Resources (
  Resource_ID int NOT NULL AUTO_INCREMENT,
  Title varchar(32),
  Description varchar(1000),
  Date_of_copyright varchar(32),
  Dewey_decimal varchar(10),
  PRIMARY KEY (Resource_ID));

CREATE TABLE Resources_Categories (
  Resource_ID int NOT NULL,
  Category_ID int NOT NULL,
  PRIMARY KEY (Resource_ID, Category_ID),
  FOREIGN KEY (Resource_ID) REFERENCES Resources (Resource_ID),
  FOREIGN KEY (Category_ID) REFERENCES Categories (Category_ID));

CREATE TABLE Resources_Creators (
  Resource_ID int NOT NULL,
  Creator_ID int NOT NULL,
  PRIMARY KEY (Resource_ID, Creator_ID),
  FOREIGN KEY (Resource_ID) REFERENCES Resources(Resource_ID),
  FOREIGN KEY (Creator_ID) REFERENCES Creators(Creator_ID));

CREATE TABLE Copies (
  Copy_ID int NOT NULL AUTO_INCREMENT,
  Resource_ID int NOT NULL,
  Publisher_ID int NOT NULL,
  Date_of_publication varchar(32),
  PRIMARY KEY (Copy_ID),
  FOREIGN KEY (Resource_ID) REFERENCES Resources (Resource_ID));

CREATE TABLE Books (
  Book_ID int NOT NULL AUTO_INCREMENT,
  Resource_ID int NOT NULL,
  Language varchar(15),
  PRIMARY KEY (Book_ID),
  FOREIGN KEY (Resource_ID) REFERENCES Resources (Resource_ID));

CREATE TABLE Authors (
  Author_ID int NOT NULL AUTO_INCREMENT,
  Creator_ID int not NULL,
  Name varchar(32) NOT NULL,
  Gender varchar(10),
  Date_of_birth varchar(32),
  PRIMARY KEY (Author_ID),
  FOREIGN KEY (Creator_ID) REFERENCES Creators (Creator_ID));

CREATE TABLE Collectives (
  Collective_ID int NOT NULL AUTO_INCREMENT,
  Creator_ID int not NULL,
  Name varchar(32),
  Date_of_formation varchar(32),
  PRIMARY KEY (Collective_ID),
  FOREIGN KEY (Creator_ID) REFERENCES Creators (Creator_ID));

CREATE TABLE Articles (
  Article_ID int NOT NULL AUTO_INCREMENT,
  Resource_ID int NOT NULL,
  Language varchar(15),
  Container_text varchar(32),
  PRIMARY KEY (Article_ID),
  FOREIGN KEY (Resource_ID) REFERENCES Resources (Resource_ID));

CREATE TABLE Essays (
  Essay_ID int NOT NULL AUTO_INCREMENT,
  Resource_ID int NOT NULL,
  Language varchar(15),
  Container_text varchar(32),
  PRIMARY KEY (Essay_ID),
  FOREIGN KEY (Resource_ID) REFERENCES Resources (Resource_ID));

CREATE TABLE Periodicals (
  Periodical_ID int NOT NULL AUTO_INCREMENT,
  Name varchar(32),
  Language varchar(15),
  Start_date varchar(32),
  End_date varchar(32),
  PRIMARY KEY (Periodical_ID)
);

CREATE TABLE Issues (
  Issue_ID int NOT NULL AUTO_INCREMENT,
  Resource_ID int NOT NULL,
  Date_of_Issue varchar(32),
  Periodical_ID int default NULL,
  PRIMARY KEY (Issue_ID),
  FOREIGN KEY (Periodical_ID) REFERENCES Periodicals (Periodical_ID),
  FOREIGN KEY (Resource_ID) REFERENCES Resources (Resource_ID));

CREATE TABLE Borrowing (
  Borrower_ID int NOT NULL,
  Copy_ID int NOT NULL,
  Borrow_date date NOT NULL,
  Must_return_date date NOT NULL,
  Is_returned boolean NOT NULL,
  FOREIGN KEY (Borrower_ID) REFERENCES Borrowers (Borrower_ID),
  PRIMARY KEY (Borrower_ID,Copy_ID,Borrow_date));

CREATE TABLE Borrowed (
  Borrower_ID int NOT NULL,
  Resource_ID int NOT NULL,
  Borrow_date date NOT NULL,
  Return_date date NOT NULL,
  FOREIGN KEY (Borrower_ID) REFERENCES Borrowers (Borrower_ID),
  FOREIGN KEY (Resource_ID) REFERENCES Resources (Resource_ID),
  PRIMARY KEY (Borrower_ID,Resource_ID,Borrow_date));

CREATE TABLE Publishers (
  Publisher_ID int NOT NULL AUTO_INCREMENT,
  Name varchar(32),
  PRIMARY KEY (Publisher_ID));

CREATE TABLE Reserves (
  Reservation_ID int NOT NULL AUTO_INCREMENT,
  Copy_ID int NOT NULL,
  Reserve_date date NOT NULL,
  end_date date NOT NULL,
  PRIMARY KEY (Reservation_ID),
  FOREIGN KEY (Copy_ID) REFERENCES Copies (Copy_ID));

CREATE TABLE Waiting_List (
  Borrower_ID int NOT NULL,
  Copy_ID int NOT NULL,
  PRIMARY KEY (Borrower_ID,Copy_ID),
  FOREIGN KEY (Borrower_ID) REFERENCES Borrowers (Borrower_ID),
  FOREIGN KEY (Copy_ID) REFERENCES Copies (Copy_ID));

INSERT INTO Creators VALUES (1);
INSERT INTO Authors (Creator_ID, Name, Gender, Date_of_birth)
VALUES (1, 'Toni Morrison', 'Female', '1931-02-18');
INSERT INTO Resources (Resource_ID, Title, Description, Date_of_copyright, Dewey_decimal)
VALUES (1, 'Beloved', 'A novel about a slave', '1987-09-15', '813.54');
INSERT INTO Resources_Creators (Resource_ID, Creator_ID) VALUES (1,1);
INSERT INTO Categories (Category_ID, Category_Name)
VALUES (1, 'Magical Realism');
INSERT INTO Resources_Categories (Category_ID, Resource_ID)
VALUES (1, 1);
INSERT INTO Books (Book_ID, Resource_ID, Language)
Values (1, 1, 'English');
INSERT INTO Copies (Copy_ID, Resource_ID, Publisher_ID, Date_of_publication)
VALUES (1, 1, 1, '1987-09-15');
INSERT INTO Publishers (Publisher_ID, Name) VALUES (1, 'Alfred A. Knopf');
INSERT INTO Borrowers (Borrower_ID, First_Name, Last_Name, Date_of_Birth, Phone_Number, Address)
VALUES (1, 'John', 'Doe', '1990-1-1', '123-456-7890', 'Robert Robertson, 1234 NW Bobcat Lane, St. Robert, MO 65584-5678');
INSERT INTO Users (User_ID, Borrower_ID, Email, Password)
VALUES (1, 1,'johndoe@example.com', 'password');
INSERT INTO Borrowing (Borrower_ID, Copy_ID, Borrow_date, Must_return_date, Is_returned)
VALUES (1, 1, '2018-10-01', '2018-10-15', 0);
