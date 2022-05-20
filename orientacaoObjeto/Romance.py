from Livro import Livro

class Romance(Livro):
    def __init__(self, titulo, autor, paginas, preco,genero):
        super().__init__(titulo, autor, paginas, preco)
        self.genero = genero

    def __repr__(self):
        return super().__repr__() + f"\nGênero: {self.genero}"