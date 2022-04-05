import sqlite3

class Database:
    """Class that takes care of all database interraction."""

    def __init__(self) -> None:
        self.db_file = r"hours.db"
        self.database = sqlite3.connect(self.db_file)
    
    def save_data(data) -> None:
        """Save given data"""

        pass