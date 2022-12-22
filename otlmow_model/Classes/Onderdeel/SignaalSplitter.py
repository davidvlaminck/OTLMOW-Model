# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.ElektrischComponentennummerObject import ElektrischComponentennummerObject
from otlmow_model.Classes.Abstracten.SerienummerObject import SerienummerObject
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.KlSignaalSplitterMerk import KlSignaalSplitterMerk
from otlmow_model.Datatypes.KlSignaalSplitterModelnaam import KlSignaalSplitterModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class SignaalSplitter(ElektrischComponentennummerObject, SerienummerObject, AIMNaamObject):
    """Een splitter laat toe een kabel in twee te splitsen en dusdanig een signaal te splitsen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SignaalSplitter'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        ElektrischComponentennummerObject.__init__(self)
        SerienummerObject.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#RHZModule')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#ASTRIDInstallatie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Datakabel')

        self._merk = OTLAttribuut(field=KlSignaalSplitterMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SignaalSplitter.merk',
                                  definition='Het merk van de signaalsplitter.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlSignaalSplitterModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SignaalSplitter.modelnaam',
                                       definition='De modelnaam van de signaalsplitter.',
                                       owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de signaalsplitter."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de signaalsplitter."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
