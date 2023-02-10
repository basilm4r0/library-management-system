import sys
from os import path

from PyQt5.QtCore import QSortFilterProxyModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUiType
from PyQt5.QtSql import (
    QSqlDatabase,
    QSqlQueryModel,
    QSqlQuery,
    QSqlRelationalTableModel,
    QSqlRelationalDelegate,
)

FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "design.ui"))


class MainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Buttons()
        self.Handle_Filters()
        self.Connect_To_DB()
        self.Read_Resources()
        self.Read_Books()
        self.Read_Essays()
        self.Read_Articles()
        self.Read_Periodicals()
        self.Read_Issues()
        self.Read_Creators(0)
        self.tabWidget.setCurrentIndex(0)
        self.Edit_Resources()
        self.Edit_Books()
        self.Edit_Essays()
        self.Edit_Articles()
        self.Edit_Periodicals()
        self.Edit_Issues()
        self.Edit_Creators(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.Edit_Borrowing()
        self.Edit_Borrowed()
        self.Edit_Reservations()
        self.Edit_Waitlist()
        self.Edit_Borrowers()
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        self.stackedWidget.setCurrentWidget(self.browse)
        self.Filter(self.tableView, 1, "Beloved")

    def Handle_Buttons(self):
        # Main Side Bar
        self.browsePageBtn.clicked.connect(self.Show_Browse)
        self.addPageBtn.clicked.connect(self.Show_Add)
        self.editPageBtn.clicked.connect(self.Show_Edit)
        self.lendingPageBtn.clicked.connect(self.Show_Lending)
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

    def Handle_Filters(self):
        self.lineEdit_4.textChanged.connect(
            lambda: self.Filter(
                self.tableView,
                self.comboBox.currentIndex(),
                self.lineEdit_4.text(),
            )
        )
        self.lineEdit_5.textChanged.connect(
            lambda: self.Filter(
                self.tableView_2,
                self.comboBox_2.currentIndex(),
                self.lineEdit_5.text(),
            )
        )
        self.lineEdit_6.textChanged.connect(
            lambda: self.Filter(
                self.tableView_3,
                self.comboBox_3.currentIndex(),
                self.lineEdit_6.text(),
            )
        )
        self.lineEdit_7.textChanged.connect(
            lambda: self.Filter(
                self.tableView_4,
                self.comboBox_4.currentIndex(),
                self.lineEdit_7.text(),
            )
        )
        self.lineEdit_8.textChanged.connect(
            lambda: self.Filter(
                self.tableView_5,
                self.comboBox_5.currentIndex(),
                self.lineEdit_8.text(),
            )
        )
        self.lineEdit_9.textChanged.connect(
            lambda: self.Filter(
                self.tableView_6,
                self.comboBox_6.currentIndex(),
                self.lineEdit_9.text(),
            )
        )
        self.lineEdit_10.textChanged.connect(
            lambda: self.Filter(
                self.tableView_7,
                self.comboBox_7.currentIndex(),
                self.lineEdit_10.text(),
            )
        )
        self.lineEdit_11.textChanged.connect(
            lambda: self.Filter(
                self.tableView_15,
                self.comboBox_8.currentIndex(),
                self.lineEdit_11.text(),
            )
        )
        self.lineEdit_12.textChanged.connect(
            lambda: self.Filter(
                self.tableView_16,
                self.comboBox_9.currentIndex(),
                self.lineEdit_10.text(),
            )
        )
        self.lineEdit_13.textChanged.connect(
            lambda: self.Filter(
                self.tableView_17,
                self.comboBox_10.currentIndex(),
                self.lineEdit_13.text(),
            )
        )
        self.lineEdit_16.textChanged.connect(
            lambda: self.Filter(
                self.tableView_8,
                self.comboBox_11.currentIndex(),
                self.lineEdit_16.text(),
            )
        )
        self.lineEdit_17.textChanged.connect(
            lambda: self.Filter(
                self.tableView_9,
                self.comboBox_12.currentIndex(),
                self.lineEdit_17.text(),
            )
        )
        self.lineEdit_18.textChanged.connect(
            lambda: self.Filter(
                self.tableView_10,
                self.comboBox_13.currentIndex(),
                self.lineEdit_18.text(),
            )
        )
        self.lineEdit_19.textChanged.connect(
            lambda: self.Filter(
                self.tableView_11,
                self.comboBox_14.currentIndex(),
                self.lineEdit_19.text(),
            )
        )
        self.lineEdit_20.textChanged.connect(
            lambda: self.Filter(
                self.tableView_12,
                self.comboBox_15.currentIndex(),
                self.lineEdit_20.text(),
            )
        )
        self.lineEdit_21.textChanged.connect(
            lambda: self.Filter(
                self.tableView_13,
                self.comboBox_16.currentIndex(),
                self.lineEdit_21.text(),
            )
        )
        self.lineEdit_22.textChanged.connect(
            lambda: self.Filter(
                self.tableView_14,
                self.comboBox_16.currentIndex(),
                self.lineEdit_21.text(),
            )
        )

    def Show_Browse(self):
        self.stackedWidget.setCurrentWidget(self.browse)

    def Show_Add(self):
        self.stackedWidget.setCurrentWidget(self.add)

    def Show_Edit(self):
        self.stackedWidget.setCurrentWidget(self.edit)

    def Show_Lending(self):
        self.stackedWidget.setCurrentWidget(self.lending)

    def Filter(self, tableView, filter_column, filter_text):
        if tableView.model() is not None:
            tableView.model().setFilterKeyColumn(filter_column)
            tableView.model().setFilterFixedString(filter_text)
        else:
            print("No model")
        pass

    # Method to read from database and display in QTableWidget
    def Read_Resources(self):
        sourceModel = QSqlQueryModel()
        proxyModel = QSortFilterProxyModel()
        query = QSqlQuery()
        query.exec_(
            "SELECT Resources.Resource_ID AS ID, "
            "Resources.Title, "
            "GROUP_CONCAT(Creators1.Name) AS `Authors(s)`, "
            "Resources.Date_of_copyright AS `Publish Date`, "
            "Resources.Dewey_decimal AS `Dewey Decimal`, "
            "GROUP_CONCAT(Categories.Category_Name) AS Categories "
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
            "INNER JOIN Resources_Categories "
            "ON Resources.Resource_ID = Resources_Categories.Resource_ID "
            "INNER JOIN Categories "
            "ON Resources_Categories.Category_ID = Categories.Category_ID "
            "GROUP BY Resources.Resource_ID, Resources.Title"
        )
        sourceModel.setQuery(query)
        print(query.lastError().text())
        proxyModel.setSourceModel(sourceModel)
        self.tableView.setSortingEnabled(True)
        self.tableView.setModel(proxyModel)

    def Read_Books(self):
        sourceModel = QSqlQueryModel()
        proxyModel = QSortFilterProxyModel()
        query = QSqlQuery()
        query.exec_(
            "SELECT Resources.Resource_ID AS ID, "
            "Resources.Title, "
            "GROUP_CONCAT(Creators1.Name) AS `Authors(s)`, "
            "Resources.Date_of_copyright AS `Publish Date`, "
            "Books.Language, "
            "Resources.Dewey_decimal AS `Dewey Decimal`, "
            "GROUP_CONCAT(Categories.Category_Name) AS Categories "
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
            "INNER JOIN Resources_Categories "
            "ON Resources.Resource_ID = Resources_Categories.Resource_ID "
            "INNER JOIN Categories "
            "ON Resources_Categories.Category_ID = Categories.Category_ID "
            "GROUP BY Resources.Resource_ID"
        )
        sourceModel.setQuery(query)
        print(query.lastError().text())
        proxyModel.setSourceModel(sourceModel)
        self.tableView_2.setSortingEnabled(True)
        self.tableView_2.setModel(proxyModel)

    def Read_Essays(self):
        sourceModel = QSqlQueryModel()
        proxyModel = QSortFilterProxyModel()
        query = QSqlQuery()
        query.exec_(
            "SELECT Resources.Resource_ID AS ID, "
            "Resources.Title, "
            "GROUP_CONCAT(Creators1.Name) AS `Author(s)`, "
            "Resources.Date_of_copyright AS `Publish Date`, "
            "Essays.Language, "
            "Essays.Container_text AS Container, "
            "GROUP_CONCAT(Categories.Category_Name) AS Categories "
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
            "INNER JOIN Resources_Categories "
            "ON Resources.Resource_ID = Resources_Categories.Resource_ID "
            "INNER JOIN Categories "
            "ON Resources_Categories.Category_ID = Categories.Category_ID "
            "GROUP BY Resources.Resource_ID"
        )
        sourceModel.setQuery(query)
        print(query.lastError().text())
        proxyModel.setSourceModel(sourceModel)
        self.tableView_3.setSortingEnabled(True)
        self.tableView_3.setModel(proxyModel)

    def Read_Articles(self):
        sourceModel = QSqlQueryModel()
        proxyModel = QSortFilterProxyModel()
        query = QSqlQuery()
        query.exec_(
            "SELECT Resources.Resource_ID AS ID, "
            "Resources.Title, "
            "GROUP_CONCAT(Creators1.Name) AS `Author(s)`, "
            "Resources.Date_of_copyright `Publish Date`, "
            "Articles.Language, "
            "Articles.Container_text AS Container, "
            "GROUP_CONCAT(Categories.Category_Name) AS Categories "
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
            "INNER JOIN Resources_Categories "
            "ON Resources.Resource_ID = Resources_Categories.Resource_ID "
            "INNER JOIN Categories "
            "ON Resources_Categories.Category_ID = Categories.Category_ID "
            "GROUP BY Resources.Resource_ID"
        )
        sourceModel.setQuery(query)
        print(query.lastError().text())
        proxyModel.setSourceModel(sourceModel)
        self.tableView_4.setSortingEnabled(True)
        self.tableView_4.setModel(proxyModel)

    def Read_Periodicals(self):
        sourceModel = QSqlQueryModel()
        proxyModel = QSortFilterProxyModel()
        query = QSqlQuery()
        query.exec_(
            "SELECT Periodical_ID AS `Periodical ID`, "
            "Name, "
            "Start_date AS `Start Date`, "
            "End_date AS `End Date`, "
            "Language "
            "FROM Periodicals"
        )
        sourceModel.setQuery(query)
        print(query.lastError().text())
        proxyModel.setSourceModel(sourceModel)
        self.tableView_5.setSortingEnabled(True)
        self.tableView_5.setModel(proxyModel)

    def Read_Issues(self):
        sourceModel = QSqlQueryModel()
        proxyModel = QSortFilterProxyModel()
        query = QSqlQuery()
        query.exec_(
            "SELECT Resources.Resource_ID AS ID, "
            "Resources.Title, "
            "Issues.Date_of_issue AS `Date of Issue`, "
            "Periodicals.Name AS `Periodical`, "
            "GROUP_CONCAT(Creators1.Name) AS `Author(s)`, "
            "Periodicals.Language, "
            "GROUP_CONCAT(Categories.Category_Name) AS Categories "
            "FROM Resources "
            "INNER JOIN Issues "
            "ON Resources.Resource_ID = Issues.Resource_ID "
            "INNER JOIN Resources_Creators "
            "ON Resources.Resource_ID = Resources_Creators.Resource_ID "
            "INNER JOIN ( "
            "SELECT Name, Creator_ID FROM Authors "
            "UNION ALL "
            "SELECT Name, Creator_ID FROM Collectives "
            ") "
            "AS Creators1 "
            "ON Resources_Creators.Creator_ID = Creators1.Creator_ID "
            "INNER JOIN Periodicals "
            "ON Issues.Periodical_ID = Periodicals.Periodical_ID "
            "INNER JOIN Resources_Categories "
            "ON Resources.Resource_ID = Resources_Categories.Resource_ID "
            "INNER JOIN Categories "
            "ON Resources_Categories.Category_ID = Categories.Category_ID "
        )
        sourceModel.setQuery(query)
        print(query.lastError().text())
        proxyModel.setSourceModel(sourceModel)
        self.tableView_6.setSortingEnabled(True)
        self.tableView_6.setModel(proxyModel)

    def Read_Creators(self, mode):
        sourceModel = QSqlQueryModel()
        proxyModel = QSortFilterProxyModel()
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
        sourceModel.setQuery(query)
        print(query.lastError().text())
        proxyModel.setSourceModel(sourceModel)
        self.tableView_7.setSortingEnabled(True)
        self.tableView_7.setModel(proxyModel)
        return 0

    def Edit_Resources(self):
        sourceModel = QSqlRelationalTableModel()
        sourceModel.setTable("Resources")
        sourceModel.select()
        proxyModel = QSortFilterProxyModel()
        proxyModel.setSourceModel(sourceModel)
        self.tableView_8.setSortingEnabled(True)
        self.tableView_8.setModel(proxyModel)

    def Edit_Books(self):
        sourceModel = QSqlRelationalTableModel()
        sourceModel.setTable("Books")
        sourceModel.select()
        proxyModel = QSortFilterProxyModel()
        proxyModel = QSortFilterProxyModel()
        proxyModel.setSourceModel(sourceModel)
        self.tableView_9.setSortingEnabled(True)
        self.tableView_9.setModel(proxyModel)

    def Edit_Essays(self):
        sourceModel = QSqlRelationalTableModel()
        sourceModel.setTable("Essays")
        sourceModel.select()
        proxyModel = QSortFilterProxyModel()
        proxyModel = QSortFilterProxyModel()
        proxyModel.setSourceModel(sourceModel)
        self.tableView_10.setSortingEnabled(True)
        self.tableView_10.setModel(proxyModel)

    def Edit_Articles(self):
        sourceModel = QSqlRelationalTableModel()
        sourceModel.setTable("Articles")
        sourceModel.select()
        proxyModel = QSortFilterProxyModel()
        proxyModel = QSortFilterProxyModel()
        proxyModel.setSourceModel(sourceModel)
        self.tableView_11.setSortingEnabled(True)
        self.tableView_11.setModel(proxyModel)

    def Edit_Periodicals(self):
        sourceModel = QSqlRelationalTableModel()
        sourceModel.setTable("Periodicals")
        sourceModel.select()
        proxyModel = QSortFilterProxyModel()
        proxyModel = QSortFilterProxyModel()
        proxyModel.setSourceModel(sourceModel)
        self.tableView_12.setSortingEnabled(True)
        self.tableView_12.setModel(proxyModel)

    def Edit_Issues(self):
        sourceModel = QSqlRelationalTableModel()
        sourceModel.setTable("Issues")
        sourceModel.select()
        proxyModel = QSortFilterProxyModel()
        proxyModel = QSortFilterProxyModel()
        proxyModel.setSourceModel(sourceModel)
        self.tableView_13.setSortingEnabled(True)
        self.tableView_13.setModel(proxyModel)

    def Edit_Creators(self, mode):
        sourceModel = QSqlRelationalTableModel()
        if mode == 0:
            sourceModel.setTable("Creators")
        elif mode == 1:
            sourceModel.setTable("Authors")
        elif mode == 2:
            sourceModel.setTable("Collectives")
        else:
            return 1
        sourceModel.select()
        proxyModel = QSortFilterProxyModel()
        proxyModel = QSortFilterProxyModel()
        proxyModel.setSourceModel(sourceModel)
        self.tableView_14.setSortingEnabled(True)
        self.tableView_14.setModel(proxyModel)
        return 0

    def Edit_Borrowing(self):
        sourceModel = QSqlRelationalTableModel()
        sourceModel.setTable("Borrowing")
        sourceModel.select()
        proxyModel = QSortFilterProxyModel()
        proxyModel = QSortFilterProxyModel()
        proxyModel.setSourceModel(sourceModel)
        self.tableView_15.setSortingEnabled(True)
        delegate = QSqlRelationalDelegate(self.tableView_15)
        self.tableView_15.setItemDelegate(delegate)
        self.tableView_15.setModel(proxyModel)

    def Edit_Borrowed(self):
        sourceModel = QSqlRelationalTableModel()
        sourceModel.setTable("Borrowed")
        sourceModel.select()
        proxyModel = QSortFilterProxyModel()
        proxyModel = QSortFilterProxyModel()
        proxyModel.setSourceModel(sourceModel)
        self.tableView_16.setSortingEnabled(True)
        delegate = QSqlRelationalDelegate(self.tableView_16)
        self.tableView_16.setItemDelegate(delegate)
        self.tableView_16.setModel(proxyModel)

    def Edit_Reservations(self):
        sourceModel = QSqlRelationalTableModel()
        sourceModel.setTable("Reserves")
        sourceModel.select()
        proxyModel = QSortFilterProxyModel()
        proxyModel = QSortFilterProxyModel()
        proxyModel.setSourceModel(sourceModel)
        self.tableView_17.setSortingEnabled(True)
        delegate = QSqlRelationalDelegate(self.tableView_17)
        self.tableView_17.setItemDelegate(delegate)
        self.tableView_17.setModel(proxyModel)

    def Edit_Waitlist(self):
        sourceModel = QSqlRelationalTableModel()
        sourceModel.setTable("Waiting_List")
        sourceModel.select()
        proxyModel = QSortFilterProxyModel()
        proxyModel = QSortFilterProxyModel()
        proxyModel.setSourceModel(sourceModel)
        self.tableView_18.setSortingEnabled(True)
        delegate = QSqlRelationalDelegate(self.tableView_18)
        self.tableView_18.setItemDelegate(delegate)
        self.tableView_18.setModel(proxyModel)

    def Edit_Borrowers(self):
        sourceModel = QSqlRelationalTableModel()
        sourceModel.setTable("Borrowers")
        sourceModel.select()
        proxyModel = QSortFilterProxyModel()
        proxyModel = QSortFilterProxyModel()
        proxyModel.setSourceModel(sourceModel)
        self.tableView_19.setSortingEnabled(True)
        delegate = QSqlRelationalDelegate(self.tableView_19)
        self.tableView_19.setItemDelegate(delegate)
        self.tableView_19.setModel(proxyModel)

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
