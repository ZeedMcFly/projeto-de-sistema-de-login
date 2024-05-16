import customtkinter as ctk
from tkinter import *
import sqlite3
from tkinter import messagebox

ctk.set_appearance_mode("dark")

class BackEnd():
    def conecta_db(self):
        self.conn = sqlite3.connect("sistema_cadastros.db")
        self.cursor = self.conn.cursor()
        print("banco de dados criado com sucesso")


    def desconect_db(self):
        self.conn.close()
        print("banco de dados desconectado")

    def criador_de_tabela(self):
        self.conecta_db()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Usuarios(
                 Id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT NOT NULL,
                 email TEXT NOT NULL,
                 senha TEXT NOT NULL,
                 confirma_senha TEXT NOT NULL                                         
            );   
        """)
        self.conn.commit()
        print("tabela criada com sucesso!")
        self.desconect_db()   
        
    def cadastrar_usuario(self):
        self.username_cadastro = self.username_cadastro_entry.get()
        self.email_cadastro = self.email_cadastro_entry.get()
        self.senha_cadastro = self.senha_cadastro_entry.get()
        self.confirma_senha = self.confirma_senha_entry.get()

        self.conecta_db()

        self.cursor.execute("""
            INSERT INTO Usuarios (username, email, senha, confirma_senha)
            VALUES (?, ?, ?, ?)""", (self.username_cadastro, self.email_cadastro, self.senha_cadastro, self.confirma_senha))
        self.conn.commit()
        print("dados cadastrados com sucesso")
        self.desconect_db()

        try:
            if (self.username_cadastro == "" or self.email_cadastro=="" or self.senha_cadastro=="" or self.confirma_senha==""):
                   messagebox.showerror(title="sistema de login", message="ERRO!!! PREENCHA TODOS OS CAMPOS!")
            elif (len(self.username_cadastro) < 4 ):
                messagebox.showwarning(title="sistemas de login", messagebox="o nome de usuario deve ser de pelo menos 4 caracteres.")
            elif (self.senha_cadastro != self.confirma_senha):
                messagebox.showerror(title="sistema de login", message="ERRO!!! AS SENHAS NÃO CONFEREM")
            elif (len(self.senha_cadastro) < 4 ):
                 messagebox.showwarning(title="sistemas de login", message="ERRO!!! AS SENHAS DEVEM SER DE NO MINIMO 4 DIGITOS.")
            else:
                self.conn.commit()
                messagebox.showinfo(title="sistemas de login", message="parabens {self.usarname cadastro} usuario cadastrado com sucesso")
                self.desconect_db()
                self.limpa_entry_cadastro()                    
        except:
            messagebox.showerror(title="sistemas de login", message="Erro de cadastro, tente novamente!")
            self.desconect_db()

    def verifica_login(self):
        self.username_login = self.username_cadastro_entry.get()
        self.senha_login = self.senha_cadastro_entry.get()
        
        print(self.username_login, self.senha_login)





class App(ctk.CTk,):
    def __init__(self):
        
        super().__init__()
        self.configuracoes_da_janela_inicial()
        self.backend = BackEnd()
        self.tela_de_login()
        self.backend.criador_de_tabela()


    #configurando a janela principal
    def configuracoes_da_janela_inicial(self):
        self.geometry("700x400")
        self.title("sistema de login")
        self.resizable(False, False)
            

    def tela_de_login(self):

        

        self.img = PhotoImage(file="imagem_de_login.png")
        self.lb_img = ctk.CTkLabel(self, text=None, image=self.img)
        self.lb_img.grid(row=1, column=0, padx=20, pady=20)

        #titulo 
        self.title = ctk.CTkLabel(self, text="Faça seu login ou Cadastre-se", font=("Century Gothic", 16), text_color="#9370DB")
        self.title.grid(row=0, column=0, pady=10, padx=10)

        #frame 
        self.frame_login = ctk.CTkFrame(self, width=350, height=380)
        self.frame_login.place(x=350, y=10)

        #widgets
        self.lb_title = ctk.CTkLabel(self.frame_login, text="faça o seu login".upper(), font=("Century Gothic bold", 22), text_color="#9370DB")
        self.lb_title.grid(row=0, column=0, padx=10, pady=10)
        
        self.username_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="seu nome de usuario", font=("Century Gothic bold", 16), corner_radius=15, border_color="#708090")
        self.username_login_entry.grid(row=1, column=0, pady=10, padx=10)

        self.pass_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="seu nome de usuario", font=("Century Gothic bold", 16), corner_radius=15, border_color="#708090")
        self.pass_login_entry.grid(row=2, column=0, pady=10, padx=10)

        self.ver_senha = ctk.CTkCheckBox(self.frame_login, text="lembrar senha", font=("Century Gothic bold", 12), corner_radius=20)
        self.ver_senha.grid(row=3, column=0, pady=10, padx=10)

        self.btn_login = ctk.CTkButton(self.frame_login, width=300, text="Fazer Login".upper(), font=("Century Gothic bold", 16), corner_radius=15)
        self.btn_login.grid(row=4, column=0, pady=10, padx=10)

        self.span = ctk.CTkLabel(self.frame_login, text="se não tiver um login clique no botão abaixo para se registrar", font=("Century Gothic", 10))
        self.span.grid(row=5, column=0, pady=10, padx=10)

        self.btn_cadastro = ctk.CTkButton(self.frame_login, width=300, fg_color="#050", hover_color="#050", text="Fazer cadastro".upper(), font=("Century Gothic bold", 16), corner_radius=15, command=self.tela_de_cadastro)
        self.btn_cadastro.grid(row=6, column=0, pady=10, padx=10)

        #tela de cadastro
    def tela_de_cadastro(self):
        self.frame_login.place_forget()
        #frame de formulário de cadastro
        self.frame_cadastro = ctk.CTkFrame(self, width=350, height=380)
        self.frame_cadastro.place(x=350, y=10)


        self.lb_title = ctk.CTkLabel(self.frame_cadastro, text="faça o seu login".upper(), font=("Century Gothic bold", 22), text_color="#9370DB")
        self.lb_title.grid(row=0, column=0, padx=10, pady=5)

        self.username_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="seu nome de usuario", font=("Century Gothic bold", 16), corner_radius=15, border_color="#708090")
        self.username_cadastro_entry.grid(row=1, column=0, pady=5, padx=10)
        
        self.email_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Email de usuario", font=("Century Gothic bold", 16), corner_radius=15, border_color="#708090")
        self.email_cadastro_entry.grid(row=2, column=0, pady=5, padx=10)

        self.senha_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Senha de usuario", font=("Century Gothic bold", 16), corner_radius=15, border_color="#708090")
        self.senha_cadastro_entry.grid(row=3, column=0, pady=5, padx=10)

        self.confirma_senha_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Confirmar senha", font=("Century Gothic bold", 16), corner_radius=15, border_color="#708090")
        self.confirma_senha_entry.grid(row=4, column=0, pady=5, padx=10)

        self.ver_senha = ctk.CTkCheckBox(self.frame_cadastro, text="lembrar senha", font=("Century Gothic bold", 12), corner_radius=20)
        self.ver_senha.grid(row=5, column=0, pady=5, padx=10)

        self.btn_cadastrar_user = ctk.CTkButton(self.frame_cadastro, width=300, fg_color="#050", hover_color="#050", text="Fazer cadastro".upper(), font=("Century Gothic bold", 14), corner_radius=15, command=self.tela_de_cadastro)
        self.btn_cadastrar_user.grid(row=6, column=0, pady=5, padx=10)

        self.btn_login_back = ctk.CTkButton(self.frame_cadastro, width=300, text="Voltar ao Login".upper(), font=("Century Gothic bold", 14), corner_radius=15, fg_color="#444", hover_color="#333", command=self.tela_de_login)
        self.btn_login_back.grid(row=7, column=0, pady=5, padx=10)

    def limpa_entry_cadastro(self):
        self.username_cadastro_entry.delete(0, END)
        self.email_cadastro_entry.delete(0, END)
        self.senha_cadastro_entry.delete(0, END)
        self.confirma_senha_entry.delete(0, END)

    def limpa_entry_login(self):
        self.username_login_entry.delete(0, END)
        self.pass_login_entry.delete(0, END)        
        
if __name__=="__main__":
    app = App()
    app.mainloop()