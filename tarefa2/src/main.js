// src/main.js
import { fetchPokemons, fetchPokemonDetails } from './api/pokemonApi.js';
import { renderPokemons, renderPokemonDetails } from './dom/pokemonDOM.js';

document.getElementById('load-pokemons-btn').addEventListener('click', async () => {
    try {
        const data = await fetchPokemons();
        renderPokemons(data);
    } catch (error) {
        console.error('Erro ao buscar Pokémon:', error);
        alert('Não foi possível carregar a lista de Pokémon.');
    }
});

async function loadPokemonDetails(url) {
    try {
        const pokemon = await fetchPokemonDetails(url);
        renderPokemonDetails(pokemon);
    } catch (error) {
        console.error('Erro ao buscar informações do Pokémon:', error);
        alert('Não foi possível carregar as informações do Pokémon.');
    }
}