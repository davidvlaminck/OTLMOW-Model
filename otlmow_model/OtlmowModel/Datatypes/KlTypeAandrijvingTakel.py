# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeAandrijvingTakel(KeuzelijstField):
    """De mogelijke types aandrijving van een takel, volgens de aard van het mechanisme waarmee de hijsbeweging wordt gerealiseerd."""
    naam = 'KlTypeAandrijvingTakel'
    label = 'Type aandrijving takel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeAandrijvingTakel'
    definition = 'De mogelijke types aandrijving van een takel, volgens de aard van het mechanisme waarmee de hijsbeweging wordt gerealiseerd.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeAandrijvingTakel'
    options = {
        'elektrisch': KeuzelijstWaarde(invulwaarde='elektrisch',
                                       label='elektrisch',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeAandrijvingTakel/elektrisch'),
        'manueel': KeuzelijstWaarde(invulwaarde='manueel',
                                    label='manueel',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeAandrijvingTakel/manueel'),
        'pneumatisch': KeuzelijstWaarde(invulwaarde='pneumatisch',
                                        label='pneumatisch',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeAandrijvingTakel/pneumatisch')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

