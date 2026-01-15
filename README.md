## 🚀 Como Inicializar o Projeto

Siga os passos abaixo para configurar o ambiente de desenvolvimento em sua máquina:

1. **Clonar o repositório:**
   ```bash
   git clone <url-do-repositorio>
   cd <nome-do-diretorio>
   ```

2. **Criar o ambiente virtual:** Utilize o nome padrão `.venv` para garantir que o ambiente seja ignorado pelo Git e reconhecido automaticamente pela sua IDE.
   ```bash
   python -m venv .venv
   ```

3. **Ativar o ambiente virtual:**
   - **Windows (PowerShell):**
      ```bash
      .\.venv\Scripts\Activate
      ```

   - **Linux / macOS / Git Bash:**
      ```bash
      source .venv/bin/activate
      ```

4. **Instalar as dependências:** Com o ambiente devidamente ativado, instale os pacotes necessários:
   ```bash
   pip install -r requirements.txt
   ```

---