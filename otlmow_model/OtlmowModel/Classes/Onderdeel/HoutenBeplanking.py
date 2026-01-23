# coding=utf-8
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.HoutenConstructieElement import HoutenConstructieElement
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.IntegerField import IntegerField
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class HoutenBeplanking(HoutenConstructieElement, AIMNaamObject, LijnGeometrie, VlakGeometrie):
    """Beplanking in hout, gebruikt voor constructieve of decoratieve afwerking van bouwelementen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoutenBeplanking'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Balk', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HorizontaleConstructieplaat', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolom', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wand', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#BeweegbareWaterkerendeConstructie', direction='o')  # o = direction: outgoing

        self._aantalLagen = OTLAttribuut(field=IntegerField,
                                         naam='aantalLagen',
                                         label='aantal lagen',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoutenBeplanking.aantalLagen',
                                         definition='Het aantal lagen dat de beplanking bevat.',
                                         owner=self)

        self._isWaterdicht = OTLAttribuut(field=BooleanField,
                                          naam='isWaterdicht',
                                          label='is waterdicht',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoutenBeplanking.isWaterdicht',
                                          definition='Geeft aan of de houten beplanking al dan niet waterdicht is.',
                                          owner=self)

        self._totaleDikte = OTLAttribuut(field=KwantWrdInMillimeter,
                                         naam='totaleDikte',
                                         label='totale dikte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoutenBeplanking.totaleDikte',
                                         definition='De totale dikte (van alle lagen samen) van de houtenbeplanking, uitgedrukt in millimeter.',
                                         owner=self)

    @property
    def aantalLagen(self) -> int:
        """Het aantal lagen dat de beplanking bevat."""
        return self._aantalLagen.get_waarde()

    @aantalLagen.setter
    def aantalLagen(self, value):
        self._aantalLagen.set_waarde(value, owner=self)

    @property
    def isWaterdicht(self) -> bool:
        """Geeft aan of de houten beplanking al dan niet waterdicht is."""
        return self._isWaterdicht.get_waarde()

    @isWaterdicht.setter
    def isWaterdicht(self, value):
        self._isWaterdicht.set_waarde(value, owner=self)

    @property
    def totaleDikte(self) -> KwantWrdInMillimeterWaarden:
        """De totale dikte (van alle lagen samen) van de houtenbeplanking, uitgedrukt in millimeter."""
        return self._totaleDikte.get_waarde()

    @totaleDikte.setter
    def totaleDikte(self, value):
        self._totaleDikte.set_waarde(value, owner=self)
