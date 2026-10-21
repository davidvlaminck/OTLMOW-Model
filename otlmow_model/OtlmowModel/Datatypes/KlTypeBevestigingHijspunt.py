# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeBevestigingHijspunt(KeuzelijstField):
    """De mogelijke wijzen waarop een hijspunt aan de bouwkundige constructie is bevestigd."""
    naam = 'KlTypeBevestigingHijspunt'
    label = 'Type bevestigingspunt'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeBevestigingHijspunt'
    definition = 'De mogelijke wijzen waarop een hijspunt aan de bouwkundige constructie is bevestigd.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeBevestigingHijspunt'
    options = {
        'chemisch-verankerd': KeuzelijstWaarde(invulwaarde='chemisch-verankerd',
                                               label='chemisch verankerd',
                                               status='ingebruik',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBevestigingHijspunt/chemisch-verankerd'),
        'gebout': KeuzelijstWaarde(invulwaarde='gebout',
                                   label='gebout',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBevestigingHijspunt/gebout'),
        'gelast': KeuzelijstWaarde(invulwaarde='gelast',
                                   label='gelast',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBevestigingHijspunt/gelast'),
        'gevezen': KeuzelijstWaarde(invulwaarde='gevezen',
                                    label='gevezen',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBevestigingHijspunt/gevezen'),
        'ingebetonneerd': KeuzelijstWaarde(invulwaarde='ingebetonneerd',
                                           label='ingebetonneerd',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBevestigingHijspunt/ingebetonneerd')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

