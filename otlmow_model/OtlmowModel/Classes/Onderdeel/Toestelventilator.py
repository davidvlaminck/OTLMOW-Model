# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.ElektrischComponentennummerObject import ElektrischComponentennummerObject
from ...Classes.Abstracten.SerienummerObject import SerienummerObject
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcAfmetingBxlInMm import DtcAfmetingBxlInMm, DtcAfmetingBxlInMmWaarden
from ...Datatypes.KlToestelventilatorFilterdoekKlasse import KlToestelventilatorFilterdoekKlasse
from ...Datatypes.KlToestelventilatorFilterdoekMateriaal import KlToestelventilatorFilterdoekMateriaal
from ...Datatypes.KlToestelventilatorMerk import KlToestelventilatorMerk
from ...Datatypes.KlToestelventilatorModelnaam import KlToestelventilatorModelnaam
from ...Datatypes.KwantWrdInWatt import KwantWrdInWatt, KwantWrdInWattWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Toestelventilator(ElektrischComponentennummerObject, SerienummerObject, AIMNaamObject, PuntGeometrie):
    """Ventilator met als primaire functie het afkoelen van een bepaald toestel, apparaat, of machineonderdeel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toestelventilator'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Elektromotor', direction='u')  # u = unidirectional

        self._filterdoekAfmeting = OTLAttribuut(field=DtcAfmetingBxlInMm,
                                                naam='filterdoekAfmeting',
                                                label='filterdoek afmeting',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toestelventilator.filterdoekAfmeting',
                                                definition='Afmeting van (de buitenzijde van) het filterdoek.',
                                                owner=self)

        self._filterdoekKlasse = OTLAttribuut(field=KlToestelventilatorFilterdoekKlasse,
                                              naam='filterdoekKlasse',
                                              label='filterdoek klasse',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toestelventilator.filterdoekKlasse',
                                              definition='De filterklassegeeft aan in hoeverre de filterdoek beschermt tegen (fijn)stof.',
                                              owner=self)

        self._filterdoekMateriaal = OTLAttribuut(field=KlToestelventilatorFilterdoekMateriaal,
                                                 naam='filterdoekMateriaal',
                                                 label='filterdoek materiaal',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toestelventilator.filterdoekMateriaal',
                                                 definition='Het materiaal waaruit de filterdoek van de toestelventilator vervaardigd is.',
                                                 owner=self)

        self._merk = OTLAttribuut(field=KlToestelventilatorMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toestelventilator.merk',
                                  definition='Het merk van de toestelventilator volgens de fabrikant.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlToestelventilatorModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toestelventilator.modelnaam',
                                       definition='De modelnaam van de toestelventilator volgens de fabrikant.',
                                       owner=self)

        self._vermogen = OTLAttribuut(field=KwantWrdInWatt,
                                      naam='vermogen',
                                      label='vermogen',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toestelventilator.vermogen',
                                      definition='Het vermogen van een ventilator is de energie die het per seconde omzet.',
                                      owner=self)

    @property
    def filterdoekAfmeting(self) -> DtcAfmetingBxlInMmWaarden:
        """Afmeting van (de buitenzijde van) het filterdoek."""
        return self._filterdoekAfmeting.get_waarde()

    @filterdoekAfmeting.setter
    def filterdoekAfmeting(self, value):
        self._filterdoekAfmeting.set_waarde(value, owner=self)

    @property
    def filterdoekKlasse(self) -> str:
        """De filterklassegeeft aan in hoeverre de filterdoek beschermt tegen (fijn)stof."""
        return self._filterdoekKlasse.get_waarde()

    @filterdoekKlasse.setter
    def filterdoekKlasse(self, value):
        self._filterdoekKlasse.set_waarde(value, owner=self)

    @property
    def filterdoekMateriaal(self) -> str:
        """Het materiaal waaruit de filterdoek van de toestelventilator vervaardigd is."""
        return self._filterdoekMateriaal.get_waarde()

    @filterdoekMateriaal.setter
    def filterdoekMateriaal(self, value):
        self._filterdoekMateriaal.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de toestelventilator volgens de fabrikant."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de toestelventilator volgens de fabrikant."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def vermogen(self) -> KwantWrdInWattWaarden:
        """Het vermogen van een ventilator is de energie die het per seconde omzet."""
        return self._vermogen.get_waarde()

    @vermogen.setter
    def vermogen(self, value):
        self._vermogen.set_waarde(value, owner=self)
