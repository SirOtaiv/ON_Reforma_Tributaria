import flet as ft
import pandas as pd

@ft.control
class DataLoad(ft.View):
   def init(self, ): #prod_df: pd.DataFrame
      # self.prod_df = prod_df

      self.route = "/data_load"

      self.content = [
         ft.Row(
            controls=[
               ft.Button(
                  content="FECHAR",
                  icon=ft.Icons.ONE_X_MOBILEDATA,
                  style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                  scale=2,
               ),
               ft.Container(
                  content=[
                     ft.Button(
                        content="RECALCULAR",
                        icon=ft.Icons.CALCULATE,
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                        scale=2,
                     ),
                     ft.Button(
                        content="EXPORTAR",
                        icon=ft.Icons.DOWNLOAD,
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                        scale=2,
                     ),
                  ]                  
               )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
         )
      ]