import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._anno=None
        self._colore=None
        self._nodo=None
    def fillDD(self):
        for i in range(2015,2019):
            self._view.ddyear.options.append(ft.dropdown.Option(text=f"{i}", on_click=self.read_anno))
        for element in self._model.getColor():
            self._view.ddcolore.options.append(ft.dropdown.Option(text=f"{element}", on_click=self.read_colore))
        pass
    def read_anno(self,e):
        self._view.txt_result.clean()
        self._view.txt_result2.clean()
        self._view.txt_result3.clean()
        self._view.btn_percorso.disabled = True
        self._view.ddprodotto.disabled = True
        self._view.update_page()
        try:
            self._anno=int(e.control.text)
        except ValueError:
            return
    def read_nodo(self,e):
        self._view.txt_result3.clean()
        self._nodo=int(e.control.text)


    def read_colore(self,e):
        self._view.txt_result.clean()
        self._view.txt_result2.clean()
        self._view.txt_result3.clean()
        self._view.btn_percorso.disabled = True
        self._view.ddprodotto.disabled = True
        self._view.update_page()
        self._colore=e.control.text
    def handle_graph(self,e):
        self._view.txt_result.clean()
        self._view.txt_result2.clean()
        self._view.txt_result3.clean()
        if not self._anno:
            self._view.create_alert("inserisci un anno")
            return
        if not self._colore:
            self._view.create_alert("inserisci un colore")
            return
        self._model.creaGrafo(self._anno,self._colore)
        self._view.txt_result.controls.append(
            ft.Text(f"Grafo Creato \nci sono {self._model.numNodi()} vertici\nci sono: {self._model.numArchi()} archi"))
        liste=self._model.ordinaArchi()
        for element in liste[0]:
            self._view.txt_result2.controls.append(
                ft.Text(
                    f"{element}"))
        if len(liste[1])==0:
            self._view.txt_result2.controls.append(ft.Text("non ci sono nodi ripetuti"))
        else:
            self._view.txt_result2.controls.append(ft.Text(f"i nodi ripetuti sono {liste[1]}"))
        self._view.btn_percorso.disabled=False
        self._view.ddprodotto.disabled=False
        self._view.ddprodotto.clean()
        for element in self._model.getNodes():
            self._view.ddprodotto.options.append(ft.dropdown.Option(text=f"{element}", on_click=self.read_nodo))
        self._view.update_page()

    def handle_percorso(self,e):
        risultati=self._model.handle_ricorsione(self._nodo)
        self._view.txt_result3.controls.append(ft.Text(f"percorso di peso max partendo da {self._nodo}: {risultati[0]}"))
        for element in risultati[1]:
            self._view.txt_result3.controls.append(ft.Text(f"{element}"))
        self._view.update_page()