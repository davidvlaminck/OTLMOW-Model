# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVGOpstelling(KeuzelijstField):
    """Beschrijft de oriëntatie van het geplaatste schermelement tov de weg. De oriëntatie van vlakke schermen kan naast loodrecht op het maaiveld ook schuin naar achter hellend of schuin naar voor hellend zijn."""
    naam = 'KlVGOpstelling'
    label = 'Vlak geluidschermelement opstelling'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVGOpstelling'
    definition = 'Beschrijft de oriëntatie van het geplaatste schermelement tov de weg. De oriëntatie van vlakke schermen kan naast loodrecht op het maaiveld ook schuin naar achter hellend of schuin naar voor hellend zijn.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVGOpstelling'
    options = {
        'gebogen': KeuzelijstWaarde(invulwaarde='gebogen',
                                    label='gebogen',
                                    status='ingebruik',
                                    definitie='Gebogen',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVGOpstelling/gebogen'),
        'loodrecht-op-maaiveld': KeuzelijstWaarde(invulwaarde='loodrecht-op-maaiveld',
                                                  label='loodrecht op maaiveld',
                                                  status='ingebruik',
                                                  definitie='loodrecht op maaiveld',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVGOpstelling/loodrecht-op-maaiveld'),
        'schuin-naar-achter-hellend': KeuzelijstWaarde(invulwaarde='schuin-naar-achter-hellend',
                                                       label='schuin naar achter hellend',
                                                       status='ingebruik',
                                                       definitie='schuin naar achter hellend t.o.v. de weg',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVGOpstelling/schuin-naar-achter-hellend'),
        'schuin-naar-voor-hellend': KeuzelijstWaarde(invulwaarde='schuin-naar-voor-hellend',
                                                     label='schuin naar voor hellend',
                                                     status='ingebruik',
                                                     definitie='schuin naar voor hellend t.o.v. de weg',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVGOpstelling/schuin-naar-voor-hellend'),
        'taludvorm': KeuzelijstWaarde(invulwaarde='taludvorm',
                                      label='taludvorm',
                                      status='ingebruik',
                                      definitie='Taludvorm',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVGOpstelling/taludvorm'),
        'taludvorm---vertikaal': KeuzelijstWaarde(invulwaarde='taludvorm---vertikaal',
                                                  label='taludvorm + vertikaal',
                                                  status='ingebruik',
                                                  definitie='Taludvorm + vertikaal',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVGOpstelling/taludvorm---vertikaal'),
        'verticaal': KeuzelijstWaarde(invulwaarde='verticaal',
                                      label='verticaal',
                                      status='ingebruik',
                                      definitie='Verticaal',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVGOpstelling/verticaal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

