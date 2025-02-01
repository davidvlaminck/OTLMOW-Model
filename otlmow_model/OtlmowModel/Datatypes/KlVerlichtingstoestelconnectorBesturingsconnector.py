# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerlichtingstoestelconnectorBesturingsconnector(KeuzelijstField):
    """Type van connector verwerkt in de behuizing van het verlichtingstoestel voor de aansluiting van de module voor lokale afstandsbediening en -bewaking."""
    naam = 'KlVerlichtingstoestelconnectorBesturingsconnector'
    label = 'WV-besturingsconnector'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVerlichtingstoestelconnectorBesturingsconnector'
    definition = 'Type van connector verwerkt in de behuizing van het verlichtingstoestel voor de aansluiting van de module voor lokale afstandsbediening en -bewaking.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerlichtingstoestelconnectorBesturingsconnector'
    options = {
        '5-pin': KeuzelijstWaarde(invulwaarde='5-pin',
                                  label='5 PIN',
                                  status='ingebruik',
                                  definitie='5 PIN',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelconnectorBesturingsconnector/5-pin'),
        'NEMA': KeuzelijstWaarde(invulwaarde='NEMA',
                                 label='NEMA',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelconnectorBesturingsconnector/NEMA'),
        'SR': KeuzelijstWaarde(invulwaarde='SR',
                               label='SR',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelconnectorBesturingsconnector/SR'),
        'nema-7-pin': KeuzelijstWaarde(invulwaarde='nema-7-pin',
                                       label='NEMA 7 PIN',
                                       status='ingebruik',
                                       definitie='Nema 7 pins connector',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelconnectorBesturingsconnector/nema-7-pin')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

