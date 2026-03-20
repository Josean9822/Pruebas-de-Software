from app import autenticar_usuario

# CP-01
def test_login_exitoso():
    resultado = autenticar_usuario("admin", "1234")
    assert resultado["success"] == True
    assert resultado["message"] == "Acceso concedido"

# CP-02
def test_usuario_vacio():
    resultado = autenticar_usuario("", "1234")
    assert resultado["success"] == False
    assert resultado["message"] == "Usuario y contraseña son requeridos"

# CP-03
def test_password_vacio():
    resultado = autenticar_usuario("admin", "")
    assert resultado["success"] == False
    assert resultado["message"] == "Usuario y contraseña son requeridos"

# CP-04
def test_usuario_inexistente():
    resultado = autenticar_usuario("pedro", "1234")
    assert resultado["success"] == False
    assert resultado["message"] == "Usuario no existe"

# CP-05
def test_password_incorrecto():
    resultado = autenticar_usuario("admin", "9999")
    assert resultado["success"] == False
    assert resultado["message"] == "Contraseña incorrecta"

# CP-06
def test_tiempo_respuesta():
    resultado = autenticar_usuario("admin", "1234")
    assert resultado["response_time_ms"] > 0

# CP-07
def test_estructura_salida():
    resultado = autenticar_usuario("admin", "1234")
    assert "success" in resultado
    assert "message" in resultado
    assert "response_time_ms" in resultado