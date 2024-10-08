# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPutType(KeuzelijstField):
    """Types van put."""
    naam = 'KlPutType'
    label = 'Put type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPutType'
    definition = 'Types van put.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPutType'
    options = {
        'aansluitingstoegangsput-(ATP)': KeuzelijstWaarde(invulwaarde='aansluitingstoegangsput-(ATP)',
                                                          label='aansluitingstoegangsput (ATP)',
                                                          status='ingebruik',
                                                          definitie='Knijpopening',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutType/aansluitingstoegangsput-(ATP)'),
        'begintoegangs--of-verbindingsput-(BIP-of-DVP)': KeuzelijstWaarde(invulwaarde='begintoegangs--of-verbindingsput-(BIP-of-DVP)',
                                                                          label='begintoegangs- of verbindingsput (BIP of DVP)',
                                                                          status='ingebruik',
                                                                          definitie='Begintoegangs- of verbindingsput (= BIP of DVP)',
                                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutType/begintoegangs--of-verbindingsput-(BIP-of-DVP)'),
        'doorlooptoegangs--of-verbindingsput-(DTP-of-DVP)': KeuzelijstWaarde(invulwaarde='doorlooptoegangs--of-verbindingsput-(DTP-of-DVP)',
                                                                             label='doorlooptoegangs- of verbindingsput (DTP of DVP)',
                                                                             status='ingebruik',
                                                                             definitie='Doorlooptoegangs- of verbindingsput (= DTP of DVP)',
                                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutType/doorlooptoegangs--of-verbindingsput-(DTP-of-DVP)'),
        'hoektoegangsput-(HTP)': KeuzelijstWaarde(invulwaarde='hoektoegangsput-(HTP)',
                                                  label='hoektoegangsput (HTP)',
                                                  status='ingebruik',
                                                  definitie='Hoektoegangsput (= HTP)',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutType/hoektoegangsput-(HTP)'),
        'putbuis-of-schachttoegangsput-(STP)': KeuzelijstWaarde(invulwaarde='putbuis-of-schachttoegangsput-(STP)',
                                                                label='putbuis of schachttoegangsput (STP)',
                                                                status='ingebruik',
                                                                definitie='Putbuis of schachttoegangsput (= STP)',
                                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutType/putbuis-of-schachttoegangsput-(STP)'),
        'vervaltoegangsput-(VTP)': KeuzelijstWaarde(invulwaarde='vervaltoegangsput-(VTP)',
                                                    label='vervaltoegangsput (VTP)',
                                                    status='ingebruik',
                                                    definitie='Vervaltoegangsput (= VTP)',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutType/vervaltoegangsput-(VTP)')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

