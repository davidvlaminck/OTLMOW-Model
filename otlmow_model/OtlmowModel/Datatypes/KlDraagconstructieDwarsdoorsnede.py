# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDraagconstructieDwarsdoorsnede(KeuzelijstField):
    """Lijst van mogelijke vormen van dwarsdoorsnedes van een draagconstructie."""
    naam = 'KlDraagconstructieDwarsdoorsnede'
    label = 'Draagconstructie dwarsdoorsnede'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDraagconstructieDwarsdoorsnede'
    definition = 'Lijst van mogelijke vormen van dwarsdoorsnedes van een draagconstructie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDraagconstructieDwarsdoorsnede'
    options = {
        'heptagonaal': KeuzelijstWaarde(invulwaarde='heptagonaal',
                                        label='heptagonaal',
                                        status='ingebruik',
                                        definitie='heptagonaal',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagconstructieDwarsdoorsnede/heptagonaal'),
        'octagonaal': KeuzelijstWaarde(invulwaarde='octagonaal',
                                       label='octagonaal',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagconstructieDwarsdoorsnede/octagonaal'),
        'rechthoekig': KeuzelijstWaarde(invulwaarde='rechthoekig',
                                        label='rechthoekig',
                                        status='ingebruik',
                                        definitie='rechthoekig',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagconstructieDwarsdoorsnede/rechthoekig'),
        'rond': KeuzelijstWaarde(invulwaarde='rond',
                                 label='rond',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagconstructieDwarsdoorsnede/rond'),
        'vierkant': KeuzelijstWaarde(invulwaarde='vierkant',
                                     label='vierkant',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagconstructieDwarsdoorsnede/vierkant')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

