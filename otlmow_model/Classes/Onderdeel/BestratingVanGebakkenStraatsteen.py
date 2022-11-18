# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.Bestrating import Bestrating
from otlmow_model.Datatypes.KlFormaatGebakkenStraatsteen import KlFormaatGebakkenStraatsteen
from otlmow_model.Datatypes.KlStandaardkwaliteitsklasse import KlStandaardkwaliteitsklasse


# Generated with OTLClassCreator. To modify: extend, do not edit
class BestratingVanGebakkenStraatsteen(Bestrating):
    """Gebakken straatstenen zijn straatstenen, in hoofdzaak vervaardigd uit klei al dan niet gemengd met leem, zand, brandstoffen of andere toeslagstoffen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanGebakkenStraatsteen'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair')

        self._formaatVanBestratingselement = OTLAttribuut(field=KlFormaatGebakkenStraatsteen,
                                                          naam='formaatVanBestratingselement',
                                                          label='formaat van bestratingselement',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanGebakkenStraatsteen.formaatVanBestratingselement',
                                                          definition='Bepaling van de afmeting van het bestratingselement.',
                                                          owner=self)

        self._standaardkwaliteitsklasse = OTLAttribuut(field=KlStandaardkwaliteitsklasse,
                                                       naam='standaardkwaliteitsklasse',
                                                       label='standaardkwaliteitsklasse',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanGebakkenStraatsteen.standaardkwaliteitsklasse',
                                                       definition='De standaardkwaliteitsklasse volgens PTV 910.',
                                                       owner=self)

    @property
    def formaatVanBestratingselement(self) -> str:
        """Bepaling van de afmeting van het bestratingselement."""
        return self._formaatVanBestratingselement.get_waarde()

    @formaatVanBestratingselement.setter
    def formaatVanBestratingselement(self, value):
        self._formaatVanBestratingselement.set_waarde(value, owner=self)

    @property
    def standaardkwaliteitsklasse(self) -> str:
        """De standaardkwaliteitsklasse volgens PTV 910."""
        return self._standaardkwaliteitsklasse.get_waarde()

    @standaardkwaliteitsklasse.setter
    def standaardkwaliteitsklasse(self, value):
        self._standaardkwaliteitsklasse.set_waarde(value, owner=self)
