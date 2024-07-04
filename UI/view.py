import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Esame 17/07/2023- TURNO A"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.ddyear = None
        self.ddcolore = None
        self.btn_graph = None
        self.txt_result=None
        self.txt_result2=None
        self.ddprodotto=None
        self.btn_percorso= None
        self.txt_result3 = None


    def load_interface(self):
        # title
        self._title = ft.Text("Esame 17/07/2023- TURNO A", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        self.ddyear = ft.Dropdown(label="Anno")
        self.ddcolore = ft.Dropdown(label="Colore")


        # button for the "creat graph" reply
        self.btn_graph = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handle_graph)
        row1 = ft.Row([self.ddyear],
                      alignment=ft.MainAxisAlignment.CENTER)
        row2 = ft.Row([self.ddcolore,self.btn_graph],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        self._page.controls.append(row2)
        self._controller.fillDD()
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self.txt_result2 = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result2)
        self.ddprodotto = ft.Dropdown(label="Prodotto", disabled=True)
        self.btn_percorso = ft.ElevatedButton(text="Cerca Percorso", on_click=self._controller.handle_percorso, disabled=True)
        row3 = ft.Row([self.ddprodotto,self.btn_percorso],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)
        self.txt_result3 = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result3)
        self._page.update()
    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
