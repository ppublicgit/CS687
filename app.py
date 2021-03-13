import sys
import pandas as pd

import mysql.connector
from mysql.connector import Error

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QTableWidgetItem
from app_ui import Ui_MainWindow

from sql_py_helper import SqlConnection

import datetime


class MainWindow(QMainWindow, Ui_MainWindow):
    """Class for creating and handling GUI
    """
    def __init__(self, parent=None):
        """Initialization of GUI
        """
        super().__init__(parent)
        self.setupUi(self)

        self.current_user = (None, None)

        self.eng = SqlConnection()

        self.setup_gui()


    def setup_gui(self):
        """Setup GUI buttons and boxes

        Connect actions of buttons and spin boxes and more to
        function handlers
        """
        # setup push buttons
        self.pb_user_select.clicked.connect(self.handle_user_select)
        self.pb_edit_details.clicked.connect(self.handle_edit_details)
        self.pb_sort.clicked.connect(self.handle_sort_transactions)
        self.pb_buy.clicked.connect(self.handle_buy)
        self.pb_new_item.clicked.connect(self.handle_new_item)
        self.pb_product_search.clicked.connect(self.handle_search_item)
        self.pb_product_search_reset.clicked.connect(self.handle_search_reset)

        # initialize table for transactions
        self.table_transactions.setColumnCount(8)

        # display all the companies, items and support in their respective tables
        self.display_all_items()
        self.display_all_companies()
        self.display_all_support()

        # intialize the user
        self.le_company_id.setEnabled(False)
        self.le_user_id.setEnabled(False)

        # get the categories found in the database
        self.setup_categories()

        # get the maximum value for the prices in listing table
        self.maxval = self.get_max_val()

        # setup the spin boxes
        self.set_sb_vals(self.sb_min_price, minval=0, maxval=1000000, val=0)
        self.set_sb_vals(self.sb_max_price, minval=0, maxval=1000000, val=self.maxval)
        self.sb_min_price.valueChanged.connect(self.sb_min_price_update)
        self.sb_max_price.valueChanged.connect(self.sb_max_price_update)


    def get_max_val(self):
        """Get the maximum listing price
        """
        self.eng.sql_command("SELECT price FROM LISTING ORDER BY price DESC")
        price = None
        for row in self.eng.cursor:
            if price is None:
                price = row[0]
        return price


    def setup_categories(self):
        """Get all the categories in the product_types table
        """
        self.eng.sql_command("SELECT category, category_name FROM PRODUCT_TYPES")
        self.cb_search_category.insertItem(0, "All")
        for (cat, cat_name) in self.eng.cursor:
            self.cb_new_item_category.insertItem(cat, cat_name)
            self.cb_search_category.insertItem(cat, cat_name)
        return


    def display_all_items(self):
        """Display all items in the item table of the gui

        Call a SQL Query to get all the items in the product and the
        associated listings and display in table_items in gui
        """
        self.table_items.setColumnCount(5)
        self.eng.sql_command((f"SELECT p.id, p.product_name, "
                              f"pt.category_name, c.cname, l.price "
                              f"FROM PRODUCT AS p JOIN PRODUCT_TYPES AS pt "
                              f"ON p.category = pt.category JOIN LISTING as l "
                              f"ON l.product_id = p.id JOIN COMPANY AS c "
                              f"ON c.id = l.company_id "
                              "ORDER BY p.id, l.price"))
        self.table_items.clear()
        for i, row in enumerate(self.eng.cursor):
            if self.table_items.rowCount() <= i:
                self.table_items.insertRow(i)
            for j, val in enumerate(row):
                val = str(val).rjust(20)
                newitem = QTableWidgetItem(val)
                self.table_items.setItem(i, j, newitem)
        self.table_items.resizeColumnsToContents()
        self.table_items.resizeRowsToContents()
        self.table_items.setHorizontalHeaderLabels(["Product ID",
                                                    "Product Name",
                                                    "Category",
                                                    "Company Name",
                                                    "Price"])
        return


    def display_all_companies(self):
        """Display all companies in company table to GUI's table company
        """
        self.table_companies.setColumnCount(4)
        self.eng.sql_command(("SELECT c.id, c.cname, c.address, c.country_code "
                             "FROM COMPANY AS c"))
        self.table_companies.clear()
        for i, row in enumerate(self.eng.cursor):
            if self.table_companies.rowCount() <= i:
                self.table_companies.insertRow(i)
            for j, val in enumerate(row):
                val = str(val).rjust(20)
                newitem = QTableWidgetItem(val)
                self.table_companies.setItem(i, j, newitem)
        self.table_companies.resizeColumnsToContents()
        self.table_companies.resizeRowsToContents()

        self.table_companies.setHorizontalHeaderLabels(["Company ID",
                                                        "Company Name",
                                                        "Address",
                                                        "Country"])
        return


    def display_all_support(self):
        """Display all support personnel in support table to GUI's table support
        """
        self.table_support.setColumnCount(4)
        self.eng.sql_command(("SELECT c.cname, s.contact_name, "
                              "s.contact_email, s.contact_phone FROM SUPPORT as s "
                              "JOIN COMPANY AS c ON c.id = s.company_id"))
        self.table_support.clear()
        for i, row in enumerate(self.eng.cursor):
            if self.table_support.rowCount() <= i:
                self.table_support.insertRow(i)
            for j, val in enumerate(row):
                val = str(val).rjust(20)
                newitem = QTableWidgetItem(val)
                self.table_support.setItem(i, j, newitem)
        self.table_support.resizeColumnsToContents()
        self.table_support.resizeRowsToContents()

        self.table_support.setHorizontalHeaderLabels(["Company Name",
                                                      "Contact Name",
                                                      "Contact Email",
                                                      "Contact Phone"])
        return


    def handle_search_reset(self):
        """Handle search reset button press

        Reset the search settings for the item table to show all the
        available items again
        """
        self.sb_min_price.setValue(0)
        self.sb_max_price.setValue(self.maxval)
        self.display_all_items()
        return


    def handle_search_item(self):
        """Handle searching the item table

        Use the paramaters set in the options on the item tab of the gui
        to query the database
        """
        lowprice = self.sb_min_price.value()
        highprice = self.sb_max_price.value()
        category = self.cb_search_category.currentIndex()
        # if check to query on category
        if not category:
            command = (f"SELECT p.id, p.product_name, pt.category_name, "
                       f"c.cname, l.price FROM PRODUCT AS p JOIN "
                       f"PRODUCT_TYPES AS pt ON p.category = pt.category "
                       "JOIN LISTING as l ON l.product_id = p.id JOIN "
                       "COMPANY as c ON c.id = l.company_id "
                       f"WHERE l.price <= {highprice+0.01} AND l.price >= {lowprice-0.01} "
                       "ORDER BY p.id, l.price")
        else:
            command = (f"SELECT p.id, p.product_name, pt.category_name, "
                       f"c.cname, l.price FROM PRODUCT AS p JOIN "
                       f"PRODUCT_TYPES AS pt ON p.category = pt.category "
                       "JOIN LISTING as l ON l.product_id = p.id JOIN "
                       "COMPANY as c ON c.id = l.company_id "
                       f"WHERE l.price <= {highprice+0.01} AND "
                       f"l.price >= {lowprice-0.01} AND p.category = {category}"
                       "ORDER BY p.id, l.price")
        self.eng.sql_command(command)
        self.table_items.clear()
        for i, row in enumerate(self.eng.cursor):
            if self.table_items.rowCount() <= i:
                self.table_items.insertRow(i)
            for j, val in enumerate(row):
                val = str(val).rjust(20)
                newitem = QTableWidgetItem(val)
                self.table_items.setItem(i, j, newitem)
        self.table_items.setHorizontalHeaderLabels(["Product ID",
                                                    "Product Name",
                                                    "Category",
                                                    "Company Name",
                                                    "Price"])
        return


    def handle_edit_details(self):
        """Handle the edit details button pressed

        Update the user or company information for the given user or company
        that is currently logged in
        """
        # check if a user, company or nobody is logged in
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
            self.eng.sql_command(command)
            self.display_all_companies()
            self.display_all_support()
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
            self.eng.sql_command(command)
        return


    def handle_sort_transactions(self):
        """Handle sort transactions button pressed

        Requery the transaction table (joined with others)
        to get the transaction information for a user or company
        and sort the output based on the sort option chosen
        """
        if self.current_user[0] == "Company":
            self.company_transaction_options()
        elif self.current_user[0] == "User":
            self.user_transaction_options()
        return


    def handle_buy(self):
        """Handle the buy button pressed

        Only available if a user is logged in. User can buy product from
        specified company. Updates the transaction table of the database
        as well and is included in the users transaction table
        """
        if self.current_user[0] != "User":
            return
        pid = self.le_buy_id.text()
        cid = self.le_buy_cid.text()
        quantity = self.le_buy_quantity.text()
        uid = self.current_user[1]
        transact_date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.eng.sql_command((f"INSERT INTO TRANSACTIONS "
                              f"(user_id, product_id, company_id, quantity, transact_date) "
                              f"VALUES ({uid}, {pid}, {cid}, {quantity}, '{transact_date}')"))
        self.user_transaction_options()
        return


    def handle_new_item(self):
        """Handle the new item button being pressed

        Only available if a company is logged in. Company is able to add an item to
        be listed. If the item already exists, only a listing pertaining to the company
        is added. IF the item does not exist, it is first added to the product table
        and then added to the listing table.
        """
        if self.current_user[0] != "Company":
            return
        pn = self.le_new_item_name.text()
        cat = self.cb_new_item_category.currentIndex()+1
        cid = self.current_user[1]
        price = self.le_new_item_price.text()
        pid = None
        # check to see if product already exists
        self.eng.sql_command(f"SELECT id FROM PRODUCT WHERE product_name = '{pn}'")
        for row in self.eng.cursor:
            pid = row[0]
        # no product id found add to product table first
        if pid is None:
            self.eng.sql_command((f"INSERT INTO PRODUCT (product_name, category) "
                                  f"VALUES ('{pn}', {cat})"))
            self.eng.sql_command(f"SELECT id FROM PRODUCT WHERE product_name = '{pn}'")
            for row in self.eng.cursor:
                pid = row[0]
        # add to listing table
        self.eng.sql_command((f"INSERT INTO LISTING (company_id, product_id, price) "
                              f"VALUES ({cid}, {pid}, {price})"))
        self.display_all_items()
        # check if new listing is the new maximum listing price
        if float(price) > self.maxval:
            self.maxval = float(price)
            self.sb_min_price.setMaximum(self.maxval)
            self.sb_min_price.setValue(0)
            self.sb_max_price.setValue(self.maxval)
        return


    def set_user_info(self, id_, fn, ln, add, disable=False):
        """Set user info

        Set the text boxes of the gui to the args passed in information and
        set the gui into either company or user mode depending on
        value of disable
        """
        self.le_user_id.setText(str(id_))
        self.le_first_name.setText(fn)
        self.le_last_name.setText(ln)
        self.le_address_user.setText(add)
        self.set_company_enabled(not disable)
        self.set_user_enabled(disable)
        return


    def set_user_enabled(self, disable):
        """Set the user mode paramaters based on disable
        to either enable or disable various buttons
        """
        self.le_first_name.setEnabled(not disable)
        self.le_last_name.setEnabled(not disable)
        self.le_address_user.setEnabled(not disable)
        self.le_buy_id.setEnabled(not disable)
        self.le_buy_quantity.setEnabled(not disable)
        self.pb_buy.setEnabled(not disable)
        return


    def set_company_enabled(self, disable):
        """Set the user mode paramaters based on disable
        to either enable or disable various buttons
        """
        self.le_address_company.setEnabled(not disable)
        self.le_country_of_origin.setEnabled(not disable)
        self.le_act_company.setEnabled(not disable)
        self.le_new_item_name.setEnabled(not disable)
        self.cb_new_item_category.setEnabled(not disable)
        self.le_new_item_price.setEnabled(not disable)
        self.pb_new_item.setEnabled(not disable)
        return


    def set_comp_info(self, id_, cn, add, cou, disable=False):
        """Set company info

        Set the text boxes of the gui to the args passed in information and
        set the gui into either company or user mode depending on
        value of disable
        """
        self.le_company_id.setText(str(id_))
        self.le_address_company.setText(add)
        self.le_country_of_origin.setText(cou)
        self.le_act_company.setText(cn)
        self.set_company_enabled(disable)
        self.set_user_enabled(not disable)
        return


    def handle_user_select(self):
        """Handle a select user button pressed

        Determines if nobody, a user or company has been selected
        and calls the appropriate functions to set up the gui for the
        user/company logging in
        """
        comp = self.rb_user_company.isChecked()
        user = self.rb_user_user.isChecked()
        # no user or company selected
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
        return


    def set_company_mode(self):
        """Setup company

        Query the database for company id chosen and if found
        set the company info and log in with company mode
        """
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
        """Setup user

        Query the database for user id chosen and if found
        set the user info and log in with user mode
        """
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
        """Set the spinbox values specified
        """
        slider.setMinimum(minval)
        slider.setMaximum(maxval)
        slider.setValue(val)


    def sb_min_price_update(self):
        """Update the spinbox min price for item search

        Checks to see if the min price is greater than the current max
        price set and if it is, updates the max to equal the min to
        make sure that max price >= min price always
        """
        curval = self.sb_min_price.value()
        if self.sb_max_price.value() < curval:
            self.sb_max_price.setValue(curval)
        return


    def sb_max_price_update(self):
        """Update the spinbox max price for item search

        Checks to see if the max price is less than the current min
        price set and if it is, updates the min to equal the max to
        make sure that max price >= min price always
        """
        curval = self.sb_max_price.value()
        if self.sb_min_price.value() > curval:
            self.sb_min_price.setValue(curval)
        return


    def user_transaction_options(self):
        """Get users transactions

        User is logged on , get all the transactions of said user and display to
        the transaction table of the gui
        """
        uid = self.le_user_id.text()
        ordering = self.get_ordering()
        self.eng.sql_command((f"SELECT t.id, t.user_id, c.cname, "
                              f"p.product_name, pt.category_name, t.quantity, "
                              f"l.price, t.transact_date FROM TRANSACTIONS AS t "
                              f"JOIN PRODUCT AS p ON p.id = t.product_id JOIN "
                              f"PRODUCT_TYPES AS pt ON p.category = pt.category "
                              f"JOIN LISTING AS l ON (l.company_id = t.company_id "
                              f"AND l.product_id = t.product_id ) "
                              f"JOIN COMPANY AS c ON c.id = t.company_id "
                              f"WHERE t.user_id = {uid} ORDER BY {ordering} DESC"))
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

        self.table_transactions.setHorizontalHeaderLabels(["Order #", "User ID", "Company Name", "Product", "Category", "Quantity", "Price", "Date"])
        return


    def company_transaction_options(self):
        """Get company transactions

        Company is logged on , get all the transactions of said company and display to
        the transaction table of the gui
        """
        cid = self.le_company_id.text()
        ordering = self.get_ordering()
        self.eng.sql_command((f"SELECT t.id, t.user_id, c.cname, "
                              f"p.product_name, pt.category_name, "
                              f"t.quantity, l.price, t.transact_date "
                              f"FROM TRANSACTIONS AS t JOIN PRODUCT AS p "
                              f"ON p.id = t.product_id JOIN PRODUCT_TYPES AS pt "
                              f"ON p.category = pt.category JOIN LISTING AS l "
                              f"ON (l.company_id = t.company_id "
                              f"AND l.product_id = t.product_id)"
                              f"JOIN COMPANY AS c ON c.id = t.company_id "
                              f"WHERE l.company_id = {cid} ORDER BY {ordering} DESC"))
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

        self.table_transactions.setHorizontalHeaderLabels(["Order #",
                                                           "User ID",
                                                           "Company Name",
                                                           "Product",
                                                           "Category",
                                                           "Qunatity",
                                                           "Price",
                                                           "Date"])
        return


    def get_ordering(self):
        """Get the ordering sort for the transaction table of the gui
        """
        if self.rb_sort_date.isChecked():
            return "t.transact_date"
        elif self.rb_sort_price.isChecked():
            return "l.price"
        elif self.rb_sort_order_num.isChecked():
            return "t.id"
        else:
            return "t.quantity"


def main():
    """Main entry point for GUI"""
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setWindowTitle("Fake Amazon")
    main_window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
