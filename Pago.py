class Pago:
    def __init__(self, cliente, monto, moneda, tipo_pago, fecha):
        self.cliente = cliente
        self.monto = monto
        self.moneda = moneda
        self.tipo_pago = tipo_pago
        self.fecha = fecha

    def __str__(self):
        return (f"Cliente: {self.cliente}, Monto: {self.monto} {self.moneda}, "
                f"Tipo de Pago: {self.tipo_pago}, Fecha: {self.fecha}")