import sys
import pandas as pd

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from app_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.current_user = (None, None)

        self.setup_gui()


    def setup_gui(self):
        #self.setup_account_tab()
        self.setup_transaction_tab()
        #self.setup_company_tab()
        #self.setup_product_tab()


    def set_hs_vals(self, slider, minval, maxval, val):
        slider.setMinimum(minval)
        slider.setMaximum(maxval)
        slider.setValue(val)


    def hs_min_price_update(self):
        curval = self.hs_min_price.value()
        if self.hs_max_price.value() < curval:
            self.hs_max_price.setValue(curval)
        return


    def hs_max_price_update(self):
        curval = self.hs_max_price.value()
        if self.hs_min_price.value() > curval:
            self.hs_min_price.setValue(curval)
        return


    def setup_transaction_tab(self):
        ### Setup Price Frame ###
        self.set_hs_vals(self.hs_min_price, minval=0, maxval=10, val=0)
        self.set_hs_vals(self.hs_max_price, minval=0, maxval=10, val=0)
        self.hs_min_price.sliderReleased.connect(self.hs_min_price_update)
        self.hs_max_price.sliderReleased.connect(self.hs_max_price_update)
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
