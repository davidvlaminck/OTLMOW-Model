# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.WaterloopRelatie import WaterloopRelatie
from ...Datatypes.KlGrachtFunctie import KlGrachtFunctie
from ...Datatypes.KlGrachtdoorsnede import KlGrachtdoorsnede


# Generated with OTLClassCreator. To modify: extend, do not edit
class Gracht(WaterloopRelatie):
    """Een kunstmatige aangelegde waterloop."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Gracht'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftAanvullendeGeometrie', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AanvullendeMiddellijn', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Rioleringsstelsel', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PutRelatie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpenInfiltratievoorziening', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spaarbekken', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpenInfiltratievoorziening', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spaarbekken', direction='i')  # i = direction: incoming

        self._doorsnede = OTLAttribuut(field=KlGrachtdoorsnede,
                                       naam='doorsnede',
                                       label='doorsnede',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Gracht.doorsnede',
                                       definition='De doorsnede van de gracht.',
                                       owner=self)

        self._functie = OTLAttribuut(field=KlGrachtFunctie,
                                     naam='functie',
                                     label='functie',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Gracht.functie',
                                     definition='De functiebepaling van de gracht, als vesting, polder,...',
                                     owner=self)

    @property
    def doorsnede(self) -> str:
        """De doorsnede van de gracht."""
        return self._doorsnede.get_waarde()

    @doorsnede.setter
    def doorsnede(self, value):
        self._doorsnede.set_waarde(value, owner=self)

    @property
    def functie(self) -> str:
        """De functiebepaling van de gracht, als vesting, polder,..."""
        return self._functie.get_waarde()

    @functie.setter
    def functie(self, value):
        self._functie.set_waarde(value, owner=self)
