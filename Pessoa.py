from pokemon import *
import random
from termcolor import colored
import time

NOMES = ['Elder Max', 'Rival Leo', 'Sienna', 'Marcos', 'Professor Thorn', 'Bianca', 'Akira',
        'Tess', 'Lucas', 'Ray', 'Serena', 'Hunter', 'Gwen', 'Fiona', 'Orion', 'Kai', 'Dylan']

POKEMONS = [
    PokemonFogo("Charmander"), PokemonFogo("Charmeleon"), PokemonFogo("Charizard"), PokemonFogo("Vulpix"),
    PokemonFogo("Ninetales"), PokemonAgua("Squirtle"), PokemonAgua("Wartortle"), PokemonAgua("Blastoise"),
    PokemonAgua("Psyduck"), PokemonAgua("Golduck"), PokemonEletrico("Pikachu"), PokemonEletrico("Raichu"),
    PokemonNormal("Rattata"), PokemonNormal("Raticate"), PokemonNormal("Meowth"), PokemonNormal("Persian"),
    PokemonPlanta("Bulbasaur"), PokemonPlanta("Ivysaur"), PokemonPlanta("Venusaur"), PokemonPlanta("Oddish"),
    PokemonPlanta("Gloom"), PokemonPlanta("Vileplume"), PokemonFada("Clefairy"), PokemonFada("Clefable"), 
    PokemonFantasma("Gastly"), PokemonFantasma("Haunter"), PokemonFantasma("Gengar"), PokemonNormal("Pidgey"),
    PokemonNormal("Pidgeotto"), PokemonNormal("Pidgeot"), PokemonNormal("Jigglypuff"), PokemonNormal("Wigglytuff"),
    PokemonNormal("Eevee"), PokemonNormal("Snorlax"), PokemonNormal("Tauros"), PokemonFogo("Arcanine"), PokemonFogo("Growlithe"),
    PokemonAgua("Tentacool"), PokemonAgua("Tentacruel"), PokemonEletrico("Magnemite"), PokemonEletrico("Magneton"), PokemonPlanta("Paras"),
    PokemonPlanta("Parasect"), PokemonFada("Clefairy"), PokemonFada("Clefable"), PokemonFantasma("Mimikyu"), PokemonFantasma("Mismagius"),
    PokemonFantasma("Sableye"),
]

def exibir_com_delay(texto, delay=1):
    """Função para exibir o texto completo com delay após a impressão."""
    print(texto, end='', flush=True)
    time.sleep(delay)  # Atraso após a mensagem completa


class Pessoa:

    def __init__(self, nome=None, pokemons=None, dinheiro=None):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)
        
        self.pokemons = pokemons if pokemons else []

        self.dinheiro = dinheiro if dinheiro else random.randint(1, 500)

    def __str__(self):
        return f'{self.nome}'
    
    def mostrar_pokemons(self):
        if self.pokemons:
            print(f'Pokemons de {self}:')
            for i, pokemon in enumerate(self.pokemons):
                print(f'Pokemon {i+1}: {pokemon}')
        else:
            print(f'{self} não possui pokemons...')

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print(f"{self} escolheu {pokemon_escolhido}")
            return pokemon_escolhido
        else:
            print(colored('ERROR: Esse jogador não possui pokemons.', 'red'))

    def mostrar_dinheiro(self):
        print(f"Você possui ${self.dinheiro} em sua conta")       

    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print(colored(f"Você ganhou ${quantidade}", 'green'))
        self.mostrar_dinheiro()

    def batalhar(self, pessoa):
        print(colored(f'{self} iniciou uma batalha com {pessoa}', 'yellow'))
        time.sleep(1)

        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()

        meu_pokemon = self.escolher_pokemon()

        if meu_pokemon and pokemon_inimigo:
            while True:
                # Ataque do jogador
                exibir_com_delay(colored(f"{meu_pokemon} ataca {pokemon_inimigo}!\n", 'red'), delay=1)
                vitoria = meu_pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    exibir_com_delay(colored(f"{self} ganhou a batalha!", 'green'), delay=1)
                    self.ganhar_dinheiro(pokemon_inimigo.level * 20)
                    break

                # Ataque do inimigo
                exibir_com_delay(colored(f"{pokemon_inimigo} ataca {meu_pokemon}!\n", 'blue'), delay=1)
                vitoria_inimiga = pokemon_inimigo.atacar(meu_pokemon)
                if vitoria_inimiga:
                    exibir_com_delay(colored(f"{pessoa} ganhou a batalha", 'red'), delay=1)
                    break
        else:
            print(colored('Está batalha não pode ocorrer...', 'red'))

class Player(Pessoa):
    tipo = 'player'

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        time.sleep(1)
        print(colored(f"Você capturou {pokemon} com sucesso!", 'green'))

    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
            while True:
                escolha = input("Escolha seu pokemon: ")
                try:
                    escolha = int(escolha)
                    escolha -= 1
                    pokemon_escolhido = self.pokemons[escolha]

                    print(colored(f'{pokemon_escolhido} eu escolho você!!!', 'green'))
                    return pokemon_escolhido
                except:
                    print(colored('Escolha inválida', 'red'))
        else:
            print(colored('ERROR: Esse jogador não possui pokemons.', 'red'))

    def explorar(self):
        if random.random() <= 0.3:
            pokemon = random.choice(POKEMONS)

            print(f"Um pokemon selvagem apareceu... É O {pokemon}")
            
            escolha = input(f'Deseja capturar pokemon? (s/n):')

            if escolha.lower() == 's':
                while True:
                    if random.random() >= 0.5:
                        self.capturar(pokemon)
                        self.mostrar_pokemons()
                        break
                    else:
                        print(colored(f"A tentativa de captura falhou...", 'red'))
                        
                        if random.random() >= 0.6:
                            print(colored(f"A tentativa de captura falhou... {pokemon} escapou!", 'red'))
                            break
                        
                        escolha2 = input("Deseja tentar pegar o pokemon novamente? (s/n): ")
                        if escolha2.lower() != 's':
                            print(colored(f"A tentativa de captura falhou... {pokemon} escapou!", 'red'))
                            break
            elif escolha.lower() == 'n':
                print("Ok, boa viagem")
            else:
                print(colored('Escolha inválida ...', 'red'))
        else:
            print(colored("Exploração sem resultado ...", 'yellow'))

class Inimigo(Pessoa):
    tipo = "inimigo"

    def __init__(self, nome=None, pokemons=None):
        if not pokemons:
            pokemons_aleatórios = []
            for i in range(random.randint(1,6)):
                pokemons_aleatórios.append(random.choice(POKEMONS))

            super().__init__(nome, pokemons=pokemons_aleatórios)
        else:
            super().__init__(nome, pokemons=pokemons)
