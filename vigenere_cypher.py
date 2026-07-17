import numpy 
import string

def vigenere_coder(file, create_file=False, coder="PYTHON"):
    # Se abre el archivo
    f = open(file)

    ### Matriz para aplicar en cifrado
    abc = list(string.ascii_lowercase)
    vig_mat = [abc]

    for i in range(1, 26):
        abc = abc[1:] + abc[:1]
        vig_mat.append(abc)

    abc = list(string.ascii_lowercase)

    # Lista de caracteres normales y convertidos
    ascii_list = [ord(char) for char in f.read()]
    ascii_c_list = []

    code = list(coder.lower())
    l = 0
    count = 0

    for a in ascii_list:

        if count == 26:
            count = 0

        if l == (len(code) - 1):
            l = 0

        if chr(a).isalpha():
            pos = abc.index(code[0])

            ascii_c_list.append(vig_mat[0][pos])

        else:
            ascii_c_list.append(chr(a))

        count +=1
        l +=1

    print("".join(ascii_c_list))
            
vigenere_coder("text.txt", coder="PYTHON")

"""
- Revisar el orden en que aparecen, si es columna o fila y cómo, para poder
terminar este código. 
Ya estoy a nada de terminarlo
"""

