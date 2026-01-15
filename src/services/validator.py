import pandas as pd

def import_csv_validator(data_frame: pd.DataFrame) -> bool:
   """
   Valida se o arquivo CSV dos produtos está de acordo e completo
   
   Args:
      data_frame: (pd.DataFrame): Data Frame panda.
      
   Returns:
      bool: True se o arquivo for válido, False caso contrário.
   """

   required_columns = ["preco_venda", "cfop", "cst_icms", "por_icms", "por_ipi", "ncm"]
   current_columns = data_frame.columns.tolist()

   missing = [c for c in required_columns if c not in current_columns]
   if missing:
      return False

   return True