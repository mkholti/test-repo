

from conf import Conf


class LDN(Conf):
    """
    class de l'entité lieu de naissance
    """

    def __init__(self, ldn):
        self.ldn = ldn
        self.ldn = clean_ldn(self.ldn)

    def controle(self):
        """
        fonction de controle de l'entité LDN

        return int : 1 or 0
        """
        pass

    def decoupe(self):
        """
        fontion de découpage de l'entité LDN
        return (ville, pays, code postal)
        """
        pass