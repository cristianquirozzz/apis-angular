class Contacto:
    id = 0
    nombres = ""
    apellidos = ""
    web = ""
    profesion=""
    foto=""
    telefono=""
    correo="" 
    
    midic = dict()

    def __init__(self, p_id, p_nombre, p_apellidos, p_web, p_profesion, p_telefono, p_correo, p_foto):
        self.midic["id"] = p_id
        self.midic["nombres"] = p_nombre
        self.midic["apellidos"] = p_apellidos
        self.midic["web"] = p_web
        self.midic["profesion"] = p_profesion
        self.midic["foto"] = p_foto
        self.midic["telefono"] = p_telefono
        self.midic["email"] = p_correo
        