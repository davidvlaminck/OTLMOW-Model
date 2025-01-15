# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlBrandwerendeMaatregelen import KlBrandwerendeMaatregelen
from ...Datatypes.KlGebruikersType import KlGebruikersType
from ...Datatypes.KlKokerTypeFundering import KlKokerTypeFundering
from ...Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter, KwantWrdInCentimeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Koker(AIMObject, LijnGeometrie, VlakGeometrie):
    """Een koker is een opdeling van het kokercomplex in de lengte richting, het heeft een doorvoerende functie met een in- en uitgang en eventuele zijgangen, die met een gesloten doorsnede verbonden zijn. """

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Koker'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AanhorigheidKoker', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AndereLaag', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Balk', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HorizontaleConstructieplaat', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kokercomplex', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolom', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Randprofiel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wand', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ConstructieSokkel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingspaal', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kokervoeg', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw', direction='i')  # i = direction: incoming

        self._brandwerendeMaatregelen = OTLAttribuut(field=KlBrandwerendeMaatregelen,
                                                     naam='brandwerendeMaatregelen',
                                                     label='type brandwerendheid',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Koker.brandwerendeMaatregelen',
                                                     definition='Keuzelijst voor aan te geven welk type brandwerendheid nodig is.',
                                                     owner=self)

        self._gebruikersInDeKoker = OTLAttribuut(field=KlGebruikersType,
                                                 naam='gebruikersInDeKoker',
                                                 label='gebruikers in de koker',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Koker.gebruikersInDeKoker',
                                                 definition='Geeft de type gebruikers aan die kunnen voorkomen in de desbetreffende koker.',
                                                 owner=self)

        self._maximaleVrijeHoogte = OTLAttribuut(field=KwantWrdInCentimeter,
                                                 naam='maximaleVrijeHoogte',
                                                 label='maximale vrije hoogte',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Koker.maximaleVrijeHoogte',
                                                 definition='Hoogte die door gebruikers kan gehanteerd worden voor vervoer, rekening houdend met voorwerpen die aan de koker bevestigd zijn.',
                                                 owner=self)

        self._ontwerpbelasting = OTLAttribuut(field=DtcDocument,
                                              naam='ontwerpbelasting',
                                              label='ontwerpbelasting',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Koker.ontwerpbelasting',
                                              definition='De ontwerpbelasting is de maximale belasting die een constructie kan opnemen zonder te bezwijken.',
                                              owner=self)

        self._typeFundering = OTLAttribuut(field=KlKokerTypeFundering,
                                           naam='typeFundering',
                                           label='type fundering',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Koker.typeFundering',
                                           definition='Het type fundering dat gebruikt wordt voor de koker.',
                                           owner=self)

    @property
    def brandwerendeMaatregelen(self) -> str:
        """Keuzelijst voor aan te geven welk type brandwerendheid nodig is."""
        return self._brandwerendeMaatregelen.get_waarde()

    @brandwerendeMaatregelen.setter
    def brandwerendeMaatregelen(self, value):
        self._brandwerendeMaatregelen.set_waarde(value, owner=self)

    @property
    def gebruikersInDeKoker(self) -> str:
        """Geeft de type gebruikers aan die kunnen voorkomen in de desbetreffende koker."""
        return self._gebruikersInDeKoker.get_waarde()

    @gebruikersInDeKoker.setter
    def gebruikersInDeKoker(self, value):
        self._gebruikersInDeKoker.set_waarde(value, owner=self)

    @property
    def maximaleVrijeHoogte(self) -> KwantWrdInCentimeterWaarden:
        """Hoogte die door gebruikers kan gehanteerd worden voor vervoer, rekening houdend met voorwerpen die aan de koker bevestigd zijn."""
        return self._maximaleVrijeHoogte.get_waarde()

    @maximaleVrijeHoogte.setter
    def maximaleVrijeHoogte(self, value):
        self._maximaleVrijeHoogte.set_waarde(value, owner=self)

    @property
    def ontwerpbelasting(self) -> DtcDocumentWaarden:
        """De ontwerpbelasting is de maximale belasting die een constructie kan opnemen zonder te bezwijken."""
        return self._ontwerpbelasting.get_waarde()

    @ontwerpbelasting.setter
    def ontwerpbelasting(self, value):
        self._ontwerpbelasting.set_waarde(value, owner=self)

    @property
    def typeFundering(self) -> str:
        """Het type fundering dat gebruikt wordt voor de koker."""
        return self._typeFundering.get_waarde()

    @typeFundering.setter
    def typeFundering(self, value):
        self._typeFundering.set_waarde(value, owner=self)
