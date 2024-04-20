class Nodo:
    def __init__(self, datos, hijos=None):
        self.datos = datos
        self.hijos = None
        self.padre = None
        self.coste = None
        self.set_hijos(hijos)
    def compara(x, y):
        return x.get_coste() - y.get_coste()
    def get_hijos(self):
        return self.hijos
    def set_hijos(self, hijos):
        self.hijos = hijos
        if self.hijos != None:
            for h in self.hijos:
                h.padre = self              
    def get_padre(self):
        return self.padre
    # Asigna al nodo padre de este nodo      
    def set_padre(self, padre):
        self.padre = padre
    # Asigna el dato almacenado en el nodo      
    def set_datos(self, datos):
        self.datos = datos
    # Devuelve el dato almacenado en el nodo         
    def get_datos(self):
        return self.datos
    # Asigna el costo del nodo dentro del árbol      
    def set_coste(self, coste):
        self.coste = coste
    # Retorna el costo       
    def get_coste(self):
        return self.coste
    # Retorna True si el dato contenido en el nodo es igual al nodo pasado como parámetro      
    def igual(self, nodo):
        if self.get_datos() == nodo.get_datos():
            return True
        else:
            return False

    def en_lista(self, lista_nodos):
        en_la_lista = False
        for n in lista_nodos:
            if self.igual(n):
                en_la_lista = True
        return en_la_lista

    def __str__(self):
        return str(self.get_datos())