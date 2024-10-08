# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMIVEenheidType(KeuzelijstField):
    """Mogelijke opties van eenheid types/"""
    naam = 'KlMIVEenheidType'
    label = 'MIV eenheid type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlMIVEenheidType'
    definition = 'Mogelijke opties van eenheid types/'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMIVEenheidType'
    options = {
        'compact': KeuzelijstWaarde(invulwaarde='compact',
                                    label='compact',
                                    status='ingebruik',
                                    definitie='compact',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVEenheidType/compact'),
        'lve-19-inch': KeuzelijstWaarde(invulwaarde='lve-19-inch',
                                        label='LVE 19 inch',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVEenheidType/lve-19-inch'),
        'lve-19-inch-3h': KeuzelijstWaarde(invulwaarde='lve-19-inch-3h',
                                           label='LVE 19 inch 3H',
                                           status='ingebruik',
                                           definitie='LVE 19 inch 3H',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVEenheidType/lve-19-inch-3h'),
        'lve-19-inch-6h': KeuzelijstWaarde(invulwaarde='lve-19-inch-6h',
                                           label='LVE 19 inch 6H',
                                           status='ingebruik',
                                           definitie='LVE 19 inch 6H',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVEenheidType/lve-19-inch-6h'),
        'lve-compact': KeuzelijstWaarde(invulwaarde='lve-compact',
                                        label='LVE compact',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVEenheidType/lve-compact'),
        'lve-ip-detectoren': KeuzelijstWaarde(invulwaarde='lve-ip-detectoren',
                                              label='LVE IP-detectoren',
                                              status='ingebruik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVEenheidType/lve-ip-detectoren'),
        'lve-mini': KeuzelijstWaarde(invulwaarde='lve-mini',
                                     label='LVE MINI',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVEenheidType/lve-mini'),
        'mini-lve': KeuzelijstWaarde(invulwaarde='mini-lve',
                                     label='mini LVE',
                                     status='ingebruik',
                                     definitie='mini LVE',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVEenheidType/mini-lve'),
        'sat': KeuzelijstWaarde(invulwaarde='sat',
                                label='SAT',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVEenheidType/sat'),
        'satelliet-module': KeuzelijstWaarde(invulwaarde='satelliet-module',
                                             label='satelliet module',
                                             status='ingebruik',
                                             definitie='satelliet module',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVEenheidType/satelliet-module')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

