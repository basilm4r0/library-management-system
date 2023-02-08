import sys
from os import path

# from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUiType
from PyQt5.QtSql import (
    QSqlDatabase,
    QSqlQueryModel,
    QSqlQuery,
    QSqlRelationalTableModel,
)

FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "design.ui"))


class MainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Buttons()
        self.Connect_To_DB()
        self.Read_Resources()
        self.Read_Books()
        self.Read_Essays()
        self.Read_Articles()
        self.Read_Periodicals()
        self.Read_Issues()
        self.Read_Creators(0)
        self.Edit_Resources()
        self.Edit_Books()
        self.Edit_Essays()
        self.Edit_Articles()
        self.Edit_Periodicals()
        self.Edit_Issues()
        self.Edit_Creators(0)
        self.stackedWidget.setCurrentWidget(self.browse)

    def Handle_Buttons(self):
        # Main Side Bar
        self.browsePageBtn.clicked.connect(self.Show_Browse)
        self.searchPageBtn.clicked.connect(self.Show_Search)
        self.addPageBtn.clicked.connect(self.Show_Add)
        self.editPageBtn.clicked.connect(self.Show_Edit)
        # Browse Page Buttons
        self.readResourcesBtn.clicked.connect(self.Read_Resources)
        self.readBooksBtn.clicked.connect(self.Read_Books)
        self.readEssaysBtn.clicked.connect(self.Read_Essays)
        self.readArticlesBtn.clicked.connect(self.Read_Articles)
        self.readPeriodicalsBtn.clicked.connect(self.Read_Periodicals)
        self.readIssuesBtn.clicked.connect(self.Read_Issues)
        self.readCreatorsBtn.clicked.connect(lambda: self.Read_Creators(0))
        self.readAuthorsBtn.clicked.connect(lambda: self.Read_Creators(1))
        self.readCollectivesBtn.clicked.connect(lambda: self.Read_Creators(2))
        # Edit Page Buttons
        self.readResourcesBtn_2.clicked.connect(self.Edit_Resources)
        self.readBooksBtn_2.clicked.connect(self.Edit_Books)
        self.readEssaysBtn_2.clicked.connect(self.Edit_Essays)
        self.readArticlesBtn_2.clicked.connect(self.Edit_Articles)
        self.readPeriodicalsBtn_2.clicked.connect(self.Edit_Periodicals)
        self.readIssuesBtn_2.clicked.connect(self.Edit_Issues)
        self.readCreatorsBtn_2.clicked.connect(lambda: self.Edit_Creators(0))
        self.readAuthorsBtn_2.clicked.connect(lambda: self.Edit_Creators(1))
        self.readCollectivesBtn_2.clicked.connect(
            lambda: self.Edit_Creators(2)
        )
        # Add Page Buttons
        self.addResourceBtn.clicked.connect(self.Add_Resource)

    def Show_Browse(self):
        self.stackedWidget.setCurrentWidget(self.browse)

    def Show_Search(self):
        self.stackedWidget.setCurrentWidget(self.search)

    def Show_Add(self):
        self.stackedWidget.setCurrentWidget(self.add)

    def Show_Edit(self):
        self.stackedWidget.setCurrentWidget(self.edit)

    # Method to read from database and display in QTableWidget
    def Read_Resources(self):
        model = QSqlQueryModel()
        query = QSqlQuery()
        query.exec_(
            "SELECT Resources.Resource_ID AS ID, "
            "Resources.Title, "
            "GROUP_CONCAT(Creators1.Name) AS `Authors(s)`, "
            "Resources.Date_of_copyright AS `Publish Date`, "
            "Resources.Dewey_decimal AS `Dewey Decimal` "
            "FROM Resources "
            "INNER JOIN Resources_Creators "
            "ON Resources.Resource_ID = Resources_Creators.Resource_ID "
            "INNER JOIN ( "
            "SELECT Name, Creator_ID FROM Authors "
            "UNION ALL "
            "SELECT Name, Creator_ID FROM Collectives "
            ") "
            "AS Creators1 "
            "ON Resources_Creators.Creator_ID = Creators1.Creator_ID "
            "GROUP BY Resources.Resource_ID, Resources.Title"
        )

        model.setQuery(query)
        print(query.lastError().text())
        self.tableView.setSortingEnabled(True)
        self.tableView.setModel(model)

    def Read_Books(self):
        model = QSqlQueryModel()
        query = QSqlQuery()
        query.exec_(
            "SELECT Resources.Resource_ID AS ID, "
            "Resources.Title, "
            "GROUP_CONCAT(Creators1.Name) AS `Authors(s)`, "
            "Resources.Date_of_copyright AS `Publish Date`, "
            "Books.Language, "
            "Resources.Dewey_decimal AS `Dewey Decimal` "
            "FROM Resources "
            "INNER JOIN Books "
            "ON Resources.Resource_ID = Books.Resource_ID "
            "INNER JOIN Resources_Creators "
            "ON Resources.Resource_ID = Resources_Creators.Resource_ID "
            "INNER JOIN ( "
            "SELECT Name, Creator_ID FROM Authors "
            "UNION ALL "
            "SELECT Name, Creator_ID FROM Collectives "
            ") "
            "AS Creators1 "
            "ON Resources_Creators.Creator_ID = Creators1.Creator_ID "
            "GROUP BY Resources.Resource_ID"
        )
        model.setQuery(query)
        print(query.lastError().text())
        self.tableView_2.setSortingEnabled(True)
        self.tableView_2.setModel(model)

    def Read_Essays(self):
        model = QSqlQueryModel()
        query = QSqlQuery()
        query.exec_(
            "SELECT Resources.Resource_ID AS ID, "
            "Resources.Title, "
            "GROUP_CONCAT(Creators1.Name) AS `Author(s)`, "
            "Resources.Date_of_copyright AS `Publish Date`, "
            "Essays.Language, "
            "Essays.Container_text AS Container "
            "FROM Resources "
            "INNER JOIN Essays "
            "ON Resources.Resource_ID = Essays.Resource_ID "
            "INNER JOIN Resources_Creators "
            "ON Resources.Resource_ID = Resources_Creators.Resource_ID "
            "INNER JOIN ( "
            "SELECT Name, Creator_ID FROM Authors "
            "UNION ALL "
            "SELECT Name, Creator_ID FROM Collectives "
            ") "
            "AS Creators1 "
            "ON Resources_Creators.Creator_ID = Creators1.Creator_ID "
            "GROUP BY Resources.Resource_ID"
        )
        model.setQuery(query)
        print(query.lastError().text())
        self.tableView_3.setSortingEnabled(True)
        self.tableView_3.setModel(model)

    def Read_Articles(self):
        model = QSqlQueryModel()
        query = QSqlQuery()
        query.exec_(
            "SELECT Resources.Resource_ID AS ID, "
            "Resources.Title, "
            "GROUP_CONCAT(Creators1.Name) AS `Author(s)`, "
            "Resources.Date_of_copyright `Publish Date`, "
            "Articles.Language, "
            "Articles.Container_text AS Container "
            "FROM Resources "
            "INNER JOIN Articles "
            "ON Resources.Resource_ID = Articles.Resource_ID "
            "INNER JOIN Resources_Creators "
            "ON Resources.Resource_ID = Resources_Creators.Resource_ID "
            "INNER JOIN ( "
            "SELECT Name, Creator_ID FROM Authors "
            "UNION ALL "
            "SELECT Name, Creator_ID FROM Collectives "
            ") "
            "AS Creators1 "
            "ON Resources_Creators.Creator_ID = Creators1.Creator_ID "
            "GROUP BY Resources.Resource_ID"
        )
        model.setQuery(query)
        print(query.lastError().text())
        self.tableView_4.setSortingEnabled(True)
        self.tableView_4.setModel(model)

    def Read_Periodicals(self):
        model = QSqlQueryModel()
        query = QSqlQuery()
        query.exec_(
            "SELECT Periodical_ID AS `Periodical ID`, "
            "Name, "
            "Start_date AS `Start Date`, "
            "End_date AS `End Date`, "
            "Language "
            "FROM Periodicals"
        )
        model.setQuery(query)
        print(query.lastError().text())
        self.tableView_5.setSortingEnabled(True)
        self.tableView_5.setModel(model)

    def Read_Issues(self):
        model = QSqlQueryModel()
        query = QSqlQuery()
        query.exec_(
            "SELECT Resources.Resource_ID AS ID, "
            "Resources.Title, "
            "Issues.Date_of_issue AS `Date of Issue`, "
            "Periodicals.Name AS `Periodical`, "
            "Periodicals.Language "
            "FROM Resources "
            "INNER JOIN Issues "
            "ON Resources.Resource_ID = Issues.Resource_ID "
            "INNER JOIN Periodicals "
            "ON Issues.Periodical_ID = Periodicals.Periodical_ID"
        )
        model.setQuery(query)
        print(query.lastError().text())
        self.tableView_6.setSortingEnabled(True)
        self.tableView_6.setModel(model)

    def Read_Creators(self, mode):
        model = QSqlQueryModel()
        query = QSqlQuery()
        if mode == 0:
            query.exec_(
                "SELECT Name, Creator_ID AS `Creator ID` FROM Authors "
                "UNION ALL "
                "SELECT Name, Creator_ID AS `Creator ID` FROM Collectives "
            )
        elif mode == 1:
            query.exec_(
                "SELECT Creator_ID AS `Creator ID`, "
                "Name, Gender, Date_of_birth AS `Date of Birth` FROM Authors "
            )
        elif mode == 2:
            query.exec_(
                "SELECT Creator_ID AS `Creator ID`, Name, "
                "Date_of_formation AS `Date of Formation` FROM Collectives "
            )
        else:
            return 1
        model.setQuery(query)
        print(query.lastError().text())
        self.tableView_7.setSortingEnabled(True)
        self.tableView_7.setModel(model)
        return 0

    def Edit_Resources(self):
        model = QSqlRelationalTableModel()
        model.setTable("Resources")
        self.tableView_8.setSortingEnabled(True)
        self.tableView_8.setModel(model)
        print(self.tableView_8.model().lastError().text())

    def Edit_Books(self):
        model = QSqlRelationalTableModel()
        model.setTable("Books")
        self.tableView_9.setSortingEnabled(True)
        self.tableView_9.setModel(model)

    def Edit_Essays(self):
        model = QSqlRelationalTableModel()
        model.setTable("Essays")
        self.tableView_10.setSortingEnabled(True)
        self.tableView_10.setModel(model)

    def Edit_Articles(self):
        model = QSqlRelationalTableModel()
        model.setTable("Articles")
        self.tableView_11.setSortingEnabled(True)
        self.tableView_11.setModel(model)

    def Edit_Periodicals(self):
        model = QSqlRelationalTableModel()
        model.setTable("Periodicals")
        self.tableView_12.setSortingEnabled(True)
        self.tableView_12.setModel(model)

    def Edit_Issues(self):
        model = QSqlRelationalTableModel()
        model.setTable("Issues")
        self.tableView_13.setSortingEnabled(True)
        self.tableView_13.setModel(model)

    def Edit_Creators(self, mode):
        model = QSqlRelationalTableModel()
        if mode == 0:
            model.setTable("Creators")
        elif mode == 1:
            model.setTable("Authors")
        elif mode == 2:
            model.setTable("Collectives")
        else:
            return 1
        self.tableView_14.setSortingEnabled(True)
        self.tableView_14.setModel(model)
        return 0

    def Add_Resource(self):
        try:
            self.Insert_To_Table(
                "Resources",
                "Title, Creator_ID, Description",
                [
                    self.lineEdit.text(),
                    self.lineEdit_2.text(),
                    # self.lineEdit_3.text(),
                    self.plainTextEdit_4.toPlainText(),
                ],
            )
            self.Read_Resources()
        except Exception as e:
            QMessageBox.information(
                self, "Add Resource", f"Error adding resource: {e}"
            )

    def Connect_To_DB(self):
        try:
            db = QSqlDatabase.addDatabase("QMYSQL")
            db.setHostName("localhost")
            db.setDatabaseName("library")
            db.setUserName("user")
            db.setPassword("password")
            if db.open():
                QMessageBox.information(
                    self, "Connection", "Connection Successful"
                )
                return True
            else:
                QMessageBox.information(
                    self, "Connection", "Connection Failed"
                )
                sys.exit(1)
                return False
        except Exception as e:
            QMessageBox.information(
                self, "Connection", f"Connection Failed: {e}"
            )
            return False

    def Insert_To_Table(self, Table, input, record):
        query = QSqlQuery()
        try:
            query.exec_(
                f"""INSERT INTO {Table} ({input})
                    VALUES ({str(record)[1:len(str(record)) - 1]}) """
            )
            print(f"Record inserted successfully into {Table} table")

        except Exception as e:
            QMessageBox.information(
                self,
                "Insert Record",
                f"Error inserting record into {Table} table: {e}",
            )


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
