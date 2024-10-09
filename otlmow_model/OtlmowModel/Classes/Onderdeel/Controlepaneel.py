# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.SerienummerObject import SerienummerObject
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlControlepaneelMerk import KlControlepaneelMerk
from ...Datatypes.KlControlepaneelModelnaam import KlControlepaneelModelnaam
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Controlepaneel(SerienummerObject, AIMNaamObject, PuntGeometrie):
    """Een inrichting voor het besturen van een systeem dat of installatie die zich in de buurt van het controlepaneel bevindt. Een controlepaneel kan onder andere uitgerust zijn met schakelaars, drukknoppen, draaiknoppen, cijfertoetsen, signaallampen, etc."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Controlepaneel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart', direction='u')  # u = unidirectional

        self._merk = OTLAttribuut(field=KlControlepaneelMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Controlepaneel.merk',
                                  definition='Het merk van het controlepaneel.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlControlepaneelModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Controlepaneel.modelnaam',
                                       definition='De modelnaam van het controlepaneel',
                                       owner=self)

    @property
    def merk(self) -> str:
        """Het merk van het controlepaneel."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van het controlepaneel"""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
