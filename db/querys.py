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
        
    def seleccionarProducto(self, texto):
        query = """
        
                    SELECT idProducto, descripcion, medida, precioVenta FROM Producto WHERE descripcion LIKE CONCAT('%', %s, '%') LIMIT 10
        
                """
        try:
            result = self.db.execute_query(query, (texto,))
            self.db.close_connection()
            return result
        except Exception as e:
            return e