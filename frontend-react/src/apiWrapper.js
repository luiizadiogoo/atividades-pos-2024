import React, { useEffect, useState } from 'react';
import { getData, postData, putData, deleteData } from './apiWrapper';

const MusicApp = () => {
  const [artists, setArtists] = useState([]);
  const [albums, setAlbums] = useState([]);
  const [musics, setMusics] = useState([]);
  
  // Função para buscar todos os artistas
  const fetchArtists = async () => {
    try {
      const data = await getData('artistas');
      setArtists(data);
    } catch (error) {
      console.error('Erro ao buscar artistas:', error);
    }
  };

  // Função para buscar todos os álbuns
  const fetchAlbums = async () => {
    try {
      const data = await getData('albuns');
      setAlbums(data);
    } catch (error) {
      console.error('Erro ao buscar álbuns:', error);
    }
  };

  // Função para buscar todas as músicas
  const fetchMusics = async () => {
    try {
      const data = await getData('musicas');
      setMusics(data);
    } catch (error) {
      console.error('Erro ao buscar músicas:', error);
    }
  };

  // Função para adicionar um novo artista
  const addArtist = async (newArtist) => {
    try {
      const data = await postData('artistas', newArtist);
      setArtists((prevArtists) => [...prevArtists, data]);
    } catch (error) {
      console.error('Erro ao adicionar artista:', error);
    }
  };

  // Função para adicionar um novo álbum
  const addAlbum = async (newAlbum) => {
    try {
      const data = await postData('albuns', newAlbum);
      setAlbums((prevAlbums) => [...prevAlbums, data]);
    } catch (error) {
      console.error('Erro ao adicionar álbum:', error);
    }
  };

  // Função para adicionar uma nova música
  const addMusic = async (newMusic) => {
    try {
      const data = await postData('musicas', newMusic);
      setMusics((prevMusics) => [...prevMusics, data]);
    } catch (error) {
      console.error('Erro ao adicionar música:', error);
    }
  };

  // Função para editar um artista
  const editArtist = async (id, updatedArtist) => {
    try {
      const data = await putData(`artistas/${id}`, updatedArtist);
      setArtists((prevArtists) =>
        prevArtists.map((artist) =>
          artist.id === id ? data : artist
        )
      );
    } catch (error) {
      console.error('Erro ao editar artista:', error);
    }
  };

  // Função para editar um álbum
  const editAlbum = async (id, updatedAlbum) => {
    try {
      const data = await putData(`albuns/${id}`, updatedAlbum);
      setAlbums((prevAlbums) =>
        prevAlbums.map((album) =>
          album.id === id ? data : album
        )
      );
    } catch (error) {
      console.error('Erro ao editar álbum:', error);
    }
  };

  // Função para editar uma música
  const editMusic = async (id, updatedMusic) => {
    try {
      const data = await putData(`musicas/${id}`, updatedMusic);
      setMusics((prevMusics) =>
        prevMusics.map((music) =>
          music.id === id ? data : music
        )
      );
    } catch (error) {
      console.error('Erro ao editar música:', error);
    }
  };

  // Função para excluir um artista
  const deleteArtist = async (id) => {
    try {
      await deleteData(`artistas/${id}`);
      setArtists((prevArtists) =>
        prevArtists.filter((artist) => artist.id !== id)
      );
    } catch (error) {
      console.error('Erro ao excluir artista:', error);
    }
  };

  // Função para excluir um álbum
  const deleteAlbum = async (id) => {
    try {
      await deleteData(`albuns/${id}`);
      setAlbums((prevAlbums) =>
        prevAlbums.filter((album) => album.id !== id)
      );
    } catch (error) {
      console.error('Erro ao excluir álbum:', error);
    }
  };

  // Função para excluir uma música
  const deleteMusic = async (id) => {
    try {
      await deleteData(`musicas/${id}`);
      setMusics((prevMusics) =>
        prevMusics.filter((music) => music.id !== id)
      );
    } catch (error) {
      console.error('Erro ao excluir música:', error);
    }
  };

  // Carregar os dados assim que o componente for montado
  useEffect(() => {
    fetchArtists();
    fetchAlbums();
    fetchMusics();
  }, []);

  return (
    <div>
      <h1>Music App</h1>
      <h2>Artists</h2>
      <ul>
        {artists.map((artist) => (
          <li key={artist.id}>
            {artist.nome}
            <button onClick={() => editArtist(artist.id, { nome: 'Novo Nome' })}>Edit</button>
            <button onClick={() => deleteArtist(artist.id)}>Delete</button>
          </li>
        ))}
      </ul>
      <button onClick={() => addArtist({ nome: 'New Artist', local: 'New York', ano_criacao: 2020 })}>Add Artist</button>

      <h2>Albums</h2>
      <ul>
        {albums.map((album) => (
          <li key={album.id}>
            {album.nome}
            <button onClick={() => editAlbum(album.id, { nome: 'New Album Name' })}>Edit</button>
            <button onClick={() => deleteAlbum(album.id)}>Delete</button>
          </li>
        ))}
      </ul>
      <button onClick={() => addAlbum({ artista: 1, nome: 'New Album', ano: 2023 })}>Add Album</button>

      <h2>Musics</h2>
      <ul>
        {musics.map((music) => (
          <li key={music.id}>
            {music.nome}
            <button onClick={() => editMusic(music.id, { nome: 'New Music Name' })}>Edit</button>
            <button onClick={() => deleteMusic(music.id)}>Delete</button>
          </li>
        ))}
      </ul>
      <button onClick={() => addMusic({ album: 1, nome: 'New Music', segundos: 180 })}>Add Music</button>
    </div>
  );
};

export default MusicApp;
