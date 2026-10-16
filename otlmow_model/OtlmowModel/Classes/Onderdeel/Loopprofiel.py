# coding=utf-8
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Loopprofiel(AIMNaamObject, PuntGeometrie):
    """Een dragend profiel dat de werkbreedte van het hijs- en hefwerktuig overspant en dient als rijbaan voor de loopkat, waarbij de uiteinden worden ondersteund door wielen die op de loopbanen rijden of vast bevestigd zijn aan de bouwkundige constructie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Loopprofiel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Balk', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HorizontaleConstructieplaat', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Portiek', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HijsEnHefwerktuig', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Loopkat', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Railconstructie', direction='o')  # o = direction: outgoing

        self._beschikbareLengte = OTLAttribuut(field=KwantWrdInMeter,
                                               naam='beschikbareLengte',
                                               label='beschikbare lengte',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Loopprofiel.beschikbareLengte',
                                               definition='De beschikbare lengte van het loopprofiel waarover een loopkat zich kan verplaatsen.',
                                               owner=self)

    @property
    def beschikbareLengte(self) -> KwantWrdInMeterWaarden:
        """De beschikbare lengte van het loopprofiel waarover een loopkat zich kan verplaatsen."""
        return self._beschikbareLengte.get_waarde()

    @beschikbareLengte.setter
    def beschikbareLengte(self, value):
        self._beschikbareLengte.set_waarde(value, owner=self)
