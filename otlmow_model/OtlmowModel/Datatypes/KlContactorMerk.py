# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlContactorMerk(KeuzelijstField):
    """Keuzelijst met merken van contactoren volgens de fabrikanten."""
    naam = 'KlContactorMerk'
    label = 'Contactor merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlContactorMerk'
    definition = 'Keuzelijst met merken van contactoren volgens de fabrikanten.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlContactorMerk'
    options = {
        'schneider': KeuzelijstWaarde(invulwaarde='schneider',
                                      label='Schneider',
                                      status='ingebruik',
                                      definitie='Schneider',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlContactorMerk/schneider'),
        'wei': KeuzelijstWaarde(invulwaarde='wei',
                                label='WEI',
                                status='ingebruik',
                                definitie='WEI',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlContactorMerk/wei')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

