# import tkinter as tk
# from tkinter import ttk

# # Janela principal
# root = tk.Tk()
# root.title("Exemplo Combobox")
# root.geometry("300x200")

# # Criar o Combobox
# combobox = ttk.Combobox(root, width=20, font=("Arial", 12))
# combobox.pack(pady=20)

# # Definir os valores do Combobox
# combobox['values'] = ["Opção 1", "Opção 2", "Opção 3", "Opção 4"]

# # Definir um valor padrão (opcional)
# combobox.set("Selecione uma opção")

# # Iniciar o loop da interface
# root.mainloop()

import tkinter as tk

# Janela principal
root = tk.Tk()
root.title("Centralizar no Grid")
root.geometry("400x300")

# Configurar o peso das colunas e linhas
root.grid_columnconfigure(0, weight=1)  # Coluna 0 se expande
root.grid_columnconfigure(1, weight=1)  # Coluna 1 se expande
root.grid_rowconfigure(0, weight=1)     # Linha 0 se expande
root.grid_rowconfigure(1, weight=1)     # Linha 1 se expande

# Widget centralizado
label = tk.Label(root, text="Centralizado", font=("Arial", 16, "bold"), bg="lightblue")
label.grid(row=0, column=0, columnspan=2, rowspan=2, sticky="nsew")  # Centraliza no grid

# Iniciar o loop da interface
root.mainloop()