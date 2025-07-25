from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import requests

app = FastAPI()

LOGIN_URL = "https://agentes.flowbets.co/api/login"
CREATE_USER_URL = "https://local-admin.flowbets.co/crear_jugador"

class UserCreateRequest(BaseModel):
    username: str
    password: str
    email: str
    phone: str

@app.post("/crear_usuario")
def crear_usuario(data: UserCreateRequest):
    # Paso 1: Login para obtener token
    login_payload = {
        "userName": "rosario",
        "password": "luciano151418"
    }

    login_headers = {
        "Content-Type": "application/json"
    }

    login_response = requests.post(LOGIN_URL, json=login_payload, headers=login_headers)

    if login_response.status_code != 200:
        raise HTTPException(status_code=500, detail="Fallo el login")

    login_json = login_response.json()
    token = login_json.get("token")
    if not token:
        raise HTTPException(status_code=500, detail="No se obtuvo token")

    # Paso 2: Crear jugador
    crear_payload = {
        "username": data.username,
        "password": data.password,
        "email": data.email,
        "phone": data.phone,
        "firstname": "-",
        "login_Id": 2017,
        "site": "86240",
        "token": token,
        "proveedores": {
            "poker": {"comision": 0, "status": True},
            "casinolive": {"comision": 0, "status": True},
            "slots": {"comision": 0, "status": True},
            "sports": {"comision": 0, "status": True}
        }
    }

    crear_headers = {
        "Content-Type": "application/json"
    }

    crear_response = requests.post(CREATE_USER_URL, json=crear_payload, headers=crear_headers)

    if crear_response.status_code != 200:
        raise HTTPException(status_code=500, detail="Error al crear el usuario")

    return {"status": "ok", "mensaje": "Usuario creado exitosamente"}
