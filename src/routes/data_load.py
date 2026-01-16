import flet as ft
import pandas as pd
import asyncio
import flet_datatable2 as fdt

class DataLoadView(ft.View):
   def __init__(self, page: ft.Page):
      self.prod_df: pd.DataFrame = page.session.store.get("prod_df")
      super().__init__(
         route="/data_load",
         padding=30,
      )
      self.controls=[
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
         ),
         fdt.DataTable2(
            empty=ft.Text("Produtos não carregados"),
            show_checkbox_column=True,
            columns=self.get_df_columns(),
            rows=self.get_df_rows(),
            expand=True,
            column_spacing=0,
            heading_row_color=ft.Colors.SECONDARY_CONTAINER,
            min_width=600,
            margin=ft.Margin.only(top=40),
         )
      ]
   
   def get_df_columns(self):
      data_columns = []
      calc_columns = ["cClassTrib", "CST IBS/CBS", "% IBS", "% CBS", "Preço de Venda Futuro"]
      
      if self.prod_df is not None:
         for col in self.prod_df.columns.to_list():
            data_columns.append(fdt.DataColumn2(label=ft.Text(col), fixed_width=160, heading_row_alignment=ft.MainAxisAlignment.CENTER,))
      
      for cl_col in calc_columns:
         data_columns.append(fdt.DataColumn2(label=ft.Text(cl_col), fixed_width=160, heading_row_alignment=ft.MainAxisAlignment.CENTER,))
      
      return data_columns
   
   def get_df_rows(self):
      data_rows = []
      if self.prod_df is not None:
         for index, row in self.prod_df.iterrows():
            data_cel = []
            new_cel = ["-", "-", "-", "-", "-",] #NOTE: Vai ser substituido depois pela list de valores calculados, default 5 novos valores
            for value in row:
               data_cel.append(ft.DataCell(
                  content=ft.Container(
                     content=ft.Text(str(value), text_align=ft.TextAlign.CENTER),
                     expand=True,
                     alignment=ft.Alignment.CENTER,
                  )
               ))
            for new_value in new_cel:
               data_cel.append(ft.DataCell(
                  content=ft.Container(
                     content=ft.Text(str(new_value), text_align=ft.TextAlign.CENTER),
                     expand=True,
                     alignment=ft.Alignment.CENTER,
                  )
               ))

            data_rows.append(fdt.DataRow2(cells=data_cel))
      return data_rows