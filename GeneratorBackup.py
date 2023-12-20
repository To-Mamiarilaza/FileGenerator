import json
import os
import shutil
import sys

from Connection import Connection
from Database import Database
from Template import Template
from ControllerTemplate import ControllerTemplate

param1 = sys.argv[1]

with open(param1, 'r') as file:
    data = json.load(file)

if len(data) != 12:
    print("Error in file configuration")
    sys.exit(1)

language = data["language"]
packageName = data["package"]
database = data["database"]
host = data["host"]
port = data["port"]
username = data["username"]
password = data["password"]
databaseName = data["databaseName"]
finalPath = data["outputDir"]
overWriteOnReScaffold = data["overWriteOnReScaffold"]
createApiController = data["createApiController"]
controllerType = data["controllerType"]

if packageName.strip() == '':
    packageName = None

print("Establishing connection to the database")

d = Connection(database, host, port, username, password, databaseName)
engine = None
try:
    engine = d.engine()
except Exception as e:
    print(str(e))
    sys.exit(1)

print("Getting tables properties")

database = Database(d.databaseName, d.database)
database.setTables(engine)

print("Generating Files")

if overWriteOnReScaffold:
    for filename in os.listdir(finalPath):
        filepath = os.path.join(finalPath, filename)
        if os.path.isfile(filepath):
            os.remove(filepath)
        else:
            shutil.rmtree(filepath)

for table in database.tables:
    t = Template(language, packageName, table, database.type)
    t.setAll()
    t.writeFile(finalPath)

    if createApiController:
        controller = ControllerTemplate(packageName, t.className, t.packageName, language, controllerType)
        controller.setAll()
        controller.writeFile(finalPath)

print("Success !!!!!")

sys.exit(0)
