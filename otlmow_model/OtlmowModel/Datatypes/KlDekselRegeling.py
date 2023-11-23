# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDekselRegeling(KeuzelijstField):
    """Mogelijke regelingen van het deksel."""
    naam = 'KlDekselRegeling'
    label = 'Dekselregeling'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDekselRegeling'
    definition = 'Mogelijke regelingen van het deksel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDekselRegeling'
    options = {
        'Traploos-instelbare-afdekkingsinrichting': KeuzelijstWaarde(invulwaarde='Traploos-instelbare-afdekkingsinrichting',
                                                                     label='Traploos instelbare afdekkingsinrichting',
                                                                     status='ingebruik',
                                                                     definitie='Traploos instelbare afdekkingsinrichting',
                                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselRegeling/Traploos-instelbare-afdekkingsinrichting'),
        'geprefabriceerd-of-ter-plaatse-gestorte-regeling': KeuzelijstWaarde(invulwaarde='geprefabriceerd-of-ter-plaatse-gestorte-regeling',
                                                                             label='geprefabriceerd of ter plaatse gestorte regeling',
                                                                             status='ingebruik',
                                                                             definitie='geprefabriceerd of ter plaatse gestorte regeling',
                                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselRegeling/geprefabriceerd-of-ter-plaatse-gestorte-regeling'),
        'ingestort-in-de-dakplaat-van-kunstwerken': KeuzelijstWaarde(invulwaarde='ingestort-in-de-dakplaat-van-kunstwerken',
                                                                     label='ingestort in de dakplaat van kunstwerken',
                                                                     status='ingebruik',
                                                                     definitie='ingestort in de dakplaat van kunstwerken',
                                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselRegeling/ingestort-in-de-dakplaat-van-kunstwerken'),
        'met-ter-plaatse-gestorte-ringbalk': KeuzelijstWaarde(invulwaarde='met-ter-plaatse-gestorte-ringbalk',
                                                              label='met ter plaatse gestorte ringbalk',
                                                              status='ingebruik',
                                                              definitie='met ter plaatse gestorte ringbalk',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselRegeling/met-ter-plaatse-gestorte-ringbalk')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

