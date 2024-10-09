# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.NietWeggebondenDetectie import NietWeggebondenDetectie
from ...Classes.Abstracten.TypeWeggebruiker import TypeWeggebruiker
from ...Datatypes.KlRadarMerk import KlRadarMerk
from ...Datatypes.KlRadarModelnaam import KlRadarModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class Radar(NietWeggebondenDetectie, TypeWeggebruiker):
    """Een detector die werkt volgens het Doppler-effect. De detectie gebeurt met behulp van een microgolfbundel die in de richting van het wegdek wordt uitgezonden. Gebruikt voor het detecteren van voertuigen, voetgangers en fietsers."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Radar'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VRIDraagconstructie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRIVirtueleDetectiezone', direction='u')  # u = unidirectional

        self._merk = OTLAttribuut(field=KlRadarMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Radar.merk',
                                  definition='Merknaam van de radar.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlRadarModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Radar.modelnaam',
                                       definition='De modelnaam van de radar.',
                                       owner=self)

    @property
    def merk(self) -> str:
        """Merknaam van de radar."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de radar."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
