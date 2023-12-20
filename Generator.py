import json
import os
import shutil
import sys

from Connection import Connection
from Database import Database
from Template import Template
from ControllerTemplate import ControllerTemplate
from RepositoryTemplate import RepositoryTemplate

param1 = sys.argv[1]

with open(param1, 'r') as file:
    data = json.load(file)

try:
    # Required informations
    language = data["language"]
    database = data["database"]["databaseType"]
    host = data["database"]["host"]
    port = data["database"]["port"]
    username = data["database"]["username"]
    password = data["database"]["password"]
    databaseName = data["database"]["databaseName"]
    outputDir = data["outputDir"]
    overwriteOnReScaffold = data["overwriteOnReScaffold"]
    generateAllTables = data["generateAllTables"]
    tables = None
    if not generateAllTables["value"]:
        tables = data["targetTables"]

except Exception as e:
    print(f"Le parametre {e} est introuvable dans le fichier de configuration !")
    sys.exit(1)

print("Establishing connection to the database")

d = Connection(database, host, port, username, password, databaseName)
engine = None
try:
    engine = d.engine()
except Exception as e:
    print(str(e))
    sys.exit(1)

print("Getting tables properties")

database = Database(d.databaseName, d.database, generateAllTables, tables)
database.setTables(engine)

print("Generating Files")

if overwriteOnReScaffold:
    os.makedirs(outputDir,exist_ok=True)
    for filename in os.listdir(outputDir):
        filepath = os.path.join(outputDir, filename)
        if os.path.isfile(filepath):
            os.remove(filepath)
        else:
            shutil.rmtree(filepath)

for table in database.tables:
    t = Template(language, table)
    t.setAll()
    t.writeFile(outputDir)

    # If spring, we should create a repository directory
    repository = None
    if table.controllerType == "spring" and table.repositoryPackage != False:
        repository = RepositoryTemplate(table, language)
        repository.writeFile(outputDir)


    # Generate controller if needed
    if table.generateController:
        controller = ControllerTemplate(table, repository, language)
        controller.setAll()
        controller.writeFile(outputDir)

print("Success !!!!!")

sys.exit(0)
