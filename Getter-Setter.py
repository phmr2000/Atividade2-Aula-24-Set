class Cliente:
    _id_counter = 1  

    def __init__(self, nome: str, email: str):
        self._id_cliente = Cliente._id_counter
        Cliente._id_counter += 1

        self.nome = nome   
        self.email = email 

    @property
    def id_cliente(self):
        return self._id_cliente

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not valor.strip():
            raise ValueError("O nome não pode ser vazio.")
        self._nome = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if not valor.strip() or "@" not in valor:
            raise ValueError("O email deve ser válido e conter '@'.")
        self._email = valor

    def __repr__(self):
        return f"Cliente(id={self.id_cliente}, nome='{self.nome}', email='{self.email}')"
