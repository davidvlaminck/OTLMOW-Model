# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIoTSensorVerbindingstype(KeuzelijstField):
    """IoT-sensor verbindingtypes."""
    naam = 'KlIoTSensorVerbindingstype'
    label = 'IoT-sensor verbindingtype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIoTSensorVerbindingstype'
    definition = 'IoT-sensor verbindingtypes.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIoTSensorVerbindingstype'
    options = {
        'simkaart': KeuzelijstWaarde(invulwaarde='simkaart',
                                     label='simkaart',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIoTSensorVerbindingstype/simkaart'),
        'zigbee': KeuzelijstWaarde(invulwaarde='zigbee',
                                   label='zigbee',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIoTSensorVerbindingstype/zigbee')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

