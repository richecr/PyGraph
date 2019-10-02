class SimpleVertex():
    """implementation of a simple vertex."""
    value = None


    def __init__(self, value):
        """
        Construtor da classe simpleVertex

        Parâmetros:
        ----------
        value: Um tipo existente ou criado por você
            - Valor a ser colocado no vértice.
        """
        self.value = value

    def set_value(self, new_value):
        """
        Método que altera o valor do vértice.

        Parâmetros:
        ----------
        value: Um tipo existente ou criado por você
            - Valor a ser alterado no vértice.
        """
        self.value = new_value
