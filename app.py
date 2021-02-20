import sys
import pandas as pd

import mysql.connector
from mysql.connector import Error

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from app_ui import Ui_MainWindow

from sql_py_helper import SqlConnection


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
        self.setup_transaction_tab()
        #self.setup_company_tab()
        #self.setup_product_tab()


    def handle_edit_details(self):

        return


    def set_user_info(self, id_, fn, ln, add, disable=False):
        self.le_user_id.setText(str(id_))
        self.le_first_name.setText(fn)
        self.le_last_name.setText(ln)
        self.le_address_user.setText(add)
        if disable:
            self.le_user_id.setEnabled(False)
            self.le_first_name.setEnabled(False)
            self.le_last_name.setEnabled(False)
            self.le_address_user.setEnabled(False)
            self.le_user_user.setEnabled(False)
        else:
            self.le_user_id.setEnabled(True)
            self.le_first_name.setEnabled(True)
            self.le_last_name.setEnabled(True)
            self.le_address_user.setEnabled(True)
            self.le_user_user.setEnabled(True)
        return


    def set_comp_info(self, id_, cn, add, cou, disable=False):
        self.le_company_id.setText(str(id_))
        self.le_address_company.setText(add)
        self.le_country_of_origin.setText(cou)
        self.le_act_company.setText(cn)
        if disable:
            self.le_company_id.setEnabled(False)
            self.le_address_company.setEnabled(False)
            self.le_country_of_origin.setEnabled(False)
            self.le_act_company.setEnabled(False)
            self.le_user_company.setEnabled(False)
        else:
            self.le_company_id.setEnabled(True)
            self.le_address_company.setEnabled(True)
            self.le_country_of_origin.setEnabled(True)
            self.le_act_company.setEnabled(True)
            self.le_user_company.setEnabled(True)
        return


    def handle_user_select(self):
        comp = self.rb_user_company.isChecked()
        user = self.rb_user_user.isChecked()
        if not comp and not user:
            self.set_user_info("", "", "", "")
            self.set_comp_info("", "", "", "")
        elif comp:
            self.set_company_mode()
        else:
            self.set_user_mode()
        return


    def set_company_mode(self):
        self.set_user_info("", "", "", "", True)
        cid = self.le_user_company.text()
        if cid == "":
            return
        self.eng.query(f"SELECT * FROM COMPANY WHERE id = {cid}")
        ret = False
        for row in self.eng.cursor:
            ret = True
            company = row
        if ret:
            self.set_comp_info(*company)
            self.current_user = ("Company", company[0])
        else:
            self.set_comp_info("", "", "", "")
            self.current_user = (None, None)
        return


    def set_user_mode(self):
        self.set_comp_info("", "", "", "", True)
        userid = self.le_user_user.text()
        if userid == "":
            return
        self.eng.query(f"SELECT * FROM USER WHERE id = {userid}")
        ret = False
        for row in self.eng.cursor:
            ret = True
            user = row
        if ret:
            self.set_user_info(*user)
            self.current_user = ("User", user[0])
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
        self.set_sb_vals(self.sb_min_price, minval=0, maxval=10, val=0)
        self.set_sb_vals(self.sb_max_price, minval=0, maxval=10, val=0)
        self.sb_min_price.valueChanged.connect(self.sb_min_price_update)
        self.sb_max_price.valueChanged.connect(self.sb_max_price_update)
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


    def get_transactions(self, **kwargs):
        uids = kwargs.get("uids", None)
        cids = kwargs.get("cids", None)
        categories = kwargs.get("categories", None)
        tids = kwargs.get("tids", None)
        rids = kwargs.get("rids", None)
        min_price = kwargs.get("min_price", None)
        max_price = kwargs.get("max_price", None)
        start_date = kwargs.get("start_date", None)
        end_date = kwargs.get("end_date", None)

        return


    def update_transaction_tab(self):
        if self.current_user[0] is not None:
            if self.current_user[0] == "Company":
                self.get_transactions(cids=self.current_user[1])
            else:
                self.get_transactions(uids=self.current_user[1])
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
