import tkinter as tk

def main():
    janela_principal = tk.Tk()
    janela_principal.title("Janela Principal")

    nova_janela = tk.Toplevel(janela_principal)
    nova_janela.title("Nova Janela")

    botao = tk.Button(janela_principal, text="Abrir Nova Janela", command=nova_janela.deiconify)
    botao.pack()

    janela_principal.mainloop()

if __name__ == "__main__":
    main()
