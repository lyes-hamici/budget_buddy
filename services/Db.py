import mysql.connector
class Db:
    """
    Class that handles the connection to the MySQL database and the execution of SQL queries.
    """
    def __init__(self):
        self.conn = self.connect_to_database()

    def connect_to_database(self):
        """
        Set up the connection to the MySQL database.
        """
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="budget"
            )
            return conn
        except mysql.connector.Error as e:
            print(f"Connection to the database error : {e}")
            return None

    def query(self, query, params=None):
        """
        Executes a SQL query with optional parameters.
        """
        results = []
        if self.conn:
            try:
                cursor = self.conn.cursor()
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                results = cursor.fetchall()
                cursor.close()
            except mysql.connector.Error as e:
                print(f"Error query execution : {e}")
        return results

    def execute(self, query, params=None):
        """
        Executes a SQL query with optional parameters.
        """
        if self.conn:
            try:
                cursor = self.conn.cursor()
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                self.conn.commit()
                cursor.close()
            except mysql.connector.Error as e:
                print(f"Error in the execution : {e}")
    

    def end_connexion(self):
        """
        Closes the connection to the database.
        """
        if self.conn:
            self.conn.close()
            print("Connection to the database closed.")
