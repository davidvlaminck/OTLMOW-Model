# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.LinkendElement import LinkendElement
from ...Datatypes.KlFlensType import KlFlensType
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Flens(LinkendElement, PuntGeometrie):
    """Een platte ring aan het uiteinde van een buis met als functie het mogelijk maken van het verbinden van de buis met een andere buis, wand, etc."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Flens'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._type = OTLAttribuut(field=KlFlensType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Flens.type',
                                  definition='Geeft aan wat voor type deze flens is.',
                                  owner=self)

    @property
    def type(self) -> str:
        """Geeft aan wat voor type deze flens is."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
