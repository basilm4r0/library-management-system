import sys
from os import path
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
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

    def Handle_Buttons(self):
        self.pushButton.clicked.connect(self.Add_Resource)
        self.pushButton_2.clicked.connect(self.Read_Resources)
        self.pushButton_3.clicked.connect(self.Read_Books)

    # Method to read from database and display in QTableWidget
    def Read_Resources(self):
        model = QSqlQueryModel()
        query = QSqlQuery()
        query.exec_("SELECT * FROM Resources")
        model.setQuery(query)
        self.tableView_2.setModel(
            model
        )  # Change to manual data reading in the future

    def Read_Books(self):
        model = QSqlQueryModel()
        query = QSqlQuery()
        query.exec_("SELECT * FROM Books")
        model.setQuery(query)
        self.tableView.setModel(model)

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
            db.open()
            QMessageBox.information(
                self, "Connection", "Connection Successful"
            )
            return True
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
