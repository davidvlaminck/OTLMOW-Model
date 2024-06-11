# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAanvaarbeschermingType(KeuzelijstField):
    """De soort van de aanvaarbescherming."""
    naam = 'KlAanvaarbeschermingType'
    label = 'Type aanvaarbescherming'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlAanvaarbeschermingType'
    definition = 'De soort van de aanvaarbescherming.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAanvaarbeschermingType'
    options = {
        'dukdalf': KeuzelijstWaarde(invulwaarde='dukdalf',
                                    label='Dukdalf',
                                    status='ingebruik',
                                    definitie='Een in het water geplaatste rechtopstaande paal, al dan niet met schoorpalen voor het vastleggen en afmeren van schepen.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAanvaarbeschermingType/dukdalf'),
        'geleidewerk': KeuzelijstWaarde(invulwaarde='geleidewerk',
                                        label='Geleidewerk',
                                        status='ingebruik',
                                        definitie='Constructie met als doel schepen zodanig te begeleiden dat zowel het schip als het kunstwerk wordt beschermd.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAanvaarbeschermingType/geleidewerk'),
        'geleidewerk-met-dukdalf': KeuzelijstWaarde(invulwaarde='geleidewerk-met-dukdalf',
                                                    label='Geleidewerk met dukdalf',
                                                    status='ingebruik',
                                                    definitie='Geleidewerk voorzien van dukdalven.',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAanvaarbeschermingType/geleidewerk-met-dukdalf'),
        'niet-opgenomen-in-de-lijst': KeuzelijstWaarde(invulwaarde='niet-opgenomen-in-de-lijst',
                                                       label='Niet opgenomen in de lijst',
                                                       status='ingebruik',
                                                       definitie='Niet opgenomen in de lijst.',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAanvaarbeschermingType/niet-opgenomen-in-de-lijst')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

