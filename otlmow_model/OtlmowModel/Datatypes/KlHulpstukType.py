# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHulpstukType(KeuzelijstField):
    """Het type van het hulpstuk."""
    naam = 'KlHulpstukType'
    label = 'Hulpstuk type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHulpstukType'
    definition = 'Het type van het hulpstuk.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHulpstukType'
    options = {
        'T-stuk': KeuzelijstWaarde(invulwaarde='T-stuk',
                                   label='T-stuk',
                                   status='ingebruik',
                                   definitie='T-stuk',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHulpstukType/T-stuk'),
        'Y-stuk': KeuzelijstWaarde(invulwaarde='Y-stuk',
                                   label='Y-stuk',
                                   status='ingebruik',
                                   definitie='Y-stuk',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHulpstukType/Y-stuk'),
        'aansluitstuk': KeuzelijstWaarde(invulwaarde='aansluitstuk',
                                         label='aansluitstuk',
                                         status='ingebruik',
                                         definitie='aansluitstuk',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHulpstukType/aansluitstuk'),
        'bochtstuk': KeuzelijstWaarde(invulwaarde='bochtstuk',
                                      label='bochtstuk',
                                      status='ingebruik',
                                      definitie='bochtstuk',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHulpstukType/bochtstuk'),
        'perrot-koppeling': KeuzelijstWaarde(invulwaarde='perrot-koppeling',
                                             label='perrot koppeling',
                                             status='ingebruik',
                                             definitie='perrot koppeling',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHulpstukType/perrot-koppeling'),
        'storz-koppeling': KeuzelijstWaarde(invulwaarde='storz-koppeling',
                                            label='storz koppeling',
                                            status='ingebruik',
                                            definitie='Een storz koppeling is bedoeld om slangen met elkaar of met vaste armaturen te verbinden. Het is een symmetrische koppeling met een bajonet dichting die door een opstaande kraag wordt beschermd.',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHulpstukType/storz-koppeling')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

