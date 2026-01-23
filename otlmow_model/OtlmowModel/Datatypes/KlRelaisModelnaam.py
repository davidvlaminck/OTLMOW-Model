# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRelaisModelnaam(KeuzelijstField):
    """Lijst met modelnamen voor relais volgens de fabrikant."""
    naam = 'KlRelaisModelnaam'
    label = 'Modelnamen relais'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRelaisModelnaam'
    definition = 'Lijst met modelnamen voor relais volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRelaisModelnaam'
    options = {
        'drm': KeuzelijstWaarde(invulwaarde='drm',
                                label='DRM',
                                status='ingebruik',
                                definitie='DRM',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRelaisModelnaam/drm'),
        'g2tf02': KeuzelijstWaarde(invulwaarde='g2tf02',
                                   label='G2TF02',
                                   status='ingebruik',
                                   definitie='G2TF02',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRelaisModelnaam/g2tf02'),
        'mur3': KeuzelijstWaarde(invulwaarde='mur3',
                                 label='MUR3',
                                 status='ingebruik',
                                 definitie='MUR3',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRelaisModelnaam/mur3'),
        'rm35l': KeuzelijstWaarde(invulwaarde='rm35l',
                                  label='RM35L',
                                  status='ingebruik',
                                  definitie='RM35L',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRelaisModelnaam/rm35l')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

