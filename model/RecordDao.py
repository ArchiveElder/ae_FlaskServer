from sqlalchemy import text

class RecordDao:
    def __init__(self, database):
        self.db = database

    def insert_user(self, user):
        return self.db.cursor().execute("""
            INSERT INTO record (text,user_user_id) values ("밥밥밥", 8)
            """)
