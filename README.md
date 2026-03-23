# 🎵 Music Playlist API

API REST desenvolvida em Python com Flask para gerenciar músicas e playlists. Permite criar músicas, organizá-las em playlists e gerenciar tudo via endpoints HTTP.

---

## 🚀 Tecnologias

- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)

---

## 📁 Estrutura do projeto

```
projeto/
├── app.py              # Aplicação principal e rotas
├── models/
│   ├── musica.py       # Classe Musica
│   └── playlist.py     # Classe Playlist
└── README.md
```

---

## ⚙️ Como rodar localmente

**1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

**2. Crie e ative um ambiente virtual**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

**3. Instale as dependências**
```bash
pip install flask
```

**4. Rode o servidor**
```bash
python app.py
```

O servidor estará disponível em `http://127.0.0.1:5000`

---

## 📌 Endpoints

### 🎵 Músicas

| Método | Rota | Descrição |
|--------|------|-----------|
| `POST` | `/musicas` | Adiciona uma nova música |
| `GET` | `/musicas` | Lista todas as músicas |
| `DELETE` | `/musicas/<id>` | Remove uma música |

#### POST /musicas
```json
// Request body
{
  "titulo": "Bohemian Rhapsody",
  "artista": "Queen",
  "duracao": 354
}

// Response 200
{
  "mensagem": "musica adicionada com sucesso"
}
```

#### GET /musicas
```json
// Response 200
[
  {
    "id": 1,
    "titulo": "Bohemian Rhapsody",
    "artista": "Queen",
    "duracao": 354
  }
]
```

#### DELETE /musicas/<id>
```json
// Response 200
{ "mensagem": "musica removida com sucesso" }

// Response 404 — música não encontrada
{ "mensagem": "nao foi possível encontrar a musica" }
```

---

### 📋 Playlists

| Método | Rota | Descrição |
|--------|------|-----------|
| `POST` | `/playlists` | Cria uma nova playlist |
| `GET` | `/playlists/<id>` | Retorna uma playlist com suas músicas |
| `POST` | `/playlists/<id>/musicas` | Adiciona uma música à playlist |
| `DELETE` | `/playlists/<id>/musicas/<musica_id>` | Remove uma música da playlist |

#### POST /playlists
```json
// Request body
{ "nome": "Favoritas" }

// Response 200
{
  "mensagem": "a playlist foi criada",
  "id": 1
}
```

#### GET /playlists/<id>
```json
// Response 200
{
  "id": 1,
  "nome": "Favoritas",
  "musicas": [
    {
      "id": 1,
      "titulo": "Bohemian Rhapsody",
      "artista": "Queen",
      "duracao": 354
    }
  ]
}

// Response 404 — playlist não encontrada
{ "mensagem": "nao foi possível encontrar a playlist" }
```

#### POST /playlists/<id>/musicas
```json
// Request body
{ "musica_id": 1 }

// Response 200
{ "mensagem": "musica adicionada com sucesso" }

// Response 404 — playlist ou música não encontrada
{ "mensagem": "playlist nao foi encontrada" }
```

#### DELETE /playlists/<id>/musicas/<musica_id>
```json
// Response 200
{ "mensagem": "musica foi removida da playlist" }

// Response 404
{ "mensagem": "a playlist n foi encontrada" }
```

---

## 💡 Observações

- Os dados são armazenados em memória — ao reiniciar o servidor, os dados são perdidos
- Projeto desenvolvido para fins de estudo de APIs REST com Flask
