# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Kokerruimte import Kokerruimte
from ...Classes.Abstracten.PutRelatie import PutRelatie
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlPompKamerFunctie import KlPompKamerFunctie
from ...Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter, KwantWrdInKubiekeMeterWaarden
from ...Datatypes.KwantWrdInMaand import KwantWrdInMaand, KwantWrdInMaandWaarden
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Pompkamer(Kokerruimte, PutRelatie):
    """Elk volume,inclusief de bouwkundige elementen die dit volume bepalen,dat deel uitmaakt van het waterbouwkundig systeem van het pompstation en als zodanig onder water kan staan."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompkamer'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Niveaumeting', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dompelpomp', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Gassensor', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderstel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pompgeleiding', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pomphuis', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schacht', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AndereLaag', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompstation', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingspaal', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', direction='i')  # i = direction: incoming

        self._breedte = OTLAttribuut(field=KwantWrdInMillimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompkamer.breedte',
                                     definition='De breedte van de pompkamer in millimeter, zoals uitgedrukt op het grondplan (eerst vermelde afmeting).',
                                     owner=self)

        self._diepte = OTLAttribuut(field=KwantWrdInMillimeter,
                                    naam='diepte',
                                    label='diepte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompkamer.diepte',
                                    definition='De diepte van de pompkamer in meter, zoals uitgedrukt op het grondplan.',
                                    owner=self)

        self._functie = OTLAttribuut(field=KlPompKamerFunctie,
                                     naam='functie',
                                     label='functie',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompkamer.functie',
                                     definition='De specifieke functie die een pompkamer kan vervullen.',
                                     owner=self)

        self._isExplosieveilig = OTLAttribuut(field=BooleanField,
                                              naam='isExplosieveilig',
                                              label='is explosief veilig',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompkamer.isExplosieveilig',
                                              definition='Geeft aan of de natte pompkelder voldoet aan de ATEX richtlijn.',
                                              owner=self)

        self._isLuchtdichtAfgesloten = OTLAttribuut(field=BooleanField,
                                                    naam='isLuchtdichtAfgesloten',
                                                    label='is luchtdicht afgesloten',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompkamer.isLuchtdichtAfgesloten',
                                                    definition='Geeft aan of de natte pompkelder hermetisch afgesloten is van de omgeving.',
                                                    owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMillimeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompkamer.lengte',
                                    definition='De lengte van de pompkamer in millimeter, zoals uitgedrukt op het grondplan (tweede vermelde afmeting) .',
                                    owner=self)

        self._reinigingsInterval = OTLAttribuut(field=KwantWrdInMaand,
                                                naam='reinigingsInterval',
                                                label='reinigingsinterval',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompkamer.reinigingsInterval',
                                                definition='Termijn uitgedrukt in maanden waarbinnen de reiniging van de pompkamer uitgevoerd dient te worden.',
                                                owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompkamer.technischeFiche',
                                             usagenote='Bestanden van het type xlsx, dwg of pdf.',
                                             kardinaliteit_max='*',
                                             definition='De technische fiche van de pompkamer.',
                                             owner=self)

        self._volume = OTLAttribuut(field=KwantWrdInKubiekeMeter,
                                    naam='volume',
                                    label='volume',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompkamer.volume',
                                    definition='De (maximale) inhoud van de pompkamer.',
                                    owner=self)

    @property
    def breedte(self) -> KwantWrdInMillimeterWaarden:
        """De breedte van de pompkamer in millimeter, zoals uitgedrukt op het grondplan (eerst vermelde afmeting)."""
        return self._breedte.get_waarde()

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def diepte(self) -> KwantWrdInMillimeterWaarden:
        """De diepte van de pompkamer in meter, zoals uitgedrukt op het grondplan."""
        return self._diepte.get_waarde()

    @diepte.setter
    def diepte(self, value):
        self._diepte.set_waarde(value, owner=self)

    @property
    def functie(self) -> str:
        """De specifieke functie die een pompkamer kan vervullen."""
        return self._functie.get_waarde()

    @functie.setter
    def functie(self, value):
        self._functie.set_waarde(value, owner=self)

    @property
    def isExplosieveilig(self) -> bool:
        """Geeft aan of de natte pompkelder voldoet aan de ATEX richtlijn."""
        return self._isExplosieveilig.get_waarde()

    @isExplosieveilig.setter
    def isExplosieveilig(self, value):
        self._isExplosieveilig.set_waarde(value, owner=self)

    @property
    def isLuchtdichtAfgesloten(self) -> bool:
        """Geeft aan of de natte pompkelder hermetisch afgesloten is van de omgeving."""
        return self._isLuchtdichtAfgesloten.get_waarde()

    @isLuchtdichtAfgesloten.setter
    def isLuchtdichtAfgesloten(self, value):
        self._isLuchtdichtAfgesloten.set_waarde(value, owner=self)

    @property
    def lengte(self) -> KwantWrdInMillimeterWaarden:
        """De lengte van de pompkamer in millimeter, zoals uitgedrukt op het grondplan (tweede vermelde afmeting) ."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def reinigingsInterval(self) -> KwantWrdInMaandWaarden:
        """Termijn uitgedrukt in maanden waarbinnen de reiniging van de pompkamer uitgevoerd dient te worden."""
        return self._reinigingsInterval.get_waarde()

    @reinigingsInterval.setter
    def reinigingsInterval(self, value):
        self._reinigingsInterval.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> List[DtcDocumentWaarden]:
        """De technische fiche van de pompkamer."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def volume(self) -> KwantWrdInKubiekeMeterWaarden:
        """De (maximale) inhoud van de pompkamer."""
        return self._volume.get_waarde()

    @volume.setter
    def volume(self, value):
        self._volume.set_waarde(value, owner=self)
