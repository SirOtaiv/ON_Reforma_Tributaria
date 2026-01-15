import flet as ft
import pandas as pd

def main(page: ft.Page):
   page.title = "ON Reforma Tributária"
   page.padding = 30

   async def handle_product_import(e: ft.Event[ft.Button]):
      prod_file = await ft.FilePicker().pick_files(allow_multiple=False, file_type=ft.FilePickerFileType.CUSTOM, allowed_extensions=["csv"])
      if prod_file:
         print(prod_file[0].path)
         prod_df = pd.read_csv(prod_file[0].path, sep=";")
         print(prod_df.head())

   page.add(
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
   )

ft.run(main)