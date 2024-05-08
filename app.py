from flask import Flask, render_template, request
import Dijkstra
import Costo_uniforme
import Hill_Clim_Ite
import annealing

app = Flask(__name__)

# Define el diccionario coord
coord = {
    'Jiloyork': (19.916012, -99.580580),
    'Toluca': (19.289165, -99.655697),
    'Atlacomulco': (19.799520, -99.873844),
    'Guadalajara': (20.677754472859146, -103.34625354877137),
    'Monterrey': (25.69161110159454, -100.321838480256),
    'QuintanaRoo': (21.163111924844458, -86.80231502121464),
    'Michohacan': (19.701400113725654, -101.20829680213464),
    'Aguascalientes': (21.87641043660486, -102.26438663286967),
    'CDMX': (19.432713075976878, -99.13318344772986),
    'QRO': (20.59719437542255, -100.38667040246602)
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejecutar_dijkstra', methods=['POST'])
def ejecutar_dijkstra():
    conexiones = {
        'EDO.MEX': {'SLP': 513, 'CDMX': 125},
        'PUEBLA': {'SLP': 514},
        'CDMX': {'MICHOACAN': 491, 'SLP': 423, 'EDO.MEX': 125},
        'MICHOACAN': {'SONORA': 346, 'SLP': 355, 'MONTERREY': 309, 'CDMX': 491},
        'SLP': {'QRO': 203, 'PUEBLA': 514, 'EDO.MEX': 513, 'SONORA': 603, 'GUADALAJARA': 437, 'CDMX': 423,
                'MICHOACAN': 355, 'MONTERREY': 313, 'HIDALGO': 599},
        'QRO': {'SLP': 203, 'HIDALGO': 390},
        'HIDALGO': {'QRO': 390, 'SLP': 599},
        'MONTERREY': {'SLP': 313, 'SONORA': 296, 'GUADALAJARA': 394, 'MICHOACAN': 309},
        'SONORA': {'MONTERREY': 296, 'SLP': 603, 'MICHOACAN': 346},
        'GUADALAJARA': {'MONTERREY': 394, 'SLP': 437}
    }
    estado_inicial = 'EDO.MEX'
    solucion = 'HIDALGO'

    nodo_solucion = Dijkstra.buscar_solucion_UCS(conexiones, estado_inicial, solucion)

    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() is not None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    resultado_str = ', '.join(resultado)

    costo_viaje = nodo_solucion.get_coste()

    return render_template('index.html', resultado_dijkstra=resultado_str, costo_viaje_dijkstra=costo_viaje)

@app.route('/ejecutar_costo_uniforme', methods=['POST'])
def ejecutar_costo_uniforme():
    conexiones = {
    '1': {'2': 3, '3': 6},
    '2': {'3':2, '4':1},
    '3': {'4': 4, '5': 2},
    '4': {'3': 4, '5': 6},
    '5': {'6': 2, '7':2},
    '6': {'7': 3},
    '7': {}
}
    estado_inicial = '1'
    nodo_destino = '7'

    previos = Costo_uniforme.dijkstra(conexiones, estado_inicial)
    camino = Costo_uniforme.reconstruir_camino(previos, nodo_destino)
    resultado_str = ', '.join(camino)

    return render_template('index.html', resultado_costo_uniforme=resultado_str)

@app.route('/ejecutar_hill_climbing', methods=['POST'])
def ejecutar_hill_climbing():
    ruta = Hill_Clim_Ite.i_hill_climbing(coord)
    resultado_str = ', '.join(ruta)
    distancia_total = Hill_Clim_Ite.evalua_ruta(ruta, coord)  # Calcula la distancia total

    return render_template('index.html', resultado_hill_climbing=resultado_str, distancia_total=distancia_total)

@app.route('/ejecutar_annealing', methods=['POST'])
def ejecutar_annealing():
    ruta = annealing.simulated_annealing(coord)
    resultado_str = ', '.join(ruta)
    distancia_total = annealing.evalua_ruta(ruta, coord)
    return render_template('index.html', resultado_annealing=resultado_str, distancia_total=distancia_total)
if __name__ == '__main__':
    app.run(debug=True)
