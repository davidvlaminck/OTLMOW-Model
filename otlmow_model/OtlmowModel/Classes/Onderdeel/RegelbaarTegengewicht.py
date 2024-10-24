# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlRegelbaarTegengewichtMateriaal import KlRegelbaarTegengewichtMateriaal
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class RegelbaarTegengewicht(AIMNaamObject, PuntGeometrie):
    """Het regelbaar tegengewicht betreft de hoeveelheid massa die relatief eenvoudig kan worden aangepast om een beweegbaar constructieonderdeel vrij nauwkeurig te balanceren; vaak bevindt dit zich in één of meerdere tegengewichtkisten. De hoeveelheid te plaatsen massa wordt bepaald door de vooropgestelde mate van onevenwicht. De massa kan bestaan uit blokken/staven/platen/puin van beton, steen, staal, gietijzer of lood."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RegelbaarTegengewicht'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Balans', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugligger', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Hefportiek', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Heftoren', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Tegengewichtkist', direction='o')  # o = direction: outgoing

        self._materiaal = OTLAttribuut(field=KlRegelbaarTegengewichtMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RegelbaarTegengewicht.materiaal',
                                       definition='Het gebruikte materiaal van een regelbaar tegengewicht.',
                                       owner=self)

    @property
    def materiaal(self) -> str:
        """Het gebruikte materiaal van een regelbaar tegengewicht."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)
