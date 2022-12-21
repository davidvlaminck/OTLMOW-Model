# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kelderpijler(AIMNaamObject, VlakGeometrie):
    """Pijler uitgerust met een kelder voor het herbergen van bewegende delen of onderhoudsvoorzieningen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kelderpijler'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AanhorighedenBrug')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brugdekvoeg')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brug')

        self._funderingsaanzetOnderDeBodemVanDeWaterweg = OTLAttribuut(field=BooleanField,
                                                                       naam='funderingsaanzetOnderDeBodemVanDeWaterweg',
                                                                       label='funderingsaanzet onder de bodem van de waterweg',
                                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kelderpijler.funderingsaanzetOnderDeBodemVanDeWaterweg',
                                                                       definition='Geeft aan of er een funderingsaanzet is onder de bodem van de waterweg, al dan niet.',
                                                                       owner=self)

        self._inOfOpDeRandVanDeWaterweg = OTLAttribuut(field=BooleanField,
                                                       naam='inOfOpDeRandVanDeWaterweg',
                                                       label='in of op de rand van de waterweg',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kelderpijler.inOfOpDeRandVanDeWaterweg',
                                                       definition='Geeft aan of de kelderpijler in of op de rand van de waterweg staat, al dan niet.',
                                                       owner=self)

    @property
    def funderingsaanzetOnderDeBodemVanDeWaterweg(self) -> bool:
        """Geeft aan of er een funderingsaanzet is onder de bodem van de waterweg, al dan niet."""
        return self._funderingsaanzetOnderDeBodemVanDeWaterweg.get_waarde()

    @funderingsaanzetOnderDeBodemVanDeWaterweg.setter
    def funderingsaanzetOnderDeBodemVanDeWaterweg(self, value):
        self._funderingsaanzetOnderDeBodemVanDeWaterweg.set_waarde(value, owner=self)

    @property
    def inOfOpDeRandVanDeWaterweg(self) -> bool:
        """Geeft aan of de kelderpijler in of op de rand van de waterweg staat, al dan niet."""
        return self._inOfOpDeRandVanDeWaterweg.get_waarde()

    @inOfOpDeRandVanDeWaterweg.setter
    def inOfOpDeRandVanDeWaterweg(self, value):
        self._inOfOpDeRandVanDeWaterweg.set_waarde(value, owner=self)
