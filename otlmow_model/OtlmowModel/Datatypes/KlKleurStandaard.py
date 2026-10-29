# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKleurStandaard(KeuzelijstField):
    """De mogelijke standaard (RAL) kleuren die gekozen kunnen worden."""
    naam = 'KlKleurStandaard'
    label = 'Kleur standaard'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlKleurStandaard'
    definition = 'De mogelijke standaard (RAL) kleuren die gekozen kunnen worden.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKleurStandaard'
    options = {
        'niet-van-toepassing': KeuzelijstWaarde(invulwaarde='niet-van-toepassing',
                                                label='Niet van toepassing',
                                                status='ingebruik',
                                                definitie="De waarde 'niet van toepassing' wordt wanneer beschermendeLaag.beschermlaag de waarde 'gegalvaniseerd' of 'inox' heeft",
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurStandaard/niet-van-toepassing'),
        'ral-1023-geel': KeuzelijstWaarde(invulwaarde='ral-1023-geel',
                                          label='RAL-1023 (geel)',
                                          status='ingebruik',
                                          definitie='RAL-1023 (geel)',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurStandaard/ral-1023-geel'),
        'ral-1023-geel-ral-9017-zwart': KeuzelijstWaarde(invulwaarde='ral-1023-geel-ral-9017-zwart',
                                                         label='RAL-1023 (geel) - RAL-9017 (zwart)',
                                                         status='ingebruik',
                                                         definitie='RAL-1023 (geel) - RAL-9017 (zwart)',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurStandaard/ral-1023-geel-ral-9017-zwart'),
        'ral-3001-rood': KeuzelijstWaarde(invulwaarde='ral-3001-rood',
                                          label='RAL-3001 (rood)',
                                          status='ingebruik',
                                          definitie='RAL-3001 (rood)',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurStandaard/ral-3001-rood'),
        'ral-3002-rood': KeuzelijstWaarde(invulwaarde='ral-3002-rood',
                                          label='RAL-3002 (rood)',
                                          status='ingebruik',
                                          definitie='RAL-3002 (rood)',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurStandaard/ral-3002-rood'),
        'ral-3004-rood': KeuzelijstWaarde(invulwaarde='ral-3004-rood',
                                          label='RAL-3004 (rood)',
                                          status='ingebruik',
                                          definitie='RAL-3004 (rood)',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurStandaard/ral-3004-rood'),
        'ral-6002-groen': KeuzelijstWaarde(invulwaarde='ral-6002-groen',
                                           label='RAL-6002 (groen)',
                                           status='ingebruik',
                                           definitie='RAL-6002 (groen)',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurStandaard/ral-6002-groen'),
        'ral-6005-groen': KeuzelijstWaarde(invulwaarde='ral-6005-groen',
                                           label='RAL-6005 (groen)',
                                           status='ingebruik',
                                           definitie='RAL-6005 (groen)',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurStandaard/ral-6005-groen'),
        'ral-7012-grijs': KeuzelijstWaarde(invulwaarde='ral-7012-grijs',
                                           label='RAL-7012 (grijs)',
                                           status='ingebruik',
                                           definitie='RAL-7012 (grijs)',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurStandaard/ral-7012-grijs'),
        'ral-7016-grijs': KeuzelijstWaarde(invulwaarde='ral-7016-grijs',
                                           label='RAL-7016 (grijs)',
                                           status='ingebruik',
                                           definitie='RAL-7016 (grijs)',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurStandaard/ral-7016-grijs'),
        'ral-7022-grijs': KeuzelijstWaarde(invulwaarde='ral-7022-grijs',
                                           label='RAL-7022 (grijs)',
                                           status='ingebruik',
                                           definitie='RAL-7022 (grijs)',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurStandaard/ral-7022-grijs'),
        'ral-7024-grijs': KeuzelijstWaarde(invulwaarde='ral-7024-grijs',
                                           label='RAL-7024 (grijs)',
                                           status='ingebruik',
                                           definitie='RAL-7024 (grijs)',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurStandaard/ral-7024-grijs'),
        'ral-7038-grijs': KeuzelijstWaarde(invulwaarde='ral-7038-grijs',
                                           label='RAL-7038 (grijs)',
                                           status='ingebruik',
                                           definitie='RAL-7038 (grijs)',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurStandaard/ral-7038-grijs'),
        'ral-9005-zwart': KeuzelijstWaarde(invulwaarde='ral-9005-zwart',
                                           label='RAL-9005 (zwart)',
                                           status='ingebruik',
                                           definitie='RAL-9005 (zwart)',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurStandaard/ral-9005-zwart'),
        'ral-9017-zwart': KeuzelijstWaarde(invulwaarde='ral-9017-zwart',
                                           label='RAL-9017 (zwart)',
                                           status='ingebruik',
                                           definitie='RAL-9017 (zwart)',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurStandaard/ral-9017-zwart'),
        'stadsgrijs': KeuzelijstWaarde(invulwaarde='stadsgrijs',
                                       label='Stadsgrijs',
                                       status='ingebruik',
                                       definitie='Stadsgrijs Antwerpen',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurStandaard/stadsgrijs')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

