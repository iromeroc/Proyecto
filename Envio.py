class Envio:
    def __init__(self, venta, servicio_envio, costo_servicio, fecha, motorizado=None):
        self.venta = venta  # Esto debe ser un objeto de la clase Venta que tiene el cliente, productos, etc.
        self.servicio_envio = servicio_envio
        self.costo_servicio = costo_servicio
        self.motorizado = motorizado  # Información sobre el motorizado solo si el servicio es delivery
        self.fecha  = fecha
    def __str__(self):
        envio_info = (
            f"Orden de Compra: {self.venta}\n"
            f"Servicio de Envío: {self.servicio_envio}\n"
            f"Costo del Servicio: ${self.costo_servicio}\n"
            f"Fecha del Envio: ${self.fecha}\n"
        )
        if self.servicio_envio.lower() == "delivery":
            envio_info += f"Motorizado: {self.motorizado}\n"
        
        return envio_info
        

