from pokemon import *
import random

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

class Pessoa:

    def __init__(self,nome=None,pokemons = [], dinheiro=None):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)
        
        self.pokemons = pokemons

        if dinheiro:
            self.dinheiro = dinheiro
        else:
            self.dinheiro = random.randint(1,500)

    def __str__(self):
        return f'{self.nome}'
    
    def mostrar_pokemons(self):

        if self.pokemons:
            print(f'Pokemons de {self}:')
            for i,pokemon in enumerate(self.pokemons):
                print(f'Pokemon {i+1}: {pokemon}')
                
        else:
            print(f'{self} não possui pokemons...')


    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print(f"{self} escolheu {pokemon_escolhido}")
            return pokemon_escolhido
        else:
            print('ERROR: Esse jogador não possui pokemons.')

    def mostrar_dinheiro(self):
        print(f"Você possui ${self.dinheiro} em sua conta")       

    def ganhar_dinheiro(self,quantidade):
        self.dinheiro += quantidade
        print(f"Você ganhou $ {quantidade}")
        self.mostrar_dinheiro()
    


    def batalhar(self,pessoa):
        print(f'{self} iniciou uma batalha com {pessoa}')

        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()

        meu_pokemon = self.escolher_pokemon()

        if meu_pokemon and pokemon_inimigo:
            while True:

                vitoria = meu_pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print(f"{self} ganhou a batalha!")
                    self.ganhar_dinheiro(pokemon_inimigo.level * 20)
                    break

                vitoria_inimiga = pokemon_inimigo.atacar(meu_pokemon)
                if vitoria_inimiga:
                    print(f"{pessoa} Ganhou a batalha")
                    break
        else:
            print('Está batalha não pode ocorrer...')


class Player(Pessoa):
    tipo = 'player'

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print(f"{self} capturou o Pokemon {pokemon}!")

    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
            while True:
                escolha = input("Escolha seu pokemon: ")
                try:
                    escolha = int(escolha)
                    escolha -= 1
                    pokemon_escolhido = self.pokemons[escolha]

                    print(f'{pokemon_escolhido} eu escolho você!!!')
                    return pokemon_escolhido
                except:
                    print('Escolha inválida')
        else:
            print('ERROR: Esse jogador não possui pokemons.')

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
                        print(f'A tentativa de captura falhou. O {pokemon} não foi capturado...')
                        
                        if random.random() >= 0.6:
                            print(f"{pokemon} conseguiu fugir...")
                            break
                        
                        escolha2 = input("Deseja tentar pegar o pokemon novamente? (s/n): ")
                        if escolha2.lower() != 's':
                            print(f"{pokemon} conseguiu fugir...")
                            break
            elif escolha.lower() == 'n':
                print("Ok, boa viagem")
            else:
                print('Escolha inválida ...')
        else:
            print("Exploração sem resultado ...")




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

