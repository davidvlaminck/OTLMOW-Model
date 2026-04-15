# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCorrosieCategorie(KeuzelijstField):
    """De mogelijke corrosiecategorieën."""
    naam = 'KlCorrosieCategorie'
    label = 'Corrosiecategorieën'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCorrosieCategorie'
    definition = 'De mogelijke corrosiecategorieën.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCorrosieCategorie'
    options = {
        'c1-zeer-laag': KeuzelijstWaarde(invulwaarde='c1-zeer-laag',
                                         label='C1 - Zeer Laag',
                                         status='ingebruik',
                                         definitie='Binnen : Verwarmde gebouwen met een schone atmosfeer.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCorrosieCategorie/c1-zeer-laag'),
        'c2-laag': KeuzelijstWaarde(invulwaarde='c2-laag',
                                    label='C2 - Laag',
                                    status='ingebruik',
                                    definitie='Binnen: Niet-verwarmde gebouwen waar condensatie kan optreden, zoals bv. magazijnen en sporthallen. Buiten: Atmosferen met lage vervuilingsniveaus; meestal landelijke gebieden.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCorrosieCategorie/c2-laag'),
        'c3-gemiddeld': KeuzelijstWaarde(invulwaarde='c3-gemiddeld',
                                         label='C3 - Gemiddeld',
                                         status='ingebruik',
                                         definitie='Binnen: Ruimten met een hoge luchtvochtigheid en enige vervuiling, zoals brouwerijen, melkerijen, washuizen. Buiten: Stedelijke en industriële gebieden met matige zwaveldioxidevervuiling; kustgebieden met lage zoutniveaus.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCorrosieCategorie/c3-gemiddeld'),
        'c4-hoog': KeuzelijstWaarde(invulwaarde='c4-hoog',
                                    label='C4 - Hoog',
                                    status='ingebruik',
                                    definitie='Binnen: Chemische fabrieken, zwembaden, kustscheepswerven. Buiten: Industriële gebieden en kustgebieden met matig zoutgehalte.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCorrosieCategorie/c4-hoog'),
        'c5-zeer-hoog': KeuzelijstWaarde(invulwaarde='c5-zeer-hoog',
                                         label='C5 (Zeer Hoog)',
                                         status='ingebruik',
                                         definitie='Industriële gebieden met een hoge vochtigheid en agressieve  atmosfeer en kustgebieden met een hoog zoutgehalte.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCorrosieCategorie/c5-zeer-hoog'),
        'cx-extreem-hoog': KeuzelijstWaarde(invulwaarde='cx-extreem-hoog',
                                            label='CX (Extreem Hoog)',
                                            status='ingebruik',
                                            definitie='Offshore-gebieden met een hoog zoutgehalte en industriële  gebieden met een zeer hoge vochtigheid en agressieve atmosfeer  en subtropische en tropische atmosferen.',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCorrosieCategorie/cx-extreem-hoog'),
        'im1-zoet-water': KeuzelijstWaarde(invulwaarde='im1-zoet-water',
                                           label='Im1 (Zoet Water) ',
                                           status='ingebruik',
                                           definitie='Rivierinstallaties - kanalen met zoet water.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCorrosieCategorie/im1-zoet-water'),
        'im2-zeewater-of-brakwater': KeuzelijstWaarde(invulwaarde='im2-zeewater-of-brakwater',
                                                      label='Im2 (Zeewater of Brakwater)',
                                                      status='ingebruik',
                                                      definitie='Immersie zonder kathodische bescherming. Havengebieden met constructies zoals sluisdeuren, dammen, pieren,  kaaimuren, offshore-constructies ',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCorrosieCategorie/im2-zeewater-of-brakwater'),
        'im3-bodem': KeuzelijstWaarde(invulwaarde='im3-bodem',
                                      label='Im3 (Bodem)',
                                      status='ingebruik',
                                      definitie='Ondergrondse opslagtanks, stalen pijlers, damwanden, stalen   leidingen.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCorrosieCategorie/im3-bodem'),
        'im4-zeewater-of-brakwater-met-kathodische-bescherming': KeuzelijstWaarde(invulwaarde='im4-zeewater-of-brakwater-met-kathodische-bescherming',
                                                                                  label='Im4 (Zeewater of Brakwater - met kathodische  bescherming)',
                                                                                  status='ingebruik',
                                                                                  definitie='Immersie met kathodische bescherming  Havengebieden met constructies zoals sluisdeuren, dammen, pieren,  kaaimuren, offshore-constructies.',
                                                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCorrosieCategorie/im4-zeewater-of-brakwater-met-kathodische-bescherming')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

