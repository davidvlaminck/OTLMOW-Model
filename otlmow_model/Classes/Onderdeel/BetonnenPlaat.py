# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Onderdeel.BetonnenConstructieObject import BetonnenConstructieObject
from otlmow_model.Datatypes.KlDikteBetonnenPlaat import KlDikteBetonnenPlaat
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class BetonnenPlaat(BetonnenConstructieObject, VlakGeometrie):
    """Een vlak, plat betonnen enkelvoudig constructie-element."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenPlaat'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        BetonnenConstructieObject.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel')

        self._dikte = OTLAttribuut(field=KlDikteBetonnenPlaat,
                                   naam='dikte',
                                   label='dikte',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenPlaat.dikte',
                                   definition='De dikte van de betonnen plaat.',
                                   owner=self)

    @property
    def dikte(self) -> str:
        """De dikte van de betonnen plaat."""
        return self._dikte.get_waarde()

    @dikte.setter
    def dikte(self, value):
        self._dikte.set_waarde(value, owner=self)
