import React, { useState } from 'react';
import './App.css';

function App() {
  const [artistas, setArtistas] = useState([]);
  const [albuns, setAlbuns] = useState([]);
  const [musicas, setMusicas] = useState([]);

  const [artistaInput, setArtistaInput] = useState('');
  const [albumInput, setAlbumInput] = useState('');
  const [musicaInput, setMusicaInput] = useState('');

  const [editArtistaId, setEditArtistaId] = useState(null);
  const [editAlbumId, setEditAlbumId] = useState(null);
  const [editMusicaId, setEditMusicaId] = useState(null);

  // Adicionar Artista
  const handleArtistaAdded = () => {
    if (artistaInput.trim() !== '') {
      setArtistas((prevArtistas) => [
        ...prevArtistas,
        { id: Date.now(), nome: artistaInput },
      ]);
      setArtistaInput(''); // Limpar o campo de entrada
    }
  };

  // Deletar Artista
  const handleArtistaDeleted = (id) => {
    setArtistas(artistas.filter((artista) => artista.id !== id));
  };

  // Atualizar Artista
  const handleArtistaUpdated = (updatedArtista) => {
    setArtistas(
      artistas.map((artista) =>
        artista.id === updatedArtista.id ? updatedArtista : artista
      )
    );
    setEditArtistaId(null); // Fecha o formulário de edição
  };

  // Adicionar Álbum
  const handleAlbumAdded = () => {
    if (albumInput.trim() !== '') {
      setAlbuns((prevAlbuns) => [
        ...prevAlbuns,
        { id: Date.now(), nome: albumInput },
      ]);
      setAlbumInput(''); // Limpar o campo de entrada
    }
  };

  // Deletar Álbum
  const handleAlbumDeleted = (id) => {
    setAlbuns(albuns.filter((album) => album.id !== id));
  };

  // Atualizar Álbum
  const handleAlbumUpdated = (updatedAlbum) => {
    setAlbuns(
      albuns.map((album) =>
        album.id === updatedAlbum.id ? updatedAlbum : album
      )
    );
    setEditAlbumId(null); // Fecha o formulário de edição
  };

  // Adicionar Música
  const handleMusicaAdded = () => {
    if (musicaInput.trim() !== '') {
      setMusicas((prevMusicas) => [
        ...musicas,
        { id: Date.now(), nome: musicaInput },
      ]);
      setMusicaInput(''); // Limpar o campo de entrada
    }
  };

  // Deletar Música
  const handleMusicaDeleted = (id) => {
    setMusicas(musicas.filter((musica) => musica.id !== id));
  };

  // Atualizar Música
  const handleMusicaUpdated = (updatedMusica) => {
    setMusicas(
      musicas.map((musica) =>
        musica.id === updatedMusica.id ? updatedMusica : musica
      )
    );
    setEditMusicaId(null); // Fecha o formulário de edição
  };

  return (
    <div className="container">
      <h1>Gestão de Artistas, Álbuns e Músicas</h1>

      {/* Artistas */}
      <div className="card">
        <h2>{editArtistaId ? 'Editar Artista' : 'Adicionar Artista'}</h2>
        {editArtistaId ? (
          <div>
            <input
              type="text"
              value={artistas.find((artista) => artista.id === editArtistaId)?.nome || ''}
              onChange={(e) =>
                handleArtistaUpdated({
                  id: editArtistaId,
                  nome: e.target.value,
                })
              }
            />
            <button onClick={() => setEditArtistaId(null)}>Cancelar</button>
          </div>
        ) : (
          <div>
            <input
              type="text"
              value={artistaInput}
              placeholder="Nome do Artista"
              onChange={(e) => setArtistaInput(e.target.value)}
            />
            <button onClick={handleArtistaAdded}>Adicionar</button>
          </div>
        )}
        <ul>
          {artistas.map((artista) => (
            <li key={artista.id}>
              {artista.nome}
              <button onClick={() => setEditArtistaId(artista.id)}>Editar</button>
              <button onClick={() => handleArtistaDeleted(artista.id)}>Deletar</button>
            </li>
          ))}
        </ul>
      </div>

      {/* Álbuns */}
      <div className="card">
        <h2>{editAlbumId ? 'Editar Álbum' : 'Adicionar Álbum'}</h2>
        {editAlbumId ? (
          <div>
            <input
              type="text"
              value={albuns.find((album) => album.id === editAlbumId)?.nome || ''}
              onChange={(e) =>
                handleAlbumUpdated({
                  id: editAlbumId,
                  nome: e.target.value,
                })
              }
            />
            <button onClick={() => setEditAlbumId(null)}>Cancelar</button>
          </div>
        ) : (
          <div>
            <input
              type="text"
              value={albumInput}
              placeholder="Nome do Álbum"
              onChange={(e) => setAlbumInput(e.target.value)}
            />
            <button onClick={handleAlbumAdded}>Adicionar</button>
          </div>
        )}
        <ul>
          {albuns.map((album) => (
            <li key={album.id}>
              {album.nome}
              <button onClick={() => setEditAlbumId(album.id)}>Editar</button>
              <button onClick={() => handleAlbumDeleted(album.id)}>Deletar</button>
            </li>
          ))}
        </ul>
      </div>

      {/* Músicas */}
      <div className="card">
        <h2>{editMusicaId ? 'Editar Música' : 'Adicionar Música'}</h2>
        {editMusicaId ? (
          <div>
            <input
              type="text"
              value={musicas.find((musica) => musica.id === editMusicaId)?.nome || ''}
              onChange={(e) =>
                handleMusicaUpdated({
                  id: editMusicaId,
                  nome: e.target.value,
                })
              }
            />
            <button onClick={() => setEditMusicaId(null)}>Cancelar</button>
          </div>
        ) : (
          <div>
            <input
              type="text"
              value={musicaInput}
              placeholder="Nome da Música"
              onChange={(e) => setMusicaInput(e.target.value)}
            />
            <button onClick={handleMusicaAdded}>Adicionar</button>
          </div>
        )}
        <ul>
          {musicas.map((musica) => (
            <li key={musica.id}>
              {musica.nome}
              <button onClick={() => setEditMusicaId(musica.id)}>Editar</button>
              <button onClick={() => handleMusicaDeleted(musica.id)}>Deletar</button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;
