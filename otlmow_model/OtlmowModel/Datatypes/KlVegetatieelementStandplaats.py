# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVegetatieelementStandplaats(KeuzelijstField):
    """De mogelijke standplaatsen van een vegetatieelement."""
    naam = 'KlVegetatieelementStandplaats'
    label = 'Vegetatieelement standplaats'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVegetatieelementStandplaats'
    definition = 'De mogelijke standplaatsen van een vegetatieelement.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVegetatieelementStandplaats'
    options = {
        'gesloten-bebouwing': KeuzelijstWaarde(invulwaarde='gesloten-bebouwing',
                                               label='gesloten bebouwing',
                                               status='ingebruik',
                                               definitie='0,9 - gesloten bebouwing',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatieelementStandplaats/gesloten-bebouwing'),
        'landelijk-gebied': KeuzelijstWaarde(invulwaarde='landelijk-gebied',
                                             label='landelijk gebied',
                                             status='ingebruik',
                                             definitie='0,6 - landelijk gebied',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatieelementStandplaats/landelijk-gebied'),
        'open-en-halfopen-bebouwing': KeuzelijstWaarde(invulwaarde='open-en-halfopen-bebouwing',
                                                       label='open en halfopen bebouwing',
                                                       status='ingebruik',
                                                       definitie='0,8 - open en halfopen bebouwing',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatieelementStandplaats/open-en-halfopen-bebouwing'),
        'overgangszone-bebouwde-kom-landelijk-gebied': KeuzelijstWaarde(invulwaarde='overgangszone-bebouwde-kom-landelijk-gebied',
                                                                        label='overgangszone bebouwde kom - landelijk gebied',
                                                                        status='ingebruik',
                                                                        definitie='0,7 - overgangszone: bebouwde kom - landelijk gebied',
                                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatieelementStandplaats/overgangszone-bebouwde-kom-landelijk-gebied'),
        'sterk-verstedelijkte-stads-of-dorpskern': KeuzelijstWaarde(invulwaarde='sterk-verstedelijkte-stads-of-dorpskern',
                                                                    label='sterk verstedelijkte stads- of dorpskern',
                                                                    status='ingebruik',
                                                                    definitie='1,0 - sterk verstedelijkte stads- of dorpskern',
                                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatieelementStandplaats/sterk-verstedelijkte-stads-of-dorpskern')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

