class Producto:

    def __init__(self, ids, nombre, descripcion, precio, categoria, inventario,carros_compa=None) -> None:
        self.ids= ids
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.categoria = categoria
        self.inventario = inventario
        self.carros_compa = carros_compa if carros_compa is not None else [] 
    
    

    def agregarCarro(self,carro):
        self.carros_compa.append(carro)
        
    def __str__(self):
        return (f"id: {self.ids}, El producto: {self.nombre}, "
                f"Descripcion: {self.descripcion}, Precio: {self.precio}, "
                f"Categoria: {self.categoria}, Cantidad: {self.inventario}, "
                f"Carros compatibles: {', '.join(self.carros_compa)}")
    
