# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Bestrating import Bestrating
from ...Datatypes.KlFormaatGebakkenStraatsteen import KlFormaatGebakkenStraatsteen
from ...Datatypes.KlStandaardkwaliteitsklasse import KlStandaardkwaliteitsklasse


# Generated with OTLClassCreator. To modify: extend, do not edit
class BestratingVanGebakkenStraatsteen(Bestrating):
    """Gebakken straatstenen zijn straatstenen, in hoofdzaak vervaardigd uit klei al dan niet gemengd met leem, zand, brandstoffen of andere toeslagstoffen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanGebakkenStraatsteen'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LijnvormigElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VegetatieElement', direction='i')  # i = direction: incoming

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
