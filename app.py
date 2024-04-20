from flask import Flask, render_template, request
import Dijkstra
import Costo_uniforme

app = Flask(__name__)

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
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    resultado_str = ', '.join(resultado)
    
    costo_viaje = nodo_solucion.get_coste()
    
    return render_template('index.html', resultado_dijkstra=resultado_str, costo_viaje_dijkstra=costo_viaje)

@app.route('/ejecutar_costo_uniforme', methods=['POST'])
def ejecutar_costo_uniforme():
    previos = Costo_uniforme.dijkstra(Costo_uniforme.grafo, Costo_uniforme.salida)
    camino = Costo_uniforme.reconstruir_camino(previos, Costo_uniforme.nodo_destino)
    resultado_str = ', '.join(camino)
    
    return render_template('index.html', resultado_costo_uniforme=resultado_str)

if __name__ == '__main__':
    app.run(debug=True)
