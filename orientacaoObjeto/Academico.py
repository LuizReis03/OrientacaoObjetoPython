from Livro import Livro

class Academico(Livro):
    def __init__(self, titulo, autor, paginas, preco, area):
        super().__init__(titulo, autor, paginas, preco)
        self.area = area

    def __repr__(self):
        return super().__repr__() + f"\nArea de conhecimento: {self.area}"