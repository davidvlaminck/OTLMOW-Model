# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRioleringsbuisFunctie(KeuzelijstField):
    """Mogelijke functies van de riolering."""
    naam = 'KlRioleringsbuisFunctie'
    label = 'Rioleringsbuis functie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRioleringsbuisFunctie'
    definition = 'Mogelijke functies van de riolering.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRioleringsbuisFunctie'
    options = {
        'bufferleiding': KeuzelijstWaarde(invulwaarde='bufferleiding',
                                          label='bufferleiding',
                                          status='ingebruik',
                                          definitie='buis bedoeld voor gravitaire afvoer en tijdelijke buffering van water',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringsbuisFunctie/bufferleiding'),
        'gravitaire-leiding': KeuzelijstWaarde(invulwaarde='gravitaire-leiding',
                                               label='gravitaire leiding',
                                               status='ingebruik',
                                               definitie='buis bedoeld voor de gravitaire afvoer van water',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringsbuisFunctie/gravitaire-leiding'),
        'infiltratieleiding': KeuzelijstWaarde(invulwaarde='infiltratieleiding',
                                               label='infiltratieleiding',
                                               status='ingebruik',
                                               definitie='buis bedoeld voor gravitaire afvoer en infiltratie van niet vervuild water',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringsbuisFunctie/infiltratieleiding'),
        'syphon': KeuzelijstWaarde(invulwaarde='syphon',
                                   label='syphon',
                                   status='ingebruik',
                                   definitie='buis bedoeld voor gravitaire afvoer van water met omgekeerde hevelwerking',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringsbuisFunctie/syphon')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

