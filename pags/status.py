import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import sqlite3

class Status:
    def __init__(self, master):
        self.master = master
        # self.master.title("Relatórios de Usuários")
        # self.master.geometry("800x600")
        
        self.create_widgets()



    def create_widgets(self):
        # Frames
        up_frame = tk.Frame(self.master, height=120, bg="#145800")
        up_frame.pack(fill=tk.X)
        
        main_frame = tk.Frame(self.master)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        footer_frame = tk.Frame(self.master, height=50, bg="#145800")
        footer_frame.pack(fill=tk.X)

        # Up frame
        intro_lbl = tk.Label(up_frame, text="💾 STATUS", bg="#145800", fg="white", font=("Arial", 28, "bold"))
        intro_lbl.pack(side=tk.LEFT, pady=10)

        # Main frame - Treeview
        columns = ("id", "nome", "email", "horario_preferido", "data_nascimento")
        self.tree = ttk.Treeview(main_frame, columns=columns, show='headings')
        
        for col in columns:
            self.tree.heading(col, text=col.replace("_", " ").title())
            self.tree.column(col, anchor=tk.CENTER)
        
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Footer frame
        footer_lbl = tk.Label(footer_frame, text=" Hexa - Soluções Empresariais - ₢ Todos direitos reservados - (38) 9 9917-8063", bg="#00580C", fg="white", font=("Arial", 10))
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

    def __del__(self):
        self.conn.close()
        
    def run(self):
        self.master.mainloop()
        
if __name__ == "__main__":
    root = tk.Tk() 
    app = Status(root)
    root.mainloop()