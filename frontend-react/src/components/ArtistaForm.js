import React, { useState } from 'react';

const ArtistaForm = ({ onArtistaAdded }) => {
  const [name, setName] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (name) {
      onArtistaAdded({ id: Date.now(), name });  // Gerando um ID único
      setName('');  // Limpa o campo após o envio
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Nome do Artista"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <button type="submit">Adicionar Artista</button>
    </form>
  );
};

export default ArtistaForm;
