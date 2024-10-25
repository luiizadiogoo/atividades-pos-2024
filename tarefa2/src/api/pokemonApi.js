// src/api/pokemonApi.js
export async function fetchPokemons() {
    const url = 'https://pokeapi.co/api/v2/pokemon?';
    const response = await fetch(url);
    if (!response.ok) throw new Error('Erro ao buscar Pokémon');
    return response.json();
}

export async function fetchPokemonDetails(url) {
    const response = await fetch(url);
    if (!response.ok) throw new Error('Erro ao buscar detalhes do Pokémon');
    return response.json();
}