# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.SerienummerObject import SerienummerObject
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlAlgMateriaal import KlAlgMateriaal
from ...Datatypes.KlBewegingssensorDetectiemethode import KlBewegingssensorDetectiemethode
from ...Datatypes.KlBewegingssensorMerk import KlBewegingssensorMerk
from ...Datatypes.KlBewegingssensorModelnaam import KlBewegingssensorModelnaam
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bewegingssensor(SerienummerObject, AIMNaamObject, PuntGeometrie):
    """Een bewegingsmelder of aanwezigheidsmelder detecteert de beweging of aanwezigheid van een persoon,dier of object binnen een bepaalde zone. Het resultaat wordt omgezet in een uitleesbaar signaal."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bewegingssensor'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Draagconstructie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wilddetectiezone', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', direction='i')  # i = direction: incoming

        self._detectieAfstand = OTLAttribuut(field=KwantWrdInMeter,
                                             naam='detectieAfstand',
                                             label='detectie afstand',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bewegingssensor.detectieAfstand',
                                             definition='De detectieafstand of het bereik van de bewegingssensor geeft de maximale afstand in meter aan voor de detectie van aanwezigheid, tov het toestel.',
                                             owner=self)

        self._detectiemethode = OTLAttribuut(field=KlBewegingssensorDetectiemethode,
                                             naam='detectiemethode',
                                             label='detectiemethode',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bewegingssensor.detectiemethode',
                                             definition='De methode waarvolgens de beweging of aanwezigheid gedetecteerd wordt.',
                                             owner=self)

        self._isBuiten = OTLAttribuut(field=BooleanField,
                                      naam='isBuiten',
                                      label='is buiten',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bewegingssensor.isBuiten',
                                      definition='Geeft aan of de bewegingssensor binnen of buiten opgesteld is.',
                                      owner=self)

        self._materiaalBehuizing = OTLAttribuut(field=KlAlgMateriaal,
                                                naam='materiaalBehuizing',
                                                label='materiaal behuizing',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bewegingssensor.materiaalBehuizing',
                                                definition='Het materiaal waaruit de behuizing van de sensor vervaardigd is.',
                                                owner=self)

        self._merk = OTLAttribuut(field=KlBewegingssensorMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bewegingssensor.merk',
                                  definition='De merknaam van de bewgingssensor.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlBewegingssensorModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bewegingssensor.modelnaam',
                                       definition='De modelnaam van de bewegingssensor.',
                                       owner=self)

        self._opstelHoogte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='opstelHoogte',
                                          label='opstelhoogte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bewegingssensor.opstelHoogte',
                                          definition='De hoogte waarop de beweginssensor opgesteld is.',
                                          owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bewegingssensor.technischeFiche',
                                             definition='De technische fiche van de bewegingssensor.',
                                             owner=self)

    @property
    def detectieAfstand(self) -> KwantWrdInMeterWaarden:
        """De detectieafstand of het bereik van de bewegingssensor geeft de maximale afstand in meter aan voor de detectie van aanwezigheid, tov het toestel."""
        return self._detectieAfstand.get_waarde()

    @detectieAfstand.setter
    def detectieAfstand(self, value):
        self._detectieAfstand.set_waarde(value, owner=self)

    @property
    def detectiemethode(self) -> str:
        """De methode waarvolgens de beweging of aanwezigheid gedetecteerd wordt."""
        return self._detectiemethode.get_waarde()

    @detectiemethode.setter
    def detectiemethode(self, value):
        self._detectiemethode.set_waarde(value, owner=self)

    @property
    def isBuiten(self) -> bool:
        """Geeft aan of de bewegingssensor binnen of buiten opgesteld is."""
        return self._isBuiten.get_waarde()

    @isBuiten.setter
    def isBuiten(self, value):
        self._isBuiten.set_waarde(value, owner=self)

    @property
    def materiaalBehuizing(self) -> str:
        """Het materiaal waaruit de behuizing van de sensor vervaardigd is."""
        return self._materiaalBehuizing.get_waarde()

    @materiaalBehuizing.setter
    def materiaalBehuizing(self, value):
        self._materiaalBehuizing.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """De merknaam van de bewgingssensor."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de bewegingssensor."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def opstelHoogte(self) -> KwantWrdInMeterWaarden:
        """De hoogte waarop de beweginssensor opgesteld is."""
        return self._opstelHoogte.get_waarde()

    @opstelHoogte.setter
    def opstelHoogte(self, value):
        self._opstelHoogte.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van de bewegingssensor."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
