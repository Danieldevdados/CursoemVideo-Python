class Retangulo:

    def __init__(self, altura= 1, base= 8):
        self._base = base
        self._altura = altura
        self._area = None
    
    # Getter e setter da base
    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        if valor < 0:
            print("Base não pode ser negativa")
        else:
            self._base = valor
            self._area = self._altura * self._base

            
            
            
            
    # Getter e Setter da altura
    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if valor < 0:
            print("Altura não pode ser negativa!")
        else:
            self._altura = valor
            self._area = self._altura * self._base


    # Getter da area
    @property
    def area(self):
        return self._area



    @property
    def medidas(self):
        return f"Base: {self._base} \nAltura: {self._altura} \nArea: {self._area}"

    @medidas.setter
    def medidas(self, valores):
        self.base, self.altura = valores[0], valores[1]


