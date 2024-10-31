import os
import tkinter as tk
from tkinter import PhotoImage

class Paco(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry('1366x768')
        #self.resizable(0,0)
        self.title('Paco')
        #self.iconbitmap('icono.ico')
        self.config(background='aqua')
        self.dias_semana = ['LUNES', 'MARTES', 'MIERCOLES', 'JUEVES', 'VIERNES', 'SABADO', 'DOMINGO']
        self.imagenes_ulcera = os.listdir("C:\\Aplicaciones\\Manejo_imagenes_TK_(caso_ulcera_paco)\\Paco_Ulcera\\Fotos_Ulcera")
        self.imagenes_pie_derecho_am = []
        self.imagenes_pie_derecho_pm = []
        self.imagenes_pie_izquierdo_am = []
        self.imagenes_pie_izquierdo_pm = []
        self.imagenes_am = dict()
        self.imagenes_pm = dict()
        self.filtro()
        self.creacion_componenetes()

    def creacion_componenetes(self):

        """Componentes para comparar las fotos de la ulcera tomadas por la mañana"""
        etiqueta = tk.Label(self,text='FOTOS POR LA MAÑANA').grid(row=0, column=0,columnspan=7, pady=3)
        for dia in range(len(self.dias_semana)):
            etiqueta = tk.Label(self,text=self.dias_semana[dia]).grid(row=1, column=dia, pady=3)

        for dia in range(len(self.imagenes_pie_derecho_am)):
            self.imagenes_am['imagen'+str(dia+1)] = PhotoImage(file=f'C:\\Aplicaciones\\Manejo_imagenes_TK_(caso_ulcera_paco)\\Paco_Ulcera\\Fotos_Ulcera\\{self.imagenes_pie_derecho_am[dia]}').subsample(6)
            label = tk.Label(self, image=self.imagenes_am[f'imagen{dia+1}']).grid(row=2, column=dia, padx=3, pady=3)

        """Componentes para comparar las fotos de la ulcera tomadas por la noche"""
        etiqueta = tk.Label(self, text='FOTOS POR LA NOCHE').grid(row=3, column=0, columnspan=7, pady=3)
        for dia in range(len(self.dias_semana)):
            etiqueta = tk.Label(self, text=self.dias_semana[dia]).grid(row=4, column=dia, pady=3)

        for dia in range(len(self.imagenes_pie_derecho_pm)):
            self.imagenes_pm['imagen' + str(dia + 1)] = PhotoImage(file=f'C:\\Aplicaciones\\Manejo_imagenes_TK_(caso_ulcera_paco)\\Paco_Ulcera\\Fotos_Ulcera\\{self.imagenes_pie_derecho_pm[dia]}').subsample(6)
            label = tk.Label(self, image=self.imagenes_pm[f'imagen{dia + 1}']).grid(row=5, column=dia, padx=3, pady=3)

    def filtro(self):
        for i in range(len(self.imagenes_ulcera)):
            if self.imagenes_ulcera[i].endswith("AM DER.png"):
                self.imagenes_pie_derecho_am.append(self.imagenes_ulcera[i])
            elif self.imagenes_ulcera[i].endswith("AM IZQ.png"):
                self.imagenes_pie_izquierdo_am.append(self.imagenes_ulcera[i])

            elif self.imagenes_ulcera[i].endswith("PM DER.png"):
                self.imagenes_pie_derecho_pm.append(self.imagenes_ulcera[i])

            elif self.imagenes_ulcera[i].endswith("PM IZQ.png"):
                self.imagenes_pie_izquierdo_pm.append(self.imagenes_ulcera[i])


if __name__ == '__main__':
    paco = Paco()
    paco.mainloop()
