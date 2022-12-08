from sqlalchemy import create_engine
import pandas as pd

class SQLHelper():
    
    def __init__(self):
        self.database_path = "Resources/hawaii.sqlite"
        self.connection_str = f"sqlite:///{self.database_path}"
        self.engine = create_engine(self.connection_str)

    def executeQuery(self, query):
        df = pd.read_sql(query, self.engine)
        return(df)
    
    def getPrecipitation(self):
        query = """SELECT
                        date,
                        station,
                        prcp
                    FROM
                        measurement
                    WHERE
                        date >= '2016-08-23'
                        and prcp is not null
                    order by
                        date asc,
                        station asc;
                """
        return(self.executeQuery(query))

    def getStations(self):
        query = """
                    SELECT * FROM station order by id asc;
                """
        return(self.executeQuery(query))

    def getTempDataSinceDate(self, start):
        query = f"""SELECT
                        min(tobs) as min_tobs,
                        max(tobs) as max_tobs,
                        avg(tobs) as avg_tobs
                    FROM
                        measurement
                    WHERE
                        date >= '{start}';
                """
        return(self.executeQuery(query))

    def getTempDataForDateRange(self, start, end):
        query = f"""SELECT
                        min(tobs) as min_tobs,
                        max(tobs) as max_tobs,
                        avg(tobs) as avg_tobs
                    FROM
                        measurement
                    WHERE
                        date >= '{start}'
                        and date <= '{end}';
                """
        return(self.executeQuery(query))
