# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalTaatsschoen(KeuzelijstField):
    """Lijst van mogelijke materialen voor de taatsschoen."""
    naam = 'KlMateriaalTaatsschoen'
    label = 'Materiaal taatsschoen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMateriaalTaatsschoen'
    definition = 'Lijst van mogelijke materialen voor de taatsschoen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalTaatsschoen'
    options = {
        'gietstaal': KeuzelijstWaarde(invulwaarde='gietstaal',
                                      label='gietstaal',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalTaatsschoen/gietstaal'),
        'smeedstaal': KeuzelijstWaarde(invulwaarde='smeedstaal',
                                       label='smeedstaal',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalTaatsschoen/smeedstaal'),
        'staal': KeuzelijstWaarde(invulwaarde='staal',
                                  label='staal',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalTaatsschoen/staal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

