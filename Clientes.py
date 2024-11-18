class Clientes:
    def __init__(self,nombre,cedula,correo,direccion_envio,telefono,tipo,nombre_contacto=None,telf_contacto=None,correo_contacto=None):
        self.nombre=nombre
        self.cedula=cedula
        self.correo=correo
        self.direccion_envio=direccion_envio
        self.telefono=telefono
        self.tipo=tipo
        self.nombre_contacto=nombre_contacto
        self.telf_contacto=telf_contacto
        self.correo_contacto=correo_contacto
    
    def __str__(self):
        if self.tipo == 'J':
            return (f"Cliente Jurídico: {self.nombre}, ID: {self.cedula}, Email: {self.correo}, "
                    f"Dirección: {self.direccion_envio}, Teléfono: {self.telefono}, "
                    f"Contacto: {self.nombre_contacto}, Teléfono de contacto: {self.telf_contacto}, "
                    f"Email de contacto: {self.correo_contacto}")
        else:
            return (f"Cliente Natural: {self.nombre}, ID: {self.cedula}, Email: {self.correo}, "
                    f"Dirección: {self.direccion_envio}, Teléfono: {self.telefono}")
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "cedula": self.cedula,
            "correo": self.correo,
            "direccion_envio": self.direccion_envio,
            "telefono": self.telefono,
            "tipo": self.tipo,
            # Incluye otros atributos opcionales si existen
            "nombre_contacto": self.nombre_contacto if hasattr(self, 'nombre_contacto') else None,
            "telf_contacto": self.telf_contacto if hasattr(self, 'telf_contacto') else None,
            "correo_contacto": self.correo_contacto if hasattr(self, 'correo_contacto') else None
        }
