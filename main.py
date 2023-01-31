import sys
from os import path

# from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUiType
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery

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

    def Handle_Buttons(self):
        self.browsePageBtn.clicked.connect(self.Show_Browse)
        self.searchPageBtn.clicked.connect(self.Show_Search)
        self.addPageBtn.clicked.connect(self.Show_Add)
        self.readResourcesBtn.clicked.connect(self.Read_Resources)
        self.readBooksBtn.clicked.connect(self.Read_Books)
        self.readEssaysBtn.clicked.connect(self.Read_Essays)
        self.readArticlesBtn.clicked.connect(self.Read_Articles)
        self.readPeriodicalsBtn.clicked.connect(self.Read_Periodicals)
        self.readIssuesBtn.clicked.connect(self.Read_Issues)
        self.addResourceBtn.clicked.connect(self.Add_Resource)

    def Show_Browse(self):
        self.stackedWidget.setCurrentWidget(self.browse)

    def Show_Search(self):
        self.stackedWidget.setCurrentWidget(self.search)

    def Show_Add(self):
        self.stackedWidget.setCurrentWidget(self.add)

    # Method to read from database and display in QTableWidget
    def Read_Resources(self):
        model = QSqlQueryModel()
        query = QSqlQuery()
        query.exec_(
            "SELECT Resources.Resource_ID, "
            "Resources.Title, "
            "Creators1.Name "
            "FROM Resources "
            "INNER JOIN ( "
            "SELECT Name, Creator_ID FROM Authors "
            "UNION ALL "
            "SELECT Name, Creator_ID FROM Collectives "
            ") "
            "AS Creators1 "
            "ON Resources.Creator_ID = Creators1.Creator_ID"
        )

        model.setQuery(query)
        print(query.lastError().text())
        self.tableView.setSortingEnabled(True)
        self.tableView.setModel(
            model
        )  # Change to manual data reading in the future

    def Read_Books(self):
        model = QSqlQueryModel()
        query = QSqlQuery()
        query.exec_(
            "SELECT Resources.Resource_ID, "
            "Resources.Title, "
            "Creators1.Name, "
            "Books.Date_of_publication, "
            "Books.Language, "
            "Books.Publisher "
            "FROM Resources "
            "INNER JOIN Books "
            "ON Resources.Resource_ID = Books.Resource_ID "
            "INNER JOIN ( "
            "SELECT Name, Creator_ID FROM Authors "
            "UNION ALL "
            "SELECT Name, Creator_ID FROM Collectives "
            ") "
            "AS Creators1 "
            "ON Resources.Creator_ID = Creators1.Creator_ID"
        )
        model.setQuery(query)
        print(query.lastError().text())
        self.tableView.setSortingEnabled(True)
        self.tableView_2.setModel(model)

    def Read_Essays(self):
        model = QSqlQueryModel()
        query = QSqlQuery()
        query.exec_(
            "SELECT Resources.Resource_ID, "
            "Resources.Title, "
            "Creators1.Name, "
            "Essays.Date_of_publication, "
            "Essays.Language, "
            "Essays.Publisher "
            "FROM Resources "
            "INNER JOIN Essays "
            "ON Resources.Resource_ID = Essays.Resource_ID "
            "INNER JOIN ( "
            "SELECT Name, Creator_ID FROM Authors "
            "UNION ALL "
            "SELECT Name, Creator_ID FROM Collectives "
            ") "
            "AS Creators1 "
            "ON Resources.Creator_ID = Creators1.Creator_ID"
        )
        model.setQuery(query)
        print(query.lastError().text())
        self.tableView.setSortingEnabled(True)
        self.tableView_3.setModel(model)

    def Read_Articles(self):
        model = QSqlQueryModel()
        query = QSqlQuery()
        query.exec_(
            "SELECT Resources.Resource_ID, "
            "Resources.Title, "
            "Creators1.Name, "
            "Articles.Date_of_publication, "
            "Articles.Language, "
            "Articles.Publisher "
            "FROM Resources "
            "INNER JOIN Articles "
            "ON Resources.Resource_ID = Articles.Resource_ID "
            "INNER JOIN ( "
            "SELECT Name, Creator_ID FROM Authors "
            "UNION ALL "
            "SELECT Name, Creator_ID FROM Collectives "
            ") "
            "AS Creators1 "
            "ON Resources.Creator_ID = Creators1.Creator_ID"
        )
        model.setQuery(query)
        print(query.lastError().text())
        self.tableView.setSortingEnabled(True)
        self.tableView_4.setModel(model)

    def Read_Periodicals(self):
        model = QSqlQueryModel()
        query = QSqlQuery()
        query.exec_(
            "SELECT Periodical_ID, "
            "Name, "
            "Publisher, "
            "Start_date, "
            "End_date, "
            "Language "
            "FROM Periodicals"
        )
        model.setQuery(query)
        print(query.lastError().text())
        self.tableView.setSortingEnabled(True)
        self.tableView_5.setModel(model)

    def Read_Issues(self):
        model = QSqlQueryModel()
        query = QSqlQuery()
        query.exec_(
            "SELECT Resources.Resource_ID, "
            "Resources.Title, "
            "Issues.Date_of_issue, "
            "Periodicals.Name, "
            "Periodicals.Language, "
            "Periodicals.Publisher "
            "FROM Resources "
            "INNER JOIN Issues "
            "ON Resources.Resource_ID = Issues.Resource_ID "
            "INNER JOIN Periodicals "
            "ON Issues.Periodical_ID = Periodicals.Periodical_ID"
        )
        model.setQuery(query)
        print(query.lastError().text())
        self.tableView.setSortingEnabled(True)
        self.tableView_6.setModel(model)

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
