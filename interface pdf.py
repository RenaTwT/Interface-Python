import tkinter
from tkinter import filedialog,messagebox
import os
import PyPDF2

Var = "Selecione um PDF:"

def Get_text_from_PDFfiles_usingPyPDF2(in_PdfFile):  
    reader = PyPDF2.PdfReader(in_PdfFile) 
    print(reader.pages[0].extract_text())

def Arquivo():
    arquivo = filedialog.askopenfilename(
        title="Selecione um PDF:",
        filetypes=[("ArquivoPDF","*.pdf"),("Todos os arquivos","*.*")]
        
        )
    Get_text_from_PDFfiles_usingPyPDF2(arquivo)

def selecionar_pdf():

    root = tkinter.Tk()
    root.title("Seletor de PDF:")
    root.geometry("400x200")

    texto = tkinter.Label(root, text = Var)
    texto.pack()

    test1 = tkinter.Button(root, text="Selecione")
    test1['command'] = Arquivo
    
    test1.pack()

        #btn_selecionar=tk.Button(
     #   root,
     #   text="Selecionar PDF",
      #  command=selecionar_pdf,
       # font=("Arial",12),
        #bg="#4CAF50",
        #fg="white",
        #padx=20,
        #pady=10
       # )
   # btn_selecionar.pack(pady=20)
    
    label_arquivo=tkinter.Label(root,text="Nenhum arquivo selecionado",wraplength=350)
    label_arquivo.pack(pady=10)

    root.mainloop()

selecionar_pdf()
