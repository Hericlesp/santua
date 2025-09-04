import tkinter as tk

class Home:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema com Sidebar Móvel")
        self.master.geometry("980x600")

        self.sidebar_visible = True  # controla se sidebar está visível

        # Frame principal
        self.container = tk.Frame(self.master)
        self.container.pack(fill="both", expand=True)

        # Criar sidebar
        self.sidebar = tk.Frame(self.container, width=200, bg="#000658")
        # self.sidebar.pack(side="left", fill="y")

        # Botões dentro do sidebar
        tk.Label(self.sidebar, text="MENU", bg="#000658", fg="white", font=("Arial", 16, "bold")).pack(pady=20)
        tk.Button(self.sidebar, text="📊 Dashboard").pack(fill="x", pady=5)
        tk.Button(self.sidebar, text="👥 Cadastro").pack(fill="x", pady=5)
        tk.Button(self.sidebar, text="📝 Lançamento").pack(fill="x", pady=5)
        tk.Button(self.sidebar, text="📑 Relatórios").pack(fill="x", pady=5)

        # Área principal
        self.main_area = tk.Frame(self.container, bg="#f0f0f0")
        self.main_area.pack(side="left", fill="both", expand=True)

        # Botão para esconder/mostrar sidebar
        self.toggle_btn = tk.Button(self.main_area, text="☰", font=("Arial", 16, "bold"), command=self.toggle_sidebar)
        self.toggle_btn.pack(anchor="nw", padx=10, pady=10)

        tk.Label(self.main_area, text="Área Principal", bg="#f0f0f0", font=("Arial", 20, "bold")).pack(pady=50)

    def toggle_sidebar(self):
        """ Mostra ou esconde o sidebar """
        if self.sidebar_visible:
            self.sidebar.pack_forget()  # esconde
            self.sidebar_visible = False
        else:
            self.sidebar.pack(side="left", fill="y")  # mostra de novo
            self.sidebar_visible = True

    def run(self):
        self.master.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = Home(root)
    app.run()
