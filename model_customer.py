from conn import ModelUmum

class ModelPelanggan(ModelUmum):
    
    def __init__(self) -> None:
        super().__init__()
    
    def input_pelanggan(self, username_input, nama_input, telp_input, alamat_input, pass_input):
        cursor = self.db.cursor()

        sql_query = """INSERT INTO user_pelanggan VALUES (%s, %s, %s, %s, %s)"""
        values = (username_input, nama_input, telp_input, alamat_input, pass_input)
        cursor.execute(sql_query, values)

        self.db.commit()
        return True

    def get_all_data(self):
        cursor = self.db.cursor()
        sql_query = """SELECT * FROM user_pelanggan"""
        cursor.execute(sql_query)

        result = cursor.fetchall()
        result = [i[:-1] for i in result]

        return result

    def auth_login(self, username, password):
        cursor = self.db.cursor()
        sql_query = """SELECT password_pelanggan FROM user_pelanggan where username_pelanggan = %s"""
        value = (username,)
        cursor.execute(sql_query, value)

        result = cursor.fetchall()

        if result == []:
            return False

        if password == result[0][0]:
            return True
        else:
            return False
