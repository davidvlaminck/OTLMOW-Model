# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeRandafwerking(KeuzelijstField):
    """De lijst verschillende types randafwerking."""
    naam = 'KlTypeRandafwerking'
    label = 'type randafwerking'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeRandafwerking'
    definition = 'De lijst verschillende types randafwerking.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeRandafwerking'
    options = {
        'deksteen': KeuzelijstWaarde(invulwaarde='deksteen',
                                     label='deksteen',
                                     status='ingebruik',
                                     definitie='Niet-dragend, vlakvormig element dat op de bovenzijde van een rand of constructiedeel wordt geplaatst, met als primair doel bescherming tegen weersinvloeden en esthetische afwerking, zonder constructieve versterkingsfunctie.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeRandafwerking/deksteen'),
        'randprofiel': KeuzelijstWaarde(invulwaarde='randprofiel',
                                        label='randprofiel',
                                        status='ingebruik',
                                        definitie='Niet-dragend, profielvormig element (doorgaans metaal of kunststof) dat op de hoek of rand van een constructie wordt bevestigd voor mechanische bescherming, waterafvoer en lokale versteviging van de randzone.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeRandafwerking/randprofiel'),
        'randsteen': KeuzelijstWaarde(invulwaarde='randsteen',
                                      label='randsteen',
                                      status='ingebruik',
                                      definitie='Niet-dragend, lineair element dat langs de rand van een brugdek, verharding of constructie wordt aangebracht om een fysieke en visuele begrenzing of opsluiting te vormen tussen verschillende zones.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeRandafwerking/randsteen')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

