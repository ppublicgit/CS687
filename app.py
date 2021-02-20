import sys
import pandas as pd

import mysql.connector
from mysql.connector import Error

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QTableWidgetItem
from app_ui import Ui_MainWindow

from sql_py_helper import SqlConnection

import datetime


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.current_user = (None, None)

        self.eng = SqlConnection()

        self.setup_gui()


    def setup_gui(self):
        self.pb_user_select.clicked.connect(self.handle_user_select)
        self.pb_edit_details.clicked.connect(self.handle_edit_details)
        self.pb_sort.clicked.connect(self.handle_sort_transactions)
        self.update_transaction_tab()

        self.table_transactions.setColumnCount(8)

        self.display_all_items()
        self.display_all_companies()
        self.display_all_support()

        self.le_company_id.setEnabled(False)
        self.le_user_id.setEnabled(False)


    def display_all_items(self):
        self.table_items.setColumnCount(5)
        self.eng.sql_command("SELECT p.id, p.product_name, pt.category_name, p.company_id, p.price FROM PRODUCT AS p JOIN PRODUCT_TYPES AS pt ON p.category = pt.category")
        self.table_items.clear()
        for i, row in enumerate(self.eng.cursor):
            self.table_items.insertRow(i)
            for j, val in enumerate(row):
                val = str(val).rjust(20)
                newitem = QTableWidgetItem(val)
                self.table_items.setItem(i, j, newitem)
        self.table_items.resizeColumnsToContents()
        self.table_items.resizeRowsToContents()

        self.table_items.setHorizontalHeaderLabels(["Product ID", "Product Name", "Category", "Company ID", "Price"])

        return


    def display_all_companies(self):
        self.table_companies.setColumnCount(4)
        self.eng.sql_command("SELECT c.id, c.cname, c.address, c.country_code FROM COMPANY AS c")
        self.table_companies.clear()
        for i, row in enumerate(self.eng.cursor):
            self.table_companies.insertRow(i)
            for j, val in enumerate(row):
                val = str(val).rjust(20)
                newitem = QTableWidgetItem(val)
                self.table_companies.setItem(i, j, newitem)
        self.table_companies.resizeColumnsToContents()
        self.table_companies.resizeRowsToContents()

        self.table_companies.setHorizontalHeaderLabels(["Company ID", "Company Name", "Address", "Country"])
        return


    def display_all_support(self):
        self.table_support.setColumnCount(4)
        self.eng.sql_command("SELECT s.company_id, s.contact_name, s.contact_email, s.contact_phone FROM SUPPORT as s")
        self.table_support.clear()
        for i, row in enumerate(self.eng.cursor):
            self.table_support.insertRow(i)
            for j, val in enumerate(row):
                val = str(val).rjust(20)
                newitem = QTableWidgetItem(val)
                self.table_support.setItem(i, j, newitem)
        self.table_support.resizeColumnsToContents()
        self.table_support.resizeRowsToContents()

        self.table_support.setHorizontalHeaderLabels(["Company ID", "Contact Name", "Contact Email", "Contact Phone"])
        return


    def handle_edit_details(self):
        if self.current_user[0] is None:
            pass
        elif self.current_user[0] == "Company":
            cname = self.le_act_company.text()
            address = self.le_address_company.text()
            country_code = self.le_country_of_origin.text()
            cid = self.le_company_id.text()
            command = ("UPDATE COMPANY SET "
                       f"cname = '{cname}', "
                       f"address = '{address}', "
                       f"country_code = '{country_code}' "
                       f"WHERE id = {cid}")
            print(command)
            _ = self.eng.sql_command(command)
        elif self.current_user[0] == "User":
            fn = self.le_first_name.text()
            ln = self.le_last_name.text()
            address = self.le_address_user.text()
            uid = self.le_user_id.text()
            command = ("UPDATE USER SET "
                       f"firstname = '{fn}', "
                       f"lastname = '{ln}', "
                       f"address = '{address}' "
                       f"WHERE id = {uid}")
            _ = self.eng.sql_command(command)
        return


    def handle_sort_transactions(self):
        if self.current_user[0] == "Company":
            self.company_transaction_options()
        elif self.current_user[0] == "User":
            self.user_transaction_options()
        return


    def set_user_info(self, id_, fn, ln, add, disable=False):
        self.le_user_id.setText(str(id_))
        self.le_first_name.setText(fn)
        self.le_last_name.setText(ln)
        self.le_address_user.setText(add)
        self.set_company_enabled(not disable)
        self.set_user_enabled(disable)
        return


    def set_user_enabled(self, disable):
        self.le_first_name.setEnabled(not disable)
        self.le_last_name.setEnabled(not disable)
        self.le_address_user.setEnabled(not disable)
        #self.le_user_user.setEnabled(not disable)
        self.le_buy_id.setEnabled(not disable)
        self.le_buy_quantity.setEnabled(not disable)
        self.pb_buy.setEnabled(not disable)
        return


    def set_company_enabled(self, disable):
        self.le_address_company.setEnabled(not disable)
        self.le_country_of_origin.setEnabled(not disable)
        self.le_act_company.setEnabled(not disable)
        #self.le_user_company.setEnabled(not disable)
        self.le_new_item_name.setEnabled(not disable)
        self.cb_new_item_category.setEnabled(not disable)
        self.le_new_item_price.setEnabled(not disable)
        self.pb_new_item.setEnabled(not disable)
        return


    def set_comp_info(self, id_, cn, add, cou, disable=False):
        self.le_company_id.setText(str(id_))
        self.le_address_company.setText(add)
        self.le_country_of_origin.setText(cou)
        self.le_act_company.setText(cn)
        self.set_company_enabled(disable)
        self.set_user_enabled(not disable)
        return


    def handle_user_select(self):
        comp = self.rb_user_company.isChecked()
        user = self.rb_user_user.isChecked()
        if not comp and not user:
            self.set_user_info("", "", "", "")
            self.set_comp_info("", "", "", "")
            self.current_user(None, None)
        elif comp:
            self.set_company_mode()
            self.le_user_user.setText("")
        else:
            self.set_user_mode()
            self.le_user_company.setText("")
        self.setup_transaction_tab()
        return


    def set_company_mode(self):
        self.set_user_info("", "", "", "", True)
        cid = self.le_user_company.text()
        if cid == "":
            return
        self.eng.sql_command(f"SELECT * FROM COMPANY WHERE id = {cid}")
        ret = False
        for row in self.eng.cursor:
            ret = True
            company = row
        if ret:
            self.set_comp_info(*company)
            self.current_user = ("Company", company[0])
            self.company_transaction_options()
        else:
            self.set_comp_info("", "", "", "")
            self.current_user = (None, None)
        return


    def set_user_mode(self):
        self.set_comp_info("", "", "", "", True)
        userid = self.le_user_user.text()
        if userid == "":
            return
        self.eng.sql_command(f"SELECT * FROM USER WHERE id = {userid}")
        ret = False
        for row in self.eng.cursor:
            ret = True
            user = row
        if ret:
            self.set_user_info(*user)
            self.current_user = ("User", user[0])
            self.user_transaction_options()
        else:
            set_user_info("", "", "", "")
            self.current_user = (None, None)
        return


    def set_sb_vals(self, slider, minval, maxval, val):
        slider.setMinimum(minval)
        slider.setMaximum(maxval)
        slider.setValue(val)


    def sb_min_price_update(self):
        curval = self.sb_min_price.value()
        if self.sb_max_price.value() < curval:
            self.sb_max_price.setValue(curval)
        return


    def sb_max_price_update(self):
        curval = self.sb_max_price.value()
        if self.sb_min_price.value() > curval:
            self.sb_min_price.setValue(curval)
        return


    def setup_transaction_tab(self):
        ### Setup Price Frame ###
        #self.set_sb_vals(self.sb_min_price, minval=0, maxval=10, val=0)
        #self.set_sb_vals(self.sb_max_price, minval=0, maxval=10, val=0)
        #self.sb_min_price.valueChanged.connect(self.sb_min_price_update)
        #self.sb_max_price.valueChanged.connect(self.sb_max_price_update)
        #self.setup_sb(self.sb_min_price)
        #self.setup_sb(self.sb_max_price)

        ### Setup Company Frame ###
        #self.setup_lw(self.lw_company, "Company")
        #self.setup_pb(self.pb_add_company, "Transactions")

        ### Setup Country Frame ###
        #self.setup_lw(self.lw_country, "Country")
        #self.setup_pb(self.pb_add_country, "Transactions")

        ### Setup Country Frame ###
        #self.setup_lw(self.lw_category, "Category")
        #self.setup_pb(self.pb_add_category, "Transactions")

        ### Setup Date Frame ###
        #self.setup_sb(self.Budgetsb_start_day)
        #self.setup_sb(self.sb_start_month)
        #self.setup_sb(self.sb_start_year)
        #self.setup_sb(self.sb_end_day)
        #self.setup_sb(self.sb_end_month)
        #self.setup_sb(self.sb_end_year)

        ### Setup Types Frame ###
        return


    def user_transaction_options(self):
        uid = self.le_user_id.text()
        ordering = self.get_ordering()
        self.eng.sql_command(f"SELECT t.id, t.user_id, p.company_id, p.product_name, pt.category_name, t.quantity, p.price, t.transact_date FROM TRANSACTIONS AS t JOIN PRODUCT AS p ON p.id = t.product_id JOIN PRODUCT_TYPES AS pt ON p.category = pt.category  WHERE t.user_id = {uid} ORDER BY {ordering} DESC")
        self.table_transactions.clear()
        for i, row in enumerate(self.eng.cursor):
            self.table_transactions.insertRow(i)
            for j, val in enumerate(row):
                if type(val) == datetime.date:
                    val = val.strftime("%H:%M:%S.%f - %b %d %Y")
                else:
                    val = str(val).rjust(20)
                newitem = QTableWidgetItem(val)
                self.table_transactions.setItem(i, j, newitem)
        self.table_transactions.resizeColumnsToContents()
        self.table_transactions.resizeRowsToContents()

        self.table_transactions.setHorizontalHeaderLabels(["Order #", "User ID", "Company ID", "Product", "Category", "Quantity", "Price", "Date"])
        return


    def company_transaction_options(self):
        cid = self.le_company_id.text()
        ordering = self.get_ordering()
        self.eng.sql_command(f"SELECT t.id, t.user_id, p.company_id, p.product_name, pt.category_name, t.quantity, p.price, t.transact_date FROM TRANSACTIONS AS t JOIN PRODUCT AS p ON p.id = t.product_id JOIN PRODUCT_TYPES AS pt ON p.category = pt.category  WHERE p.company_id = {cid} ORDER BY {ordering} DESC")
        self.table_transactions.clear()
        for i, row in enumerate(self.eng.cursor):
            if self.table_transactions.rowCount() <= i:
                self.table_transactions.insertRow(i)
            for j, val in enumerate(row):
                if type(val) == datetime.date:
                    val = val.strftime("%H:%M:%S.%f - %b %d %Y")
                else:
                    val = str(val).rjust(20)
                newitem = QTableWidgetItem(val)
                self.table_transactions.setItem(i, j, newitem)
        self.table_transactions.resizeColumnsToContents()
        self.table_transactions.resizeRowsToContents()

        self.table_transactions.setHorizontalHeaderLabels(["Order #", "User ID", "Company ID", "Product", "Category", "Qunatity", "Price", "Date"])
        return


    def get_ordering(self):
        if self.rb_sort_date.isChecked():
            return "t.transact_date"
        elif self.rb_sort_price.isChecked():
            return "p.price"
        elif self.rb_sort_order_num.isChecked():
            return "t.id"
        else:
            return "t.quantity"


    def update_transaction_tab(self):
        if self.current_user[0] is not None:
            categories = self.categories
            min_price = self.sb_min_price.value()
            max_price = self.sb_max_price.value()
            if self.current_user[0] == "Company":
                cid = self.le_company_id.text()
                transactions = self.get_transactions()
            else:
                uid = self.le_user_id.text()
                transactions = self.get_transactions()
        return



def main():
    """Main entry point for Plot RCS app."""
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setWindowTitle("Fake Amazon")
    main_window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
