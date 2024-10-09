# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlPrinterMerk import KlPrinterMerk
from ...Datatypes.KlPrinterModelnaam import KlPrinterModelnaam
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Printer(AIMNaamObject, PuntGeometrie):
    """Een apparaat dat de uitvoer van een ander toestel afdrukt, in de meeste gevallen op papier."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Printer'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aswegersite', direction='o')  # o = direction: outgoing

        self._merk = OTLAttribuut(field=KlPrinterMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Printer.merk',
                                  definition='Merknaam van de printer volgens de fabrikant.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlPrinterModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Printer.modelnaam',
                                       definition='Modelnaam van de printer volgens de fabrikant.',
                                       owner=self)

    @property
    def merk(self) -> str:
        """Merknaam van de printer volgens de fabrikant."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """Modelnaam van de printer volgens de fabrikant."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
