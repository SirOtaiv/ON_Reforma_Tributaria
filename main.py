import flet as ft
import pandas as pd

from src.routes.data_load import DataLoadView
from src.services.validator import import_csv_validator

def main(page: ft.Page):
   page.title = "ON Reforma Tributária"
   page.padding = 30

   async def handle_product_import(e: ft.Event[ft.Button]):
      prod_file = await ft.FilePicker().pick_files(allow_multiple=False, file_type=ft.FilePickerFileType.CUSTOM, allowed_extensions=["csv"])
      if not prod_file:
         print("Importação cancelada.")
         return

      if not prod_file[0].path.lower().endswith('.csv'):
         print("Arquivo inválido. Por favor, selecione um arquivo CSV.")
         return   

      print(prod_file[0].path)
      df = pd.read_csv(prod_file[0].path, sep=";")
      if import_csv_validator(df):
         print("Arquivo CSV importado com sucesso!")
         df
         await page.push_route("/data")
         print(df.head())

   
   def handler_route_change():
      page.views.clear()
      page.views.append(
         ft.View(
            route="/",
            controls=[
               ft.Row(
                  controls=[
                     ft.Button(
                        content="IMPORTAR CSV",
                        icon=ft.Icons.UPLOAD_FILE,
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                        scale=2,
                        margin=ft.Margin.only(top=60),
                        on_click=handle_product_import,
                     ),
                  ],
                  alignment=ft.MainAxisAlignment.CENTER,
               ),
               ft.Container(
                  content=ft.Text("Sistema de apoio à ON Reforma Tributária", size=20),
                  alignment=ft.Alignment.CENTER,
                  margin=ft.Margin.only(top=40),
                  expand=True,
                  
               )
            ],
         )
      )
      if page.route == "/data":
         page.views.append(
            DataLoadView()
         )
      page.update()

   async def view_pop(e):
      if e.view is not None:
         print("View pop:", e.view)
         page.views.remove(e.view)
         top_view = page.views[-1]
         await page.push_route(top_view.route)

   page.on_route_change = handler_route_change
   page.on_view_pop = view_pop

   handler_route_change()

ft.run(main)