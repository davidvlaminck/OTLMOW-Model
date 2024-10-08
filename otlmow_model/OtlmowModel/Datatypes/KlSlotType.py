# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSlotType(KeuzelijstField):
    """Keuzelijst voor de types sloten volgens de gebruikte uitvoering."""
    naam = 'KlSlotType'
    label = 'Slot type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSlotType'
    definition = 'Keuzelijst voor de types sloten volgens de gebruikte uitvoering.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSlotType'
    options = {
        'hangslot': KeuzelijstWaarde(invulwaarde='hangslot',
                                     label='hangslot',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlotType/hangslot'),
        'lockerslot': KeuzelijstWaarde(invulwaarde='lockerslot',
                                       label='lockerslot',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlotType/lockerslot'),
        'motorslot': KeuzelijstWaarde(invulwaarde='motorslot',
                                      label='motorslot',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlotType/motorslot'),
        'ontsluiter': KeuzelijstWaarde(invulwaarde='ontsluiter',
                                       label='ontsluiter',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlotType/ontsluiter'),
        'simpel-mechanisch-slot': KeuzelijstWaarde(invulwaarde='simpel-mechanisch-slot',
                                                   label='simpel mechanisch slot',
                                                   status='ingebruik',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlotType/simpel-mechanisch-slot'),
        'solenoide-slot': KeuzelijstWaarde(invulwaarde='solenoide-slot',
                                           label='solenoide slot',
                                           status='ingebruik',
                                           definitie='solenoide slot',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlotType/solenoide-slot')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

