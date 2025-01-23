import pickle
from pokemon import *
from Pessoa import *
from colorama import init, Fore, Back, Style

# Inicia a colorama
init(autoreset=True)

def escolher_pokemon_inicial(player):
    print(Fore.GREEN + "Agora você irá poder escolher o seu Pokemon inicial que irá te acompanhar nessa jornada!")

    pikachu = PokemonEletrico('Pikachu', level=5)
    charmander = PokemonFogo('Charmander', level=5)
    bulbasalro = PokemonPlanta('Bulbasalro', level=5)
    squarly = PokemonAgua('Squarly', level=5)
    eevee = PokemonNormal('Eevee', level=5)

    print(Fore.CYAN + f"""Você tem 5 escolhas:
    1 - {pikachu}
    2 - {charmander}
    3 - {bulbasalro}
    4 - {squarly}
    5 - {eevee}""")
    
    while True:
        escolha = input(Fore.YELLOW + "Escolha seu pokemon: ")

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
            print(Fore.RED + 'Escolha inválida...')

def salvar_game(player):
    try:
        with open('database.db', 'wb') as arquivo:
            pickle.dump(player, arquivo)
            print(Fore.GREEN + "Jogo salvo com sucesso!")
    except Exception as error:
        print(Fore.RED + 'Erro ao salvar game')

def carregar_game():
    try:
        with open('database.db', 'rb') as arquivo:
            player = pickle.load(arquivo)
            print(Fore.GREEN + 'Load feito com sucesso')
            return player
    except Exception as error:
        print(Fore.RED + 'Save não encontrado')



if __name__ == "__main__":

    print(Fore.MAGENTA + f'''
          Bem-vindo ao jogo 

            +=============================================================+
            | ____   ___  _  _______ __  __  ___  _   _                   |
            ||  _ \ / _ \| |/ / ____|  \/  |/ _ \| \ | |                  |
            || |_) | | | | ' /|  _| | |\/| | | | |  \| |                  |
            ||  __/| |_| | . \| |___| |  | | |_| | |\  |                  |
            ||_|___ \___/|_|\_\_____|_|__|_|\___/|_|_\_| _       _   ___  |
            ||_   _| ____|  _ \|  \/  |_ _| \ | |  / \  | |     / | / _ \ |
            |  | | |  _| | |_) | |\/| || ||  \| | / _ \ | |     | || | | ||
            |  | | | |___|  _ <| |  | || || |\  |/ ___ \| |___  | || |_| ||
            |  |_| |_____|_| \_\_|  |_|___|_| \_/_/   \_\_____| |_(_)___/ |
            +=============================================================+

          ''')
    
    player = carregar_game()

    if not player:

        nome = input(Fore.YELLOW + "Olá, eu sou o professor Marcos Vinícius. Qual o seu nome? \n")
        player = Player(nome)

        print(Fore.CYAN + f"Olá {player}, esse é o mundo pokemon, habitado por criaturas das mais diversas peculiariedades e a partir de agora sua missão é se tornar um mestre dos pokemons!")
        print('Capture o máximo de pokemons que conseguir e lute com seus inimigos\n')
        player.mostrar_dinheiro()

        if player.pokemons:
            print(Fore.GREEN + "Já vi que você tem alguns pokemons\n")
            player.mostrar_pokemons()
        else:
            print(Fore.RED + "Vejo que você não tem pokemons ainda, portanto precisa escolher um:\n")
            escolher_pokemon_inicial(player)

            print(Fore.GREEN + "Agora com pokemon em mãos, enfrente seu arqui-rival e colega Gary")
            Gary = Inimigo(nome='Gary', pokemons=[PokemonAgua('Squirtle', level=4)])
            player.batalhar(Gary)
            salvar_game(player)

            print(Fore.MAGENTA + "\nSua jornada começa agora, seja bem-vindo e divirta-se.\n")

    while True:
        print(Fore.YELLOW + '''
---------------------------------------
O que deseja fazer?

1 - Explorar pelo mundo afora
2 - Lutar com um inimigo
3 - Pokeagenda
0 - Sair do jogo
---------------------------------------
''')
        
        escolha = input(Fore.YELLOW + "Sua escolha: ")
        if escolha == "0":
            print(Fore.CYAN + 'Fechando jogo...')
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
            print(Fore.RED + "Escolha inválida...")
