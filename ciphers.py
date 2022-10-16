from string import ascii_uppercase

letras = ascii_uppercase


class Atbash:
    """ Cifra de Atbash:
        Substitui a primeira letra do alfabeto pela última,
        invertendo todo o alfabeto usual.
        Ex.:
            normal: a b c d e f g h i j k l m n o p q r s t u v w x y z
            código: Z Y X W V U T S R Q P O N M L K J I H G F E D C B A
        Obs.: É necessário chamar alguma função
        """
    def __init__(self, frase:str):
        """
        :param str frase: Frase a ser cifrada ou decifrada
        """
        self.frase = frase.upper()

        self.find_index = lambda lista, w: lista.index(w)  # retorna o indice da letra do alfabeto

    def decoder(self):
        return ''.join([letras[self.find_index(letras[::-1], i)] if i in letras else i for i in self.frase])

    def encoder(self):
        return ''.join([letras[::-1][self.find_index(letras, i)] if i in letras else i for i in self.frase])


class Cesar:
    """ Cifra de Cesar:
        O alfabeto cifrado é o alfabeto normal rotacionado à direita ou esquerda por um número de posições.
        Ex.:
            aqui está uma cifra de César usando uma rotação à esquerda de três posições.
            Neste caso, a chave é três.
        Normal:  ABCDEFGHIJKLMNOPQRSTUVWXYZ
        Cifrado: DEFGHIJKLMNOPQRSTUVWXYZABC
    """
    def __init__(self, frase:str, chave:int):
        """
        :param str frase: Frase a ser cifrada ou decifrada
        :param int chave: Chave para cifrar ou decifrar a frase
        """
        self.frase = frase.upper()
        self.chave = chave

        if not isinstance(self.chave, int):
            raise TypeError("O parâmetro \'chave\' deve ser do tipo \'int\'")

    def decoder(self) -> str:
        return ''.join([letras[(letras.index(i) - self.chave) % 26]
                        if i in letras else i
                        for i in self.frase])

    def encoder(self) -> str:
        return ''.join([letras[(letras.index(i) + self.chave) % 26]
                        if i in letras else i
                        for i in self.frase])


class Viginere:
    """
    Cifra de Vigenère:
    Consiste no uso de cifras de cesar em sequência,
    com diferentes valores de deslocamento ditados
    por uma "palavra chave", sendo a chave uma string.
    Ex.:
           Texto:	ATACARBASESUL
           Chave:	LIMAOLIMAOLIM
    Texto cifrado:	LBMCOCJMSSDCX
    """
    def __init__(self, frase:str, chave:str):
        """
        :param str frase: Frase a ser cifrada ou decifrada
        :param str chave: Chave para cifrar ou decifrar a frase
        """
        self.frase = frase.upper()
        self.chave = chave.upper()

        self.tratamentos()

    def tratar_chave(self):
        remove_espaco = lambda x: ''.join(x.strip(" ")) # remove os espaços

        # replica os espaços da frase na chave, caso existam
        add_espaco = lambda x: ''.join([next(x) if not c.isspace() else ' ' for c in self.frase])

        # Se o tamanho da chave for menor que a frase, essa função aumentará o tamanho dela sendo >= ao length da frase
        aumenta_tamanho_chave = lambda x: x * round(len(remove_espaco(self.frase)) / len(x)) \
            if len(x) < len(remove_espaco(self.frase)) else x

        itera_chave = iter(aumenta_tamanho_chave(self.chave))
        return add_espaco(itera_chave)

    def tratamentos(self):
        if not self.chave.isalpha():
            raise ValueError("Somente caracteres alfabéticos, sem espaçamento na chave!")

    def decoder(self):
        chave = self.tratar_chave()
        return ''.join([letras[(letras.index(i) - letras.index(j)) % 26]
                        if i in letras and j in letras else i
                        for i, j in zip(self.frase, chave)])

    def encoder(self):
        chave = self.tratar_chave()
        return ''.join([letras[(letras.index(i) + letras.index(j)) % 26]
                        if i in letras and j in letras else i
                        for i, j in zip(self.frase, chave)])


class AsciiShift:
    def __new__(self, frase: str, chave: int):
        """
        Cifra de cesar utilizando caracteres da tabela ASCII entre 33 e 126
        :param str frase: mensagem a ser cifrado ou descifrado
        :param int chave: Chave para cifrar ou descifrar a mensagem
        """
        if not isinstance(chave, int):
            raise TypeError("O parâmetro \'chave\' deve ser do tipo \'int\'")

        return ''.join([chr((ord(i) + chave - 32) % 94 + 32)
                        if 33 < ord(i) < 126 else i
                        for i in frase])