# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMotorbeveiligingMerk(KeuzelijstField):
    """Lijst met merknamen voor motorbeveiligingen volgens de fabrikant.."""
    naam = 'KlMotorbeveiligingMerk'
    label = 'Merken  motorbeveiligingen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMotorbeveiligingMerk'
    definition = 'Lijst met merknamen voor motorbeveiligingen volgens de fabrikant..'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMotorbeveiligingMerk'
    options = {
        'schneider': KeuzelijstWaarde(invulwaarde='schneider',
                                      label='Schneider',
                                      status='ingebruik',
                                      definitie='Schneider',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMotorbeveiligingMerk/schneider')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

