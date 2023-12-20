import textwrap
import NameFormatter

sql = {
    "mysql": {
        "urlPrefix": "mysql+mysqlconnector",
        "tables": "SHOW TABLES",
        "columns": lambda tablename: f"SHOW COLUMNS FROM {tablename}"
    },
    "postgresql": {
        "urlPrefix": "postgresql",
        "tables": "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'",
        "columns": lambda
            tablename: f"""
                SELECT col.column_name, data_type, constraint_type as key FROM 
                information_schema.columns col 
                LEFT JOIN
                (
                    SELECT c.column_name, t.constraint_type
                    FROM information_schema.constraint_column_usage c 
                    LEFT JOIN information_schema.table_constraints t ON c.constraint_name = t.constraint_name 
                    WHERE constraint_type = 'PRIMARY KEY' AND c.table_name = '{tablename}'
                ) const ON col.column_name = const.column_name 
                WHERE col.table_name = '{tablename}'
            """
    }
}

type = {
    "mysql": {
        "int": {
            "java": "Integer",
            ".net": "int"
        },
        "double": {
            "java": "Double",
            ".net": "double"
        },
        "varchar": {
            "java": "String",
            ".net": "string"
        },
        "date": {
            "java": "Date",
            ".net": "DateTime"
        },
        "time": {
            "java": "Time",
            ".net": "TimeSpan"
        },
        "datetime": {
            "java": "Timestamp",
            ".net": "DateTime"
        },
        "timestamp": {
            "java": "Timestamp",
            ".net": "DateTime"
        },
        "boolean": {
            "java": "Boolean",
            ".net": "bool"
        }
    },
    "postgresql": {
        "integer": {
            "java": "Integer",
            ".net": "int"
        },
        "numeric": {
            "java": "Double",
            ".net": "double"
        },
        "double precision": {
            "java": "Double",
            ".net": "double"
        },
        "character varying": {
            "java": "String",
            ".net": "string"
        },
        "date": {
            "java": "Date",
            ".net": "DateTime"
        },
        "time without time zone": {
            "java": "Time",
            ".net": "TimeSpan"
        },
        "timestamp without time zone": {
            "java": "Timestamp",
            ".net": "DateTime"
        },
        "boolean": {
            "java": "Boolean",
            ".net": "bool"
        }
    }
}

typeimport = {
    "java": {
        "Integer": None,
        "Double": None,
        "String": None,
        "Date": "java.sql.Date",
        "Time": "java.sql.Time",
        "Timestamp": "java.sql.Timestamp",
        "Boolean": None,
        "List": "java.util.List"
    },
    ".net": {
        "int": None,
        "double": None,
        "string": None,
        "DateTime": "System",
        "TimeSpan": "System",
        "bool": None,
        "List": "System.Collections.Generic"
    }
}

packaging = {
    "java": lambda packageName: f"package {packageName};" if packageName else None,
    ".net": lambda packageName: f"namespace {packageName};" if packageName else None
}

imports = {
    "java": lambda type: f"import {type};\n" if type else None,
    ".net": lambda type: f"using {type};\n" if type else None
}

# get convenable field annotation 
def getFieldAnnotation(name, type, controller, isPrimaryKey):
    result = ""
    if controller == "spring":
        # Trying to maintain all identification
        if isPrimaryKey:
            result = result + """
                                    @Id"""
            if type == "int":
                result = result + """
                                    @GeneratedValue(strategy = GenerationType.IDENTITY)"""
        result = result + f"""
                                    @Column(name = \"{name}\")"""
    return result

attributes = {
    "java": lambda name, type, controller, isPrimaryKey:  textwrap.dedent(f"""
                                    {getFieldAnnotation(name, type, controller, isPrimaryKey)}
                                    {type} {NameFormatter.fieldToCamelCase(name)};""").replace("\n", "\n\t"),
    ".net": lambda name, type, controller, isPrimaryKey: textwrap.dedent(f"""
                                    {type} {NameFormatter.fieldToCamelCase(name)};""").replace("\n", "\n\t")
}

gettersAndSetters = {
    "java": lambda name,
                    type: textwrap.dedent(f"""
                            public {type} get{NameFormatter.capitalizeFirstLetter(name)}() {{
                                return {name};
                            }}
                            
                            public void set{NameFormatter.capitalizeFirstLetter(name)}({type} {name}) {{
                                this.{name} = {name};
                            }}
                            """).replace("\n", "\n\t"),
    ".net": lambda name,
                    type: textwrap.dedent(f"""
                            public {type} {NameFormatter.capitalizeFirstLetter(name)}{{
                                get {{ return {name}; }}
                                set {{ {name} = value; }}
                            }}
                            """).replace("\n", "\n\t")
}

fileExtension = {
    "java": ".java",
    ".net": ".cs"
}

crudMethods = {
    "java": {
        "spring": {
            "all": lambda className, repositoryField : textwrap.dedent(f"""
                @GetMapping 
                public List<{className}> getAll{className}s() {{
                    return {repositoryField}.findAll();
                }}
                """).replace("\n", "\n\t"),
            "id": lambda className, repositoryField, pkType : textwrap.dedent(f"""
                @GetMapping(\"/{{id}}\")
                public ResponseEntity<{className}> get{className}ById(@PathVariable {pkType} id) {{
                    {className} {NameFormatter.toLowerFirstLetter(className)} = {repositoryField}.findById(id).orElseThrow(() -> new Exception("{className} avec l' id " + id + " n'existe pas"));
                    return ResponseEntity.ok({NameFormatter.toLowerFirstLetter(className)});
                }}
                """).replace("\n", "\n\t"),
            "create": lambda className, repositoryField : textwrap.dedent(f"""
                @PostMapping 
                public {className} save{className}(@RequestBody {className} new{className}) {{
                    return {repositoryField}.save(new{className});
                }}
                """).replace("\n", "\n\t"),
            "update": lambda className, repositoryField, pkType : textwrap.dedent(f"""
                @PutMapping(\"/{{id}}\") 
                public {className} update{className}(@PathVariable {pkType} id, @RequestBody {className} updated{className}) {{
                    {className} {NameFormatter.toLowerFirstLetter(className)} = {repositoryField}.findById(id).orElseThrow(() -> new Exception("{className} avec l' id " + id + " n'existe pas"));
                    update{className}.setId{className}(id);
                    return udpate{className}.save(updated{className});
                }}
                """).replace("\n", "\n\t"),
            "delete": lambda className, repositoryField, pkType : textwrap.dedent(f"""
                @DeleteMapping(\"/{{id}}\") 
                public ResponseEntity<Map<String, Boolean>> delete{className}(@PathVariable {pkType} id) {{
                    {className} {NameFormatter.toLowerFirstLetter(className)} = {repositoryField}.findById(id).orElseThrow(() -> new Exception("{className} avec l' id " + id + " n'existe pas"));
                    {repositoryField}.delete({NameFormatter.toLowerFirstLetter(className)});
                    Map<String, Boolean> response = new HashMap<>();
                    response.put("deleted", Boolean.TRUE);
                    return ResponseEntity.ok(response);
                }}
                """).replace("\n", "\n\t")
        }
    },
    ".net": {
        "entity": {
            "all": lambda className, DBContextField : textwrap.dedent(f"""
                [HttpGet]
                public ActionResult<IEnumerable<{className}>> GetAll{className}s() {{
                    return null;
                }}
                """).replace("\n", "\n\t"),
            "id": lambda className, DBContextField, pkType : textwrap.dedent(f"""
                [HttpGet(\"{{id}}\")]
                public ActionResult<User> Get{className}({pkType} id) {{
                    return null;
                }}
                """).replace("\n", "\n\t"),
            "create": lambda className, DBContextField  : textwrap.dedent(f"""
                [HttpPost]
                public IActionResult Save{className}([FromBody] {className} new{className}) {{
                    // Empty method
                }}
                """).replace("\n", "\n\t"),
            "update": lambda className, DBContextField, pkType : textwrap.dedent(f"""
                [HttpPut(\"{{id}}\")]
                public IActionResult Update{className}({pkType} id, [FromBody] {className} updated{className}) {{
                    // Empty method
                }}
                """).replace("\n", "\n\t"),
            "delete": lambda className, DBContextField, pkType : textwrap.dedent(f"""
                [HttpDelete(\"{{id}}\")]
                public IActionResult Delete{className}({pkType} id) {{
                    // Empty method
                }}
                """).replace("\n", "\n\t")
        }
    }
}

dbContext = {
    "java": {
        "spring": lambda dbContextClass, dbContextField: textwrap.dedent(f"""
                @Autowired
                private {dbContextClass} {dbContextField};""").replace("\n", "\n\t")
    },
    ".net": { 
        "entity": lambda dbContextClass, dbContextField: textwrap.dedent(f"""
                private readonly {dbContextClass} {dbContextField};""").replace("\n", "\n\t")
    }
}

restAnnotation = {
    "java": "@RestController",
    ".net": "[ApiController]"
}

restMapping = {
    "java": lambda mapping: f"@RequestMapping(\"{mapping}\")",
    ".net": lambda mapping: f"[Route(\"{mapping}\")]"
}

controllerImports = {
    "spring": [
        "org.springframework.beans.factory.annotation.Autowired",
        "org.springframework.http.ResponseEntity",
        "org.springframework.web.bind.annotation.CrossOrigin",
        "org.springframework.web.bind.annotation.DeleteMapping",
        "org.springframework.web.bind.annotation.GetMapping",
        "org.springframework.web.bind.annotation.PathVariable",
        "org.springframework.web.bind.annotation.PostMapping",
        "org.springframework.web.bind.annotation.PutMapping",
        "org.springframework.web.bind.annotation.RequestBody",
        "org.springframework.web.bind.annotation.RequestMapping",
        "org.springframework.web.bind.annotation.RestController"
    ],
    "entity": []
}

CORS = {
    "java": "@CrossOrigin(origins = \"*\")",
    ".net": "[EnableCors(\"AllowSpecificOrigins\")]"
}