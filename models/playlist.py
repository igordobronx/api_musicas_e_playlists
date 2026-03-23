class Playlist:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.musicas = []


    def to_dict(self):
        conversor = {
            "id": self.id,
            "nome": self.nome,
            "musicas": [m.to_dict() for m in self.musicas]
        }
        return conversor