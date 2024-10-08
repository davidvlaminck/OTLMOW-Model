# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHSBeveiligingscelHoogspanningszekering(KeuzelijstField):
    """Waarde van de hoogspanningszekering."""
    naam = 'KlHSBeveiligingscelHoogspanningszekering'
    label = 'HS-beveiligingscel hoogspanningszekering'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHSBeveiligingscelHoogspanningszekering'
    definition = 'Waarde van de hoogspanningszekering.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHSBeveiligingscelHoogspanningszekering'
    options = {
        '10': KeuzelijstWaarde(invulwaarde='10',
                               label='10',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelHoogspanningszekering/10'),
        '100': KeuzelijstWaarde(invulwaarde='100',
                                label='100',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelHoogspanningszekering/100'),
        '16': KeuzelijstWaarde(invulwaarde='16',
                               label='16',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelHoogspanningszekering/16'),
        '25': KeuzelijstWaarde(invulwaarde='25',
                               label='25',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelHoogspanningszekering/25'),
        '32': KeuzelijstWaarde(invulwaarde='32',
                               label='32',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelHoogspanningszekering/32'),
        '40': KeuzelijstWaarde(invulwaarde='40',
                               label='40',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelHoogspanningszekering/40'),
        '50': KeuzelijstWaarde(invulwaarde='50',
                               label='50',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelHoogspanningszekering/50'),
        '63': KeuzelijstWaarde(invulwaarde='63',
                               label='63',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelHoogspanningszekering/63'),
        '80': KeuzelijstWaarde(invulwaarde='80',
                               label='80',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHSBeveiligingscelHoogspanningszekering/80')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

