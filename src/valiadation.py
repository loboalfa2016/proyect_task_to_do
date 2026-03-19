def validar_titulo(titulo):
    return len(titulo) > 0

def validar_descripcion(descripcion):
    return len(descripcion) > 0

def validar_prioridad(prioridad):
    return prioridad in ["alta", "media", "baja"]