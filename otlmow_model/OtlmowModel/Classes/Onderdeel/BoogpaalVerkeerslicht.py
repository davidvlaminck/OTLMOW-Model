# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.VRIDraagconstructie import VRIDraagconstructie
from ...Datatypes.KlBoogpaalType import KlBoogpaalType
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class BoogpaalVerkeerslicht(VRIDraagconstructie, PuntGeometrie):
    """Paal bestemd voor het bevestigen van seinlantaarns boven het wegdek. Geschikt voor het bevestigen van ten hoogste 4 seinlantaarns van het type 300 en van één of meerdere lantaarns van het type 200 op de paalschacht. De vrije hoogte ten opzichte van het wegdek bedraagt onder de lantaarns 6.500 millimeter voor palen met grote draagwijdte (7,5 meter overspanning) en 5.500 millimeter voor de palen met middelgrote draagwijdte (3,5 meter overspanning)."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BoogpaalVerkeerslicht'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang', direction='u')  # u = unidirectional

        self._typeBoogpaal = OTLAttribuut(field=KlBoogpaalType,
                                          naam='typeBoogpaal',
                                          label='type boogpaal',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BoogpaalVerkeerslicht.typeBoogpaal',
                                          definition='Draagwijdte van de boogpaal.',
                                          owner=self)

    @property
    def typeBoogpaal(self) -> str:
        """Draagwijdte van de boogpaal."""
        return self._typeBoogpaal.get_waarde()

    @typeBoogpaal.setter
    def typeBoogpaal(self, value):
        self._typeBoogpaal.set_waarde(value, owner=self)
