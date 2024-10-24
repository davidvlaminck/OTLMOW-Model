# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeWand(KeuzelijstField):
    """De functie die de wand uitoefent."""
    naam = 'KlTypeWand'
    label = 'Type wand'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeWand'
    definition = 'De functie die de wand uitoefent.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeWand'
    options = {
        'binnenwand': KeuzelijstWaarde(invulwaarde='binnenwand',
                                       label='binnenwand',
                                       status='ingebruik',
                                       definitie='Wand zonder dragende functie, meestal gebruikt om ruimtes van elkaar te scheiden.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeWand/binnenwand'),
        'brilwand': KeuzelijstWaarde(invulwaarde='brilwand',
                                     label='brilwand',
                                     status='ingebruik',
                                     definitie='Wand met een uitsparing/opening voor het doorlaten van een tunnelboormachine.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeWand/brilwand'),
        'frontmuur': KeuzelijstWaarde(invulwaarde='frontmuur',
                                      label='frontmuur',
                                      status='ingebruik',
                                      definitie=' Muur van een landhoofd die de belastingen van de bovenbouw van de brug afdraagt.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeWand/frontmuur'),
        'retourmuur': KeuzelijstWaarde(invulwaarde='retourmuur',
                                       label='retourmuur',
                                       status='ingebruik',
                                       definitie='Zijdelingse muur van een landhoofd die ongeveer evenwijdig is met de brugas.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeWand/retourmuur'),
        'scheenmuur': KeuzelijstWaarde(invulwaarde='scheenmuur',
                                       label='scheenmuur',
                                       status='ingebruik',
                                       definitie='Grondkerende muur op de zool of frontmuur van een landhoofd die de voeg ondersteund en de vlotplaat draagt. De scheenmuur draagt geen belastingen van de bovenbouw van de brug af.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeWand/scheenmuur'),
        'steunwand': KeuzelijstWaarde(invulwaarde='steunwand',
                                      label='steunwand',
                                      status='ingebruik',
                                      definitie='Wand die ontworpen is om belastingen te dragen.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeWand/steunwand'),
        'tunnelfronton': KeuzelijstWaarde(invulwaarde='tunnelfronton',
                                          label='tunnelfronton',
                                          status='ingebruik',
                                          definitie='Het voorste deel van een tunnel, dat de overgang vormt tussen de tunnelopening en het omliggende landschap. Het biedt structurele ondersteuning en bescherming tegen instorting en erosie rond de tunnelopening.',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeWand/tunnelfronton'),
        'vleugelmuur': KeuzelijstWaarde(invulwaarde='vleugelmuur',
                                        label='vleugelmuur',
                                        status='ingebruik',
                                        definitie=' Zijdelingse muur van een landhoofd die in het verlengde ligt van de frontmuur.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeWand/vleugelmuur')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

