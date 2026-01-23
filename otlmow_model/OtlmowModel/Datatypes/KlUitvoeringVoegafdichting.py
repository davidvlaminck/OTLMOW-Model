# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlUitvoeringVoegafdichting(KeuzelijstField):
    """De lijst met de mogelijke uitvoeringen van de voegafdichting."""
    naam = 'KlUitvoeringVoegafdichting'
    label = 'uitvoering voegafdichting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlUitvoeringVoegafdichting'
    definition = 'De lijst met de mogelijke uitvoeringen van de voegafdichting.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlUitvoeringVoegafdichting'
    options = {
        'band-bv-combiflex': KeuzelijstWaarde(invulwaarde='band-bv-combiflex',
                                              label='band (bv combiflex)',
                                              status='ingebruik',
                                              definitie='band (bv combiflex)',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitvoeringVoegafdichting/band-bv-combiflex'),
        'mat': KeuzelijstWaarde(invulwaarde='mat',
                                label='mat',
                                status='ingebruik',
                                definitie='mat',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitvoeringVoegafdichting/mat'),
        'plaat': KeuzelijstWaarde(invulwaarde='plaat',
                                  label='plaat',
                                  status='ingebruik',
                                  definitie='plaat',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitvoeringVoegafdichting/plaat')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

