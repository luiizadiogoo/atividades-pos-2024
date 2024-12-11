import React, { useState, useEffect } from 'react';

const EditArtistaForm = ({ artistaId, onArtistaUpdated }) => {
  const [name, setName] = useState('');

  useEffect(() => {
    // Simulando o carregamento de um artista pelo ID (substitua com sua lógica)
    const artista = { id: artistaId, name: 'Artista Exemplo' };  // Exemplo estático
    setName(artista.name);
  }, [artistaId]);

  const handleSubmit = (e) => {
    e.preventDefault();
    onArtistaUpdated({ id: artistaId, name });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <button type="submit">Atualizar Artista</button>
    </form>
  );
};

export default EditArtistaForm;
