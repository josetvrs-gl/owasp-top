Esta aplicación busca mostrar algunas vulnerabilidades del top 10 de OWASP

Sobre la aplicación:

La aplicación esta desarrollada en flask y utiliza una base de datos sqlite.
Al iniciar la aplicación, se crea una tabla de usuarios con la siguiente información:
[('admin', 'password123'), ('guest', 'guest123'), ('jose', 'passwd432')"]
La aplicación tiene rutas para login, logout, y signup dentro de /auth
La aplicación permite ver el perfil del usuario en /users/<id> y permite al admin ver la lista de todos los usuarios en /users

Vulnerabilidades existentes:
1. SQL Injection
2. Bad Authentication
3. Missing Sessions
4. Command Injection
5. Passwords
6. Criptographic