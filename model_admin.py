from conn import ModelUmum

class ModelKaryawan(ModelUmum):
    
    def __init__(self) -> None:
        super().__init__()

    def auth_login(self, username, password):
        cursor = self.db.cursor()
        sql_query = """SELECT password_karyawan FROM user_karyawan where username_karyawan = %s"""
        value = (username,)
        cursor.execute(sql_query, value)

        result = cursor.fetchall()

        if result == []:
            return False

        if password == result[0][0]:
            return True
        else:
            return False


