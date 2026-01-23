# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMarkeringssysteem(KeuzelijstField):
    """De mogelijke markeringssystemen."""
    naam = 'KlMarkeringssysteem'
    label = 'Markeringssysteem'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlMarkeringssysteem'
    definition = 'De mogelijke markeringssystemen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMarkeringssysteem'
    options = {
        'geluidsproducerend': KeuzelijstWaarde(invulwaarde='geluidsproducerend',
                                               label='Geluidsproducerend',
                                               status='ingebruik',
                                               definitie='Verschillende soorten wegmarkeringen zullen trillingen en geluid produceren bij het overrijden. Zo zijn er ribbelmarkeringen, ribbelstrips en ribbelstroken.',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMarkeringssysteem/geluidsproducerend'),
        'geprofileerd': KeuzelijstWaarde(invulwaarde='geprofileerd',
                                         label='Geprofileerd',
                                         status='ingebruik',
                                         definitie='Geprofileerde systemen hebben in dwars- en of lengterichting veranderlijke filmdikte. Hierdoor ontstaat een reliëf met een wisselende hoogte.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMarkeringssysteem/geprofileerd'),
        'vlak': KeuzelijstWaarde(invulwaarde='vlak',
                                 label='Vlak',
                                 status='ingebruik',
                                 definitie='Een vlak systeem is een film met constante dosering. De wegmarkering wordt nagestrooid met kleine glasparels. ',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMarkeringssysteem/vlak')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

