# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalVoegband(KeuzelijstField):
    """Lijst met de verschillende opties van materiaal voor een voegband."""
    naam = 'KlMateriaalVoegband'
    label = 'keuzelijst materiaal voegband'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMateriaalVoegband'
    definition = 'Lijst met de verschillende opties van materiaal voor een voegband.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalVoegband'
    options = {
        'manillatouw': KeuzelijstWaarde(invulwaarde='manillatouw',
                                        label='manillatouw',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalVoegband/manillatouw'),
        'rubber': KeuzelijstWaarde(invulwaarde='rubber',
                                   label='rubber',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalVoegband/rubber'),
        'rubber-staal': KeuzelijstWaarde(invulwaarde='rubber-staal',
                                         label='rubber-staal',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalVoegband/rubber-staal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

