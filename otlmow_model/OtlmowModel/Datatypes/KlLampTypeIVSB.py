# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLampTypeIVSB(KeuzelijstField):
    """Het type van de lamp(en) aanwezig in het inwendig verlicht signalisatiebord."""
    naam = 'KlLampTypeIVSB'
    label = 'lamp type inwendig verlicht signalisatiebord'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLampTypeIVSB'
    definition = 'Het type van de lamp(en) aanwezig in het inwendig verlicht signalisatiebord.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLampTypeIVSB'
    options = {
        'cdm-t-mw-eco-230w-842-mastercolour-e40': KeuzelijstWaarde(invulwaarde='cdm-t-mw-eco-230w-842-mastercolour-e40',
                                                                   label='CDM-T MW eco 230W/842 – MASTERColour E40',
                                                                   status='ingebruik',
                                                                   definitie='CDM-T MW eco 230W/842 – MASTERColour E40',
                                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLampTypeIVSB/cdm-t-mw-eco-230w-842-mastercolour-e40'),
        'cdm-t-mw-eco-360w-842-mastercolour-e40': KeuzelijstWaarde(invulwaarde='cdm-t-mw-eco-360w-842-mastercolour-e40',
                                                                   label='CDM-T MW eco 360W/842 – MASTERColour E40',
                                                                   status='ingebruik',
                                                                   definitie='CDM-T MW eco 360W/842 – MASTERColour E40',
                                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLampTypeIVSB/cdm-t-mw-eco-360w-842-mastercolour-e40'),
        'hpit-250w': KeuzelijstWaarde(invulwaarde='hpit-250w',
                                      label='HPIT 250W',
                                      status='ingebruik',
                                      definitie='HPIT 250W',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLampTypeIVSB/hpit-250w'),
        'hpit-400w': KeuzelijstWaarde(invulwaarde='hpit-400w',
                                      label='HPIT 400W',
                                      status='ingebruik',
                                      definitie='HPIT 400W',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLampTypeIVSB/hpit-400w'),
        'led': KeuzelijstWaarde(invulwaarde='led',
                                label='LED',
                                status='ingebruik',
                                definitie='LED',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLampTypeIVSB/led'),
        'mhhp-t-100-lv-e40': KeuzelijstWaarde(invulwaarde='mhhp-t-100-lv-e40',
                                              label='MHHP-T-100 lv. E40',
                                              status='ingebruik',
                                              definitie='MHHP-T-100 lv. E40',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLampTypeIVSB/mhhp-t-100-lv-e40'),
        'nahp-t-250-son-t-250w': KeuzelijstWaarde(invulwaarde='nahp-t-250-son-t-250w',
                                                  label='NaHP-T-250 – SON-T 250W',
                                                  status='ingebruik',
                                                  definitie='NaHP-T-250 – SON-T 250W',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLampTypeIVSB/nahp-t-250-son-t-250w'),
        'nahp-t-400-son-t-400w': KeuzelijstWaarde(invulwaarde='nahp-t-400-son-t-400w',
                                                  label='NaHP-T-400 – SON-T 400W',
                                                  status='ingebruik',
                                                  definitie='NaHP-T-400 – SON-T 400W',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLampTypeIVSB/nahp-t-400-son-t-400w'),
        'tl': KeuzelijstWaarde(invulwaarde='tl',
                               label='TL',
                               status='ingebruik',
                               definitie='TL',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLampTypeIVSB/tl'),
        'tl-30w': KeuzelijstWaarde(invulwaarde='tl-30w',
                                   label='TL 30W',
                                   status='ingebruik',
                                   definitie='TL 30W',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLampTypeIVSB/tl-30w'),
        'tl-36w': KeuzelijstWaarde(invulwaarde='tl-36w',
                                   label='TL 36W',
                                   status='ingebruik',
                                   definitie='TL 36W',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLampTypeIVSB/tl-36w')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

