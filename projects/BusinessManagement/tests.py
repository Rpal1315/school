# tests/test_csvdb.py
import pytest
from csvdb import CSVDBObject
import os
import csv
import pickle

CSVDBTableObject = CSVDBObject.CSVDBTableObject

def test_csvdb_object_init():
    dbname = "testdb"
    folderpath = "test_folder"
    csvdb = CSVDBObject(dbname, folderpath)
    assert csvdb.dbname == dbname
    assert csvdb.folderpath == folderpath + "\\"

def test_csvdb_object_init_folder_does_not_exist():
    dbname = "testdb"
    folderpath = "test_folder"
    with pytest.raises(NotADirectoryError):
        CSVDBObject(dbname, folderpath)

def test_csvdb_object_init_db_file_exists():
    dbname = "testdb"
    folderpath = "test_folder"
    os.mkdir(folderpath)
    with open(os.path.join(folderpath, dbname + ".dat"), "wb") as f:
        pickle.dump({"dbname": dbname, "folderpath": folderpath, "tables": {}}, f)
    csvdb = CSVDBObject(dbname, folderpath)
    assert csvdb.dbname == dbname
    assert csvdb.folderpath == folderpath + "\\"
    os.rmdir(folderpath)

def test_create_table():
    dbname = "testdb"
    folderpath = "test_folder"
    csvdb = CSVDBObject(dbname, folderpath)
    table_name = "test_table"
    columns = {"col1": (str, False, False), "col2": (int, True, True)}
    table = csvdb.create_table(table_name, columns)
    assert isinstance(table, CSVDBTableObject)
    assert table.tablename == table_name
    assert table.columns == columns

def test_create_table_file_already_exists():
    dbname = "testdb"
    folderpath = "test_folder"
    csvdb = CSVDBObject(dbname, folderpath)
    table_name = "test_table"
    columns = {"col1": (str, False, False), "col2": (int, True, True)}
    with open(os.path.join(folderpath, table_name + ".csv"), "w") as f:
        csv.writer(f).writerow(["col1", "col2"])
    table = csvdb.create_table(table_name, columns)
    assert isinstance(table, CSVDBTableObject)
    assert table.tablename == table_name
    assert table.columns == columns

def test_insert_into_table():
    dbname = "testdb"
    folderpath = "test_folder"
    csvdb = CSVDBObject(dbname, folderpath)
    table_name = "test_table"
    columns = {"col1": (str, False, False), "col2": (int, True, True)}
    table = csvdb.create_table(table_name, columns)
    values = ["test", 1]
    table.insert(csvdb, values)
    with open(os.path.join(folderpath, table_name + ".csv"), "r") as f:
        reader = csv.reader(f)
        rows = list(reader)
        assert rows[1] == ["test", "1"]

def test_select_from_table():
    dbname = "testdb"
    folderpath = "test_folder"
    csvdb = CSVDBObject(dbname, folderpath)
    table_name = "test_table"
    columns = {"col1": (str, False, False), "col2": (int, True, True)}
    table = csvdb.create_table(table_name, columns)
    values = ["test", 1]
    table.insert(csvdb, values)
    result = table.select(csvdb)
    assert result == [{"col1": "test", "col2": 1}]