# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlStortsteenPlaatsingswijze(KeuzelijstField):
    """De manier waarop de stenen worden geplaatst."""
    naam = 'KlStortsteenPlaatsingswijze'
    label = 'Plaatsingswijze'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlStortsteenPlaatsingswijze'
    definition = 'De manier waarop de stenen worden geplaatst.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlStortsteenPlaatsingswijze'
    options = {
        'gestapeld': KeuzelijstWaarde(invulwaarde='gestapeld',
                                      label='gestapeld',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenPlaatsingswijze/gestapeld'),
        'gewone-bestorting-met-fixatie-colloïdaal-beton': KeuzelijstWaarde(invulwaarde='gewone-bestorting-met-fixatie-colloïdaal-beton',
                                                                           label='gewone bestorting met fixatie colloïdaal beton',
                                                                           status='ingebruik',
                                                                           definitie='gewone bestorting met fixatie colloïdaal beton',
                                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenPlaatsingswijze/gewone-bestorting-met-fixatie-colloïdaal-beton'),
        'gewone-bestorting-zonder-fixatie-colloïdaal-beton': KeuzelijstWaarde(invulwaarde='gewone-bestorting-zonder-fixatie-colloïdaal-beton',
                                                                              label='gewone bestorting zonder fixatie colloïdaal beton',
                                                                              status='ingebruik',
                                                                              definitie='gewone bestorting zonder fixatie colloïdaal beton',
                                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenPlaatsingswijze/gewone-bestorting-zonder-fixatie-colloïdaal-beton'),
        'stroomkuilenprofiel-met-fixatie-colloïdaal-beton': KeuzelijstWaarde(invulwaarde='stroomkuilenprofiel-met-fixatie-colloïdaal-beton',
                                                                             label='stroomkuilenprofiel met fixatie colloïdaal beton',
                                                                             status='ingebruik',
                                                                             definitie='stroomkuilenprofiel met fixatie colloïdaal beton',
                                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenPlaatsingswijze/stroomkuilenprofiel-met-fixatie-colloïdaal-beton'),
        'stroomkuilenprofiel-zonder-fixatie-colloïdaal-beton': KeuzelijstWaarde(invulwaarde='stroomkuilenprofiel-zonder-fixatie-colloïdaal-beton',
                                                                                label='stroomkuilenprofiel zonder fixatie colloïdaal beton',
                                                                                status='ingebruik',
                                                                                definitie='stroomkuilenprofiel zonder fixatie colloïdaal beton',
                                                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenPlaatsingswijze/stroomkuilenprofiel-zonder-fixatie-colloïdaal-beton')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

