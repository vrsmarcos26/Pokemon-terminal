import random

class Pokemon:
    def __init__(self, especie, level=None, nome=None):
        self.especie = especie
        if level:    
            self.level = level
        else:
            self.level = random.randint(1,100)

        if nome:
            self.nome = nome
        else:
            self.nome = especie

        self.ataque = self.level * 5
        self.vida = self.level * 10

    def __str__(self):
        return f'{self.especie} (Lv:{self.level}) // {self.vida}hp   {self.ataque}attk'

    def atacar(self,pokemon):
        ataque_efetivo = int(self.ataque * random.random() * 1.3)
        pokemon.vida -= ataque_efetivo

        print(f"{pokemon} perdeu {ataque_efetivo} pontos de vida (hp)...")

        if pokemon.vida <= 0:
            print(f"{pokemon} foi derrotado")
            return True
        else:
            return False


class PokemonEletrico(Pokemon):
    tipo = 'Elétrico'

    def atacar(self, pokemon):
         print(f'{self} lançou um raio do trovão em {pokemon} e tirou {self.vida}')
         return super().atacar(pokemon)

class PokemonFogo(Pokemon):
    tipo = 'Fogo'
    
    def atacar(self, pokemon):
         print(f'{self} lançou uma bola de fogo em {pokemon}')
         return super().atacar(pokemon)

class PokemonAgua(Pokemon):
    tipo = 'Água'
    
    def atacar(self, pokemon):
         print(f"{self} lançou uma jato d'água em {pokemon}")
         return super().atacar(pokemon)

class PokemonPlanta(Pokemon):
    tipo = 'Planta'
    
    def atacar(self, pokemon):
         print(f'{self} lançou um chicote de planta em {pokemon}')
         return super().atacar(pokemon)
    
class PokemonNormal(Pokemon):
    tipo = 'Normal'

    def atacar(self, pokemon):
         print(f'{self} lançou uma investida em {pokemon}')
         return super().atacar(pokemon)

class PokemonFada(Pokemon):
    tipo = 'Fada'

    def atacar(self, pokemon):
         print(f'{self} lançou um flash de luz em {pokemon}')
         return super().atacar(pokemon)

class PokemonFantasma(Pokemon):
    tipo = 'Fantasma'

    def atacar(self, pokemon):
         print(f'{self} lançou uma bola de escuridão em {pokemon}')
         return super().atacar(pokemon)