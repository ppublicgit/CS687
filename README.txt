    README.txt
    Paul Abers
    CS 687 Project 1

    To open the GUI, one must have python3 installed with packages
    PyQt5, mysql and datetime

    README for running application to help users/companies interact
    with the FAKE_AMAZON database.

    The GUI has 8 tabs to view:
    Select User
    My Account
    My Transactions
    Buy Product
    Add Item
    All Items
    All Companies
    Support

    The first tab is in essence a login page. The GUI has no security
    measures so to login just put the company id or user id in their
    respective text edit box, and select the radio button for whether to
    sign in as a user or a company. The idea is that a company or user
    would know their own login. However, in this toy example, one can just
    find the user ids and company ids in the database and select one to use.
    If a valid login is passed, that user/company is logged in.

    The second tab is the my account table. If no user/company is logged in,
    the information is blank. If a user/company is logged in then the information
    is populated in the text boxes. If a user/company wants to update their
    information, then change the information in the boxes and then press the edit
    details button.

    The third tab is for the user's/company's transactions. The table is
    populated with all the transactions involving the currently logged in user/company.
    The transactions can be sorted via various parameters to choose from at the top.

    The next two tabs are only available based on the type of the logged in
    session. If a user is logged in, the add item tab is disabled. If a company is
    logged in, then the buy product tab is disabled. A user can buy a product that is
    listed by a company. To find the available items to buy, a user can check the
    all items page and perform such searches to narrow down to the product of
    interest. A company can add a listing to the items page via the add item tab.
    A product name, category and price are required. If the product name already exists,
    then just a listing entry is added with the associated price. If the product
    does not yet exist, then the product is first added and then a listing is added.

    The next three tabs, all items, all companies and support display information
    to any user/company logged in. In fact, noone need be logged in at all to view these
    tabs. Company and support both simply display all the entries in their tables
    without any search parameters possible. The all items page can be searched by
    limiting the price range or the category of products to display. To reset to show
    all items again after searching, simply press the reset button.
