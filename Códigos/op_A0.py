def op_A0(parametro):
    dirección = str(parámetros[0]) + str(parámetros[1])
    dirección = int(dirección, 16)
    if dirección <= 65534 and dirección >= 1025:
        memoria[dirección] = parámetros[2]
    


