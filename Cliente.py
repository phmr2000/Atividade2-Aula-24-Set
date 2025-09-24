class Cliente:
    _id_counter = 1  

    def __init__(self, nome: str, email: str):
        
        if not nome.strip():
            raise ValueError("O nome não pode ser vazio.")
        if not email.strip() or "@" not in email:
            raise ValueError("O email deve ser válido e conter '@'.")

        
        self._id_cliente = Cliente._id_counter
        Cliente._id_counter += 1

        self.nome = nome
        self.email = email

    @property
    def id_cliente(self):
        """Propriedade somente leitura para o id do cliente"""
        return self._id_cliente

    def __repr__(self):
        return f"Cliente(id={self.id_cliente}, nome='{self.nome}', email='{self.email}')"
