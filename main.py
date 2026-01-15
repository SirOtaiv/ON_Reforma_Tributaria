import flet as ft

def main(page: ft.Page):
   page.title = "ON Reforma Tributária"
   page.padding = 30

   page.add(
      ft.Row(
         controls=[
            ft.Button(
               content="IMPORTAR CSV",
               icon=ft.Icons.UPLOAD_FILE,
               style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
               scale=2,
               margin=ft.Margin.only(top=60)
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