from .conexion import ConexionMysql

class Query:
    def __init__(self) -> None:
        self.db = ConexionMysql()
        self.db.connection()
        
    def insertarProducto(self, cantidad, descripcion, medida, precioC, PrecioV, fechaRegistro):
        query = """

                    INSERT INTO Producto(cantidad, descripcion, medida, precioCosto, precioVenta, fechaRegistro) VALUES(%s, %s, %s, %s, %s, %s)
                    
                """
        try:
            values = (cantidad, descripcion, medida, precioC, PrecioV, fechaRegistro)
            self.db.execute_query(query, values)
            
        except Exception as e:
            return e