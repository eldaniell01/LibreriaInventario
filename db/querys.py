from .conexion import ConexionMysql
import json

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
        
                    SELECT idProducto, cantidad, descripcion, medida, precioCosto, precioVenta FROM Producto WHERE descripcion LIKE CONCAT('%', %s, '%') LIMIT 10
        
                """
        try:
            result = self.db.execute_query(query, (texto,))
            self.db.close_connection()
            return result
        except Exception as e:
            return e
        finally: 
            self.db.close_connection()
    def actualizarProductos(self, cantidad, descripcion, medida, precioC, PrecioV, fechaActualizacion, id):
        query = """
        
                UPDATE Producto SET cantidad=%s, descripcion=%s, medida=%s, precioCosto=%s, precioVenta=%s, fechaActualizacion=%s WHERE idProducto=%s
        
                """
        try: 
            values = (cantidad, descripcion, medida, precioC, PrecioV, fechaActualizacion, id)  
            result = self.db.execute_query(query, values)
            self.db.close_connection()
            return result
        except Exception as e:
            return e
        finally: 
            self.db.close_connection()
            
    def insertarVenta(self, fecha, listaProducto, totalVenta):
        query = """
                
                CALL insertarVenta(%s, %s, %s)
        
                """
        try: 
            datajs = json.dumps(listaProducto)
            values= (fecha, datajs, totalVenta)
            result = self.db.execute_query(query, values)
            self.db.close_connection()
            return result
        except Exception as e:
            return e
        finally: 
            self.db.close_connection()
    
        