# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlSiloMateriaal import KlSiloMateriaal
from ...Datatypes.KlSiloMerk import KlSiloMerk
from ...Datatypes.KlSiloModelnaam import KlSiloModelnaam
from ...Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter, KwantWrdInCentimeterWaarden
from ...Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter, KwantWrdInKubiekeMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Silo(NaampadObject, VlakGeometrie):
    """Meestal een metalen reservoir voor eerder vaste vulmiddelen,zoals korrels,kristallen: zout,zand,enz…,waarbij op een gecontroleerde manier middelen kunnen afgenomen of bijgevuld worden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Silo'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Niveaumeting', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Elektromotor', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omvormer', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegcel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Zoutbijlaadplaats', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Persleiding', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Persleiding', direction='o')  # o = direction: outgoing

        self._diameter = OTLAttribuut(field=KwantWrdInCentimeter,
                                      naam='diameter',
                                      label='diameter',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Silo.diameter',
                                      definition='De diamater in centimeter van de silo.',
                                      owner=self)

        self._hoogte = OTLAttribuut(field=KwantWrdInCentimeter,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Silo.hoogte',
                                    definition='De hoogte in centimeter tussen het grondoppervlak en de bovenkant van de silo.',
                                    owner=self)

        self._materiaal = OTLAttribuut(field=KlSiloMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Silo.materiaal',
                                       definition='Het materiaal waaruit de silo vervaardigd is.',
                                       owner=self)

        self._merk = OTLAttribuut(field=KlSiloMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Silo.merk',
                                  definition='Het merk van de silo.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlSiloModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Silo.modelnaam',
                                       definition='De modelnaam van de silo.',
                                       owner=self)

        self._onderDoorrijHoogte = OTLAttribuut(field=KwantWrdInCentimeter,
                                                naam='onderDoorrijHoogte',
                                                label='onderdoorrijhoogte',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Silo.onderDoorrijHoogte',
                                                definition='De maximale doorrijhoogte voor een voertuig in centimeter beschikbaar tussen het grondoppervlak en de onderkant van de silo.',
                                                owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Silo.technischeFiche',
                                             definition='De technische fiche van de silo.',
                                             owner=self)

        self._volume = OTLAttribuut(field=KwantWrdInKubiekeMeter,
                                    naam='volume',
                                    label='volume',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Silo.volume',
                                    definition='Het volume in kubieke meter van de silo.',
                                    owner=self)

    @property
    def diameter(self) -> KwantWrdInCentimeterWaarden:
        """De diamater in centimeter van de silo."""
        return self._diameter.get_waarde()

    @diameter.setter
    def diameter(self, value):
        self._diameter.set_waarde(value, owner=self)

    @property
    def hoogte(self) -> KwantWrdInCentimeterWaarden:
        """De hoogte in centimeter tussen het grondoppervlak en de bovenkant van de silo."""
        return self._hoogte.get_waarde()

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self)

    @property
    def materiaal(self) -> str:
        """Het materiaal waaruit de silo vervaardigd is."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de silo."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de silo."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def onderDoorrijHoogte(self) -> KwantWrdInCentimeterWaarden:
        """De maximale doorrijhoogte voor een voertuig in centimeter beschikbaar tussen het grondoppervlak en de onderkant van de silo."""
        return self._onderDoorrijHoogte.get_waarde()

    @onderDoorrijHoogte.setter
    def onderDoorrijHoogte(self, value):
        self._onderDoorrijHoogte.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van de silo."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def volume(self) -> KwantWrdInKubiekeMeterWaarden:
        """Het volume in kubieke meter van de silo."""
        return self._volume.get_waarde()

    @volume.setter
    def volume(self, value):
        self._volume.set_waarde(value, owner=self)
