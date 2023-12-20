import os
import NameFormatter
import Data
import shutil

class RepositoryTemplate:
    def __init__(self, table, language):
        self.table = table
        self.language = language
        self.package = table.repositoryPackage
        self.className = NameFormatter.classToCamelCase(table.name) + "Repository"
        self.idType = table.getPrimaryKeyField().type
        self.fileName = NameFormatter.classToCamelCase(table.name) + "Repository" + Data.fileExtension[self.language]


    def writeFile(self, finalpath):
        parentDirectory = finalpath + "/" + self.package.replace(".", "/")
        os.makedirs(parentDirectory, exist_ok=True)
        destination_file = parentDirectory + "/" + self.fileName
        if not os.path.exists(destination_file):
            source_file = "./template/repository/repository.tmp"
            shutil.copyfile(source_file, destination_file)
            with open(destination_file, 'r') as file:
                content = file.read()
            modified_content = content \
                .replace('#repositoryPackage#', self.package) \
                .replace('#classPackage#', self.table.package + "." + NameFormatter.classToCamelCase(self.table.name)) \
                .replace('#className#', NameFormatter.classToCamelCase(self.table.name)) \
                .replace('#idType#', Data.type[self.table.type][self.idType][self.language])
            with open(destination_file, 'w') as file:
                file.write(modified_content)

    