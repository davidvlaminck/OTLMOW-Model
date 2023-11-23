# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerlichtingstoestelMerk(KeuzelijstField):
    """Het merk van het verlichtingstoestel."""
    naam = 'KlVerlichtingstoestelMerk'
    label = 'Verlichtingstoestel merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVerlichtingstoestelMerk'
    definition = 'Het merk van het verlichtingstoestel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerlichtingstoestelMerk'
    options = {
        'ARC': KeuzelijstWaarde(invulwaarde='ARC',
                                label='ARC',
                                status='uitgebruik',
                                definitie='ARC',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelMerk/ARC'),
        'HCI-TS': KeuzelijstWaarde(invulwaarde='HCI-TS',
                                   label='HCI-TS',
                                   status='uitgebruik',
                                   definitie='HCI-TS',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelMerk/HCI-TS'),
        'Philips': KeuzelijstWaarde(invulwaarde='Philips',
                                    label='Philips',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelMerk/Philips'),
        'Rombalux': KeuzelijstWaarde(invulwaarde='Rombalux',
                                     label='Rombalux',
                                     status='uitgebruik',
                                     definitie='Rombalux',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelMerk/Rombalux'),
        'Schreder': KeuzelijstWaarde(invulwaarde='Schreder',
                                     label='Schreder',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelMerk/Schreder'),
        'andere': KeuzelijstWaarde(invulwaarde='andere',
                                   label='andere',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelMerk/andere'),
        'lightwell': KeuzelijstWaarde(invulwaarde='lightwell',
                                      label='Lightwell',
                                      status='ingebruik',
                                      definitie='Lightwell',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelMerk/lightwell')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

