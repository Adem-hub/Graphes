class Graphe:
    def __init__(self,V,E,Oriente_ou_Pas):
        self.Oriente=Oriente_ou_Pas
        self.V=V
        self.E=E
        self.Matrice= 0
        self.Meth()
        self.nd= Noeud
        self.Liste=[]
        self.Voisins()

    def Meth(self):
        x=[]
        for i in range(len(self.V)):
            y=[]
            for j in range(len(self.V)):
                if self.Oriente:
                    if [self.V[i],self.V[j]] in self.E or [self.V[j],self.V[i]] in self.E:
                        y.append(1)
                    else:
                        y.append(0)
                if self.Oriente==False:
                    if [self.V[i],self.V[j]] in self.E:
                        y.append(1)
                    else:
                        y.append(0)
            x.append(y)
        self.Matrice=x


    def PrintT(self):
        print('__',end='| ')
        for i in range(len(self.V)):
            print(self.V[i], end=' | ')
        print()
        for j in range (len(self.V)):
            print(self.V[j], end=' | ')
            for elt in range(len(self.Matrice)):
                print(self.Matrice[j][elt], end='   ')
            print()




class Noeud:
    def __init__(self):
        self.nom=""
        self.voisins=[]


class Chemin:
    def __init__(self,A,origine,sortie):
        self.origine=origine
        self.sortie=sortie
        self.Graphe=A
        self.V=self.Graphe.V
        self.Noeuds=self.Graphe.Liste
        self.L=[]
        self.found=False







