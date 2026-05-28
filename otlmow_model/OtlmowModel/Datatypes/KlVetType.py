# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVetType(KeuzelijstField):
    """De verschillende soorten vet die kunnen worden gebruikt voor smering."""
    naam = 'KlVetType'
    label = 'Vet type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVetType'
    definition = 'De verschillende soorten vet die kunnen worden gebruikt voor smering.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVetType'
    options = {
        'biologisch-vet': KeuzelijstWaarde(invulwaarde='biologisch-vet',
                                           label='biologisch vet',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVetType/biologisch-vet'),
        'synthetisch-vet': KeuzelijstWaarde(invulwaarde='synthetisch-vet',
                                            label='synthetisch vet',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVetType/synthetisch-vet')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

