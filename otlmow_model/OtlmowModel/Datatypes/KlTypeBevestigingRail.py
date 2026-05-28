# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeBevestigingRail(KeuzelijstField):
    """Lijst met de verschillende types bevestiging van een rail."""
    naam = 'KlTypeBevestigingRail'
    label = 'Type bevestiging rail'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeBevestigingRail'
    definition = 'Lijst met de verschillende types bevestiging van een rail.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeBevestigingRail'
    options = {
        'bout': KeuzelijstWaarde(invulwaarde='bout',
                                 label='bout',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBevestigingRail/bout'),
        'draadstang': KeuzelijstWaarde(invulwaarde='draadstang',
                                       label='draadstang',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBevestigingRail/draadstang'),
        'klassieke-spoorklem': KeuzelijstWaarde(invulwaarde='klassieke-spoorklem',
                                                label='klassieke spoorklem',
                                                status='ingebruik',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBevestigingRail/klassieke-spoorklem')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

