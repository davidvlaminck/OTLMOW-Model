# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDwarseMarkeringVerschuindSoort(KeuzelijstField):
    """Soorten van de schuine dwarse markering."""
    naam = 'KlDwarseMarkeringVerschuindSoort'
    label = 'Dwarse markering soort verschuind'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDwarseMarkeringVerschuindSoort'
    definition = 'Soorten van de schuine dwarse markering.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDwarseMarkeringVerschuindSoort'
    options = {
        'fietsoversteekplaats-met-blokken-(FOP)-schuin': KeuzelijstWaarde(invulwaarde='fietsoversteekplaats-met-blokken-(FOP)-schuin',
                                                                          label='fietsoversteekplaats met blokken (FOP) schuin',
                                                                          status='ingebruik',
                                                                          definitie='Een oversteekplaats voor fietsers gemarkeerd door witte parallellogrammen.',
                                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringVerschuindSoort/fietsoversteekplaats-met-blokken-(FOP)-schuin')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))
