# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlBeheerExoten import KlBeheerExoten
from ...Datatypes.KlNazorgJaarfrequentie import KlNazorgJaarfrequentie
from ...Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter, KwantWrdInVierkanteMeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class BeheerExoten(AIMObject):
    """Het beheerobject voor de exoten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerExoten'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBeheer', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Exoten', direction='i', deprecated='2.1.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBeheer', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#InvasieveExoten', direction='i')  # i = direction: incoming

        self._beheeroptie = OTLAttribuut(field=KlBeheerExoten,
                                         naam='beheeroptie',
                                         label='beheeroptie',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerExoten.beheeroptie',
                                         definition='Behandelingswijzen van exoten.',
                                         owner=self)

        self._bijzondereAfvoerVereist = OTLAttribuut(field=BooleanField,
                                                     naam='bijzondereAfvoerVereist',
                                                     label='bijzondere afvoer vereist',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerExoten.bijzondereAfvoerVereist',
                                                     definition='Aanduiding of voor de verwijderde exoten een niet-reguliere afvoer is voorzien.',
                                                     owner=self)

        self._heeftDeponie = OTLAttribuut(field=BooleanField,
                                          naam='heeftDeponie',
                                          label='heeft deponie',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerExoten.heeftDeponie',
                                          definition='Aanduiding of de Japanse duizendknoop terplaatse kan worden gedeponeerd in een gecontamineerde zone.',
                                          owner=self)

        self._nazorgJaarfrequentie = OTLAttribuut(field=KlNazorgJaarfrequentie,
                                                  naam='nazorgJaarfrequentie',
                                                  label='nazorg jaarfrequentie',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerExoten.nazorgJaarfrequentie',
                                                  definition='Aantal keer dat de behandelde zone jaarlijks dient te worden gecontroleerd.',
                                                  owner=self)

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerExoten.oppervlakte',
                                         definition='De oppervlakte in vierkante meter van de te behandelen exoten.',
                                         owner=self)

    @property
    def beheeroptie(self) -> str:
        """Behandelingswijzen van exoten."""
        return self._beheeroptie.get_waarde()

    @beheeroptie.setter
    def beheeroptie(self, value):
        self._beheeroptie.set_waarde(value, owner=self)

    @property
    def bijzondereAfvoerVereist(self) -> bool:
        """Aanduiding of voor de verwijderde exoten een niet-reguliere afvoer is voorzien."""
        return self._bijzondereAfvoerVereist.get_waarde()

    @bijzondereAfvoerVereist.setter
    def bijzondereAfvoerVereist(self, value):
        self._bijzondereAfvoerVereist.set_waarde(value, owner=self)

    @property
    def heeftDeponie(self) -> bool:
        """Aanduiding of de Japanse duizendknoop terplaatse kan worden gedeponeerd in een gecontamineerde zone."""
        return self._heeftDeponie.get_waarde()

    @heeftDeponie.setter
    def heeftDeponie(self, value):
        self._heeftDeponie.set_waarde(value, owner=self)

    @property
    def nazorgJaarfrequentie(self) -> str:
        """Aantal keer dat de behandelde zone jaarlijks dient te worden gecontroleerd."""
        return self._nazorgJaarfrequentie.get_waarde()

    @nazorgJaarfrequentie.setter
    def nazorgJaarfrequentie(self, value):
        self._nazorgJaarfrequentie.set_waarde(value, owner=self)

    @property
    def oppervlakte(self) -> KwantWrdInVierkanteMeterWaarden:
        """De oppervlakte in vierkante meter van de te behandelen exoten."""
        return self._oppervlakte.get_waarde()

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)
