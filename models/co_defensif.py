from models.comportement import Comportement


class ComportementDefensif(Comportement):

    def agir(self, ennemi) -> str:
        return "defend"