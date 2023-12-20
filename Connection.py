from sqlalchemy import create_engine
import textwrap
import Data


class Connection:

    def __init__(self, database, host, port, username, password, databaseName):
        self.database = database
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.databaseName = databaseName

    def engine(self):
        url = Data.sql[self.database][
                  "urlPrefix"] + "://" + self.username + ":" + self.password + "@" + self.host + ":" + self.port + "/" + self.databaseName
        engine = create_engine(url)
        engine.connect().close()
        return engine
