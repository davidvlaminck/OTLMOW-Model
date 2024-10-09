# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcBurgerlijkeKlasseBrug import DtcBurgerlijkeKlasseBrug, DtcBurgerlijkeKlasseBrugWaarden
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter, KwantWrdInVierkanteMeterWaarden
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Brug(AIMNaamObject, VlakGeometrie):
    """Een beweegbare, vaste of drijvende verbinding voor het verkeer tussen twee punten, die door water of iets anders gescheiden zijn."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brug'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kelderlandhoofd', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kelderpijler', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Landhoofd', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pijler', direction='i')  # i = direction: incoming

        self._burgerlijkeKlasse = OTLAttribuut(field=DtcBurgerlijkeKlasseBrug,
                                               naam='burgerlijkeKlasse',
                                               label='burgerlijke klasse',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brug.burgerlijkeKlasse',
                                               definition='Maximaal toegelaten belasting door gestandariseerde assen, meestal uitgedrukt als totaalgewicht / aslast in kN. Dit dient als ontwerpbelasting en om te oordelen of reële konvooien de brug kunnen overschrijden.',
                                               owner=self)

        self._dwarseIndelingOpBrug = OTLAttribuut(field=DtcDocument,
                                                  naam='dwarseIndelingOpBrug',
                                                  label='dwarse indeling op de brug',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brug.dwarseIndelingOpBrug',
                                                  definition='Een dwarse indeling op de brug (wie maakt gebruik van welk deel van de brug,...). Dit wordt weergegeven in een schets of een plan.',
                                                  owner=self)

        self._ontwerpbelasting = OTLAttribuut(field=StringField,
                                              naam='ontwerpbelasting',
                                              label='ontwerpbelasting',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brug.ontwerpbelasting',
                                              definition='De draagkracht waarvoor de brug ontworpen is.',
                                              owner=self)

        self._totaleBreedteBrug = OTLAttribuut(field=KwantWrdInMeter,
                                               naam='totaleBreedteBrug',
                                               label='totale breedte brug',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brug.totaleBreedteBrug',
                                               definition='De totale breedte van de hele brug, in meter.',
                                               owner=self)

        self._totaleLengteBrug = OTLAttribuut(field=KwantWrdInMeter,
                                              naam='totaleLengteBrug',
                                              label='totale lengte brug',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brug.totaleLengteBrug',
                                              definition='De lengte, uitgedrukt in meter, van uiterste brugdekvoeg tot uiterste brugdekvoeg (gemeten over de ganse lengte van de brug).',
                                              owner=self)

        self._totaleOppervlakteBrug = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                                   naam='totaleOppervlakteBrug',
                                                   label='totale oppervlakte brug',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brug.totaleOppervlakteBrug',
                                                   definition='De oppervlakte van de brug, uitgedrukt in vierkante meter. Dit is meestal de breedte maal lengte.',
                                                   owner=self)

    @property
    def burgerlijkeKlasse(self) -> DtcBurgerlijkeKlasseBrugWaarden:
        """Maximaal toegelaten belasting door gestandariseerde assen, meestal uitgedrukt als totaalgewicht / aslast in kN. Dit dient als ontwerpbelasting en om te oordelen of reële konvooien de brug kunnen overschrijden."""
        return self._burgerlijkeKlasse.get_waarde()

    @burgerlijkeKlasse.setter
    def burgerlijkeKlasse(self, value):
        self._burgerlijkeKlasse.set_waarde(value, owner=self)

    @property
    def dwarseIndelingOpBrug(self) -> DtcDocumentWaarden:
        """Een dwarse indeling op de brug (wie maakt gebruik van welk deel van de brug,...). Dit wordt weergegeven in een schets of een plan."""
        return self._dwarseIndelingOpBrug.get_waarde()

    @dwarseIndelingOpBrug.setter
    def dwarseIndelingOpBrug(self, value):
        self._dwarseIndelingOpBrug.set_waarde(value, owner=self)

    @property
    def ontwerpbelasting(self) -> str:
        """De draagkracht waarvoor de brug ontworpen is."""
        return self._ontwerpbelasting.get_waarde()

    @ontwerpbelasting.setter
    def ontwerpbelasting(self, value):
        self._ontwerpbelasting.set_waarde(value, owner=self)

    @property
    def totaleBreedteBrug(self) -> KwantWrdInMeterWaarden:
        """De totale breedte van de hele brug, in meter."""
        return self._totaleBreedteBrug.get_waarde()

    @totaleBreedteBrug.setter
    def totaleBreedteBrug(self, value):
        self._totaleBreedteBrug.set_waarde(value, owner=self)

    @property
    def totaleLengteBrug(self) -> KwantWrdInMeterWaarden:
        """De lengte, uitgedrukt in meter, van uiterste brugdekvoeg tot uiterste brugdekvoeg (gemeten over de ganse lengte van de brug)."""
        return self._totaleLengteBrug.get_waarde()

    @totaleLengteBrug.setter
    def totaleLengteBrug(self, value):
        self._totaleLengteBrug.set_waarde(value, owner=self)

    @property
    def totaleOppervlakteBrug(self) -> KwantWrdInVierkanteMeterWaarden:
        """De oppervlakte van de brug, uitgedrukt in vierkante meter. Dit is meestal de breedte maal lengte."""
        return self._totaleOppervlakteBrug.get_waarde()

    @totaleOppervlakteBrug.setter
    def totaleOppervlakteBrug(self, value):
        self._totaleOppervlakteBrug.set_waarde(value, owner=self)
