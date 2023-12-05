class KeuzelijstWaarde:
    def __init__(self, invulwaarde: str = '', label: str = '', definitie: str = '', objectUri: str = '',
                 status: str = ''):
        self.invulwaarde: str = invulwaarde
        self.label: str = label
        self.definitie: str = definitie
        self.objectUri: str = objectUri
        self.status: str = status

    def __str__(self) -> str:
        if self.status == '' or self.status == 'ingebruik':
            return self.invulwaarde

        return self.invulwaarde + ' (' + self.status + ')'
