class Musica:
    def __init__(self, id, titulo, artista, duracao):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.duracao = duracao

    def to_dict(self):
        conversor = {
            "titulo": self.titulo,
            "artista": self.artista,
            "duracao": self.duracao,
            "id": self.id
        }
        return conversor

   

