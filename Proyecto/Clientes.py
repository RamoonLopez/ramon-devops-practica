#Clase cliente

class Usuario: 
    def __init__(self, nombre, email): 
        self.nombre = nombre
        self.email = email
                    
    def __str__(self):
        return f"Nombre: {self.nombre}, Email: {self.email}"

class Cliente(Usuario): 
    def __init__(self, nombre, direccion, telefono, email, motivo_visita ): 
        super().__init__(nombre, email )
        self.direccion = direccion
        self.telefono = telefono
        self.motivo_visita = motivo_visita

        def __str__(self):
            return f"Nombre: {self.nombre}, Direccion: {self.direccion}, Telefono: {self.telefono}, Email: {self.email}, Motivo de la visita: {self.motivo_visita}"
        

class Administrador(Usuario): 
    def __init__(self, nombre, email, contraseña): 
        super().__init__(nombre, email)
        self.contraseña = contraseña

        def __str__(self):
            return f"Nombre: {self.nombre}, Email: {self.email}, Contraseña: {self.contraseña}"
        

