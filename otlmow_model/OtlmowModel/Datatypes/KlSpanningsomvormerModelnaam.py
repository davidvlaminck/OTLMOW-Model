# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSpanningsomvormerModelnaam(KeuzelijstField):
    """Lijst van modelnamen van spanningsomvormers volgens de fabrikant."""
    naam = 'KlSpanningsomvormerModelnaam'
    label = 'Modelnamen spanningsomvormers'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSpanningsomvormerModelnaam'
    definition = 'Lijst van modelnamen van spanningsomvormers volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSpanningsomvormerModelnaam'
    options = {
        'cp10-241': KeuzelijstWaarde(invulwaarde='cp10-241',
                                     label='CP10.241',
                                     status='ingebruik',
                                     definitie='CP10.241',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSpanningsomvormerModelnaam/cp10-241'),
        'cp5-241': KeuzelijstWaarde(invulwaarde='cp5-241',
                                    label='CP5.241',
                                    status='ingebruik',
                                    definitie='CP5.241',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSpanningsomvormerModelnaam/cp5-241'),
        'minipack': KeuzelijstWaarde(invulwaarde='minipack',
                                     label='Minipack',
                                     status='ingebruik',
                                     definitie='Minipack',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSpanningsomvormerModelnaam/minipack'),
        'qs10-241': KeuzelijstWaarde(invulwaarde='qs10-241',
                                     label='QS10.241',
                                     status='ingebruik',
                                     definitie='QS10.241',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSpanningsomvormerModelnaam/qs10-241'),
        'qs5-241': KeuzelijstWaarde(invulwaarde='qs5-241',
                                    label='QS5.241',
                                    status='ingebruik',
                                    definitie='QS5.241',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSpanningsomvormerModelnaam/qs5-241'),
        'smartpack-s': KeuzelijstWaarde(invulwaarde='smartpack-s',
                                        label='Smartpack S ',
                                        status='ingebruik',
                                        definitie='Smartpack S ',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSpanningsomvormerModelnaam/smartpack-s'),
        'trio': KeuzelijstWaarde(invulwaarde='trio',
                                 label='Trio',
                                 status='ingebruik',
                                 definitie='Trio',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSpanningsomvormerModelnaam/trio')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

