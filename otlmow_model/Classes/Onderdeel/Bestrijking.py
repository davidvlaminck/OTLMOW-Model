# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.AndereLaag import AndereLaag
from otlmow_model.Datatypes.KlBestrijkingKaliber import KlBestrijkingKaliber
from otlmow_model.Datatypes.KlBestrijkingProductfamilie import KlBestrijkingProductfamilie
from otlmow_model.Datatypes.KlBestrijkingsoort import KlBestrijkingsoort
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bestrijking(AndereLaag, VlakGeometrie):
    """Een bestrijking bestaat in het sproeien op een verharding of een fundering van één of twee eenvormige lagen bindmiddel met een geschikte viscositeit."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bestrijking'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair')

        self._kaliber = OTLAttribuut(field=KlBestrijkingKaliber,
                                     naam='kaliber',
                                     label='kaliber',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bestrijking.kaliber',
                                     definition='De korrelmaat gebruikt bij de bestrijking.',
                                     owner=self)

        self._productfamilie = OTLAttribuut(field=KlBestrijkingProductfamilie,
                                            naam='productfamilie',
                                            label='productfamilie',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bestrijking.productfamilie',
                                            definition='Bepaling tot welke productfamilie de bestrijking behoort.',
                                            owner=self)

        self._soort = OTLAttribuut(field=KlBestrijkingsoort,
                                   naam='soort',
                                   label='soort',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bestrijking.soort',
                                   definition='De soort bestrijking.',
                                   owner=self)

    @property
    def kaliber(self) -> str:
        """De korrelmaat gebruikt bij de bestrijking."""
        return self._kaliber.get_waarde()

    @kaliber.setter
    def kaliber(self, value):
        self._kaliber.set_waarde(value, owner=self)

    @property
    def productfamilie(self) -> str:
        """Bepaling tot welke productfamilie de bestrijking behoort."""
        return self._productfamilie.get_waarde()

    @productfamilie.setter
    def productfamilie(self, value):
        self._productfamilie.set_waarde(value, owner=self)

    @property
    def soort(self) -> str:
        """De soort bestrijking."""
        return self._soort.get_waarde()

    @soort.setter
    def soort(self, value):
        self._soort.set_waarde(value, owner=self)
