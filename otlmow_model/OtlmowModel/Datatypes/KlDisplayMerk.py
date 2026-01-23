# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDisplayMerk(KeuzelijstField):
    """Lijst met merknamen van displays volgens de fabrikant."""
    naam = 'KlDisplayMerk'
    label = 'Display merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDisplayMerk'
    definition = 'Lijst met merknamen van displays volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDisplayMerk'
    options = {
        'siemens': KeuzelijstWaarde(invulwaarde='siemens',
                                    label='Siemens',
                                    status='ingebruik',
                                    definitie='Siemens',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDisplayMerk/siemens')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

