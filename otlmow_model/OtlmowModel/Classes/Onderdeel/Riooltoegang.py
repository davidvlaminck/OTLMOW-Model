# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Put import Put
from ...Classes.Abstracten.PutRelatie import PutRelatie
from ...Datatypes.KlUitlaatType import KlUitlaatType
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Riooltoegang(Put, PutRelatie, PuntGeometrie):
    """Het uiteinde van een rioolbuis."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Riooltoegang'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kopmuur', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#WaterdoorvoerendeDuiker', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', direction='o')  # o = direction: outgoing

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
