from app import autenticar_usuario
import time

#Pruebas Funcionales (CP-01 a CP-07)
def test_cp01_login_exitoso():
    resultado = autenticar_usuario("admin", "1234")
    assert resultado["success"] == True
    assert resultado["message"] == "Acceso concedido"
    assert resultado["response_time_ms"] > 0

def test_cp02_usuario_vacio():
    resultado = autenticar_usuario("", "1234")
    assert resultado["success"] == False
    assert resultado["message"] == "Usuario y contraseña son requeridos"

def test_cp03_contrasena_vacia():
    resultado = autenticar_usuario("admin", "")
    assert resultado["success"] == False
    assert resultado["message"] == "Usuario y contraseña son requeridos"

def test_cp04_usuario_inexistente():
    resultado = autenticar_usuario("pedro", "1234")
    assert resultado["success"] == False
    assert resultado["message"] == "Usuario no existe"

def test_cp05_contrasena_incorrecta():
    resultado = autenticar_usuario("admin", "9999")
    assert resultado["success"] == False
    assert resultado["message"] == "Contraseña incorrecta"

def test_cp06_tiempo_respuesta_valido():
    resultado = autenticar_usuario("admin", "1234")
    assert resultado["response_time_ms"] > 0

def test_cp07_estructura_salida():
    resultado = autenticar_usuario("admin", "1234")
    assert "success" in resultado
    assert "message" in resultado
    assert "response_time_ms" in resultado

#5 Pruebas Exploratorias 
def test_exploratorio_espacios_en_blanco():
    
    #Espacios en blanco al inicio y final
    resultado = autenticar_usuario(" admin ", "1234")
    assert resultado["success"] == False
    assert resultado["message"] == "Usuario no existe"

def test_exploratorio_mayusculas_minusculas():
    #Mayúsculas y minúsculas
    resultado = autenticar_usuario("ADMIN", "1234")
    assert resultado["success"] == False
    assert resultado["message"] == "Usuario no existe"

def test_exploratorio_caracteres_especiales():
    #Caracteres especiales en el username
    resultado = autenticar_usuario("admin@#", "1234")
    assert resultado["success"] == False
    assert resultado["message"] == "Usuario no existe"

def test_exploratorio_ambos_campos_vacios():
    #Ambos campos completamente vacíos
    resultado = autenticar_usuario("", "")
    assert resultado["success"] == False
    assert resultado["message"] == "Usuario y contraseña son requeridos"

def test_exploratorio_password_con_espacios():
    #Contraseña con espacios en blanco
    resultado = autenticar_usuario("admin", " 1234 ")
    assert resultado["success"] == False
    assert resultado["message"] == "Contraseña incorrecta"

#Pruebas De Tiempo
def test_tiempo_respuesta_razonable():
    inicio = time.perf_counter()
    resultado = autenticar_usuario("admin", "1234")
    fin = time.perf_counter()
    tiempo_ms = (fin - inicio) * 1000
    assert resultado["success"] == True
    assert tiempo_ms < 500

def test_tiempo_reportado_por_sistema():
    resultado = autenticar_usuario("admin", "1234")
    assert resultado["response_time_ms"] < 500