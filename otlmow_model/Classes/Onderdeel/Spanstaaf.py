# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from otlmow_model.Datatypes.KwantWrdInVierkanteMillimeter import KwantWrdInVierkanteMillimeter, KwantWrdInVierkanteMillimeterWaarden
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Spanstaaf(AIMNaamObject, LijnGeometrie):
    """Een staaf die gebruikt kan worden als externe naspanning."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spanstaaf'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        LijnGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#ExterneNaspanning')

        self._diameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                      naam='diameter',
                                      label='diameter',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spanstaaf.diameter',
                                      definition='De diameter van de spanstaaf, uitgedrukt in millimeter.',
                                      owner=self)

        self._sectieSpanstaaf = OTLAttribuut(field=KwantWrdInVierkanteMillimeter,
                                             naam='sectieSpanstaaf',
                                             label='sectie spanstaaf',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spanstaaf.sectieSpanstaaf',
                                             definition='De staafdoorsnede, uitgedrukt in vierkante millimeter.',
                                             owner=self)

    @property
    def diameter(self) -> KwantWrdInMillimeterWaarden:
        """De diameter van de spanstaaf, uitgedrukt in millimeter."""
        return self._diameter.get_waarde()

    @diameter.setter
    def diameter(self, value):
        self._diameter.set_waarde(value, owner=self)

    @property
    def sectieSpanstaaf(self) -> KwantWrdInVierkanteMillimeterWaarden:
        """De staafdoorsnede, uitgedrukt in vierkante millimeter."""
        return self._sectieSpanstaaf.get_waarde()

    @sectieSpanstaaf.setter
    def sectieSpanstaaf(self, value):
        self._sectieSpanstaaf.set_waarde(value, owner=self)
