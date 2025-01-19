import os
import pickle
import csv
import unittest
import pytest


class CSVDBObject(object):
    def __init__(self, dbname: str, folderpath: str):
        self.tables = {}
        self.dbname = dbname
        self.folderpath = folderpath
        if not self.folderpath.endswith("\\"):
            self.folderpath += "\\"
        if not os.path.exists(self.folderpath):
            os.mkdir(self.folderpath)
        try:
            with open(self.folderpath +"\\"+ self.dbname + ".dat", "rb") as f:
                data = pickle.load(f)
                self.dbname = data["dbname"]
                self.folderpath = data["folderpath"]
        except (EOFError, FileNotFoundError):
            with open(self.folderpath +"\\"+ self.dbname + ".dat", "wb") as f:
                pickle.dump(
                    {
                        "dbname": self.dbname,
                        "folderpath": self.folderpath,
                        "tables": self.tables,
                    },
                    f,
                )
        with open(self.folderpath + "\\" + self.dbname + ".dat", "rb") as f:
            data = pickle.load(f)
            self.tables = data["tables"]

    class CSVDBTableObject(object):
        def __init__(
            self,
            tablename: str,
            columns: dict[str, tuple[type, bool, bool]],
            defaults: dict[str, any] = None,
        ):
            """
            Parameters
            ----------
            db : CSVDBObject
                The database object where the table will be created
            tablename : str
                The name of the table
            columns : dict[str,tuple[type,bool,bool]]
                A dictionary where the keys are column names and the value is a tuple of three values: the type of the column, whether the column is not null, and whether the column needs to be unique
            """
            self.tablename = tablename
            self.columns = columns
            self.defaults = defaults or {}

        def __repr__(self):
            return (
                f"CSVDBTableObject(tablename={self.tablename}, columns={self.columns})"
            )

        def select(self, dbobject, column_names: list[str] = None):
            """
            Select rows from the table.

            Parameters
            ----------
            column_names : list[str]
                A list of column names to select
            """
            with open(dbobject.folderpath + self.tablename + ".csv", "r") as f:
                if column_names is None:
                    return list(csv.DictReader(f))
                else:
                    a = list(csv.DictReader(f))
                    for i in a:
                        # only return the selected columns
                        return {k: i[k] for k in column_names}

        def insert(self, dbobject, values: list, column_names: list[str] = None):
            """
            Insert a row into the table.

            Parameters
            ----------
            values : list
                A list of values to insert
            column_names : list[str]
                A list of column names

            Returns
            -------
            None
            """


            with open(
                self.folderpath + self.tablename + ".csv", "a", newline=""
            ) as f:
                if column_names is None:
                    column_names = list(self.columns.keys())
                writer = csv.DictWriter(f, fieldnames=column_names)

                # Check if the file is empty
                if f.tell() == 0:
                    writer.writeheader()

                # Validate the values
                for i, value in zip(column_names, values):
                    if i not in self.columns:
                        raise KeyError(f"Column({i}) does not exist")
                    elif self.columns[i][0] is not type(value):
                        raise TypeError(f"Column({i}) type does not match")
                    elif self.columns[i][1] and (value is None or value == ""):
                        if self.defaults.get(i) is not None:
                            value = self.defaults[i]
                        else:
                            raise ValueError(f"Column({i}) value is not allowed to be null")
                    elif self.columns[i][2]:  # Check if unique is True
                        with open(
                            dbobject.folderpath + self.tablename + ".csv", "r"
                        ) as existing_file:
                            existing_reader = csv.DictReader(existing_file)
                            for row in existing_reader:
                                if row[i] == str(
                                    value
                                ):  # Check if value already exists
                                    raise ValueError(
                                        f"Column({i}) value must be unique"
                                    )

                # Write the row
                writer.writerow(dict(zip(column_names, values)))

    def create_table(
        self, tablename: str, columns: dict[str, tuple[type, bool, bool]], defaults: dict[str, any] = None
    ) -> CSVDBTableObject:
        """
        Create a table in the database.

        Parameters
        ----------
        tablename : str
            The name of the table to be created.
        columns : dict[str, tuple[type,bool,bool]]
            A dictionary where the keys are the column names and the value is a tuple of (type, is_not_null, is_unique)

        Returns
        -------
        CSVDBTableObject
            The created table object
        """
        file_path = self.folderpath + tablename + ".csv"
        if os.path.exists(file_path):
            # File already exists, append to it
            pass
        else:
            # File does not exist, create it
            with open(file_path, "w", newline="") as f:
                csv.DictWriter(f, columns.keys()).writeheader()
        self.tables[tablename] = self.CSVDBTableObject(tablename, columns, defaults)
        return CSVDBObject.CSVDBTableObject(tablename, columns, defaults)


db = CSVDBObject("Test", "test_folder")
table = db.create_table(tablename="test_table", columns={"col1": (str, False, False), "col2": (int, True, True)})

assert isinstance(table, CSVDBObject.CSVDBTableObject)

table.insert(db, ["test", 1])
assert table.select(db) == [{"col1": "test", "col2": 1}]

table.insert(db, ["test", 2])  # This should raise ValueError as the value of col1 is already in the table

table.insert(db, ["test", 1])  # This should raise ValueError as the value of col2 is not unique

table.insert(db, ["test2", 1], ["col1", "col2"])

assert table.select(db) == [{"col1": "test", "col2": 1}, {"col1": "test2", "col2": 1}]

table.insert(db, ["test3", 2], ["col1", "col2"])

assert table.select(db) == [{"col1": "test", "col2": 1}, {"col1": "test2", "col2": 1}, {"col1": "test3", "col2": 2}]



    



