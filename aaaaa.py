import os
import sys
from time import sleep
import subprocess

## --------------------------------------------
## ---                AVISO                 ---
## --------------------------------------------
## ESTE PROGRAMA PUEDE QUE ESTÉ PROGRAMADO DE
## UNA FORMA MUY INEFICIENTE, PERO YO QUE SÉ,
## NO SOY NI CIENTÍFICO NI PROGRAMADOR.



# SETUP MATRICULA
# EDITAR SEGUN EJEMPLO: 1234-BJZ
matri_num = int(1234)
matri_ltr_1 = "B"
matri_ltr_2 = "J"
matri_ltr_3 = "Z"

# DECLARACION DE VARIABLES
# - - - ¡¡NO TOCAR!! - - -
matri_info = "test"
matri_temp = "0386GWT"
cont_sin = 0
cont_zro = 0
cont_eco = 0
cont_c = 0
cont_b = 0
cont_nul = 0
url_p1 = "https://sede.dgt.gob.es/es/vehiculos/distintivo-ambiental/?accion=1&matriculahd=&matricula="
url_p2 = "&submit=Consultar"
matri_back = "0000ZZZ"
# Diccionario LETRAS >> NÚMEROS de uso interno.
ltr_dict = {'B': 1, 'C': 2, 'D': 3, 'F': 4, 'G': 5, 'H': 6, 'J': 7, 'K': 8, 'L': 9, 'M': 10, 'N': 11, 'P': 12, 'R': 13,
            'S': 14, 'T': 15, 'V': 16, 'W': 17, 'X': 18, 'Y': 19, 'Z': 20, 'A':21}

# Diccionario NUMEROS de uso interno >> LETRAS
ltr_inv_dict = {1: 'B', 2: 'C', 3: 'D', 4: 'F', 5: 'G', 6: 'H', 7: 'J', 8: 'K', 9: 'L', 10: 'M', 11: 'N', 12: 'P',
                13: 'R', 14: 'S', 15: 'T', 16: 'V', 17: 'W', 18: 'X', 19: 'Y', 20: 'Z', 21:"A"}

# ALMACENAR LETRAS CONVERTIDAS A NUMEROS
matri_ltr_1_n = int(ltr_dict[matri_ltr_1])
matri_ltr_2_n = int(ltr_dict[matri_ltr_2])
matri_ltr_3_n = int(ltr_dict[matri_ltr_3])


# Ejecutar en bucle HASTA EL INFINITO Y MÁS ALLÁ!!!
while True:
    # Esto se hace para que el programa termine con un EXCEPT e imprima resultados en pantalla.
    try:
        # Convertir la parte numérica de la matrícula a STRING y rellenar ceros, ejemplo 0001.
        matri_num_st = str(matri_num).zfill(4)

        # Sumar una unidad al número INTEGER de la matrícula.
        matri_num = matri_num + 1

        # Si matrícula es 0000-9999, ignorar. Si supera 9999, poner números a 0000 y avanzar letra.
        if matri_num >= 10000:
            matri_num = 0
            matri_ltr_3_n = matri_ltr_3_n + 1

        # Convertir (OTRA VEZ, a saber) la parte numérica de la matrícula a STRING y rellenar ceros, ejemplo 0001.
        matri_num_st = str(matri_num).zfill(4)



        # Sistema de avance de letras.
        # Si la letra de la derecha llega al fin:
        # - Resetear su conteo y avanzar la letra del medio.
        # - Comprobar si la letra central ha superado el rango de letras (20).
        #   - Si está entre 1 y 20, continuar.
        #   - Si es 21, resetear a 1 y avanzar la siguiente letra.

        if matri_ltr_3_n == 21:
            matri_ltr_3_n = 1
            matri_ltr_2_n = matri_ltr_2_n + 1

            if matri_ltr_2_n == 21:
                matri_ltr_2_n = 1
                matri_ltr_1_n = matri_ltr_1_n + 1



        # Detectar y evitar combinaciones LL y CH.
        # Valores:    CH = 2 y 6   -   L = 9

        # Si la letra izquierda es C...
        # (en realidad no es necesario pues ya se han pasado las matrículas C**, pero puede ser útil para otro posible uso)
        elif matri_ltr_1_n == 2:
            # Si la letra central es H, avanzarla.
            if matri_ltr_2_n == 6:
                matri_ltr_2_n = matri_ltr_2_n + 1


        # Si la letra central es C...
        elif matri_ltr_2_n == 2:
            # Si la letra derecha es H, avanzarla.
            if matri_ltr_3_n == 6:
                matri_ltr_3_n = matri_ltr_3_n + 1



        # Si la letra central es L...
        elif matri_ltr_2_n == 9:
            # Comprobar si la letra a la derecha es L, si es así avanzar dicha letra.
            if matri_ltr_3_n == 9:
                matri_ltr_3_n = matri_ltr_3_n + 1
            # Comprobar si la letra a la izqurda es L, si es aśi avanzar la letra del medio.
            elif matri_ltr_1_n == 9:
                matri_ltr_2_n = matri_ltr_2_n = + 1


        # Pasar valores números internos de letras individuales a STRING.
        matri_ltr_1_d = str(ltr_inv_dict[matri_ltr_1_n])
        matri_ltr_2_d = str(ltr_inv_dict[matri_ltr_2_n])
        matri_ltr_3_d = str(ltr_inv_dict[matri_ltr_3_n])

        # Generar código de matrícula.
        matri_fin = "{nr}{l1}{l2}{l3}".format(nr=matri_num_st, l1=matri_ltr_1_d, l2=matri_ltr_2_d, l3=matri_ltr_3_d)

        print("Testeando matrícula {mt}".format(mt=matri_fin))

        # Genera un comando de Terminal, que cargará el buscador de la DGT. No existe API pública.
        matri_url = "links -dump '{u1}{m}{u2}'".format(u1=url_p1,m=matri_fin,u2=url_p2)
        # Se ejecuta el comando.
        matri_bus = str(subprocess.check_output(matri_url, shell=True))

        # Comando de debug.
        #print(matri_bus)


        # Si la matrícula es X tipo, notificarlo en pantalla y agregar al contador estadístico.
        # Existe un contador de fallos para evitar falsos positivos. Si se llega a dicho límite
        # el programa se abortará. Se entenderá por "matrícula válida más reciente" la última
        # buena detectada a partir de las L** y tras un número de fallos en serie determinado.
        if 'ulo no cumple los requisitos' in matri_bus:
            print('Matrícula válida, sin etiqueta.')
            cont_sin = cont_sin + 1
            cont_nul = 0
            matri_back = matri_fin

        elif 'Azul. Pulsa' in matri_bus:
            print('Matrícula válida, con etiqueta 0.')
            cont_zro = cont_zro + 1
            cont_nul = 0
            matri_back = matri_fin

        elif 'Eco. Pulsa' in matri_bus:
            print('Matrícula válida, con etiqueta ECO.')
            cont_eco = cont_eco + 1
            cont_nul = 0
            matri_back = matri_fin

        elif 'Verde. Pulsa' in matri_bus:
            print('Matrícula válida, con etiqueta C.')
            cont_c = cont_c + 1
            cont_nul = 0
            matri_back = matri_fin

        elif 'illa. Pulsa' in matri_bus:
            print('Matrícula válida, con etiqueta B.')
            cont_b = cont_b + 1
            cont_nul = 0
            matri_back = matri_fin
        elif 'n resultado para la matr' in matri_bus:
            print('Matrícula no válida.')
            if matri_ltr_1_n >= 9:
                cont_nul = cont_nul + 1
            if cont_nul == 10:
                sys.exit("""CERRANDO PROGRAMA. --- ÚLTIMA MATRÍCULA BUENA o VÁLIDA ANALIZADA ES {mbk}
    Licencias encontradas:
    Nulo: {sin}            Ø: {zr}           ECO: {eco}
    C:    {cc}            B: {bb}""".format(mbk=matri_back, sin=cont_sin, zr=cont_zro, eco=cont_eco, cc=cont_c, bb=cont_b))
    except:
        print("""CERRANDO PROGRAMA. --- ÚLTIMA MATRÍCULA BUENA o VÁLIDA ANALIZADA ES {mbk}
            Licencias encontradas:
            Nulo: {sin}            Ø: {zr}           ECO: {eco}
            C:    {cc}            B: {bb}""".format(mbk=matri_back, sin=cont_sin, zr=cont_zro, eco=cont_eco, cc=cont_c, bb=cont_b))
        sys.exit()
