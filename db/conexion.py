import mysql.connector

class ConexionMysql:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = '123'
        self.data_base = 'libreria'
        self.conexion = None
        self.cursor = None
    
    def connection(self):
        try:
            self.conexion = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.data_base,
                charset='utf8mb4',  # Establecer el charset
                collation='utf8mb4_general_ci' 
            )
            self.cursor = self.conexion.cursor()
            print(f"Conectado a {self.data_base}")
        except mysql.connector.Error as error:
            print(f"Error al conectar a la base de datos: {error}")
            self.conexion = None  # Para asegurar que la conexión se detecte como fallida
    
    
    def execute_query(self, query, values=None):
        if not self.conexion or not self.cursor:
            print("No hay conexión a la base de datos.", self.conexion, self.cursor)
            return None
        
        try:
            if values:
                self.cursor.execute(query, values)
            else:
                self.cursor.execute(query)
            
            result = self.cursor.fetchall()
            self.conexion.commit()
            return result
        except mysql.connector.Error as e:
            print(f"Error en la consulta: {e}")
            return None
    
    def close_connection(self):
        try:
            if self.cursor is not None:
                self.cursor.close()
                print("conexion cerrada")
        except Exception as e:
            print('error', e)
            
        try:
            if self.conexion is not None and self.conexion.is_connected():
                self.conexion.close()
                print(f"{self.conexion} sea cerrado")
                
        except Exception as e:
            print('error', e)