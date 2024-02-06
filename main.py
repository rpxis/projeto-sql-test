import pymysql.cursors
from tkinter import *
from tkinter import ttk

def criarConexao() -> None:
    try:
        conexao = pymysql.connect(user='root',
                                  password='',
                                  host='localhost',
                                  database='escola')
        return conexao
    except Exception as error:
        print(f"Erro ao conectar! {error}")

def cadastrarAluno():
    try:
        nome = txt_nome.get()
        nota = float(txt_nota.get())
        turma_id = int(txt_turma.get())
        # test = categorias.index(comboCategoria.get())
        sql = "INSERT INTO aluno (nome, nota, turma_id) VALUES (%s, %s, %s)"
        conexao = criarConexao()
        cursor = conexao.cursor()
        cursor.execute(sql, (nome, nota, turma_id))
        conexao.commit()
        print(f'Dados cadastrados com sucesso!')
    except Exception as error:
        print(f'Erro ao cadastrar! Erro: {error}')

window = Tk()
window.title('Cadastro de alunos')

label_matricula = Label(window, text='Matricula:', font='Tahoma 16')
label_matricula.grid(row=0, column=0)

txt_matricula = Entry(window, font='Tahoma 16')
txt_matricula.grid(row=0, column=1)

label_nome = Label(window, text='Nome:', font='Tahoma 16')
label_nome.grid(row=1, column=0)

txt_nome = Entry(window, font='Tahoma 16')
txt_nome.grid(row=1, column=1)

label_turma = Label(window, text='Turma:', font='Tahoma 16')
label_turma.grid(row=2, column=0)

txt_turma = Entry(window, font='Tahoma 16')
txt_turma.grid(row=2, column=1)

# categorias = ['Amigos', 'Trabalho', 'Familia']
# comboCategoria = ttk.Combobox(window, values=categorias, font='Tahoma 14', width=25)
# comboCategoria.grid(row=2, column=1)


label_nota = Label(window, text='Nota:', font='Tahoma 16')
label_nota.grid(row=3, column=0)

txt_nota = Entry(window, font='Tahoma 16')
txt_nota.grid(row=3, column=1)

btn_cadastrar = Button(window, text='Cadastrar', font='Tahoma 16', fg='white', bg='blue', command=cadastrarAluno)
btn_cadastrar.grid(row=4, column=0)
window.mainloop()
