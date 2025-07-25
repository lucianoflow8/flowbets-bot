# FlowBets Auto User Creator

Este backend permite crear usuarios automáticamente desde un frontend, haciendo login en el panel de FlowBets y usando el token para crear cuentas mediante POST.

## Rutas disponibles

- POST /crear_usuario
  Requiere: username, password, email, phone
