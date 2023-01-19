# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.KlTypeLandhoofd import KlTypeLandhoofd
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Landhoofd(AIMNaamObject, VlakGeometrie):
    """Eindsteunpunt van een brug die de overgang vormt naar het achterliggend grondlichaam én als hoofdfunctie heeft de brug te ondersteunen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Landhoofd'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AanhorighedenBrug')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brugdekvoeg')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brug')

        self._funderingsAanzetOnderDeBodemVanDeWaterweg = OTLAttribuut(field=BooleanField,
                                                                       naam='funderingsAanzetOnderDeBodemVanDeWaterweg',
                                                                       label='funderingsaanzet onder de bodem van de waterweg',
                                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Landhoofd.funderingsAanzetOnderDeBodemVanDeWaterweg',
                                                                       definition='Geeft aan of er een funderingsaanzet is onder de bodem van de waterweg, al dan niet.',
                                                                       owner=self)

        self._inOfOpDeRandVanDeWaterweg = OTLAttribuut(field=BooleanField,
                                                       naam='inOfOpDeRandVanDeWaterweg',
                                                       label='in of op de rand van de waterweg',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Landhoofd.inOfOpDeRandVanDeWaterweg',
                                                       definition='Geeft aan of het landhoofd in of op de rand van de waterweg staat, al dan niet.',
                                                       owner=self)

        self._typeLandhoofd = OTLAttribuut(field=KlTypeLandhoofd,
                                           naam='typeLandhoofd',
                                           label='type landhoofd',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Landhoofd.typeLandhoofd',
                                           definition='Het soort landhoofd.',
                                           owner=self)

    @property
    def funderingsAanzetOnderDeBodemVanDeWaterweg(self) -> bool:
        """Geeft aan of er een funderingsaanzet is onder de bodem van de waterweg, al dan niet."""
        return self._funderingsAanzetOnderDeBodemVanDeWaterweg.get_waarde()

    @funderingsAanzetOnderDeBodemVanDeWaterweg.setter
    def funderingsAanzetOnderDeBodemVanDeWaterweg(self, value):
        self._funderingsAanzetOnderDeBodemVanDeWaterweg.set_waarde(value, owner=self)

    @property
    def inOfOpDeRandVanDeWaterweg(self) -> bool:
        """Geeft aan of het landhoofd in of op de rand van de waterweg staat, al dan niet."""
        return self._inOfOpDeRandVanDeWaterweg.get_waarde()

    @inOfOpDeRandVanDeWaterweg.setter
    def inOfOpDeRandVanDeWaterweg(self, value):
        self._inOfOpDeRandVanDeWaterweg.set_waarde(value, owner=self)

    @property
    def typeLandhoofd(self) -> str:
        """Het soort landhoofd."""
        return self._typeLandhoofd.get_waarde()

    @typeLandhoofd.setter
    def typeLandhoofd(self, value):
        self._typeLandhoofd.set_waarde(value, owner=self)
