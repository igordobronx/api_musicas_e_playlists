from flask import Flask, request, jsonify
from models.musica import Musica
from models.playlist import Playlist

app = Flask(__name__)

musicas = []
musicas_id_control = 1
playlists = []
playlist_id_control = 1

def buscar_id(lista, id):
    for item in lista:
        if item.id == id:
            return item
    return None

@app.route('/musicas', methods=['POST'])
def adicionar_musica():
    global musicas_id_control
    data = request.get_json()
    nova_musica = Musica(
        id=musicas_id_control,
        titulo=data.get("titulo"),
        artista=data.get("artista"),
        duracao=data.get("duracao")
    )
        

    musicas_id_control += 1
    musicas.append(nova_musica)
    return jsonify({"mensagem": "musica adicionada com sucesso"})

@app.route('/musicas', methods=['GET'])
def listar_musicas():
    return jsonify([m.to_dict() for m in musicas])

@app.route('/musicas/<int:id>', methods=['DELETE'])
def deletar_musica(id):
    musica = None
    for i in musicas:
            if i.id == id:
                musica = i
                break

    if musica is None:
        return jsonify({"mensagem": "nao foi possível encontrar a musica"}), 404

    musicas.remove(musica)
    return jsonify({"mensagem": "musica removida com sucesso"})


#playlist

@app.route('/playlists', methods=['POST'])
def criar_playlist():
    global playlist_id_control
    data = request.get_json()
    nova_playlist = Playlist(
        id=playlist_id_control,
        nome=data.get("nome"),
    )
    playlist_id_control += 1 
    playlists.append(nova_playlist)
    return jsonify({"mensagem": "a playlist foi criada", "id": nova_playlist.id})

@app.route('/playlists/<int:id>', methods=['GET'])
def listar_playlists(id):
    playlist = None
    for i in playlists:
            if i.id == id:
                playlist = i
                break

    if playlist is None:
        return jsonify({"mensagem": "nao foi possível encontrar a playlist"}), 404
    
    return jsonify( {
        "id": playlist.id,
        "nome": playlist.nome,
        "musicas": [m.to_dict() for m in playlist.musicas]
    })

@app.route('/playlists/<int:id>/musicas', methods=['POST'])
def adicionar_musica_playlist(id):
    data = request.get_json()
    musica_id = data.get("musica_id")

    playlist = buscar_id(playlists, id)
    musica = buscar_id(musicas, musica_id)

    if not playlist:
        return jsonify({"mensagem": "playlist nao foi encontrada"}), 404

    if not musica:
        return jsonify({"mensagem": "musica não foi encontrada"}), 404

    playlist.musicas.append(musica)
    return jsonify({"mensagem": "musica adicionada com sucesso"})

@app.route('/playlists/<int:id>/musicas/<int:musica_id>', methods=['DELETE'])
def remover_musica_playlist(id, musica_id):
    playlist = buscar_id(playlists, id)

    if not playlist:
        return jsonify({"mensagem": "a playlist n foi encontrada"}), 404

    musica = buscar_id(playlist.musicas if playlist else [], musica_id)
    if not musica:
        return jsonify({"mensagem": "a musica nao foi encontrada"}), 404

    playlist.musicas.remove(musica)
    return jsonify({"mensagem": "musica foi removida da playlist"})


if __name__ == "__main__":
    app.run(debug=True)