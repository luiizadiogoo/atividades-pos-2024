import React from 'react';

const ArtistaList = ({ artistas, onArtistaDeleted, onArtistaEdit }) => {
  return (
    <div>
      <h2>Lista de Artistas</h2>
      <ul>
        {artistas.map(artista => (
          <li key={artista.id}>
            {artista.name}
            <button onClick={() => onArtistaEdit(artista.id)}>Editar</button>
            <button onClick={() => onArtistaDeleted(artista.id)}>Excluir</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ArtistaList;
