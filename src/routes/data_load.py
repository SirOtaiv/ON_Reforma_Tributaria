import flet as ft
import pandas as pd
import asyncio

class DataLoadView(ft.View):
   def __init__(self, prod_df: pd.DataFrame = None):
      super().__init__(
         route="/data_load",
         padding=30,
         controls=[
            ft.Row(
               controls=[
                  ft.Button(
                     content="FECHAR",
                     icon=ft.Icons.CANCEL,
                     style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                     on_click=lambda: asyncio.create_task(
                        self.page.push_route("/")
                     ),
                  ),
                  ft.Row(
                     controls=[
                        ft.Button(
                           content="RECALCULAR",
                           icon=ft.Icons.CALCULATE,
                           style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                        ),
                        ft.Button(
                           content="EXPORTAR",
                           icon=ft.Icons.DOWNLOAD,
                           style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                        ),
                     ],        
                  )
               ],
               alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            )
         ]
      
      )