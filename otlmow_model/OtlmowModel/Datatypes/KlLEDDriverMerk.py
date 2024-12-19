# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEDDriverMerk(KeuzelijstField):
    """Het merk van de LED-driver."""
    naam = 'KlLEDDriverMerk'
    label = 'LED-driver merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEDDriverMerk'
    definition = 'Het merk van de LED-driver.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEDDriverMerk'
    options = {
        'inventronics': KeuzelijstWaarde(invulwaarde='inventronics',
                                         label='Inventronics',
                                         status='ingebruik',
                                         definitie='Inventronics',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEDDriverMerk/inventronics'),
        'mean-well': KeuzelijstWaarde(invulwaarde='mean-well',
                                      label='Mean Well',
                                      status='ingebruik',
                                      definitie='Mean Well',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEDDriverMerk/mean-well'),
        'osram': KeuzelijstWaarde(invulwaarde='osram',
                                  label='OSRAM',
                                  status='ingebruik',
                                  definitie='OSRAM',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEDDriverMerk/osram'),
        'philips': KeuzelijstWaarde(invulwaarde='philips',
                                    label='PHILIPS',
                                    status='ingebruik',
                                    definitie='PHILIPS',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEDDriverMerk/philips'),
        'signify': KeuzelijstWaarde(invulwaarde='signify',
                                    label='Signify',
                                    status='ingebruik',
                                    definitie='Signify',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEDDriverMerk/signify')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

