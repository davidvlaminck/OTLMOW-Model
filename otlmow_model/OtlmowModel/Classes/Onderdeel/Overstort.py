# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.LinkendElement import LinkendElement
from ...Datatypes.KlOverstortMateriaalDrempel import KlOverstortMateriaalDrempel
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW, KwantWrdInMeterTAWWaarden
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Overstort(LinkendElement, VlakGeometrie):
    """Een overstort is een drempel tussen twee kamers waar water vanaf een bepaald peil van de ene naar de andere kamer kan stromen. Tussen twee kamers kunnen een of meerdere overstorten voorkomen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Overstort'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Duikschot', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Overstortrand', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Brandvoorziening', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PutRelatie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', direction='i')  # i = direction: incoming

        self._drempellengte = OTLAttribuut(field=KwantWrdInMillimeter,
                                           naam='drempellengte',
                                           label='breedte',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Overstort.drempellengte',
                                           definition='Drempellengte of breedte van de overstort. Deze wordt gemeten aan de kortste zijde van de drempel.',
                                           owner=self)

        self._materiaalDrempel = OTLAttribuut(field=KlOverstortMateriaalDrempel,
                                              naam='materiaalDrempel',
                                              label='materiaal drempel',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Overstort.materiaalDrempel',
                                              definition='Het gebruikte materiaal voor het vervaardigen van de overstort (drempel).',
                                              owner=self)

        self._peil = OTLAttribuut(field=KwantWrdInMeterTAW,
                                  naam='peil',
                                  label='peil',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Overstort.peil',
                                  definition='Drempelpeil van de overstort. Uitgedrukt in meter-TAW gemeten in het midden van de drempel.',
                                  owner=self)

        self._vrijeHoogte = OTLAttribuut(field=KwantWrdInMeter,
                                         naam='vrijeHoogte',
                                         label='vrije hoogte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Overstort.vrijeHoogte',
                                         definition='De vrije hoogte tussen de overstortdrempel en het plafond van de constructie ter hoogte van de drempel. Voor drempels in leidingen worden de vrije hoogte voor de databank genomen tussen de drempel en de binnenbovenkant buis. Indien er geen sprake is van een vrije hoogte (vb drempels in grachten) wordt dit niet ingevuld.',
                                         owner=self)

    @property
    def drempellengte(self) -> KwantWrdInMillimeterWaarden:
        """Drempellengte of breedte van de overstort. Deze wordt gemeten aan de kortste zijde van de drempel."""
        return self._drempellengte.get_waarde()

    @drempellengte.setter
    def drempellengte(self, value):
        self._drempellengte.set_waarde(value, owner=self)

    @property
    def materiaalDrempel(self) -> str:
        """Het gebruikte materiaal voor het vervaardigen van de overstort (drempel)."""
        return self._materiaalDrempel.get_waarde()

    @materiaalDrempel.setter
    def materiaalDrempel(self, value):
        self._materiaalDrempel.set_waarde(value, owner=self)

    @property
    def peil(self) -> KwantWrdInMeterTAWWaarden:
        """Drempelpeil van de overstort. Uitgedrukt in meter-TAW gemeten in het midden van de drempel."""
        return self._peil.get_waarde()

    @peil.setter
    def peil(self, value):
        self._peil.set_waarde(value, owner=self)

    @property
    def vrijeHoogte(self) -> KwantWrdInMeterWaarden:
        """De vrije hoogte tussen de overstortdrempel en het plafond van de constructie ter hoogte van de drempel. Voor drempels in leidingen worden de vrije hoogte voor de databank genomen tussen de drempel en de binnenbovenkant buis. Indien er geen sprake is van een vrije hoogte (vb drempels in grachten) wordt dit niet ingevuld."""
        return self._vrijeHoogte.get_waarde()

    @vrijeHoogte.setter
    def vrijeHoogte(self, value):
        self._vrijeHoogte.set_waarde(value, owner=self)
