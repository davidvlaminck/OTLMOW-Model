# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AanhorigheidSluisStuw import AanhorigheidSluisStuw
from ...Classes.Abstracten.Toegangselement import Toegangselement
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcAfmetingBxhInM import DtcAfmetingBxhInM, DtcAfmetingBxhInMWaarden
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlDeurFabrikant import KlDeurFabrikant
from ...Datatypes.KlDeurHandgreeptype import KlDeurHandgreeptype
from ...Datatypes.KlDeurType import KlDeurType
from ...Datatypes.KlToegangsdeurTypeOpening import KlToegangsdeurTypeOpening
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from ...Datatypes.KwantWrdInSeconde import KwantWrdInSeconde, KwantWrdInSecondeWaarden
from ...Datatypes.KwantWrdInUur import KwantWrdInUur, KwantWrdInUurWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Deur(AanhorigheidSluisStuw, Toegangselement, AIMNaamObject, PuntGeometrie):
    """Een beweegbaar element ter afsluiting van een ruimte. In een gebouw is een deur meestal bevestigd in een kozijn,dat weer in een muur of wand is aangebracht."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Deur'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wand', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aanstraalverlichting', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contourverlichting', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pictogram', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GeluidwerendeConstructie', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Hulppost', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Vluchtganginrichting', direction='o')  # o = direction: outgoing

        self._afmetingDeuropening = OTLAttribuut(field=DtcAfmetingBxhInM,
                                                 naam='afmetingDeuropening',
                                                 label='afmeting deuropening',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Deur.afmetingDeuropening',
                                                 definition='Afmeting van de vrije ruimte die ontstaat wanneer de deur volledig geopend is.',
                                                 owner=self)

        self._brandweerstand = OTLAttribuut(field=KwantWrdInUur,
                                            naam='brandweerstand',
                                            label='brandweerstand',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Deur.brandweerstand',
                                            definition='Brandwerendheid is een maat voor de tijd die een constructie heeft voor dat deze bezwijkt onder invloed van een brand.',
                                            owner=self)

        self._breedte = OTLAttribuut(field=KwantWrdInMillimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Deur.breedte',
                                     definition='De afmeting van de rechtopstaande deur gemeten van de ene zijkant naar de andere.',
                                     owner=self)

        self._dikte = OTLAttribuut(field=KwantWrdInMillimeter,
                                   naam='dikte',
                                   label='dikte',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Deur.dikte',
                                   definition='De dikte van de deur gemeten van de ene buitenzijde van de deur tot de andere.',
                                   owner=self)

        self._fabrikant = OTLAttribuut(field=KlDeurFabrikant,
                                       naam='fabrikant',
                                       label='fabrikant',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Deur.fabrikant',
                                       definition='Naam van de producent van de deur.',
                                       owner=self)

        self._handgreeptype = OTLAttribuut(field=KlDeurHandgreeptype,
                                           naam='handgreeptype',
                                           label='handgreeptype',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Deur.handgreeptype',
                                           definition='Soort greep aan waarmee de deur geopend wordt.',
                                           owner=self)

        self._hoogte = OTLAttribuut(field=KwantWrdInMillimeter,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Deur.hoogte',
                                    definition='De afmeting van de rechtopstaande deur gemeten van de onderkant tot de bovenkant.',
                                    owner=self)

        self._isWaterdicht = OTLAttribuut(field=BooleanField,
                                          naam='isWaterdicht',
                                          label='is waterdicht',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Deur.isWaterdicht',
                                          definition='Geeft aan of de deur al dan niet waterdicht is.',
                                          owner=self)

        self._ophangconstructie = OTLAttribuut(field=DtcDocument,
                                               naam='ophangconstructie',
                                               label='ophangconstructie',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Deur.ophangconstructie',
                                               definition='Documentatie met betrekking tot de manier waarop de deur met het kozijn bevestigd is aan de ruimte waartoe ze toegang biedt.',
                                               owner=self)

        self._sluitingstijd = OTLAttribuut(field=KwantWrdInSeconde,
                                           naam='sluitingstijd',
                                           label='sluitingstijd',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Deur.sluitingstijd',
                                           definition='Duurtijd voor het automatische sluiten van een zelfsluitende deur die volledig open staat.',
                                           owner=self)

        self._typeDeur = OTLAttribuut(field=KlDeurType,
                                      naam='typeDeur',
                                      label='type deur',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Deur.typeDeur',
                                      kardinaliteit_max='*',
                                      definition='Aanduiding tot welk type de deur behoort.',
                                      owner=self)

        self._typeOpening = OTLAttribuut(field=KlToegangsdeurTypeOpening,
                                         naam='typeOpening',
                                         label='type opening',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Deur.typeOpening',
                                         definition='Geeft aan hoe de deur in de af te sluiten ruimte draait of schuift.',
                                         owner=self)

    @property
    def afmetingDeuropening(self) -> DtcAfmetingBxhInMWaarden:
        """Afmeting van de vrije ruimte die ontstaat wanneer de deur volledig geopend is."""
        return self._afmetingDeuropening.get_waarde()

    @afmetingDeuropening.setter
    def afmetingDeuropening(self, value):
        self._afmetingDeuropening.set_waarde(value, owner=self)

    @property
    def brandweerstand(self) -> KwantWrdInUurWaarden:
        """Brandwerendheid is een maat voor de tijd die een constructie heeft voor dat deze bezwijkt onder invloed van een brand."""
        return self._brandweerstand.get_waarde()

    @brandweerstand.setter
    def brandweerstand(self, value):
        self._brandweerstand.set_waarde(value, owner=self)

    @property
    def breedte(self) -> KwantWrdInMillimeterWaarden:
        """De afmeting van de rechtopstaande deur gemeten van de ene zijkant naar de andere."""
        return self._breedte.get_waarde()

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def dikte(self) -> KwantWrdInMillimeterWaarden:
        """De dikte van de deur gemeten van de ene buitenzijde van de deur tot de andere."""
        return self._dikte.get_waarde()

    @dikte.setter
    def dikte(self, value):
        self._dikte.set_waarde(value, owner=self)

    @property
    def fabrikant(self) -> str:
        """Naam van de producent van de deur."""
        return self._fabrikant.get_waarde()

    @fabrikant.setter
    def fabrikant(self, value):
        self._fabrikant.set_waarde(value, owner=self)

    @property
    def handgreeptype(self) -> str:
        """Soort greep aan waarmee de deur geopend wordt."""
        return self._handgreeptype.get_waarde()

    @handgreeptype.setter
    def handgreeptype(self, value):
        self._handgreeptype.set_waarde(value, owner=self)

    @property
    def hoogte(self) -> KwantWrdInMillimeterWaarden:
        """De afmeting van de rechtopstaande deur gemeten van de onderkant tot de bovenkant."""
        return self._hoogte.get_waarde()

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self)

    @property
    def isWaterdicht(self) -> bool:
        """Geeft aan of de deur al dan niet waterdicht is."""
        return self._isWaterdicht.get_waarde()

    @isWaterdicht.setter
    def isWaterdicht(self, value):
        self._isWaterdicht.set_waarde(value, owner=self)

    @property
    def ophangconstructie(self) -> DtcDocumentWaarden:
        """Documentatie met betrekking tot de manier waarop de deur met het kozijn bevestigd is aan de ruimte waartoe ze toegang biedt."""
        return self._ophangconstructie.get_waarde()

    @ophangconstructie.setter
    def ophangconstructie(self, value):
        self._ophangconstructie.set_waarde(value, owner=self)

    @property
    def sluitingstijd(self) -> KwantWrdInSecondeWaarden:
        """Duurtijd voor het automatische sluiten van een zelfsluitende deur die volledig open staat."""
        return self._sluitingstijd.get_waarde()

    @sluitingstijd.setter
    def sluitingstijd(self, value):
        self._sluitingstijd.set_waarde(value, owner=self)

    @property
    def typeDeur(self) -> List[str]:
        """Aanduiding tot welk type de deur behoort."""
        return self._typeDeur.get_waarde()

    @typeDeur.setter
    def typeDeur(self, value):
        self._typeDeur.set_waarde(value, owner=self)

    @property
    def typeOpening(self) -> str:
        """Geeft aan hoe de deur in de af te sluiten ruimte draait of schuift."""
        return self._typeOpening.get_waarde()

    @typeOpening.setter
    def typeOpening(self, value):
        self._typeOpening.set_waarde(value, owner=self)
