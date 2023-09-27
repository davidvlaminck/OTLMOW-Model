# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.GrazigeVegetatie import GrazigeVegetatie
from otlmow_model.Datatypes.KlNSB import KlNSB
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ruigte(GrazigeVegetatie, VlakGeometrie):
    """Terrein of zoomvegetatie gedomineerd door ruigtekruiden of riet,die niet jaarlijks gemaaid wordt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ruigte'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBeheer', target='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerGrazigeVegetatie')

        self._natuurstreefbeeld = OTLAttribuut(field=KlNSB,
                                               naam='natuurstreefbeeld',
                                               label='natuurstreefbeeld',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ruigte.natuurstreefbeeld',
                                               definition='Een natuurstreefbeeld is een nagestreefd biotoop, mozaïek van biotopen of een leefgebied van een soort dat je wil behouden of verkrijgen via een goed natuurbeheer. In het definitief plan van type twee, drie of vier wordt het ecologisch einddoel vastgesteld aan de hand van natuurstreefbeelden.',
                                               owner=self)

    @property
    def natuurstreefbeeld(self) -> str:
        """Een natuurstreefbeeld is een nagestreefd biotoop, mozaïek van biotopen of een leefgebied van een soort dat je wil behouden of verkrijgen via een goed natuurbeheer. In het definitief plan van type twee, drie of vier wordt het ecologisch einddoel vastgesteld aan de hand van natuurstreefbeelden."""
        return self._natuurstreefbeeld.get_waarde()

    @natuurstreefbeeld.setter
    def natuurstreefbeeld(self, value):
        self._natuurstreefbeeld.set_waarde(value, owner=self)
