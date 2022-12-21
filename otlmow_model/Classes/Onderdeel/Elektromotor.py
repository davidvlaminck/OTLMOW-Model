# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.ElektrischComponentennummerObject import ElektrischComponentennummerObject
from otlmow_model.Classes.Abstracten.SerienummerObject import SerienummerObject
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.BaseClasses.FloatOrDecimalField import FloatOrDecimalField
from otlmow_model.Datatypes.KlElektromotorBeschermingsgraad import KlElektromotorBeschermingsgraad
from otlmow_model.Datatypes.KlElektromotorBouwvorm import KlElektromotorBouwvorm
from otlmow_model.Datatypes.KlElektromotorMerk import KlElektromotorMerk
from otlmow_model.Datatypes.KlElektromotorModelnaam import KlElektromotorModelnaam
from otlmow_model.Datatypes.KlElektromotorRol import KlElektromotorRol
from otlmow_model.Datatypes.KlNominaleSpanning import KlNominaleSpanning
from otlmow_model.Datatypes.KwantWrdInAmpere import KwantWrdInAmpere, KwantWrdInAmpereWaarden
from otlmow_model.Datatypes.KwantWrdInKiloWatt import KwantWrdInKiloWatt, KwantWrdInKiloWattWaarden
from otlmow_model.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from otlmow_model.Datatypes.KwantWrdInRPM import KwantWrdInRPM, KwantWrdInRPMWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Elektromotor(ElektrischComponentennummerObject, SerienummerObject, AIMNaamObject):
    """Een machine die elektrische energie omzet in mechanische energie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Elektromotor'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        ElektrischComponentennummerObject.__init__(self)
        SerienummerObject.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Silo')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PLC')

        self._arbeidsfactor = OTLAttribuut(field=FloatOrDecimalField,
                                           naam='arbeidsfactor',
                                           label='arbeidsfactor',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Elektromotor.arbeidsfactor',
                                           definition='De arbeidsfactor of cosinus phi is de verhouding van het effectief elektrisch vermogen en het schijnbaar vermogen. Om het elektrisch net minimaal te belasten moet deze waarde zo dicht mogelijk bij 1 liggen.',
                                           owner=self)

        self._asdiameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                        naam='asdiameter',
                                        label='asdiameter',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Elektromotor.asdiameter',
                                        definition='De diameter van de uitgaande as van de elektromotor.',
                                        owner=self)

        self._ashoogte = OTLAttribuut(field=KwantWrdInMillimeter,
                                      naam='ashoogte',
                                      label='ashoogte',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Elektromotor.ashoogte',
                                      definition='De afstand tussen het rustvlak van de voeten van de elektromotor en het midden van de uitgaande as.',
                                      owner=self)

        self._beschermingsgraad = OTLAttribuut(field=KlElektromotorBeschermingsgraad,
                                               naam='beschermingsgraad',
                                               label='beschermingsgraad',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Elektromotor.beschermingsgraad',
                                               definition='De beschermingsgraad geeft aan in welke mate elektrische apparatuur tegen indringing van vreemde objecten en water bestand is. Dit gebeurt met de code IP, gevolgd door twee cijfers.',
                                               owner=self)

        self._bouwvorm = OTLAttribuut(field=KlElektromotorBouwvorm,
                                      naam='bouwvorm',
                                      label='bouwvorm',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Elektromotor.bouwvorm',
                                      definition='De bouwvorm, uitgedrukt als een IM-code, zegt iets over de wijze waarop de elektromotor gemonteerd is.',
                                      owner=self)

        self._gebruik = OTLAttribuut(field=KlElektromotorRol,
                                     naam='gebruik',
                                     label='gebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Elektromotor.gebruik',
                                     definition='Geeft aan hoe de elektromotor gebruikt wordt in het systeem waar hij deel van uitmaakt.',
                                     owner=self)

        self._heeftGeforceerdeKoeling = OTLAttribuut(field=BooleanField,
                                                     naam='heeftGeforceerdeKoeling',
                                                     label='heeft geforceerde koeling',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Elektromotor.heeftGeforceerdeKoeling',
                                                     definition='Geeft aan of de elektromotor voorzien is van geforceerde koeling.',
                                                     owner=self)

        self._merk = OTLAttribuut(field=KlElektromotorMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Elektromotor.merk',
                                  definition='Het merk van de elektromotor.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlElektromotorModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Elektromotor.modelnaam',
                                       definition='De modelnaam volgens de fabrikant van de elektromotor.',
                                       owner=self)

        self._nominaalToerental = OTLAttribuut(field=KwantWrdInRPM,
                                               naam='nominaalToerental',
                                               label='nominaal toerental',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Elektromotor.nominaalToerental',
                                               definition='Het nominale toerental van de elektromotor.',
                                               owner=self)

        self._nominaalVermogen = OTLAttribuut(field=KwantWrdInKiloWatt,
                                              naam='nominaalVermogen',
                                              label='nominaal vermogen',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Elektromotor.nominaalVermogen',
                                              definition='Het nominale vermogen van de elektromotor.',
                                              owner=self)

        self._nominaleSpanning = OTLAttribuut(field=KlNominaleSpanning,
                                              naam='nominaleSpanning',
                                              label='nominale spanning',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Elektromotor.nominaleSpanning',
                                              definition='De nominale spanning van de elektromotor.',
                                              owner=self)

        self._nominaleStroom = OTLAttribuut(field=KwantWrdInAmpere,
                                            naam='nominaleStroom',
                                            label='nominale stroom',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Elektromotor.nominaleStroom',
                                            definition='De nominale stroom van de elektromotor.',
                                            owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Elektromotor.technischeFiche',
                                             definition='De technische fiche van een elektromotor.',
                                             owner=self)

    @property
    def arbeidsfactor(self) -> float:
        """De arbeidsfactor of cosinus phi is de verhouding van het effectief elektrisch vermogen en het schijnbaar vermogen. Om het elektrisch net minimaal te belasten moet deze waarde zo dicht mogelijk bij 1 liggen."""
        return self._arbeidsfactor.get_waarde()

    @arbeidsfactor.setter
    def arbeidsfactor(self, value):
        self._arbeidsfactor.set_waarde(value, owner=self)

    @property
    def asdiameter(self) -> KwantWrdInMillimeterWaarden:
        """De diameter van de uitgaande as van de elektromotor."""
        return self._asdiameter.get_waarde()

    @asdiameter.setter
    def asdiameter(self, value):
        self._asdiameter.set_waarde(value, owner=self)

    @property
    def ashoogte(self) -> KwantWrdInMillimeterWaarden:
        """De afstand tussen het rustvlak van de voeten van de elektromotor en het midden van de uitgaande as."""
        return self._ashoogte.get_waarde()

    @ashoogte.setter
    def ashoogte(self, value):
        self._ashoogte.set_waarde(value, owner=self)

    @property
    def beschermingsgraad(self) -> str:
        """De beschermingsgraad geeft aan in welke mate elektrische apparatuur tegen indringing van vreemde objecten en water bestand is. Dit gebeurt met de code IP, gevolgd door twee cijfers."""
        return self._beschermingsgraad.get_waarde()

    @beschermingsgraad.setter
    def beschermingsgraad(self, value):
        self._beschermingsgraad.set_waarde(value, owner=self)

    @property
    def bouwvorm(self) -> str:
        """De bouwvorm, uitgedrukt als een IM-code, zegt iets over de wijze waarop de elektromotor gemonteerd is."""
        return self._bouwvorm.get_waarde()

    @bouwvorm.setter
    def bouwvorm(self, value):
        self._bouwvorm.set_waarde(value, owner=self)

    @property
    def gebruik(self) -> str:
        """Geeft aan hoe de elektromotor gebruikt wordt in het systeem waar hij deel van uitmaakt."""
        return self._gebruik.get_waarde()

    @gebruik.setter
    def gebruik(self, value):
        self._gebruik.set_waarde(value, owner=self)

    @property
    def heeftGeforceerdeKoeling(self) -> bool:
        """Geeft aan of de elektromotor voorzien is van geforceerde koeling."""
        return self._heeftGeforceerdeKoeling.get_waarde()

    @heeftGeforceerdeKoeling.setter
    def heeftGeforceerdeKoeling(self, value):
        self._heeftGeforceerdeKoeling.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de elektromotor."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam volgens de fabrikant van de elektromotor."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def nominaalToerental(self) -> KwantWrdInRPMWaarden:
        """Het nominale toerental van de elektromotor."""
        return self._nominaalToerental.get_waarde()

    @nominaalToerental.setter
    def nominaalToerental(self, value):
        self._nominaalToerental.set_waarde(value, owner=self)

    @property
    def nominaalVermogen(self) -> KwantWrdInKiloWattWaarden:
        """Het nominale vermogen van de elektromotor."""
        return self._nominaalVermogen.get_waarde()

    @nominaalVermogen.setter
    def nominaalVermogen(self, value):
        self._nominaalVermogen.set_waarde(value, owner=self)

    @property
    def nominaleSpanning(self) -> str:
        """De nominale spanning van de elektromotor."""
        return self._nominaleSpanning.get_waarde()

    @nominaleSpanning.setter
    def nominaleSpanning(self, value):
        self._nominaleSpanning.set_waarde(value, owner=self)

    @property
    def nominaleStroom(self) -> KwantWrdInAmpereWaarden:
        """De nominale stroom van de elektromotor."""
        return self._nominaleStroom.get_waarde()

    @nominaleStroom.setter
    def nominaleStroom(self, value):
        self._nominaleStroom.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van een elektromotor."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
