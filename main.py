import pickle
from pokemon import *
from Pessoa import *


def escolher_pokemon_inicial(player):
    print(f'Agora você irá poder escolher o seu Pokemon inicial que irá te acompanhar nessa jornada!')

    pikachu = PokemonEletrico('Pikachu', level=5)
    charmander = PokemonFogo('Charmander', level=5)
    bulbasalro = PokemonPlanta('Bulbasalro', level=5)
    squarly = PokemonAgua('Squarly', level=5)
    eevee = PokemonNormal('Eevee', level=5)

    print(f"""Você tem 3 escolhas: 
    1 - {pikachu}
    2 - {charmander}
    3 - {bulbasalro}
    4 - {squarly}
    5 - {eevee}""")
    
    while True:
        escolha = input("Escolha seu pokemon: ")

        if escolha == '1':
            player.capturar(pikachu)
            break
        elif escolha == '2':
            player.capturar(charmander)
            break
        elif escolha == '3':
            player.capturar(bulbasalro)
            break
        elif escolha == '4':
            player.capturar(squarly)
            break
        elif escolha == '5':
            player.capturar(eevee)
            break
        else:
            print('Escolha inválida...')

def salvar_game(player):
    try:
        with open('database.db', 'wb') as arquivo:
            pickle.dump(player, arquivo)
            print("Jogo salvo com sucesso!")
    except Exception as error:
        print('Erro ao salvar game')

def carregar_game():
    try:
        with open('database.db', 'rb') as arquivo:
            player = pickle.load(arquivo)
            print('Load feito com sucesso')
            return player
    except Exception as error:
        print('Save não encontrado')

if __name__ == "__main__":

    print('''
          ============================================
          Bem vindo ao jogo Pokemon RPG de terminal 2.
          ============================================
          ''')
    
    player = carregar_game()

    if not player:

        nome = input("Olá, eu sou o professor Marcos Vinícius. Qual o seu nome? \n")
        player = Player(nome)

        print(f"Olá {player}, esse é o mundo pokemon, habitado por criaturas das mais diversas peculhariedades e a partir de agora sua missão é se tornar um mestre dos pokemons!")
        print('Capture o máximo de pokemons que conseguir e lute com seus inimigos\n')
        player.mostrar_dinheiro()

        if player.pokemons:
            print("Já vi que você tem alguns pokemons\n")
            player.mostrar_pokemons()
        else:
            print("Vejo que você não tem pokemons ainda, portando precisa escolher um: \n")
            escolher_pokemon_inicial(player)

            print("Agora com pokemon em mãos, enfrente seu arqui-rival e colega Gary")
            Gary = Inimigo(nome='Gary', pokemons=[PokemonAgua('Squirtle', level=4)])
            player.batalhar(Gary)
            salvar_game(player)

            print("\n Sua jornada começa agora, seja bem vindo e divirta-se.\n")

    while True:
        print('''---------------------------------------
    O que deseja fazer?
              
    1 - Explorar pelo mundo a fora
    2 - Lutar com um inimigo
    3 - Pokeagenda
    0 - Sair do jogo
---------------------------------------\n''')
        
        escolha = input("Sua escolha: ")
        if escolha == "0":
            print('Fechando jogo...')
            break
        elif escolha == '1':
            player.explorar()
            salvar_game(player)
        elif escolha == '2':
            ini_aleatorio = Inimigo()
            player.batalhar(ini_aleatorio)
            salvar_game(player)
        elif escolha == '3':
            player.mostrar_pokemons()
        else:
            print("Escolha inválida...")