# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWegbermType(KeuzelijstField):
    """Types van wegberm die de plaats ten opzichte van de weg aangeven."""
    naam = 'KlWegbermType'
    label = 'Wegberm type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlWegbermType'
    definition = 'Types van wegberm die de plaats ten opzichte van de weg aangeven.'
    status = 'ingebruik'
    deprecated_version = '2.11.0'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWegbermType'
    options = {
        'buitenberm': KeuzelijstWaarde(invulwaarde='buitenberm',
                                       label='buitenberm',
                                       status='ingebruik',
                                       definitie='Wegberm tussen de grens van het wegplatform en de buitengrens van de verharde zijstrook of van de rijbaan, als er geen verharde zijstrook is.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbermType/buitenberm'),
        'middenberm': KeuzelijstWaarde(invulwaarde='middenberm',
                                       label='middenberm',
                                       status='ingebruik',
                                       definitie='Wegberm tussen de middelste rijbanen van een weg met een even aantal rijbanen.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbermType/middenberm'),
        'tussenberm': KeuzelijstWaarde(invulwaarde='tussenberm',
                                       label='tussenberm',
                                       status='ingebruik',
                                       definitie='Wegberm tussen twee rijbanen van een weg met meer dan één rijbaan, de middenberm uitgezonderd. ',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbermType/tussenberm')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

