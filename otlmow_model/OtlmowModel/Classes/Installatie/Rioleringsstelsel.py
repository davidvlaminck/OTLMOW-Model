# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KlFunctieRioleringsstelsel import KlFunctieRioleringsstelsel
from ...Datatypes.KlRioleringStelsel import KlRioleringStelsel
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Rioleringsstelsel(AIMObject, VlakGeometrie):
    """De groepering van de objecten die behoren tot het riolering, aanvoer- of afvoerstelsel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Rioleringsstelsel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PutRelatie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bouwput', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Gracht', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sleuf', direction='i')  # i = direction: incoming

        self._functie = OTLAttribuut(field=KlFunctieRioleringsstelsel,
                                     naam='functie',
                                     label='functie',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Rioleringsstelsel.functie',
                                     definition='Geeft aan welke functie het rioleringsstelsel vervult,',
                                     owner=self)

        self._rioleringsstelsel = OTLAttribuut(field=KlRioleringStelsel,
                                               naam='rioleringsstelsel',
                                               label='rioleringsstelsel',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Rioleringsstelsel.rioleringsstelsel',
                                               usagenote='Attribuut uit gebruik sinds versie 2.1.0 ',
                                               deprecated_version='2.1.0',
                                               definition='Geeft aan wat voor afvoerwater er door de riolering afgevoerd wordt.',
                                               owner=self)

        self._systeemtype = OTLAttribuut(field=KlRioleringStelsel,
                                         naam='systeemtype',
                                         label='systeemtype',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Rioleringsstelsel.systeemtype',
                                         definition='Geeft aan wat voor afvoerwater er door de riolering afgevoerd wordt.',
                                         owner=self)

    @property
    def functie(self) -> str:
        """Geeft aan welke functie het rioleringsstelsel vervult,"""
        return self._functie.get_waarde()

    @functie.setter
    def functie(self, value):
        self._functie.set_waarde(value, owner=self)

    @property
    def rioleringsstelsel(self) -> str:
        """Geeft aan wat voor afvoerwater er door de riolering afgevoerd wordt."""
        return self._rioleringsstelsel.get_waarde()

    @rioleringsstelsel.setter
    def rioleringsstelsel(self, value):
        self._rioleringsstelsel.set_waarde(value, owner=self)

    @property
    def systeemtype(self) -> str:
        """Geeft aan wat voor afvoerwater er door de riolering afgevoerd wordt."""
        return self._systeemtype.get_waarde()

    @systeemtype.setter
    def systeemtype(self, value):
        self._systeemtype.set_waarde(value, owner=self)
