# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlToegangsprocedureBijlageType(KeuzelijstField):
    """De bijlagetypes van een toegangsprocedure."""
    naam = 'KlToegangsprocedureBijlageType'
    label = 'Bijlagetype toegangsprocedure'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlToegangsprocedureBijlageType'
    definition = 'De bijlagetypes van een toegangsprocedure.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlToegangsprocedureBijlageType'
    options = {
        'aanvraagformulier': KeuzelijstWaarde(invulwaarde='aanvraagformulier',
                                              label='aanvraagformulier',
                                              status='ingebruik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToegangsprocedureBijlageType/aanvraagformulier'),
        'andere': KeuzelijstWaarde(invulwaarde='andere',
                                   label='andere',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToegangsprocedureBijlageType/andere'),
        'handleiding': KeuzelijstWaarde(invulwaarde='handleiding',
                                        label='handleiding',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToegangsprocedureBijlageType/handleiding'),
        'reglement': KeuzelijstWaarde(invulwaarde='reglement',
                                      label='reglement',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToegangsprocedureBijlageType/reglement'),
        'routebeschrijving': KeuzelijstWaarde(invulwaarde='routebeschrijving',
                                              label='routebeschrijving',
                                              status='ingebruik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToegangsprocedureBijlageType/routebeschrijving')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

