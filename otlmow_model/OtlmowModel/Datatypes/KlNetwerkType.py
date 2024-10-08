# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNetwerkType(KeuzelijstField):
    """Zie ook http://inspire.ec.europa.eu/codelist/UtilityNetworkTypeExtendedValue. Codelijst van types voor nutsvoorzieningennetwerken volgens IMKL."""
    naam = 'KlNetwerkType'
    label = 'Netwerk type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNetwerkType'
    definition = 'Zie ook http://inspire.ec.europa.eu/codelist/UtilityNetworkTypeExtendedValue. Codelijst van types voor nutsvoorzieningennetwerken volgens IMKL.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNetwerkType'
    options = {
        'crosstheme': KeuzelijstWaarde(invulwaarde='crosstheme',
                                       label='crossTheme',
                                       status='ingebruik',
                                       definitie='crossTheme',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkType/crosstheme'),
        'electricity': KeuzelijstWaarde(invulwaarde='electricity',
                                        label='electricity',
                                        status='ingebruik',
                                        definitie='electricity',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkType/electricity'),
        'elektriciteit': KeuzelijstWaarde(invulwaarde='elektriciteit',
                                          label='elektriciteit',
                                          status='ingebruik',
                                          definitie='De Klasse hoort in het elektriciteitsnet.',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkType/elektriciteit'),
        'gemengd': KeuzelijstWaarde(invulwaarde='gemengd',
                                    label='gemengd',
                                    status='ingebruik',
                                    definitie='De Klasse hoort zowel bij het elektriciteitsnet als bij het telecomnet.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkType/gemengd'),
        'glasvezel': KeuzelijstWaarde(invulwaarde='glasvezel',
                                      label='glasvezel',
                                      status='ingebruik',
                                      definitie='glasvezel',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkType/glasvezel'),
        'sewer': KeuzelijstWaarde(invulwaarde='sewer',
                                  label='sewer',
                                  status='ingebruik',
                                  definitie='sewer',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkType/sewer'),
        'telecom': KeuzelijstWaarde(invulwaarde='telecom',
                                    label='telecom',
                                    status='ingebruik',
                                    definitie='telecom',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkType/telecom'),
        'telecommunicatie': KeuzelijstWaarde(invulwaarde='telecommunicatie',
                                             label='telecommunicatie',
                                             status='ingebruik',
                                             definitie='De Klasse hoort in het telecomnet.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkType/telecommunicatie')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

