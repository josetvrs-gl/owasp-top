Sobre este proyecto:
Esta aplicación busca mostrar algunas vulnerabilidades del top 10 de OWASP.
Desarrollada en Flask y base de datos sqlite3

Ejecución:
* python -m venv venv
* source venv/bin/activate
* pip install -r requirements.txt
* python run.py


Al iniciar la aplicación, se crea una tabla de usuarios con la siguiente información:
[('admin', 'password123'), ('guest', 'guest123'), ('jose', 'passwd432')"]
Rutas:
* / -> Página de inicio

* /auth/login
* /auth/logout
* /auth/signup

* /users -> listado de usuarios
* /users/<id> -> Perfile de usuario

* /cards?user_id=<id> -> Listado de tarjetas de usuario

* /ping -> Ejemplo de funcionalidad no segura (ping a servidor)

Vulnerabilidades existentes:
1. Inyección SQL
2. Errores de autenticación
3. Sesiones no invalidadas
4. Inyección de comandos
5. Constraseñas no seguras y en texto plano
6. Encriptación de información sensible débil
7. Errores exponiendo información innecesaria y sensible