# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KlTankKleur import KlTankKleur
from otlmow_model.Datatypes.KlTankMateriaal import KlTankMateriaal
from otlmow_model.Datatypes.KlTankMerk import KlTankMerk
from otlmow_model.Datatypes.KlTankModelnaam import KlTankModelnaam
from otlmow_model.Datatypes.KlTankOpstelling import KlTankOpstelling
from otlmow_model.Datatypes.KlTankVorm import KlTankVorm
from otlmow_model.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter, KwantWrdInCentimeterWaarden
from otlmow_model.Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter, KwantWrdInKubiekeMeterWaarden
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Tank(AIMNaamObject, VlakGeometrie):
    """Een constructie voor het opslaan van goederen, typisch in vloeibare of gasvormige toestand, zoals water, brandstof, aardgas, lucht, etc."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tank'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Niveaumeting')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Zoutbijlaadplaats')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Persleiding')

        self._diameter = OTLAttribuut(field=KwantWrdInCentimeter,
                                      naam='diameter',
                                      label='diameter',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tank.diameter',
                                      definition='De diameter in centimeter van de tank.',
                                      owner=self)

        self._heeftTrapconstructie = OTLAttribuut(field=BooleanField,
                                                  naam='heeftTrapconstructie',
                                                  label='heeft trapconstructie',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tank.heeftTrapconstructie',
                                                  definition='Geeft aan of het object al dan niet een trapconstructie bevat.',
                                                  owner=self)

        self._kleur = OTLAttribuut(field=KlTankKleur,
                                   naam='kleur',
                                   label='kleur',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tank.kleur',
                                   definition='De kleur van een tank.',
                                   owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInCentimeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tank.lengte',
                                    definition='Lengte in centimeter van de tank. ',
                                    owner=self)

        self._materiaal = OTLAttribuut(field=KlTankMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tank.materiaal',
                                       definition='Het materiaal waaruit de tank vervaardigd is.',
                                       owner=self)

        self._merk = OTLAttribuut(field=KlTankMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tank.merk',
                                  definition='Het merk van de tank.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlTankModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tank.modelnaam',
                                       definition='De modelnaam van de tank.',
                                       owner=self)

        self._opstelHoogte = OTLAttribuut(field=KwantWrdInCentimeter,
                                          naam='opstelHoogte',
                                          label='opstelhoogte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tank.opstelHoogte',
                                          definition='De hoogte in centimeter beschikbaar tussen het grondoppervlak en de tank.',
                                          owner=self)

        self._opstelling = OTLAttribuut(field=KlTankOpstelling,
                                        naam='opstelling',
                                        label='oriëntatie',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tank.opstelling',
                                        definition='De oriëntatie van de opstelling van de tank.',
                                        owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tank.technischeFiche',
                                             definition='De technische fiche van de tank.',
                                             owner=self)

        self._volume = OTLAttribuut(field=KwantWrdInKubiekeMeter,
                                    naam='volume',
                                    label='volume',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tank.volume',
                                    definition='Het volume in kubieke meter van de tank.',
                                    owner=self)

        self._vorm = OTLAttribuut(field=KlTankVorm,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tank.vorm',
                                  definition='De vorm van de tank.',
                                  owner=self)

    @property
    def diameter(self) -> KwantWrdInCentimeterWaarden:
        """De diameter in centimeter van de tank."""
        return self._diameter.get_waarde()

    @diameter.setter
    def diameter(self, value):
        self._diameter.set_waarde(value, owner=self)

    @property
    def heeftTrapconstructie(self) -> bool:
        """Geeft aan of het object al dan niet een trapconstructie bevat."""
        return self._heeftTrapconstructie.get_waarde()

    @heeftTrapconstructie.setter
    def heeftTrapconstructie(self, value):
        self._heeftTrapconstructie.set_waarde(value, owner=self)

    @property
    def kleur(self) -> str:
        """De kleur van een tank."""
        return self._kleur.get_waarde()

    @kleur.setter
    def kleur(self, value):
        self._kleur.set_waarde(value, owner=self)

    @property
    def lengte(self) -> KwantWrdInCentimeterWaarden:
        """Lengte in centimeter van de tank. """
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def materiaal(self) -> str:
        """Het materiaal waaruit de tank vervaardigd is."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de tank."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de tank."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def opstelHoogte(self) -> KwantWrdInCentimeterWaarden:
        """De hoogte in centimeter beschikbaar tussen het grondoppervlak en de tank."""
        return self._opstelHoogte.get_waarde()

    @opstelHoogte.setter
    def opstelHoogte(self, value):
        self._opstelHoogte.set_waarde(value, owner=self)

    @property
    def opstelling(self) -> str:
        """De oriëntatie van de opstelling van de tank."""
        return self._opstelling.get_waarde()

    @opstelling.setter
    def opstelling(self, value):
        self._opstelling.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van de tank."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def volume(self) -> KwantWrdInKubiekeMeterWaarden:
        """Het volume in kubieke meter van de tank."""
        return self._volume.get_waarde()

    @volume.setter
    def volume(self, value):
        self._volume.set_waarde(value, owner=self)

    @property
    def vorm(self) -> str:
        """De vorm van de tank."""
        return self._vorm.get_waarde()

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value, owner=self)
