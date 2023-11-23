# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBouwmethode(KeuzelijstField):
    """Keuzelijst om aan te geven welke bouwmethode gebruikt is om het koker element tot stand te brengen."""
    naam = 'KlBouwmethode'
    label = 'type bouwmethode'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlBouwmethode'
    definition = 'Keuzelijst om aan te geven welke bouwmethode gebruikt is om het koker element tot stand te brengen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBouwmethode'
    options = {
        'box-in-box': KeuzelijstWaarde(invulwaarde='box-in-box',
                                       label='Box in Box',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBouwmethode/box-in-box'),
        'cut-and-cover': KeuzelijstWaarde(invulwaarde='cut-and-cover',
                                          label='Cut and Cover',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBouwmethode/cut-and-cover'),
        'doorgeperst': KeuzelijstWaarde(invulwaarde='doorgeperst',
                                        label='Doorgeperst',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBouwmethode/doorgeperst'),
        'geboord': KeuzelijstWaarde(invulwaarde='geboord',
                                    label='Geboord',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBouwmethode/geboord'),
        'in-situ': KeuzelijstWaarde(invulwaarde='in-situ',
                                    label='In Situ',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBouwmethode/in-situ'),
        'microtunneling': KeuzelijstWaarde(invulwaarde='microtunneling',
                                           label='Microtunneling',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBouwmethode/microtunneling'),
        'paralumen': KeuzelijstWaarde(invulwaarde='paralumen',
                                      label='Paralumen',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBouwmethode/paralumen'),
        'zink': KeuzelijstWaarde(invulwaarde='zink',
                                 label='Zink',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBouwmethode/zink')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

