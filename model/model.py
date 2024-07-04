import networkx as nx


from database.DAO import DAO
class Model:
    def __init__(self):
        self._grafo=nx.Graph()
        self._dizionarioNodi={}
        self._distanzaBest=0
        self._bestSol=[]
        pass
    def getColor(self):
        return DAO.getColor()
    def creaGrafo(self,anno,colore):
        self._grafo.clear()
        self._dizionarioNodi={}
        for element in DAO.getNodi(colore):
            self._grafo.add_node(element)
            self._dizionarioNodi[element.Product_number]=element
        for element in DAO.getArchi(anno,colore):
            self._grafo.add_edge(self._dizionarioNodi[element[0]],self._dizionarioNodi[element[1]], weight=element[2])
    def numArchi(self):
        return len(self._grafo.edges())
    def numNodi(self):
        return len(self._grafo.nodes())
    def ordinaArchi(self):
        dizionario={}
        for nodo1 in self._grafo.nodes():
            for nodo2 in self._grafo.nodes():
                if nodo1 != nodo2 and self._grafo.has_edge(nodo1,nodo2) and (nodo2.Product_number,nodo1.Product_number) not in dizionario:
                    dizionario[(nodo1.Product_number,nodo2.Product_number)]=self._grafo[nodo1][nodo2]["weight"]
        dizionario_ordinato=dict(sorted(dizionario.items(), key=lambda item: item[1], reverse=True))
        lista1=[]
        for element in dizionario_ordinato:
            lista1.append(element)
        lista1=lista1[:3]
        listadainviare=[]
        lista_visti=[]
        lista_doppioni=[]
        for element in lista1:
            listadainviare.append(f"Arco da {element[0]} a {element[1]}, peso={dizionario_ordinato[element]}")
            if element[0] in lista_visti and element[0] not in lista_doppioni:
                lista_doppioni.append(element[0])
            elif element[0] not in lista_visti:
                lista_visti.append(element[0])
            if element[1] in lista_visti and element[1] not in lista_doppioni:
                lista_doppioni.append(element[1])
            elif element[1] not in lista_visti:
                lista_visti.append(element[1])
        return listadainviare,lista_doppioni
    def getNodes(self):
        lista=[]
        for element in self._grafo.nodes():
            lista.append(element.Product_number)
        return lista
    def _ricorsione(self,parziale,nodo,pesomax):
        successori=list(self._grafo.neighbors(nodo))
        for element in successori.copy():
            if ((nodo.Product_number,element.Product_number) in parziale or (element.Product_number,nodo.Product_number) in parziale) or self._grafo[nodo][element]['weight']<pesomax:
                successori.remove(element)
        if len(successori)==0:
            if len(parziale)>self._distanzaBest:
                self._bestSol=parziale
                self._distanzaBest=len(parziale)
            return
        else:
            for item in successori:
                nuovo_nodo = item
                parziale_nuovo = list(parziale)
                parziale_nuovo.append((nodo.Product_number,nuovo_nodo.Product_number))
                nuovopesomax=self._grafo[nodo][nuovo_nodo]['weight']
                self._ricorsione(parziale_nuovo,nuovo_nodo,nuovopesomax)
    def handle_ricorsione(self,nodo):
        self._distanzaBest=0
        self._bestSol=[]
        self._ricorsione([],self._dizionarioNodi[nodo],0)
        lista=[]
        for element in self._bestSol:
            lista.append(f"Arco da: {element[0]} a {element[1]}")
        return self._distanzaBest, lista


