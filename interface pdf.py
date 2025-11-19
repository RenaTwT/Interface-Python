import tkinter
from tkinter.filedialog import askopenfilename 
import PyPDF2
import requests
from datetime import datetime, date
import re

def ChamadaAPI(Ano):
    url = "https://date.nager.at/api/v3/PublicHolidays/"+Ano+"/BR"

    payload = {}
    headers = {
    'accept': 'application/json',
    'X-CSRF-TOKEN': 'pYBqfz7tfH5NFeqA2YXNhdZIsqRCMmef6FjOTNJz'
    }

    response = requests.request("GET", url, headers=headers, data=payload)


    return response.text

def Get_text_from_PDFfiles_usingPyPDF2(in_PdfFile):  
    reader = PyPDF2.PdfReader(in_PdfFile) 
    return reader.pages[0].extract_text()
    #print(response.text)

#def Arquivo():
 #   arquivo = filedialog.askopenfilename(
  #      title="Selecione um PDF:",
   #     filetypes=[("ArquivoPDF","*.pdf"),("Todos os arquivos","*.*")]
        
    #    )
    #Get_text_from_PDFfiles_usingPyPDF2(arquivo)

def LerPDF():
    filename = askopenfilename()
    ConteudoPDF = Get_text_from_PDFfiles_usingPyPDF2(filename)
    ListaDeAnos = set(re.findall(r"\d{4}(?=-\d{2})",ConteudoPDF))

    ListaFeriados = ""
    for Ano in ListaDeAnos:
        ListaFeriados = ListaFeriados+ ChamadaAPI(Ano)

    for Data in ConteudoPDF.split("\n"):
        if Data.strip() in ListaFeriados:
            print(Data)


def selecionar_pdf():

    root = tkinter.Tk()
    root.title("Seletor de PDF:")
    root.geometry("400x200")

    texto = tkinter.Label(root, text = "teste")
    texto.pack()

    test1 = tkinter.Button(root, text="Selecione")
    test1['command'] = LerPDF
    
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


