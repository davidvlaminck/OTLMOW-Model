# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAlgIngressProtectionCode(KeuzelijstField):
    """De IP-codering als een aanduiding voor de mate van beveiliging van de constructie van elektrische of elektronische apparatuur tegen eigen schade door gebruik in 'vijandige omgevingen' en tegen eventueel gevaar voor de gebruiker volgens IEC 60529."""
    naam = 'KlAlgIngressProtectionCode'
    label = 'Ingress Protection Codering'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAlgIngressProtectionCode'
    definition = "De IP-codering als een aanduiding voor de mate van beveiliging van de constructie van elektrische of elektronische apparatuur tegen eigen schade door gebruik in 'vijandige omgevingen' en tegen eventueel gevaar voor de gebruiker volgens IEC 60529."
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgIngressProtectionCode'
    options = {
        'i-p-44': KeuzelijstWaarde(invulwaarde='i-p-44',
                                   label='IP44',
                                   status='uitgebruik',
                                   definitie='Bescherming tegen spitse voorwerpen en plensdicht.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgIngressProtectionCode/i-p-44'),
        'i-p-65': KeuzelijstWaarde(invulwaarde='i-p-65',
                                   label='IP65',
                                   status='uitgebruik',
                                   definitie='Stofvrij en sproeidicht.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgIngressProtectionCode/i-p-65'),
        'ip44': KeuzelijstWaarde(invulwaarde='ip44',
                                 label='IP44',
                                 status='ingebruik',
                                 definitie='Bescherming tegen spitse voorwerpen en plensdicht.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgIngressProtectionCode/ip44'),
        'ip46': KeuzelijstWaarde(invulwaarde='ip46',
                                 label='IP46',
                                 status='ingebruik',
                                 definitie='ip46',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgIngressProtectionCode/ip46'),
        'ip47': KeuzelijstWaarde(invulwaarde='ip47',
                                 label='IP47',
                                 status='ingebruik',
                                 definitie='ip47',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgIngressProtectionCode/ip47'),
        'ip48': KeuzelijstWaarde(invulwaarde='ip48',
                                 label='IP48',
                                 status='ingebruik',
                                 definitie='ip48',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgIngressProtectionCode/ip48'),
        'ip49': KeuzelijstWaarde(invulwaarde='ip49',
                                 label='IP49',
                                 status='ingebruik',
                                 definitie='ip49',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgIngressProtectionCode/ip49'),
        'ip54': KeuzelijstWaarde(invulwaarde='ip54',
                                 label='IP54',
                                 status='ingebruik',
                                 definitie='Spatwaterdicht en stofvrij.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgIngressProtectionCode/ip54'),
        'ip55': KeuzelijstWaarde(invulwaarde='ip55',
                                 label='IP55',
                                 status='ingebruik',
                                 definitie='ip55',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgIngressProtectionCode/ip55'),
        'ip56': KeuzelijstWaarde(invulwaarde='ip56',
                                 label='IP56',
                                 status='ingebruik',
                                 definitie='ip56',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgIngressProtectionCode/ip56'),
        'ip57': KeuzelijstWaarde(invulwaarde='ip57',
                                 label='IP57',
                                 status='ingebruik',
                                 definitie='ip57',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgIngressProtectionCode/ip57'),
        'ip58': KeuzelijstWaarde(invulwaarde='ip58',
                                 label='IP58',
                                 status='ingebruik',
                                 definitie='ip58',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgIngressProtectionCode/ip58'),
        'ip59': KeuzelijstWaarde(invulwaarde='ip59',
                                 label='IP59',
                                 status='ingebruik',
                                 definitie='ip59',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgIngressProtectionCode/ip59'),
        'ip64': KeuzelijstWaarde(invulwaarde='ip64',
                                 label='IP64',
                                 status='ingebruik',
                                 definitie='ip64',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgIngressProtectionCode/ip64'),
        'ip65': KeuzelijstWaarde(invulwaarde='ip65',
                                 label='IP65',
                                 status='ingebruik',
                                 definitie='Stofvrij en sproeidicht.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgIngressProtectionCode/ip65'),
        'ip66': KeuzelijstWaarde(invulwaarde='ip66',
                                 label='IP66',
                                 status='ingebruik',
                                 definitie='ip66',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgIngressProtectionCode/ip66'),
        'ip67': KeuzelijstWaarde(invulwaarde='ip67',
                                 label='IP67',
                                 status='ingebruik',
                                 definitie='ip67',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgIngressProtectionCode/ip67'),
        'ip68': KeuzelijstWaarde(invulwaarde='ip68',
                                 label='IP68',
                                 status='ingebruik',
                                 definitie='ip68',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgIngressProtectionCode/ip68')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

