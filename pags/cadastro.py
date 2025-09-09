# import tkinter as tk
# from tkinter import messagebox
# from tkinter import ttk
# from datetime import datetime

# class Cadastro:
#     def __init__(self, master):
#         self.master = master
#         # self.master.title("Cadastro de Usuário")
#         # self.master.geometry("800x650")
        
#         self.create_widgets()
        
   
#     def create_widgets(self):      
#        # frames
       
#         up_frame = tk.Frame(self.master, height=120, bg="#145800")
#         up_frame.pack(fill=tk.X)
        
#         main_frame = tk.Frame(self.master, height=300)
#         main_frame.pack(fill=tk.BOTH, expand=True)
        
#         footer_frme = tk.Frame(self.master, height=200, bg="#145800")
#         footer_frme.pack(fill=tk.X)

#         #Up frame
#         intro_lbl = self.label_title = tk.Label(up_frame, text="Cadastro de Usuário", bg="#145800", fg="white", font=("Arial", 20,"bold"))
#         intro_lbl.pack(pady=20)

#         self.label_nome = tk.Label(main_frame, text="Nome:", font=("Arial", 16,"bold"))
#         self.label_nome.pack(pady=5)
#         self.entry_nome = tk.Entry(main_frame, width=40, font=("Arial", 12,"bold"))
#         self.entry_nome.pack(pady=5)

#         self.label_email = tk.Label(main_frame, text="Email:", font=("Arial", 16,"bold"))
#         self.label_email.pack(pady=5)
#         self.entry_email = tk.Entry(main_frame, width=40, font=("Arial", 12,"bold"))
#         self.entry_email.pack(pady=5)

#         self.label_senha = tk.Label(main_frame, text="Senha:", font=("Arial", 16,"bold"))
#         self.label_senha.pack(pady=5)
#         self.entry_senha = tk.Entry(main_frame, show="*", width=40, font=("Arial", 12,"bold"))
#         self.entry_senha.pack(pady=5)
        
#         self.label_horario = tk.Label(main_frame, text="Horário Preferido\n (HH:MM):", font=("Arial", 16,"bold"))
#         self.label_horario.pack(pady=5) 
#         self.entry_horario = tk.Entry(main_frame, width=40, font=("Arial", 12,"bold"))
#         self.entry_horario.pack(pady=5)

#         self.label_data_nascimento = tk.Label(main_frame, text="Data de Nascimento\n (DD/MM/AAAA):", font=("Arial", 16,"bold"))
#         self.label_data_nascimento.pack(pady=5)
#         self.entry_data_nascimento = tk.Entry(main_frame, width=40, font=("Arial", 12,"bold"))
#         self.entry_data_nascimento.pack(pady=5)

#         self.button_cadastrar = tk.Button(main_frame, text="Cadastrar", font=("Arial", 16,"bold"), command=self.cadastrar)
#         self.button_cadastrar.pack(pady=20)
        
#         #footer frame
#         footer = tk.Label(footer_frme, text=("Hexa"), fg="white", bg="#145800",font=("Arial", 12,"bold"))
#         footer.pack()
#         footer_donw = tk.Label(footer_frme, text="Soluções Empresariais",fg="white", bg="#145800",font=("Arial", 10))
#         footer_donw.pack()
#         celular = tk.Label()
#         celular.pack()
        

#     def cadastrar(self):
#         nome = self.entry_nome.get()
#         email = self.entry_email.get()
#         senha = self.entry_senha.get()
#         horario = self.entry_horario.get()
#         data_nascimento_str = self.entry_data_nascimento.get()

#         if not nome or not email or not senha or not data_nascimento_str:
#             messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
#             return

#         try:
#             data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")
#             if data_nascimento >= datetime.now():
#                 raise ValueError("Data de nascimento inválida.")
#         except ValueError as e:
#             messagebox.showerror("Erro", f"Data de nascimento inválida: {e}")
#             return

#         # Aqui você pode adicionar a lógica para salvar os dados do usuário
#         messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
#         self.master.destroy()
        
#     def run(self):
#         self.master.mainloop()
        
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = Cadastro(root)
#     app.run()

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

import Home101
    
class Cadastro:
    def __init__(self, master):
        self.master = master
        
        # Frame raiz da tela de cadastro
        self.frame = tk.Frame(self.master, bg="white")
        self.frame.pack(fill="both", expand=True)
        
        self.create_widgets()
        
    def create_widgets(self):      
        # frames
        up_frame = tk.Frame(self.frame, height=120, bg="#145800")
        up_frame.pack(fill=tk.X)
        
        main_frame = tk.Frame(self.frame, bg="#F3F3F3",height=300)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        footer_frme = tk.Frame(self.frame, height=50, bg="#145800")
        footer_frme.pack(fill=tk.X)

        #Up frame


        intro_lbl = tk.Label(up_frame, text="📊 CADASTRO", bg="#00580C", fg="white", font=("Arial", 28, "bold"))
        intro_lbl.grid(row=0, column=1, pady=10)

        self.label_nome = tk.Label(main_frame, text="NOME:", font=("Arial", 16,"bold"))
        self.label_nome.pack(pady=5)
        self.entry_nome = tk.Entry(main_frame, width=40, font=("Arial", 12,"bold"))
        self.entry_nome.pack(pady=5)

        self.dateadm_lbl = tk.Label(main_frame, text="ADMISSÃO:", font=("Arial", 16,"bold"))
        self.dateadm_lbl.pack(pady=5)
        self.dateadm_ent = tk.Entry(main_frame, width=40, font=("Arial", 12,"bold"))
        self.dateadm_ent.pack(pady=5)

        self.cargo_lbl = tk.Label(main_frame, text="CARGO:", font=("Arial", 16,"bold"))
        self.cargo_lbl.pack(pady=5)
        self.cargo_ent = tk.Entry(main_frame, width=40, font=("Arial", 12,"bold"))
        self.cargo_ent.pack(pady=5)



        self.button_cadastrar = tk.Button(main_frame, text="Cadastrar", font=("Arial", 16,"bold"), command=self.cadastrar)
        self.button_cadastrar.pack(pady=20)
        
        #footer frame
        # footer = tk.Label(footer_frme, text="Hexa", fg="white", bg="#145800",font=("Arial", 10,"bold"))
        # footer.pack()
        footer_donw = tk.Label(footer_frme, text=" Hexa - Soluções Empresariais - ₢ Todos direitos reservados - (38) 9 9917-8063",fg="white", bg="#145800",font=("Arial", 10))
        footer_donw.pack(pady=10)

    def cadastrar(self):
        nome = self.entry_nome.get().upper()
        email = self.entry_email.get()
        senha = self.entry_senha.get()
        horario = self.entry_horario.get()
        data_nascimento_str = self.entry_data_nascimento.get()

        if not nome or not email or not senha or not data_nascimento_str:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
            return

        try:
            data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")
            if data_nascimento >= datetime.now():
                raise ValueError("Data de nascimento inválida.")
        except ValueError as e:
            messagebox.showerror("Erro", f"Data de nascimento inválida: {e}")
            return

        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        self.frame.destroy()  # fecha só a tela de cadastro

    def open_toggle(self):
        Home101.Home.toggle_sidebar(self)


    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = Cadastro(root)
    app.run()