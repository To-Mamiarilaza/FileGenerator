import Data
import os
import shutil
import NameFormatter

class ControllerTemplate:
    def __init__(self, table, repository, language):
        self.table = table
        self.packageDisplay = Data.packaging[language](table.controllerPackage)
        self.className = NameFormatter.classToCamelCase(table.name.capitalize())
        self.classPackage = table.package
        self.language = language
        self.package = table.controllerPackage
        self.idType = self.idType = table.getPrimaryKeyField().type
        self.pkType = Data.type[self.table.type][self.idType][self.language]

        self.repository = repository
        if(repository == None):
            self.DBContextInjection = ""
            self.DBContextField = ""
        else:
            self.DBContextField = NameFormatter.toLowerFirstLetter(repository.className) # repository field in controller
            self.DBContextInjection = Data.dbContext[self.language][self.table.controllerType](repository.className, self.DBContextField)

        self.controllerType = table.controllerType
        self.imports = []
        self.crudMethods = []
        self.fileName = self.className + "Controller" + Data.fileExtension[self.language]
        if table.controllerName != None:
            self.fileName = self.table.controllerName + Data.fileExtension[self.language]
        self.restAnnotation = Data.restAnnotation[self.language]
        self.restMapping = Data.restMapping[self.language](self.table.controllerMapping)
        self.CORS = Data.CORS[self.language]

    def setAll(self):
        # Import all required List and the class
        self.imports.append(Data.imports[self.language](Data.typeimport[self.language]["List"]))
        self.imports.append(Data.imports[self.language](self.classPackage + "." + self.className))
        if self.repository != None:
            self.imports.append(Data.imports[self.language](self.repository.package + "." + self.repository.className))
        requiredImports = Data.controllerImports[self.table.controllerType]
        for element in requiredImports:
            self.imports.append(Data.imports[self.language](element))


        self.crudMethods.append(Data.crudMethods[self.language][self.controllerType]["all"](self.className, self.DBContextField))
        self.crudMethods.append(Data.crudMethods[self.language][self.controllerType]["id"](self.className, self.DBContextField, self.pkType))
        self.crudMethods.append(Data.crudMethods[self.language][self.controllerType]["create"](self.className, self.DBContextField))
        self.crudMethods.append(Data.crudMethods[self.language][self.controllerType]["update"](self.className, self.DBContextField, self.pkType))
        self.crudMethods.append(Data.crudMethods[self.language][self.controllerType]["delete"](self.className, self.DBContextField, self.pkType))

    def writeFile(self, finalpath):
        parentDirectory = finalpath + "/" + self.package.replace(".", "/")
        os.makedirs(parentDirectory, exist_ok=True)
        destination_file = parentDirectory + "/" + self.fileName
        if not os.path.exists(destination_file):
            source_file = "./template/controller/controller.tmp"
            shutil.copyfile(source_file, destination_file)
            with open(destination_file, 'r') as file:
                content = file.read()
            modified_content = content \
                .replace('#className#', self.className) \
                .replace('#imports#', ''.join(self.imports)) \
                .replace('#DBContext#', ''.join(self.DBContextInjection)) \
                .replace('#crudMethods#', ''.join(self.crudMethods)) \
                .replace('#package#', ''.join(self.packageDisplay)) \
                .replace('#restAnnotation#', self.restAnnotation) \
                .replace('#restMapping#', self.restMapping) \
                .replace('#CORS#', self.CORS) 
            with open(destination_file, 'w') as file:
                file.write(modified_content)