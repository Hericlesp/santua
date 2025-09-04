# # import tkinter as tk
# # from tkinter import ttk

# # # Janela principal
# # root = tk.Tk()
# # root.title("Exemplo Combobox")
# # root.geometry("300x200")

# # # Criar o Combobox
# # combobox = ttk.Combobox(root, width=20, font=("Arial", 12))
# # combobox.pack(pady=20)

# # # Definir os valores do Combobox
# # combobox['values'] = ["Opção 1", "Opção 2", "Opção 3", "Opção 4"]

# # # Definir um valor padrão (opcional)
# # combobox.set("Selecione uma opção")

# # # Iniciar o loop da interface
# # root.mainloop()

# import tkinter as tk

# # Janela principal
# root = tk.Tk()
# root.title("Centralizar no Grid")
# root.geometry("400x300")

# # Configurar o peso das colunas e linhas
# root.grid_columnconfigure(0, weight=1)  # Coluna 0 se expande
# root.grid_columnconfigure(1, weight=1)  # Coluna 1 se expande
# root.grid_rowconfigure(0, weight=1)     # Linha 0 se expande
# root.grid_rowconfigure(1, weight=1)     # Linha 1 se expande

# # Widget centralizado
# label = tk.Label(root, text="Centralizado", font=("Arial", 16, "bold"), bg="lightblue")
# label.grid(row=0, column=0, columnspan=2, rowspan=2, sticky="nsew")  # Centraliza no grid

# # Iniciar o loop da interface
# root.mainloop()

import tkinter as tk
from tkinter import ttk

class Home:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Gestão")
        self.master.geometry("980x600")

        self.create_widgets()

    def create_widgets(self):
        # ===== FRAME PRINCIPAL =====
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)

        # Sidebar (menu lateral)
        sidebar = tk.Frame(self.master, width=200, bg="#000658")
        sidebar.grid(row=0, column=0, sticky="ns")
        sidebar.grid_propagate(False)  # trava o tamanho fixo

        # Área principal
        main_area = tk.Frame(self.master, bg="#f0f0f0")
        main_area.grid(row=0, column=1, sticky="nsew")

        # ===== ITENS DO SIDEBAR =====
        title = tk.Label(sidebar, text="MENU", bg="#000658", fg="white", font=("Arial", 16, "bold"))
        title.pack(pady=20)

        btn_dashboard = tk.Button(sidebar, text="📊 Dashboard", font=("Arial", 12, "bold"), width=20, anchor="w")
        btn_dashboard.pack(pady=5)

        btn_cadastro = tk.Button(sidebar, text="👥 Cadastro", font=("Arial", 12, "bold"), width=20, anchor="w")
        btn_cadastro.pack(pady=5)

        btn_lancamento = tk.Button(sidebar, text="📝 Lançamento", font=("Arial", 12, "bold"), width=20, anchor="w")
        btn_lancamento.pack(pady=5)

        btn_status = tk.Button(sidebar, text="📌 Status", font=("Arial", 12, "bold"), width=20, anchor="w")
        btn_status.pack(pady=5)

        btn_relatorios = tk.Button(sidebar, text="📑 Relatórios", font=("Arial", 12, "bold"), width=20, anchor="w")
        btn_relatorios.pack(pady=5)

        btn_sair = tk.Button(sidebar, text="🚪 Sair", font=("Arial", 12, "bold"), width=20, anchor="w", command=self.master.quit)
        btn_sair.pack(pady=5)

        # ===== ÁREA PRINCIPAL (CONTEÚDO) =====
        lbl_title = tk.Label(main_area, text="Bem-vindo ao Sistema de Gestão", 
                             font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#333")
        lbl_title.pack(pady=50)

        lbl_sub = tk.Label(main_area, text="Selecione uma opção no menu lateral", 
                           font=("Arial", 14), bg="#f0f0f0", fg="#555")
        lbl_sub.pack()

    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = Home(root)
    app.run()
