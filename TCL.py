# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 20:18:19 2019

@author: Pablo Quintana
"""

import numpy as np


class TeoremaCentraldelLimite():
    
    def __init__(self,tamñoMuestra,variables):
        
        self.mediaW = []
        self.varianzaW = []
        self.sumaW = []
        self.sumaW2 = []
        self.sumaWraiz = []
        self.W = []
        self.n = tamñoMuestra
        self.k = variables 
        
        
    def variable(self,n,k = 1):
        # n es el tamaño muestral
        # k son la cantidad de variables
        cant = range(n)
        W = []
        for j in cant:
            wi = np.random.randn(k)
            W.append(wi)
        W = np.matrix(W)
        self.W.append(W)
        self.mediaW.append(np.mean(W, axis = 0))
        self.varianzaW.append(np.var(W, axis = 0))
        self.sumaW.append(np.sum(W, axis = 0))
        #self.sumaW2.append(np.sum(W**2, axis= 0))
        self.sumaWraiz.append(np.sum(W,axis = 0)/np.sqrt(n))
        
    def iteraW(self,n= 1000):
        
        self.itera = n
        for i in range(n):
            self.variable(self.n,self.k)
        
        self.mediaW = np.array(self.mediaW).reshape(n,self.k)
        self.varianzaW = np.array(self.varianzaW).reshape(n,self.k)
        self.sumaW = np.array(self.sumaW).reshape(n,self.k)
        self.sumaWraiz =np.array(self.sumaWraiz).reshape(n,self.k)
        
        self.media_real = np.mean(self.sumaWraiz, axis = 0)
        self.var_real = np.var(self.sumaWraiz, axis = 0)

    def elige_muestra(self, numero = False):
        
        if numero == False:
            i = int(np.round(np.random.rand()*self.itera))
        else:
            i = int(numero)
             
        media_asint = np.mean(self.W[i],axis = 0)
        var_asint = self.W[i].T*self.W[i]/self.n
        
        return media_asint,var_asint
    def graf(self):
        
        import matplotlib.pyplot as plt
        import seaborn as sns
        for i in range(self.k):
            n,bins,patches = plt.hist(self.sumaWraiz[:,i],bins = 'auto', range = (-3,3), density = False)
            plt.show()
