# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTijdschakelaarUitvoering(KeuzelijstField):
    """Mogelijke uitvoeringen voor tijdschakelaars volgens de manier waarop instellingen ingegeven worden."""
    naam = 'KlTijdschakelaarUitvoering'
    label = 'Uitvoeringen tijdschakelaar'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTijdschakelaarUitvoering'
    definition = 'Mogelijke uitvoeringen voor tijdschakelaars volgens de manier waarop instellingen ingegeven worden.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTijdschakelaarUitvoering'
    options = {
        'analoog': KeuzelijstWaarde(invulwaarde='analoog',
                                    label='analoog',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTijdschakelaarUitvoering/analoog'),
        'digitaal': KeuzelijstWaarde(invulwaarde='digitaal',
                                     label='digitaal',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTijdschakelaarUitvoering/digitaal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

