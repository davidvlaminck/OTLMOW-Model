# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSensorOpstelwijze(KeuzelijstField):
    """Senor opstelwijzen."""
    naam = 'KlSensorOpstelwijze'
    label = 'Sensor opstelwijze'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlSensorOpstelwijze'
    definition = 'Senor opstelwijzen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSensorOpstelwijze'
    options = {
        'rechtstreeks-op-rechte-steun': KeuzelijstWaarde(invulwaarde='rechtstreeks-op-rechte-steun',
                                                         label='Rechtstreeks op rechte steun',
                                                         status='ingebruik',
                                                         definitie='Rechtstreeks op rechte steun',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSensorOpstelwijze/rechtstreeks-op-rechte-steun'),
        'via-dwarsligger-op-rechte-steun': KeuzelijstWaarde(invulwaarde='via-dwarsligger-op-rechte-steun',
                                                            label='Via dwarsligger op rechte steun',
                                                            status='ingebruik',
                                                            definitie='Via dwarsligger op rechte steun',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSensorOpstelwijze/via-dwarsligger-op-rechte-steun')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

