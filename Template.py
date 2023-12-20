import os

import Data
import shutil
import NameFormatter;


class Template:

    def __init__(self, language, table):
        self.table = table
        self.databaseType = table.type
        self.language = language
        self.className = NameFormatter.classToCamelCase(table.name)
        self.fileName = NameFormatter.classToCamelCase(table.name) + Data.fileExtension[self.language]
        self.imports = []
        self.attributes = []
        self.gettersAndSetters = []
        self.package = Data.packaging[self.language](table.package)

    def setAll(self):
        for column in self.table.columns:
            correspondingtype = Data.type[self.databaseType][column.type][self.language]
            attribute = Data.attributes[self.language](column.name, correspondingtype, self.table.controllerType, column.isPrimaryKey)
            correspondingimport = Data.imports[self.language](Data.typeimport[self.language][correspondingtype])
            self.attributes.append(attribute)
            self.imports.append(correspondingimport)
            getterAndSetter = Data.gettersAndSetters[self.language](NameFormatter.fieldToCamelCase(column.name), correspondingtype)
            self.gettersAndSetters.append(getterAndSetter)
            filtered_data = list(set(item for item in self.imports if item is not None))
            self.imports = filtered_data

    def writeFile(self, finalpath):
        parentDirectory = finalpath + "/" + self.table.package.replace(".", "/")
        os.makedirs(parentDirectory, exist_ok=True)
        destination_file = parentDirectory + "/" + self.fileName
        if not os.path.exists(destination_file):
            source_file = "./template/class/template.tmp"
            shutil.copyfile(source_file, destination_file)
            with open(destination_file, 'r') as file:
                content = file.read()
            modified_content = content \
                .replace('#className#', self.className) \
                .replace('#imports#', ''.join(self.imports)) \
                .replace('#attributes#', ''.join(self.attributes)) \
                .replace('#gettersAndSetters#', ''.join(self.gettersAndSetters)) \
                .replace('#package#', ''.join(self.package))
            with open(destination_file, 'w') as file:
                file.write(modified_content)

