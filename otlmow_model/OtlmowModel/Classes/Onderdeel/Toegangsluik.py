# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AanhorigheidKoker import AanhorigheidKoker
from ...Classes.Abstracten.AanhorigheidSluisStuw import AanhorigheidSluisStuw
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcAfmetingBxlInM import DtcAfmetingBxlInM, DtcAfmetingBxlInMWaarden
from ...Datatypes.KlBelastingsklasse import KlBelastingsklasse
from ...Datatypes.KlMateriaalToegangsluik import KlMateriaalToegangsluik
from ...Datatypes.KlOpeningswijze import KlOpeningswijze
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Toegangsluik(AanhorigheidKoker, AanhorigheidSluisStuw, AIMNaamObject, PuntGeometrie):
    """Een luik om toegang te bieden tot de binnenruimte van een constructie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangsluik'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kokerruimte', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ballastcompartiment', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactpunt', direction='u')  # u = unidirectional

        self._afmetingen = OTLAttribuut(field=DtcAfmetingBxlInM,
                                        naam='afmetingen',
                                        label='afmetingen',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangsluik.afmetingen',
                                        definition='De afmetingen van het toegangsluik.',
                                        owner=self)

        self._belastingsklasse = OTLAttribuut(field=KlBelastingsklasse,
                                              naam='belastingsklasse',
                                              label='belastingsklasse',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangsluik.belastingsklasse',
                                              definition='De klasses die worden gebruikt om het verwachte gewicht en de belasting te specificeren waaraan het toegangsluik kan worden blootgesteld.',
                                              owner=self)

        self._isWaterdicht = OTLAttribuut(field=BooleanField,
                                          naam='isWaterdicht',
                                          label='is waterdicht',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangsluik.isWaterdicht',
                                          definition='Geeft aan of het toegangsluik waterdicht is.',
                                          owner=self)

        self._materiaal = OTLAttribuut(field=KlMateriaalToegangsluik,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangsluik.materiaal',
                                       definition='Het gebruikte materiaal voor het toegangsluik.',
                                       owner=self)

        self._openingswijze = OTLAttribuut(field=KlOpeningswijze,
                                           naam='openingswijze',
                                           label='openingswijze',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangsluik.openingswijze',
                                           definition='De openingswijzen van een toegansluik.',
                                           owner=self)

    @property
    def afmetingen(self) -> DtcAfmetingBxlInMWaarden:
        """De afmetingen van het toegangsluik."""
        return self._afmetingen.get_waarde()

    @afmetingen.setter
    def afmetingen(self, value):
        self._afmetingen.set_waarde(value, owner=self)

    @property
    def belastingsklasse(self) -> str:
        """De klasses die worden gebruikt om het verwachte gewicht en de belasting te specificeren waaraan het toegangsluik kan worden blootgesteld."""
        return self._belastingsklasse.get_waarde()

    @belastingsklasse.setter
    def belastingsklasse(self, value):
        self._belastingsklasse.set_waarde(value, owner=self)

    @property
    def isWaterdicht(self) -> bool:
        """Geeft aan of het toegangsluik waterdicht is."""
        return self._isWaterdicht.get_waarde()

    @isWaterdicht.setter
    def isWaterdicht(self, value):
        self._isWaterdicht.set_waarde(value, owner=self)

    @property
    def materiaal(self) -> str:
        """Het gebruikte materiaal voor het toegangsluik."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def openingswijze(self) -> str:
        """De openingswijzen van een toegansluik."""
        return self._openingswijze.get_waarde()

    @openingswijze.setter
    def openingswijze(self, value):
        self._openingswijze.set_waarde(value, owner=self)
