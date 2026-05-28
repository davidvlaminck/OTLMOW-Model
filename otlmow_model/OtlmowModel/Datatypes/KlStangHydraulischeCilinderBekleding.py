# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlStangHydraulischeCilinderBekleding(KeuzelijstField):
    """Keuzelijst voor de soorten bekleding voor een stang van een hydraulishe cilinder."""
    naam = 'KlStangHydraulischeCilinderBekleding'
    label = 'Stang hydraulische cilinder bekleding'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlStangHydraulischeCilinderBekleding'
    definition = 'Keuzelijst voor de soorten bekleding voor een stang van een hydraulishe cilinder.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlStangHydraulischeCilinderBekleding'
    options = {
        'keramisch': KeuzelijstWaarde(invulwaarde='keramisch',
                                      label='keramisch',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStangHydraulischeCilinderBekleding/keramisch'),
        'metallisch': KeuzelijstWaarde(invulwaarde='metallisch',
                                       label='metallisch',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStangHydraulischeCilinderBekleding/metallisch'),
        'nikkelchroom': KeuzelijstWaarde(invulwaarde='nikkelchroom',
                                         label='nikkelchroom',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStangHydraulischeCilinderBekleding/nikkelchroom')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

