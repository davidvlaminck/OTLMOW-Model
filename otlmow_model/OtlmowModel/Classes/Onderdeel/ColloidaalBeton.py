# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AndereVerharding import AndereVerharding
from ...Classes.Abstracten.BetonnenConstructieElement import BetonnenConstructieElement
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlUitvoeringsmethodeColloidaalbeton import KlUitvoeringsmethodeColloidaalbeton


# Generated with OTLClassCreator. To modify: extend, do not edit
class ColloidaalBeton(AndereVerharding, BetonnenConstructieElement):
    """Betonspecie voor toepassing onder water,waarvan de samenhang is verbeterd door toevoeging van een waterretentiemiddel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ColloidaalBeton'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolkvloer')

        self._heeftOpenStructuur = OTLAttribuut(field=BooleanField,
                                                naam='heeftOpenStructuur',
                                                label='heeft open structuur',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ColloidaalBeton.heeftOpenStructuur',
                                                definition='Geeft aan of het colloïdaal beton al dan niet een open structuur heeft.',
                                                owner=self)

        self._uitvoeringsmethodeColloidaalBeton = OTLAttribuut(field=KlUitvoeringsmethodeColloidaalbeton,
                                                               naam='uitvoeringsmethodeColloidaalBeton',
                                                               label='uitvoeringsmethode colloïdaal beton',
                                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ColloidaalBeton.uitvoeringsmethodeColloidaalBeton',
                                                               definition='De uitvoeringsmethode van het colloïdaal beton.',
                                                               owner=self)

    @property
    def heeftOpenStructuur(self) -> bool:
        """Geeft aan of het colloïdaal beton al dan niet een open structuur heeft."""
        return self._heeftOpenStructuur.get_waarde()

    @heeftOpenStructuur.setter
    def heeftOpenStructuur(self, value):
        self._heeftOpenStructuur.set_waarde(value, owner=self)

    @property
    def uitvoeringsmethodeColloidaalBeton(self) -> str:
        """De uitvoeringsmethode van het colloïdaal beton."""
        return self._uitvoeringsmethodeColloidaalBeton.get_waarde()

    @uitvoeringsmethodeColloidaalBeton.setter
    def uitvoeringsmethodeColloidaalBeton(self, value):
        self._uitvoeringsmethodeColloidaalBeton.set_waarde(value, owner=self)
