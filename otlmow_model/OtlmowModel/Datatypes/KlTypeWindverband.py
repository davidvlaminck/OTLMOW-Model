# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeWindverband(KeuzelijstField):
    """Het type windverband."""
    naam = 'KlTypeWindverband'
    label = 'Type windverband'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeWindverband'
    definition = 'Het type windverband.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeWindverband'
    options = {
        'horizontaal-boven': KeuzelijstWaarde(invulwaarde='horizontaal-boven',
                                              label='Horizontaal boven',
                                              status='ingebruik',
                                              definitie='Horizontaal boven',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeWindverband/horizontaal-boven'),
        'horizontaal-onder': KeuzelijstWaarde(invulwaarde='horizontaal-onder',
                                              label='Horizontaal onder',
                                              status='ingebruik',
                                              definitie='Horizontaal onder',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeWindverband/horizontaal-onder'),
        'verticaal': KeuzelijstWaarde(invulwaarde='verticaal',
                                      label='Verticaal',
                                      status='ingebruik',
                                      definitie='Verticaal',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeWindverband/verticaal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

