# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAlgMateriaal(KeuzelijstField):
    """Het materiaal waaruit een object voornamelijk gebouwd is."""
    naam = 'KlAlgMateriaal'
    label = 'Materiaal soorten'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAlgMateriaal'
    definition = 'Het materiaal waaruit een object voornamelijk gebouwd is.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgMateriaal'
    options = {
        'aluminium': KeuzelijstWaarde(invulwaarde='aluminium',
                                      label='aluminium',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/aluminium'),
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/beton'),
        'glasvezelversterkt-polyester': KeuzelijstWaarde(invulwaarde='glasvezelversterkt-polyester',
                                                         label='glasvezelversterkt polyester',
                                                         status='ingebruik',
                                                         definitie='glasvezelversterkt polyester',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/glasvezelversterkt-polyester'),
        'hdpe': KeuzelijstWaarde(invulwaarde='hdpe',
                                 label='HDPE',
                                 status='ingebruik',
                                 definitie='HDPE',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/hdpe'),
        'hout': KeuzelijstWaarde(invulwaarde='hout',
                                 label='hout',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/hout'),
        'houtvezelbeton': KeuzelijstWaarde(invulwaarde='houtvezelbeton',
                                           label='houtvezelbeton',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/houtvezelbeton'),
        'inox': KeuzelijstWaarde(invulwaarde='inox',
                                 label='Inox',
                                 status='ingebruik',
                                 definitie='Inox',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/inox'),
        'kunstof': KeuzelijstWaarde(invulwaarde='kunstof',
                                    label='kunstof',
                                    status='uitgebruik',
                                    definitie='kunststof',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/kunstof'),
        'kunststof': KeuzelijstWaarde(invulwaarde='kunststof',
                                      label='kunststof',
                                      status='ingebruik',
                                      definitie='kunststof',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/kunststof'),
        'metselwerk': KeuzelijstWaarde(invulwaarde='metselwerk',
                                       label='metselwerk',
                                       status='ingebruik',
                                       definitie='metselwerk',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/metselwerk'),
        'polycarbonaat': KeuzelijstWaarde(invulwaarde='polycarbonaat',
                                          label='polycarbonaat',
                                          status='ingebruik',
                                          definitie='polycarbonaat',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/polycarbonaat'),
        'pvc': KeuzelijstWaarde(invulwaarde='pvc',
                                label='PVC',
                                status='ingebruik',
                                definitie='PVC',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/pvc'),
        'roestvrijstaal': KeuzelijstWaarde(invulwaarde='roestvrijstaal',
                                           label='roestvrijstaal',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/roestvrijstaal'),
        'rvs': KeuzelijstWaarde(invulwaarde='rvs',
                                label='RVS',
                                status='ingebruik',
                                definitie='RVS',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/rvs'),
        'staal': KeuzelijstWaarde(invulwaarde='staal',
                                  label='staal',
                                  status='ingebruik',
                                  definitie='staal',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMateriaal/staal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

