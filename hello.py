#!python 3.11.3

"""Hello World Multi Linguas

Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente.

Usage:
"""
__version__ = "0.0.1"
__author__  = "Wesley Sousa"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "pt_BR")[:5]
print(current_language)

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"


print(msg)
