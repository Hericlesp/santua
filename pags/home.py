import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime


#pastas
from pags import cadastro

class Home:
    def __init__(self, master, cadastro = cadastro):
        self.master = master
        self.master.title("Cadastro de Usuário")
        self.master.geometry("980x180")
        self.cadastro = cadastro
        
        self.create_widgets()



   
    def create_widgets(self):      
       # frames
        # principal_frame = tk.Frame(self.master, bg="#D9D9D9")
        # principal_frame.pack(fill=tk.BOTH, expand=True)

        # lateral_frame = tk.Frame(self.master, width=150, bg="#000658")
        # lateral_frame.pack(side=tk.LEFT, fill=tk.Y)

        up_frame = tk.Frame(self.master, height=250, bg="#145800")
        up_frame.pack(fill=tk.X)
        
        main_frame = tk.Frame(self.master, height=300)
        main_frame.pack(fill=tk.BOTH, expand=False, anchor="center")
        
        footer_frme = tk.Frame(self.master, height=200, bg="#145800")
        footer_frme.pack(fill=tk.X)



        #Up frame
        intro_lbl = self.label_title = tk.Label(up_frame, text="GESTÃO DE HORARIO", bg="#145800", fg="white", font=("Arial", 20,"bold"))
        intro_lbl.pack(pady=20)

        # self.label_nome = tk.Label(main_frame, text="Nome:", font=("Arial", 16,"bold"))
        # self.label_nome.pack(pady=5)
        # self.entry_nome = tk.Entry(main_frame, width=40, font=("Arial", 12,"bold"))
        # self.entry_nome.pack(pady=5)

        # self.label_email = tk.Label(main_frame, text="Email:", font=("Arial", 16,"bold"))
        # self.label_email.pack(pady=5)
        # self.entry_email = tk.Entry(main_frame, width=40, font=("Arial", 12,"bold"))
        # self.entry_email.pack(pady=5)

        # self.label_senha = tk.Label(main_frame, text="Senha:", font=("Arial", 16,"bold"))
        # self.label_senha.pack(pady=5)
        # self.entry_senha = tk.Entry(main_frame, show="*", width=40, font=("Arial", 12,"bold"))
        # self.entry_senha.pack(pady=5)
        
        # self.label_horario = tk.Label(main_frame, text="Horário Preferido\n (HH:MM):", font=("Arial", 16,"bold"))
        # self.label_horario.pack(pady=5) 
        # self.entry_horario = tk.Entry(main_frame, width=40, font=("Arial", 12,"bold"))
        # self.entry_horario.pack(pady=5)

        # self.label_data_nascimento = tk.Label(main_frame, text="Data de Nascimento\n (DD/MM/AAAA):", font=("Arial", 16,"bold"))
        # self.label_data_nascimento.pack(pady=5)
        # self.entry_data_nascimento = tk.Entry(main_frame, width=40, font=("Arial", 12,"bold"))
        # self.entry_data_nascimento.pack(pady=5)

        self.button_cadastrar = tk.Button(main_frame, text="CADASTRO", font=("Arial", 16,"bold"), width=13, height=1, command=lambda: self.cadastro(tk.Toplevel(self.master)).run())
        self.button_cadastrar.grid(row=0 , column=0, padx=5, pady=5)

        self.button_cadastrar = tk.Button(main_frame, text="LANÇAMENTO", font=("Arial", 16,"bold"), width=13, height=1)
        self.button_cadastrar.grid(row=0 , column=1, padx=5, pady=5)

        self.button_cadastrar = tk.Button(main_frame, text="STATUS", font=("Arial", 16,"bold"), width=13, height=1)
        self.button_cadastrar.grid(row=0 , column=2, padx=5, pady=5)

        self.button_cadastrar = tk.Button(main_frame, text="RELATORIOS", font=("Arial", 16,"bold"), width=13, height=1)
        self.button_cadastrar.grid(row=0 , column=3, padx=5, pady=5)

        self.button_cadastrar = tk.Button(main_frame, text="SAIR", font=("Arial", 16,"bold"), width=13, height=1)
        self.button_cadastrar.grid(row=0 , column=4, padx=5, pady=5)
        
        #footer frame
        footer = tk.Label(footer_frme, text=("Hexa"), fg="white", bg="#145800",font=("Arial", 12,"bold"))
        footer.pack()
        footer_donw = tk.Label(footer_frme, text="Soluções Empresariais",fg="white", bg="#145800",font=("Arial", 10))
        footer_donw.pack()
        celular = tk.Label(footer_frme, text="(38)99917-8063",fg="white", bg="#145800",font=("Arial", 10))
        celular.pack()
        

    def run(self):
        self.master.mainloop()
        
if __name__ == "__main__":
    root = tk.Tk()
    app = Home(root)
    app.run()
    