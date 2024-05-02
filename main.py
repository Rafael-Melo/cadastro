import flet as ft
from useaction_table import create_table
import sqlite3
conn = sqlite3.connect("db/dbcad.db",check_same_thread = False)

def main(page:ft.Page):
    page.scroll = "auto"

    def showinput(e):
        pass


    def hidecon(e):
        pass


    name = ft.TextField(label="name")

    inputcont = ft.Card(
        elevation=30,
        content=ft.Container([
            ft.Row([
                ft.Text("add dados",size=20,weight="bold"),
                ft.IconButton(icon="Sair",icon_size=30,on_click=hidecon)
            ])
        ])
    )
    page.add(
        ft.Column([
            ft.Text("CADASTRO DE USUÁRIOS",size=30,weight="bold"),
            ft.ElevatedButton("Cadastrar", on_click=showinput)
        ])
    )


ft.app(target=main)
# ft.app(target=main, view=ft.WEB_BROWSER)