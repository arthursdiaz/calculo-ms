import tkinter as tk
from tkinter import messagebox
import json
import os

# Definindo o nome do arquivo JSON onde vamos salvar os dados
ARQUIVO_DADOS = "dados_ms.json"

# Função para validar a entrada de dados (só números ou vírgulas)
def validar_entrada(texto):
    return texto.replace(",", ".", 1).isdigit() or texto == ""

# Função para salvar os dados no arquivo JSON
def salvar_dados():
    # Criamos um dicionário com os dados que queremos salvar
    dados = {
        "np1": entry_np1.get(),
        "np2": entry_np2.get(),
        "pim": entry_pim.get()
    }

    # Abrimos o arquivo JSON e salvamos os dados
    with open(ARQUIVO_DADOS, "w") as f:
        json.dump(dados, f)

# Função para carregar os dados do arquivo JSON (se existir)
def carregar_dados():
    # Verificamos se o arquivo JSON já existe
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r") as f:
            dados = json.load(f)

        # Limpamos os campos antes de preencher com os dados carregados
        entry_np1.delete(0, tk.END)
        entry_np2.delete(0, tk.END)
        entry_pim.delete(0, tk.END)

        # Preenchemos os campos com os valores do arquivo JSON
        entry_np1.insert(0, dados.get("np1", ""))
        entry_np2.insert(0, dados.get("np2", ""))
        entry_pim.insert(0, dados.get("pim", ""))

# Função para criar o arquivo JSON caso ele não exista, com valores padrão
def criar_arquivo_json():
    if not os.path.exists(ARQUIVO_DADOS):
        # Caso o arquivo não exista, criamos com valores padrão
        dados_iniciais = {
            "np1": "",
            "np2": "",
            "pim": ""
        }

        with open(ARQUIVO_DADOS, "w") as f:
            json.dump(dados_iniciais, f)

# Função que calcula a média do aluno (MS) com base nos valores inseridos
def calcular_ms():
    try:
        # Pegamos os valores digitados, permitindo vírgula como separador decimal
        np1 = float(entry_np1.get().replace(",", "."))
        np2 = float(entry_np2.get().replace(",", "."))
        pim = float(entry_pim.get().replace(",", "."))

        # Calculamos a MS com a fórmula
        ms = (np1 * 4 + pim * 2 + np2 * 4) / 10
        resultado_label.config(text=f"Sua MS é: {ms:.2f}")

        # Exibimos uma mensagem de acordo com o resultado da MS
        if ms < 7.0:
            messagebox.showinfo("Resultado", f"Sua MS é {ms:.2f}. Você se aplica a MF.")
        else:
            messagebox.showinfo("Resultado", f"Sua MS é {ms:.2f}. Parabéns, você passou!")

    except ValueError:
        # Caso o usuário não insira valores válidos, mostramos um erro
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Função para resetar os campos e apagar os dados do arquivo JSON
def resetar():
    # Limpa os campos de entrada na interface
    entry_np1.delete(0, tk.END)
    entry_np2.delete(0, tk.END)
    entry_pim.delete(0, tk.END)
    resultado_label.config(text="")

    # Apaga o arquivo JSON se ele existir (resetando os dados salvos)
    if os.path.exists(ARQUIVO_DADOS):
        os.remove(ARQUIVO_DADOS)

    # Mostra uma mensagem de confirmação informando o reset
    messagebox.showinfo("Reset", "Os valores foram resetados e o arquivo JSON foi apagado!")

# Função que salva os dados sempre que o usuário digitar algo
def salvar_automaticamente(*args):
    salvar_dados()

# Criando a janela principal da aplicação
root = tk.Tk()
root.title("Calculadora de MS")
root.geometry("300x400")
root.configure(bg="#f0f0f0")

# Criando um frame para centralizar os elementos na interface
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(expand=True, padx=20, pady=10)

# Estilo comum para todos os rótulos de texto
label_style = {"bg": "#f0f0f0", "font": ("Arial", 11, "bold")}

# Validação de entrada: a função que define o que é aceito (apenas números ou vírgula)
vcmd = root.register(validar_entrada)

# Criando os campos de entrada para o usuário digitar os dados
tk.Label(frame, text="NP1:", **label_style).pack(pady=3)
entry_np1 = tk.Entry(frame, font=("Arial", 12), justify="center", validate="key", validatecommand=(vcmd, "%P"))
entry_np1.pack(ipady=5, fill="x")
entry_np1.bind("<KeyRelease>", salvar_automaticamente)  # Salva automaticamente ao digitar

tk.Label(frame, text="NP2:", **label_style).pack(pady=3)
entry_np2 = tk.Entry(frame, font=("Arial", 12), justify="center", validate="key", validatecommand=(vcmd, "%P"))
entry_np2.pack(ipady=5, fill="x")
entry_np2.bind("<KeyRelease>", salvar_automaticamente)  # Salva automaticamente ao digitar

tk.Label(frame, text="PIM:", **label_style).pack(pady=3)
entry_pim = tk.Entry(frame, font=("Arial", 12), justify="center", validate="key", validatecommand=(vcmd, "%P"))
entry_pim.pack(ipady=5, fill="x")
entry_pim.bind("<KeyRelease>", salvar_automaticamente)  # Salva automaticamente ao digitar

# Botão de Calcular MS: ao clicar, calcula a média e salva os dados
btn_calcular = tk.Button(frame, text="Calcular MS", command=calcular_ms, font=("Arial", 12, "bold"), fg="white", bg="#0066ff",
                         activebackground="#0044cc", activeforeground="white", relief="flat")
btn_calcular.pack(pady=10, ipadx=10, ipady=5, fill="x")

# Botão de Resetar: limpa os campos e apaga o arquivo JSON
btn_reset = tk.Button(frame, text="Resetar Valores", command=resetar, font=("Arial", 12, "bold"), fg="white", bg="#ff4444",
                      activebackground="#cc0000", activeforeground="white", relief="flat")
btn_reset.pack(pady=5, ipadx=10, ipady=5, fill="x")

# Rótulo onde o resultado da MS será mostrado
resultado_label = tk.Label(frame, text="", bg="#f0f0f0", font=("Arial", 12, "bold"))
resultado_label.pack(pady=5)

# Criar o arquivo JSON caso ele não exista
criar_arquivo_json()

# Carregar dados salvos no arquivo JSON quando o programa iniciar
carregar_dados()

# Inicia a interface gráfica
root.mainloop()
