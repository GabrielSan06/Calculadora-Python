# Biblioteca para criação da interface 
import tkinter as tk
from tkinter import messagebox

# Função para atualizar o display quando o usuário interagir
def update_display(value):
    current_text = display.get() # Pega o texto atual do display
    display.delete(0, tk.END) # Limpa a tela
    display.insert(tk.END, current_text + value) # Inserindo o novo valor
    
    
# Função para calcular o resultado
def calculate():
    try:
        result = eval(display.get()) # Calculando o resultado com a função eval
        display.delete(0, tk.END)
        display.insert(tk.END, str(result)) # Exibindo o resultado
        
    except Exception:
        messagebox.showerror("Erro", "Entrada Inválida!")
        display.delete(0, tk.END)


# Função para limpar o visor
def clear():
    display.delete(0, tk.END)


# Definindo a janela principal
root = tk.Tk()
root.title("Calculadora Simples com Python")

# Configuração do visor
display = tk.Entry(root, width=20, font=("Arial", 24), bd=10, relief="sunken", justify="right")
display.grid(row=0, column=0, columnspan=4)

# Definindo os botôes (Valor seguido da coordenada)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Adicionando os botões na interface
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=calculate)
    elif text == 'C':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=clear)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=lambda t=text: update_display(t))
    button.grid(row=row, column=col, padx=5, pady=5)
    
# Iniciar a interface gráfica
root.mainloop()