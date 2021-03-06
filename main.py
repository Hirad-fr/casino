from Joueur import Joueur
from MachineASous import MachineASous

from Casino import Casino
from Roulette import Roulette


def main():
    casino = Casino(100000)
    jeu1 = Roulette("my wheel", casino)
    jeu2 = MachineASous("bandit manchot", casino)
    joueur = Joueur("Clement", 1000)
    joueur.entrer_casino(casino)
    joueur.jouer()


if __name__ == '__main__':
    main()
