import tkinter as tk

import cadastro
import status

class Home:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema com Sidebar Móvel")
        self.master.geometry("980x620") 

        self.criar_widgets()

    def criar_widgets(self):
        
        self.sidebar_visible = True  # controla se sidebar está visível

        # Frame principal
        self.container = tk.Frame(self.master)
        self.container.pack(fill="both", expand=True)

        # Criar sidebar
        self.sidebar = tk.Frame(self.container, bg="#00580C")
        self.sidebar.pack(side="left", fill="y")

        # Botões dentro do sidebar
        tk.Label(self.sidebar, text="  ", bg="#00580C", fg="white", font=("Arial", 37, "bold")).pack(pady=15, padx=30)
        tk.Button(self.sidebar, text="📊 Home", command=self.abrir_home).pack(fill="x", pady=5)
        tk.Button(self.sidebar, text="👥 Cadastro", command=self.abrir_Cadastro).pack(fill="x", pady=5)
        tk.Button(self.sidebar, text="📝 Lançamento").pack(fill="x", pady=5)
        tk.Button(self.sidebar, text="🔎 Status", command=self.abrir_status).pack(fill="x", pady=5)
        tk.Button(self.sidebar, text="📑 Relatórios").pack(fill="x", pady=5)
        tk.Button(self.sidebar, text="❌ Sair", command=self.abrir_sair).pack(fill="x", pady=5)

        # Área principal
        self.main_area = tk.Frame(self.container, bg="#f0f0f0")
        self.main_area.pack(side="left", fill="both" , expand=True)

        self.abrir_home()



    def limpar_center(self):
        for widget in self.main_area.winfo_children():
            widget.destroy()

    def abrir_home(self):
        self.limpar_center()
        # Home
        self.up_frame = tk.Frame(self.main_area, bg="#00580C", height=150)
        self.up_frame.pack(fill="x")

        self.principal_frame = tk.Frame(self.main_area, bg="#DDDDDD")
        self.principal_frame.pack(fill="both",expand=True )

        self.footer_frame = tk.Frame(self.main_area, bg="#00580C")
        self.footer_frame.pack(fill="x")

        #    Botão para esconder/mostrar sidebar

        # Configurar o peso das colunas e linhas
        self.principal_frame.grid_columnconfigure(0, weight=1)  # Coluna 0 se expande
        self.principal_frame.grid_columnconfigure(1, weight=1)  # Coluna 1 se expande
        self.principal_frame.grid_rowconfigure(0, weight=1)     # Linha 0 se expande
        self.principal_frame.grid_rowconfigure(1, weight=1)     # Linha 1 se expande
        self.principal_frame.grid_rowconfigure(1, weight=1)     # Linha 0 se expande
        self.principal_frame.grid_rowconfigure(2, weight=1)     # Linha 1 se expande


        # self.toggle_btn = tk.Button(self.up_frame, text="☰", font=("Arial", 16, "bold"), command=self.toggle_sidebar)
        # self.toggle_btn.grid(row=0 ,column=0, padx=10, pady=10)

        tk.Label(self.up_frame, text="📊 DASHBOARD", bg="#00580C", fg="white", font=("Arial", 28, "bold")).grid(row=0, column=2,pady=10)

        tk.Label(self.principal_frame, text="HEXA", bg="#DDDDDD", fg="black", font=("Arial", 98, "bold")).grid(row=0, column=0, columnspan=2, rowspan=2, sticky="nsew")

        tk.Label(self.principal_frame, text="Soluções Empresariais", bg="#DDDDDD", fg="black", font=("Arial", 18)).grid(row=1, column=0, columnspan=2, rowspan=1)

        tk.Label(self.footer_frame, text="₢ Todos diresitos reservados", bg="#00580C", fg="white", font=("Arial", 12, )).pack(pady=10)




    def abrir_Cadastro(self):
        self.limpar_center()
        cadastro.Cadastro(self.main_area)

    def abrir_status(self):
        # self.limpar_center()
        status.Status(tk.Toplevel(self.main_area))

    def abrir_sair(self):
        self.master.destroy()

    def toggle_sidebar(self):
        """ Mostra ou esconde o sidebar """
        if self.sidebar_visible:
            self.sidebar.pack_forget()  # esconde
            self.sidebar_visible = False
        else:
            self.sidebar.pack(side="right", fill="y")  # mostra de novo
            self.sidebar_visible = True

    def run(self):
        self.master.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = Home(root)
    app.run()