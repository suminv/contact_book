"""This module provides RP Contacts entry point script."""
# TODO: Add new data fields: Adding new data fields to store more information
#  about your contacts would be great. For example, you can add the contact’s
#  photo, phone number, web page, Twitter handle, and so on.
#  To do this, you might need to create new tables and set up relations
#  between them. PyQt provides the QSqlRelationalTableModel,
#  which defines an editable data model for a single table and
#  provides foreign key support.
# TODO: Provide search capability: Giving your users a way to search for a
#  contact in the database is arguably a must-have feature in this kind of
#  application. To implement it, you can use
#  PyQt’s QSqlQuery and QSqlQueryModel.


from rpcontacts.main import main

if __name__ == "__main__":
    main()