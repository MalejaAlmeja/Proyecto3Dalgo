# Integrantes:
# Daniela González: 202320856
# Sofía Arias: 202310260
# María Alejandra Carrillo: 202321854

import sys
import random
from pyeasyga import pyeasyga

#constantes globales
TAMANO = 1000
LONG = 4
longitud_minima = TAMANO * LONG

# Subcadenas
FRAGMENTOS = [
    'much', 'ucho', 'hosa', 'osañ', 'años', 'osde', 'desp', 'espu', 'spué', 'pués',
    'ésfr', 'sfre', 'fren', 'rent', 'ente', 'ntea', 'teal', 'ealp', 'alpe', 'lelo',
    'elot', 'otón', 'tond', 'ondef', 'defu', 'fusi', 'usil', 'sila', 'ilam', 'lami',
    'amie', 'mien', 'ient', 'ntoe', 'toel', 'elco', 'lcor', 'coro', 'oron', 'rone',
    'onel', 'nela', 'elau', 'aure', 'urel', 'elia', 'lian', 'iano', 'anob', 'nobu',
    'buend', 'endí', 'ndía', 'díah', 'íaha', 'habí', 'abía', 'biad', 'iade', 'ader',
    'dere', 'ecor', 'cord', 'orda', 'rdar', 'dara', 'raqu', 'aque', 'uell', 'ella',
    'llat', 'tard', 'arde', 'derem', 'remo', 'mota', 'taen', 'aenq', 'enqu', 'nque',
    'ques', 'esup', 'supa', 'upad', 'padre', 'drel', 'relo', 'elol', 'loll', 'lleva',
    'evóa', 'voac', 'oaco', 'cono', 'onoc', 'noce', 'ocer', 'cerel', 'erel', 'elhi',
    'hiel','ielo',
    'much', 'ucho', 'hosa', 'osañ', 'años', 'osde', 'desp', 'espu', 'spué', 'pués',
    'ésfr', 'sfre', 'fren', 'rent', 'ente', 'ntea', 'teal', 'ealp', 'alpe', 'lelo',
    'elot', 'otón', 'tond', 'ondef', 'defu', 'fusi', 'usil', 'sila', 'ilam', 'lami',
    'amie', 'mien', 'ient', 'ntoe', 'toel', 'elco', 'lcor', 'coro', 'oron', 'rone',
    'onel', 'nela', 'elau', 'aure', 'urel', 'elia', 'lian', 'iano', 'anob', 'nobu',
    'buend', 'endí', 'ndía', 'díah', 'íaha', 'habí', 'abía', 'biad', 'iade', 'ader',
    'dere', 'ecor', 'cord', 'orda', 'rdar', 'dara', 'raqu', 'aque', 'uell', 'ella',
    'llat', 'tard', 'arde', 'derem', 'remo', 'mota', 'taen', 'aenq', 'enqu', 'nque',
    'ques', 'esup', 'supa', 'upad', 'padre', 'drel', 'relo', 'elol', 'loll', 'lleva',
    'evóa', 'voac', 'oaco', 'cono', 'onoc', 'noce', 'ocer', 'cerel', 'erel', 'elhi',
    'hiel','ielo',
    'much', 'ucho', 'hosa', 'osañ', 'años', 'osde', 'desp', 'espu', 'spué', 'pués',
    'ésfr', 'sfre', 'fren', 'rent', 'ente', 'ntea', 'teal', 'ealp', 'alpe', 'lelo',
    'elot', 'otón', 'tond', 'ondef', 'defu', 'fusi', 'usil', 'sila', 'ilam', 'lami',
    'amie', 'mien', 'ient', 'ntoe', 'toel', 'elco', 'lcor', 'coro', 'oron', 'rone',
    'onel', 'nela', 'elau', 'aure', 'urel', 'elia', 'lian', 'iano', 'anob', 'nobu',
    'buend', 'endí', 'ndía', 'díah', 'íaha', 'habí', 'abía', 'biad', 'iade', 'ader',
    'dere', 'ecor', 'cord', 'orda', 'rdar', 'dara', 'raqu', 'aque', 'uell', 'ella',
    'llat', 'tard', 'arde', 'derem', 'remo', 'mota', 'taen', 'aenq', 'enqu', 'nque',
    'ques', 'esup', 'supa', 'upad', 'padre', 'drel', 'relo', 'elol', 'loll', 'lleva',
    'evóa', 'voac', 'oaco', 'cono', 'onoc', 'noce', 'ocer', 'cerel', 'erel', 'elhi',
    'hiel','ielo',
    'much', 'ucho', 'hosa', 'osañ', 'años', 'osde', 'desp', 'espu', 'spué', 'pués',
    'ésfr', 'sfre', 'fren', 'rent', 'ente', 'ntea', 'teal', 'ealp', 'alpe', 'lelo',
    'elot', 'otón', 'tond', 'ondef', 'defu', 'fusi', 'usil', 'sila', 'ilam', 'lami',
    'amie', 'mien', 'ient', 'ntoe', 'toel', 'elco', 'lcor', 'coro', 'oron', 'rone',
    'onel', 'nela', 'elau', 'aure', 'urel', 'elia', 'lian', 'iano', 'anob', 'nobu',
    'buend', 'endí', 'ndía', 'díah', 'íaha', 'habí', 'abía', 'biad', 'iade', 'ader',
    'dere', 'ecor', 'cord', 'orda', 'rdar', 'dara', 'raqu', 'aque', 'uell', 'ella',
    'llat', 'tard', 'arde', 'derem', 'remo', 'mota', 'taen', 'aenq', 'enqu', 'nque',
    'ques', 'esup', 'supa', 'upad', 'padre', 'drel', 'relo', 'elol', 'loll', 'lleva',
    'evóa', 'voac', 'oaco', 'cono', 'onoc', 'noce', 'ocer', 'cerel', 'erel', 'elhi',
    'hiel','ielo',
    'much', 'ucho', 'hosa', 'osañ', 'años', 'osde', 'desp', 'espu', 'spué', 'pués',
    'ésfr', 'sfre', 'fren', 'rent', 'ente', 'ntea', 'teal', 'ealp', 'alpe', 'lelo',
    'elot', 'otón', 'tond', 'ondef', 'defu', 'fusi', 'usil', 'sila', 'ilam', 'lami',
    'amie', 'mien', 'ient', 'ntoe', 'toel', 'elco', 'lcor', 'coro', 'oron', 'rone',
    'onel', 'nela', 'elau', 'aure', 'urel', 'elia', 'lian', 'iano', 'anob', 'nobu',
    'buend', 'endí', 'ndía', 'díah', 'íaha', 'habí', 'abía', 'biad', 'iade', 'ader',
    'dere', 'ecor', 'cord', 'orda', 'rdar', 'dara', 'raqu', 'aque', 'uell', 'ella',
    'llat', 'tard', 'arde', 'derem', 'remo', 'mota', 'taen', 'aenq', 'enqu', 'nque',
    'ques', 'esup', 'supa', 'upad', 'padre', 'drel', 'relo', 'elol', 'loll', 'lleva',
    'evóa', 'voac', 'oaco', 'cono', 'onoc', 'noce', 'ocer', 'cerel', 'erel', 'elhi',
    'hiel','ielo',
    'much', 'ucho', 'hosa', 'osañ', 'años', 'osde', 'desp', 'espu', 'spué', 'pués',
    'ésfr', 'sfre', 'fren', 'rent', 'ente', 'ntea', 'teal', 'ealp', 'alpe', 'lelo',
    'elot', 'otón', 'tond', 'ondef', 'defu', 'fusi', 'usil', 'sila', 'ilam', 'lami',
    'amie', 'mien', 'ient', 'ntoe', 'toel', 'elco', 'lcor', 'coro', 'oron', 'rone',
    'onel', 'nela', 'elau', 'aure', 'urel', 'elia', 'lian', 'iano', 'anob', 'nobu',
    'buend', 'endí', 'ndía', 'díah', 'íaha', 'habí', 'abía', 'biad', 'iade', 'ader',
    'dere', 'ecor', 'cord', 'orda', 'rdar', 'dara', 'raqu', 'aque', 'uell', 'ella',
    'llat', 'tard', 'arde', 'derem', 'remo', 'mota', 'taen', 'aenq', 'enqu', 'nque',
    'ques', 'esup', 'supa', 'upad', 'padre', 'drel', 'relo', 'elol', 'loll', 'lleva',
    'evóa', 'voac', 'oaco', 'cono', 'onoc', 'noce', 'ocer', 'cerel', 'erel', 'elhi',
    'hiel','ielo',
    'much', 'ucho', 'hosa', 'osañ', 'años', 'osde', 'desp', 'espu', 'spué', 'pués',
    'ésfr', 'sfre', 'fren', 'rent', 'ente', 'ntea', 'teal', 'ealp', 'alpe', 'lelo',
    'elot', 'otón', 'tond', 'ondef', 'defu', 'fusi', 'usil', 'sila', 'ilam', 'lami',
    'amie', 'mien', 'ient', 'ntoe', 'toel', 'elco', 'lcor', 'coro', 'oron', 'rone',
    'onel', 'nela', 'elau', 'aure', 'urel', 'elia', 'lian', 'iano', 'anob', 'nobu',
    'buend', 'endí', 'ndía', 'díah', 'íaha', 'habí', 'abía', 'biad', 'iade', 'ader',
    'dere', 'ecor', 'cord', 'orda', 'rdar', 'dara', 'raqu', 'aque', 'uell', 'ella',
    'llat', 'tard', 'arde', 'derem', 'remo', 'mota', 'taen', 'aenq', 'enqu', 'nque',
    'ques', 'esup', 'supa', 'upad', 'padre', 'drel', 'relo', 'elol', 'loll', 'lleva',
    'evóa', 'voac', 'oaco', 'cono', 'onoc', 'noce', 'ocer', 'cerel', 'erel', 'elhi',
    'hiel','ielo',
    'much', 'ucho', 'hosa', 'osañ', 'años', 'osde', 'desp', 'espu', 'spué', 'pués',
    'ésfr', 'sfre', 'fren', 'rent', 'ente', 'ntea', 'teal', 'ealp', 'alpe', 'lelo',
    'elot', 'otón', 'tond', 'ondef', 'defu', 'fusi', 'usil', 'sila', 'ilam', 'lami',
    'amie', 'mien', 'ient', 'ntoe', 'toel', 'elco', 'lcor', 'coro', 'oron', 'rone',
    'onel', 'nela', 'elau', 'aure', 'urel', 'elia', 'lian', 'iano', 'anob', 'nobu',
    'buend', 'endí', 'ndía', 'díah', 'íaha', 'habí', 'abía', 'biad', 'iade', 'ader',
    'dere', 'ecor', 'cord', 'orda', 'rdar', 'dara', 'raqu', 'aque', 'uell', 'ella',
    'llat', 'tard', 'arde', 'derem', 'remo', 'mota', 'taen', 'aenq', 'enqu', 'nque',
    'ques', 'esup', 'supa', 'upad', 'padre', 'drel', 'relo', 'elol', 'loll', 'lleva',
    'evóa', 'voac', 'oaco', 'cono', 'onoc', 'noce', 'ocer', 'cerel', 'erel', 'elhi',
    'hiel','ielo',
    'much', 'ucho', 'hosa', 'osañ', 'años', 'osde', 'desp', 'espu', 'spué', 'pués',
    'ésfr', 'sfre', 'fren', 'rent', 'ente', 'ntea', 'teal', 'ealp', 'alpe', 'lelo',
    'elot', 'otón', 'tond', 'ondef', 'defu', 'fusi', 'usil', 'sila', 'ilam', 'lami',
    'amie', 'mien', 'ient', 'ntoe', 'toel', 'elco', 'lcor', 'coro', 'oron', 'rone',
    'onel', 'nela', 'elau', 'aure', 'urel', 'elia', 'lian', 'iano', 'anob', 'nobu',
    'buend', 'endí', 'ndía', 'díah', 'íaha', 'habí', 'abía', 'biad', 'iade', 'ader',
    'dere', 'ecor', 'cord', 'orda', 'rdar', 'dara', 'raqu', 'aque', 'uell', 'ella',
    'llat', 'tard', 'arde', 'derem', 'remo', 'mota', 'taen', 'aenq', 'enqu', 'nque',
    'ques', 'esup', 'supa', 'upad', 'padre', 'drel', 'relo', 'elol', 'loll', 'lleva',
    'evóa', 'voac', 'oaco', 'cono', 'onoc', 'noce', 'ocer', 'cerel', 'erel', 'elhi',
    'hiel','ielo',
    'much', 'ucho', 'hosa', 'osañ', 'años', 'osde', 'desp', 'espu', 'spué', 'pués',
    'ésfr', 'sfre', 'fren', 'rent', 'ente', 'ntea', 'teal', 'ealp', 'alpe', 'lelo',
    'elot', 'otón', 'tond', 'ondef', 'defu', 'fusi', 'usil', 'sila', 'ilam', 'lami',
    'amie', 'mien', 'ient', 'ntoe', 'toel', 'elco', 'lcor', 'coro', 'oron', 'rone',
    'onel', 'nela', 'elau', 'aure', 'urel', 'elia', 'lian', 'iano', 'anob', 'nobu',
    'buend', 'endí', 'ndía', 'díah', 'íaha', 'habí', 'abía', 'biad', 'iade', 'ader',
    'dere', 'ecor', 'cord', 'orda', 'rdar', 'dara', 'raqu', 'aque', 'uell', 'ella',
    'llat', 'tard', 'arde', 'derem', 'remo', 'mota', 'taen', 'aenq', 'enqu', 'nque',
    'ques', 'esup', 'supa', 'upad', 'padre', 'drel', 'relo', 'elol', 'loll', 'lleva',
    'evóa', 'voac', 'oaco', 'cono', 'onoc', 'noce', 'ocer', 'cerel', 'erel', 'elhi',
    'hiel','ielo',
]

# control greedy
generados_greedy = 0
MAXIMO_GREEDY = 25

def reconstruccion_optima(n: int, k: int, bloques: list):
    minFit=900
    minVec=[]
    
    for i in range(0,51):
        vec=generar_greedy()
        fit=evaluar(vec, "")
        if minFit>fit:
            minFit=fit
            minVec=vec
        
    print(minFit)
    reconstruida=""
    
    for idx in range(1, TAMANO):
        actual = FRAGMENTOS[minVec[idx] - 1]
        anterior = reconstruida[-LONG:]
        solape = 0
        for i in range(LONG, 0, -1):
            if anterior[-i:] == actual[:i]:
                solape = i
                break
        reconstruida += actual[solape:]
    
    print(reconstruida)


def evaluar(cromosoma, _):
    reconstruida = FRAGMENTOS[cromosoma[0] - 1]
            
    for idx in range(1, TAMANO):
        actual = FRAGMENTOS[cromosoma[idx] - 1]
        anterior = reconstruida[-LONG:]
        solape = 0
        for i in range(LONG, 0, -1):
            if anterior[-i:] == actual[:i]:
                solape = i
                break
        reconstruida += actual[solape:]

    return len(reconstruida) 

def generar_greedy():
    added={}
    first=random.randint(0, TAMANO-1)
    added[first]=0
    secuencia=[first+1]

    while len(secuencia)<TAMANO: 
        ultimo = FRAGMENTOS[secuencia[-1] - 1]
        maxOverlap=-1
        maxIdx=-1
        
        for i in range(0, TAMANO-1):
            if i not in added:
                overlap=calcular_solape(ultimo, FRAGMENTOS[i])
                if maxOverlap<overlap:
                    maxOverlap=overlap
                    maxIdx=i
                       
        secuencia.append(maxIdx+1)
        added[maxIdx]=0
        
    return secuencia

def calcular_solape(a, b):
    for i in range(LONG, 0, -1):
        if a[-i:] == b[:i]:
            return i
    return 0

'''
linea = sys.stdin.readline().strip()
ncasos = int(linea)
for _ in range(ncasos):
    subcadenas = []
    dicc_subcadenas={}
    linea = sys.stdin.readline().strip()
    n, k = map(int, linea.split())
    for _ in range(n):
        subcadena = sys.stdin.readline().strip()
        if subcadena not in dicc_subcademnas:
            subcadenas.append(subcadena)
            dicc_subcadenas[subcadena]=0
            
    SUBCADENAS = subcadenas
    NUMERO = len(subcadenas)
    LONGITUD = k
    rta = texto_minimo_reconstruible(int(n), int(k), subcadenas)
    print(rta[0])
'''
# 
respuesta = reconstruccion_optima(TAMANO, LONG, FRAGMENTOS)

"""
orden_final = respuesta[0]
texto = FRAGMENTOS[orden_final[0] - 1]

for idx in range(1, TAMANO):
    anterior = texto[-LONG:]
    actual = FRAGMENTOS[orden_final[idx] - 1]
    anadir = actual
    for i in range(LONG, 0, -1):
        if anterior[-i:] == actual[:i]:
            anadir = actual[i:]
            break
    texto += anadir

print("Orden Final:", orden_final)
print("Fitness Final:", respuesta[1])
print("Texto Reconstruido:", texto)
print("Longitud Total:", len(texto))
"""