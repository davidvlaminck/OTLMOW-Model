# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.AfwijkendeKantopsluiting import AfwijkendeKantopsluiting
from otlmow_model.BaseClasses.IntegerField import IntegerField


# Generated with OTLClassCreator. To modify: extend, do not edit
class WatergreppelAfw(AfwijkendeKantopsluiting):
    """Afwijkende kantopsluiting, bestemd om water van de verharding op te vangen en af te voeren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WatergreppelAfw'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')

        self._aantalRijenBetonstraatsteen = OTLAttribuut(field=IntegerField,
                                                         naam='aantalRijenBetonstraatsteen',
                                                         label='aantal rijen betonstraatsteen',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WatergreppelAfw.aantalRijenBetonstraatsteen',
                                                         definition='Het aantal rijen betonstraatsteen waaruit de watergreppel is opgebouwd.',
                                                         owner=self)

    @property
    def aantalRijenBetonstraatsteen(self) -> int:
        """Het aantal rijen betonstraatsteen waaruit de watergreppel is opgebouwd."""
        return self._aantalRijenBetonstraatsteen.get_waarde()

    @aantalRijenBetonstraatsteen.setter
    def aantalRijenBetonstraatsteen(self, value):
        self._aantalRijenBetonstraatsteen.set_waarde(value, owner=self)
