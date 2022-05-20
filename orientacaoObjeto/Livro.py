from abc import abstractmethod


from abc import ABC, abstractclassmethod 

class Livro(ABC):
    def __init__(self,titulo,autor,paginas,preco):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.__preco = preco
        self.__desconto = None

    def set_desconto(self,desconto):
        if desconto < 0 or desconto > 1:
            raise Exception("Desconto inválido.")
        else:
            self.__desconto = desconto
        
    def get_desconto(self):
        return self.__desconto

    def get_preco(self):
        if self.__desconto:
            return self.__preco * (1 - self.__desconto)
        return self.__preco

    desconto = property(fget=get_desconto,fset=set_desconto)
    preco = property(fget=get_preco)
    
    @abstractmethod
    def __repr__(self):
        return f"\n\nTitulo: {self.titulo}, - Autor: {self.autor} \nPáginas: {self.paginas} - Preço: R${self.preco} \n\n"

    def __gt__(self,other):
        return self.paginas > other.paginas