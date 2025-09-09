import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
from datetime import datetime
import sqlite3


class Gerar_relatorios:
    def __init__(self, master):
        self.master = master
        # self.master.title("Relatórios de Usuários")
        # self.master.geometry("800x750")
        

        self.frame = tk.Frame(self.master, bg="white")
        self.frame.pack(fill="both", expand=True)
        
        self.create_widgets()
        

    def create_widgets(self):
        # Frames
        up_frame = tk.Frame(self.frame, height=120, bg="#145800")
        up_frame.pack(fill=tk.X)

        sub1_up_frame = tk.Frame(up_frame,  bg="#145800")
        sub1_up_frame.pack(fill=tk.X, pady=10)

        sub_up_frame = tk.Frame(up_frame,  bg="#f0f0f0")
        sub_up_frame.pack(fill=tk.X)
        
         
        main_frame = tk.Frame(self.frame)
        main_frame.pack(fill=tk.BOTH, expand=True)#
        
        sub_main_frame = tk.Frame(main_frame, bg="#f0f0f0")
        sub_main_frame.pack(pady=20 , anchor="center")  
 
        sub2_main_frame = tk.Frame(main_frame)
        sub2_main_frame.pack(pady=10, anchor="center")
        
        footer_frame = tk.Frame(self.frame, height=50, bg="#145800")
        footer_frame.pack(fill=tk.X)

        # Up frame
        intro_lbl = tk.Label(sub1_up_frame, text="📤 Relatórios de Usuários", bg="#145800", fg="white", font=("Arial", 28, "bold"))
        intro_lbl.grid(row=0, columnspan=4,sticky="w")

        id_func_lbl = tk.Label(sub_up_frame, text="ID do Funcionário:", bg="#f0f0f0", fg="black", font=("Arial", 12, "bold"))
        id_func_lbl.grid(row=1,column=0, pady=10)
        id_func_entry = ttk.Combobox(sub_up_frame, width=15, font=("Arial", 12, "bold"))   
        id_func_entry.grid(row=1, column=1)
        
        #db
        id_func_entry['values'] = ["Funcionario2","Funcionario3","ALL"] # Aqui você pode adicionar os IDs dos funcionários disponíveis pelo db
        id_func_entry.set("Funcionario")
        
        #periodo
        periodo_lbl = tk.Label(sub_up_frame, text="MES:", bg="#f0f0f0", fg="black", font=("Arial", 12, "bold"))
        periodo_lbl.grid(row=1,column=2, pady=10)
        periodo_cbx = ttk.Combobox(sub_up_frame, width=15, font=("Arial", 12, "bold"))   
        periodo_cbx.grid(row=1, column=3)
        
        #db
        periodo_cbx['values'] = ["mes2","mes3"] #mes de referencia
        periodo_cbx.set("Mês")
        
        
        
        
        
        
        
            
        # main frame
        label_nome = tk.Label(sub_main_frame, text="Nome:", font=("Arial", 16,"bold"))
        label_nome.pack()
        entry_nome = tk.Entry(sub_main_frame, width=40, font=("Arial", 12,"bold"))
        entry_nome.pack()
        
    

        feriados = tk.Checkbutton(sub2_main_frame, text="FERIADOS", font=("Arial", 16,"bold"))
        feriados.grid(row=0 , column=0 ,pady=5)
        
        faltas = tk.Checkbutton(sub2_main_frame, text="FALTAS", font=("Arial", 16,"bold"))
        faltas.grid(row=1 , column=0 ,pady=5)
        
        h_extra = tk.Checkbutton(sub2_main_frame, text="HORAS EXTRA", font=("Arial", 16,"bold"))
        h_extra.grid(row=0 , column=1 ,pady=5)
        
        trabalhados = tk.Checkbutton(sub2_main_frame, text="TRABALHADOS", font=("Arial", 16,"bold"))
        trabalhados.grid(row=1 , column=1 ,pady=5)
        
        
        
        #========= botão ===================
        donwload_btn = ttk.Button(main_frame, text="DONWLOAD", padding=(20,10))
        donwload_btn.pack(pady=20, anchor="center")
        
        #========= viem ===================
        # view = ttk.Treeview(main_frame, columns=("hora","detalhe","comando"))
        # view.pack(fill=tk.X, pady=20, anchor="center")
        
        
        # entry_email = tk.Entry(main_frame, width=40, font=("Arial", 12,"bold"))
        # entry_email.pack(pady=5)


        
        # label_horario = tk.Label(main_frame, text="Horário Preferido\n (HH:MM):", font=("Arial", 16,"bold"))
        # label_horario.pack(pady=5) 
        # entry_horario = tk.Entry(main_frame, width=40, font=("Arial", 12,"bold"))
        # entry_horario.pack(pady=5)

        # label_data_nascimento = tk.Label(main_frame, text="Data de Nascimento\n (DD/MM/AAAA):", font=("Arial", 16,"bold"))
        # label_data_nascimento.pack(pady=5)
        # entry_data_nascimento = tk.Entry(main_frame, width=40, font=("Arial", 12,"bold"))
        # entry_data_nascimento.pack(pady=5)

        


        # Footer frame
        footer_lbl = tk.Label(footer_frame, text=" Hexa - Soluções Empresariais - ₢ Todos direitos reservados - (38) 9 9917-8063", fg="white", bg="#145800", font=("Arial", 10))
        footer_lbl.pack(pady=10)

    def setup_database(self):
        self.conn = sqlite3.connect('usuarios.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                senha TEXT NOT NULL,
                horario_preferido TEXT,
                data_nascimento TEXT
            )
        ''')
        self.conn.commit()

    def load_data(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        self.cursor.execute("SELECT id, nome, email, horario_preferido, data_nascimento FROM usuarios")
        rows = self.cursor.fetchall()
        
        for row in rows:
            self.tree.insert("", tk.END, values=row)
            
    def run(self):
        self.master.mainloop()
        
if __name__ == "__main__":
    root = tk.Tk()
    app = Gerar_relatorios(root)
    app.run()