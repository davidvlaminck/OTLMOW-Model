# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSmeringType(KeuzelijstField):
    """Keuzelijst voor de verschillende wijzen van smering van een mechanisch systeem."""
    naam = 'KlSmeringType'
    label = 'Smering type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlSmeringType'
    definition = 'Keuzelijst voor de verschillende wijzen van smering van een mechanisch systeem.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSmeringType'
    options = {
        'drooglopend': KeuzelijstWaarde(invulwaarde='drooglopend',
                                        label='drooglopend',
                                        status='ingebruik',
                                        definitie='drooglopend',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSmeringType/drooglopend'),
        'handmatig-te-smeren': KeuzelijstWaarde(invulwaarde='handmatig-te-smeren',
                                                label='handmatig te smeren',
                                                status='ingebruik',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSmeringType/handmatig-te-smeren'),
        'met-automatische-smering': KeuzelijstWaarde(invulwaarde='met-automatische-smering',
                                                     label='met automatische smering',
                                                     status='ingebruik',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSmeringType/met-automatische-smering'),
        'zelfsmerend': KeuzelijstWaarde(invulwaarde='zelfsmerend',
                                        label='zelfsmerend',
                                        status='ingebruik',
                                        definitie='zelfsmerend',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSmeringType/zelfsmerend')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

