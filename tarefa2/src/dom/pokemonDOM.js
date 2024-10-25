// src/dom/pokemonDOM.js
import { capitalizeFirstLetter } from '../utils.js';

export function renderPokemons(pokemons) {
    const pokemonList = document.getElementById('pokemon-list');
    pokemonList.innerHTML = '';
    pokemons.results.forEach((pokemon) => {
        const col = document.createElement('div');
        col.className = 'col-md-3';

        const card = document.createElement('div');
        card.className = 'card pokemon-card';

        const button = document.createElement('button');
        button.className = 'btn btn-info w-100';
        button.textContent = capitalizeFirstLetter(pokemon.name);
        button.addEventListener('click', () => loadPokemonDetails(pokemon.url));
        
        card.appendChild(button);
        col.appendChild(card);
        pokemonList.appendChild(col);
    });
}

export function renderPokemonDetails(pokemon) {
    const pokemonInfo = document.getElementById('pokemon-info');
    pokemonInfo.innerHTML = `
        <div class="card pokemon-card">
            <div class="card-body text-center">
                <h5 class="card-title">${capitalizeFirstLetter(pokemon.name)}</h5>
                <img src="${pokemon.sprites.front_default}" alt="${pokemon.name}" class="pokemon-img" />
                <p class="card-text"><strong>Altura:</strong> ${pokemon.height / 10} m</p>
                <p class="card-text"><strong>Peso:</strong> ${pokemon.weight / 10} kg</p>
                <p class="card-text"><strong>Habilidades:</strong></p>
                <ul class="list-unstyled">
                    ${pokemon.abilities.map(ability => `<li>${capitalizeFirstLetter(ability.ability.name)}</li>`).join('')}
                </ul>
            </div>
        </div>
    `;
}