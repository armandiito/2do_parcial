
class Nodo:
    def __init__(self, nombre=None, cedula=None, izq=None, der=None):
        self.nombre=nombre
        self.cedula=cedula
        self.izq=izq
        self.der=der
        
    def __str__(self):
        return "%s %s" %(self.nombre, self.cedula)
    
class aBinarios:
    def __init__(self):
        self.raiz=None
    
    def agregar(self, elemento):
        if self.raiz==None:
            self.raiz=elemento
        else:
            aux=self.raiz
            padre=None
            while aux !=None:
                padre=aux
                if int(elemento.cedula)>= int(aux.cedula):
                    aux=aux.der
                else:
                    aux=aux.izq
            if int(elemento.cedula)>= int(padre.cedula):
                padre.der=elemento
            else:
                padre.izq=elemento
                
    def preorden(self, elemento):
        if elemento !=None:
            self.preorden(elemento.izq)
            self.preorden(elemento.der)
            print(elemento)
            
    def postorden(self, elemento):
        if elemento !=None:
            print(elemento)
            self.postorden(elemento.izq)
            self.postorden(elemento.der)      
            
    def inorden(self, elemento):
            if elemento !=None:
                self.inorden(elemento.izq)
                print(elemento)
                self.inorden(elemento.der) 
    
    def getRaiz(self):
        return self.raiz
                
    
                
if __name__=="__main__":
    ab=aBinarios()
    
    while(True):
        print("---Menu---\n"+ 
              "1. Agregar\n"+
              "2. preorden\n"+
              "3. postorden\n"+
              "4. inorden\n")
        
        num=input("ingrese la opcion: ")
        if num=="1":
            nombre=input("ingrese el nombre: ")
            cedula=input("ingrese la cedula: ")
            nod=Nodo(nombre, cedula)
            ab.agregar(nod)
        elif num=="2":
            print("imprimiendo en preorden")
            ab.preorden(ab.getRaiz())
        elif num=="3":
            print("imprimiento por postorden")
            ab.postorden(ab.getRaiz())
        elif num=="4":
            print("imprimiendo en inorden")
            ab.inorden(ab.getRaiz())