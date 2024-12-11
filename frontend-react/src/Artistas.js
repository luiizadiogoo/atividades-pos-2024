import React, { useState } from 'react';
import ArtistaList from './components/ArtistaList';
import ArtistaForm from './components/ArtistaForm';
import EditArtistaForm from './components/EditArtistaForm';

const Artistas = () => {
  const [artistas, setArtistas] = useState([]);
  const [editArtistaId, setEditArtistaId] = useState(null);

  const handleArtistaAdded = (newArtista) => {
    setArtistas((prevArtistas) => [...prevArtistas, newArtista]);
  };

  const handleArtistaDeleted = (id) => {
    setArtistas(artistas.filter(artista => artista.id !== id));
  };

  const handleArtistaUpdated = (updatedArtista) => {
    setArtistas(artistas.map(artista => 
      artista.id === updatedArtista.id ? updatedArtista : artista
    ));
    setEditArtistaId(null); // Fecha o formulário de edição após atualização
  };

  return (
    <div>
      <h1>Gestão de Artistas</h1>
      {editArtistaId ? (
        <EditArtistaForm
          artistaId={editArtistaId}
          onArtistaUpdated={handleArtistaUpdated}
        />
      ) : (
        <>
          <ArtistaForm onArtistaAdded={handleArtistaAdded} />
          <ArtistaList
            artistas={artistas}
            onArtistaDeleted={handleArtistaDeleted}
            onArtistaEdit={setEditArtistaId} // Passa a função para editar artista
          />
        </>
      )}
    </div>
  );
};

export default Artistas;
