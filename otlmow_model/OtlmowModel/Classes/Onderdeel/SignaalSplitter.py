# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.ElektrischComponentennummerObject import ElektrischComponentennummerObject
from ...Classes.Abstracten.SerienummerObject import SerienummerObject
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlSignaalSplitterMerk import KlSignaalSplitterMerk
from ...Datatypes.KlSignaalSplitterModelnaam import KlSignaalSplitterModelnaam
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class SignaalSplitter(ElektrischComponentennummerObject, SerienummerObject, AIMNaamObject, PuntGeometrie):
    """Een splitter laat toe een kabel in twee te splitsen en dusdanig een signaal te splitsen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SignaalSplitter'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#RHZModule', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#ASTRIDInstallatie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Datakabel', direction='u')  # u = unidirectional

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
