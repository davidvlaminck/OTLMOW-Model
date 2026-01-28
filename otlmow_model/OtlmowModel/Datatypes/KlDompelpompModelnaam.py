# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDompelpompModelnaam(KeuzelijstField):
    """Lijst van modelnamen van dompelpompen volgens de fabrikant."""
    naam = 'KlDompelpompModelnaam'
    label = 'Modelnamen dompelpompen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDompelpompModelnaam'
    definition = 'Lijst van modelnamen van dompelpompen volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDompelpompModelnaam'
    options = {
        'tp50v26': KeuzelijstWaarde(invulwaarde='tp50v26',
                                    label='TP50V26',
                                    status='ingebruik',
                                    definitie='TP50V26',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDompelpompModelnaam/tp50v26')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

