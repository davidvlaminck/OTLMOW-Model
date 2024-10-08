# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNetwerklinkMediumtype(KeuzelijstField):
    """Mogelijke waarden voor het type drager waarlangs data door de link getransporteerd wordt."""
    naam = 'KlNetwerklinkMediumtype'
    label = 'Netwerklink mediumtype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNetwerklinkMediumtype'
    definition = 'Mogelijke waarden voor het type drager waarlangs data door de link getransporteerd wordt.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNetwerklinkMediumtype'
    options = {
        'andere': KeuzelijstWaarde(invulwaarde='andere',
                                   label='andere',
                                   status='ingebruik',
                                   definitie='De link tussen de netwerkpoorten wordt gerealiseerd via een andere dan een optische, UTP, DSL of transportnetwerk verbinding.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerklinkMediumtype/andere'),
        'dsl': KeuzelijstWaarde(invulwaarde='dsl',
                                label='DSL',
                                status='ingebruik',
                                definitie='De link tussen de netwerkpoorten wordt gerealiseerd via een DSL verbinding.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerklinkMediumtype/dsl'),
        'optisch': KeuzelijstWaarde(invulwaarde='optisch',
                                    label='optisch',
                                    status='ingebruik',
                                    definitie='De link tussen de netwerkpoorten wordt gerealiseerd via een glasvezelkabel.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerklinkMediumtype/optisch'),
        'transportnetwerk': KeuzelijstWaarde(invulwaarde='transportnetwerk',
                                             label='transportnetwerk',
                                             status='ingebruik',
                                             definitie='De link tussen de netwerkpoorten wordt gerealiseerd via het optisch transportnetwerk.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerklinkMediumtype/transportnetwerk'),
        'utp': KeuzelijstWaarde(invulwaarde='utp',
                                label='UTP',
                                status='ingebruik',
                                definitie='De link tussen de netwerkpoorten wordt gerealiseerd via een UTP kabel.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerklinkMediumtype/utp')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

