class SimpleVertex():
    """Implementação de um simples vértice."""
    value = None

    def __init__(self, value):
        """
        Construtor da classe simpleVertex.

        Parâmetros:
        ----------
        value: Um tipo existente ou criado por você.
            - Valor a ser colocado no vértice.
        """
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        """
        Método que altera o valor do vértice.

        Parâmetros:
        ----------
        value: Um tipo existente ou criado por você
            - Valor a ser alterado no vértice.
        """
        self.value = new_value

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __str__(self):
        return "Vértice {}".format(self.value)

    def __repr__(self):
        return str(self)
