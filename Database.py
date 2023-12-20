from sqlalchemy import text

import Data
import re
import sys

class Column:
    def __init__(self, name, type, isPrimaryKey):
        self.name = name
        self.type = type
        if(isPrimaryKey != None and isPrimaryKey.startswith("PRI")):
            self.isPrimaryKey = True
        else :
            self.isPrimaryKey = False

class Table:
    def __init__(self, name, type, package, repository, generateController = False, controllerName = None, controllerType = None, controllerPackage = None, controllerMapping = None):
        self.name = name
        self.columns = []
        self.type = type
        self.repositoryPackage = repository
        self.package = package
        self.generateController = generateController
        self.controllerName = controllerName
        self.controllerType = controllerType
        self.controllerPackage = controllerPackage
        self.controllerMapping = controllerMapping

    def setCoulmns(self, engine):
        with engine.connect() as connection:
            execute = connection.execute(text(Data.sql[self.type]["columns"](self.name)))
            results = execute.fetchall()
        for result in results:
            self.columns.append(Column(result[0], re.sub(r'\(.*$','',result[1]), result[2]))

    def getPrimaryKeyField(self):
        for column in self.columns:
            if column.isPrimaryKey == True:
                return column
        return None


class Database:

    def __init__(self, name, type, allTables, tablesConfig = None):
        self.name = name
        self.type = type
        self.allTables = allTables
        self.tablesConfig = tablesConfig
        self.tables = []

    def setTables(self, engine):
        if self.allTables["value"]:
            try:
                with engine.connect() as connection:
                    execute = connection.execute(text(Data.sql[self.type]["tables"]))
                    results = execute.fetchall()
                for result in results:
                    table = Table(result[0], self.type, self.allTables["classPackage"], self.allTables["repositoryPackage"], self.allTables["generateController"], None, self.allTables["controllerType"], self.allTables["controllerPackage"], self.allTables["endPoint"] + "/" + result[0])
                    table.setCoulmns(engine)
                    self.tables.append(table)
            except Exception as e:
                print(f"La clé {e} n'est pas trouvé dans le fichier de configuration !")
                sys.exit(1)
        else:
            try:
                for tableConfig in self.tablesConfig:
                    table = Table(tableConfig["tableName"], self.type, tableConfig["package"], tableConfig["repositoryPackage"], tableConfig["controller"]["generate"], tableConfig["controller"]["controllerName"], tableConfig["controller"]["controllerType"], tableConfig["controller"]["controllerPackage"], tableConfig["controller"]["requestMapping"])
                    table.setCoulmns(engine)
                    self.tables.append(table)
            except Exception as e:
                print(f"La clé {e} n'est pas trouvé dans le fichier de configuration !")
                sys.exit(1)