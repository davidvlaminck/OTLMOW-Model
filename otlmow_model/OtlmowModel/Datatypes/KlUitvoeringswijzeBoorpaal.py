# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlUitvoeringswijzeBoorpaal(KeuzelijstField):
    """De manier waarop de boorpaal is uitgevoerd."""
    naam = 'KlUitvoeringswijzeBoorpaal'
    label = 'Uitvoeringswijze boorpaal.'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlUitvoeringswijzeBoorpaal'
    definition = 'De manier waarop de boorpaal is uitgevoerd.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlUitvoeringswijzeBoorpaal'
    options = {
        'met-bentoniet-zonder-voerbuis': KeuzelijstWaarde(invulwaarde='met-bentoniet-zonder-voerbuis',
                                                          label='met bentoniet zonder voerbuis',
                                                          status='ingebruik',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitvoeringswijzeBoorpaal/met-bentoniet-zonder-voerbuis'),
        'met-continue-schroefboor': KeuzelijstWaarde(invulwaarde='met-continue-schroefboor',
                                                     label='met continue schroefboor',
                                                     status='ingebruik',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitvoeringswijzeBoorpaal/met-continue-schroefboor'),
        'met-voerbuis': KeuzelijstWaarde(invulwaarde='met-voerbuis',
                                         label='met voerbuis',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitvoeringswijzeBoorpaal/met-voerbuis')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

