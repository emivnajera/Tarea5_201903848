cadena1="_servidor1"
cadena2="3servidor"
cadena3="_u1"
cadena4="__r3"
cadena5="rfl4"
correcto = False

def automata(cadena):
    estado = 0
    for i in range(len(cadena)):
        if (estado == 0):
            if (cadena[i]=="_"):
                estado = 1
                continue
            elif(cadena[i].isalpha()):
                estado = 2
                continue
            else:
                print("Palabra Incorrecta: "+cadena)
                break
        if(estado == 1):
            if(cadena[i]=="_"):
                estado = 1
                continue
            if(cadena[i].isalpha()):
                estado = 3
                continue
            else:
                print("Palabra Incorrecta: "+cadena)
                break
        if(estado == 2):
            if(cadena[i].isalpha()):
                estado = 2
                continue
            if(cadena[i].isdigit()):
                estado = 4
                pass
            else:
                print("Palabra Incorrecta: "+cadena)
                break
        if(estado == 3):
            if(cadena[i].isdigit()):
                estado = 4
                pass
            else:
                print("Palabra Incorrecta: "+cadena)
                break
        if(estado == 4):
            print("Palabra Correcta: "+cadena)
            break

automata(cadena1)
automata(cadena2)
automata(cadena3)
automata(cadena4)
automata(cadena5)