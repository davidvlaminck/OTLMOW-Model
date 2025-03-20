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
                                    status='uitgebruik',
                                    definitie='compact',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVEenheidType/compact'),
        'lve-19-inch': KeuzelijstWaarde(invulwaarde='lve-19-inch',
                                        label='LVE 19 inch',
                                        status='uitgebruik',
                                        definitie='LVE 19 inch',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVEenheidType/lve-19-inch'),
        'lve-19-inch-3h': KeuzelijstWaarde(invulwaarde='lve-19-inch-3h',
                                           label='LVE 19 inch 3H',
                                           status='uitgebruik',
                                           definitie='LVE 19 inch 3H',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVEenheidType/lve-19-inch-3h'),
        'lve-19-inch-6h': KeuzelijstWaarde(invulwaarde='lve-19-inch-6h',
                                           label='LVE 19 inch 6H',
                                           status='uitgebruik',
                                           definitie='LVE 19 inch 6H',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVEenheidType/lve-19-inch-6h'),
        'lve-compact': KeuzelijstWaarde(invulwaarde='lve-compact',
                                        label='LVE compact',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVEenheidType/lve-compact'),
        'lve-compact-mk2': KeuzelijstWaarde(invulwaarde='lve-compact-mk2',
                                            label='LVE compact Mk2',
                                            status='ingebruik',
                                            definitie='LVE compact Mk2',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVEenheidType/lve-compact-mk2'),
        'lve-ip-detectoren': KeuzelijstWaarde(invulwaarde='lve-ip-detectoren',
                                              label='LVE IP-detectoren',
                                              status='uitgebruik',
                                              definitie='LVE IP-detectoren',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVEenheidType/lve-ip-detectoren'),
        'lve-mini': KeuzelijstWaarde(invulwaarde='lve-mini',
                                     label='LVE MINI',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVEenheidType/lve-mini'),
        'lve-mini-mk2': KeuzelijstWaarde(invulwaarde='lve-mini-mk2',
                                         label='LVE mini Mk2',
                                         status='ingebruik',
                                         definitie='LVE mini Mk2',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVEenheidType/lve-mini-mk2'),
        'lve-v1': KeuzelijstWaarde(invulwaarde='lve-v1',
                                   label='LVE V1',
                                   status='ingebruik',
                                   definitie='LVE V1',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVEenheidType/lve-v1'),
        'mini-lve': KeuzelijstWaarde(invulwaarde='mini-lve',
                                     label='mini LVE',
                                     status='uitgebruik',
                                     definitie='mini LVE',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVEenheidType/mini-lve'),
        'sat': KeuzelijstWaarde(invulwaarde='sat',
                                label='SAT',
                                status='uitgebruik',
                                definitie='SAT',
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

