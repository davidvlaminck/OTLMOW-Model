# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.Put import Put
from otlmow_model.Classes.Abstracten.PutRelatie import PutRelatie
from otlmow_model.Datatypes.KlUitlaatType import KlUitlaatType
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Riooltoegang(PutRelatie, Put, PuntGeometrie):
    """Het uiteinde van een rioolbuis."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Riooltoegang'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        PutRelatie.__init__(self)
        Put.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kopmuur')

        self._typeRiooltoegang = OTLAttribuut(field=KlUitlaatType,
                                              naam='typeRiooltoegang',
                                              label='type riooltoegang',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Riooltoegang.typeRiooltoegang',
                                              definition='Bepaalt het type van een riooltoegang.',
                                              owner=self)

    @property
    def typeRiooltoegang(self) -> str:
        """Bepaalt het type van een riooltoegang."""
        return self._typeRiooltoegang.get_waarde()

    @typeRiooltoegang.setter
    def typeRiooltoegang(self, value):
        self._typeRiooltoegang.set_waarde(value, owner=self)
