# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBeheerBoomvorm(KeuzelijstField):
    """Behandelingswijzen van bomen."""
    naam = 'KlBeheerBoomvorm'
    label = 'Beheer boomvorm'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlBeheerBoomvorm'
    definition = 'Behandelingswijzen van bomen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBeheerBoomvorm'
    options = {
        'aanpassen-beschermingselementen-tegen-vraatschade': KeuzelijstWaarde(invulwaarde='aanpassen-beschermingselementen-tegen-vraatschade',
                                                                              label='Aanpassen beschermingselementen tegen vraatschade',
                                                                              status='ingebruik',
                                                                              definitie='Aanpassen van beschermingselementen tegen vraatschade bij bomen.',
                                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/aanpassen-beschermingselementen-tegen-vraatschade'),
        'afzagen-boompalen': KeuzelijstWaarde(invulwaarde='afzagen-boompalen',
                                              label='afzagen boompalen',
                                              status='ingebruik',
                                              definitie='Afzagen van boompalen van boompaalconstructies.',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/afzagen-boompalen'),
        'anti-wortelscherm': KeuzelijstWaarde(invulwaarde='anti-wortelscherm',
                                              label='anti-wortelscherm',
                                              status='ingebruik',
                                              definitie='Plaatsen van anti-wortel scherm in de grond onder een boom.',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/anti-wortelscherm'),
        'begeleidingssnoei': KeuzelijstWaarde(invulwaarde='begeleidingssnoei',
                                              label='begeleidingssnoei',
                                              status='ingebruik',
                                              definitie='Begeleidingssnoei van bomen.',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/begeleidingssnoei'),
        'begieten': KeuzelijstWaarde(invulwaarde='begieten',
                                     label='begieten',
                                     status='ingebruik',
                                     definitie='Periodisch begieten van bomen.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/begieten'),
        'bodemafdekking': KeuzelijstWaarde(invulwaarde='bodemafdekking',
                                           label='bodemafdekking',
                                           status='ingebruik',
                                           definitie='Bodemafdekking van de grond rond bomen.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/bodemafdekking'),
        'bodembeluchting-luchtinjectie': KeuzelijstWaarde(invulwaarde='bodembeluchting-luchtinjectie',
                                                          label='bodembeluchting-luchtinjectie',
                                                          status='ingebruik',
                                                          definitie='Bodembeluchting-luchtinjectie van de grond rond bomen.',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/bodembeluchting-luchtinjectie'),
        'boren-grondpijler': KeuzelijstWaarde(invulwaarde='boren-grondpijler',
                                              label='boren grondpijler',
                                              status='ingebruik',
                                              definitie='Boren van een grondpijler in de grond rond de boom.',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/boren-grondpijler'),
        'dynamische-kroonverankering': KeuzelijstWaarde(invulwaarde='dynamische-kroonverankering',
                                                        label='dynamische kroonverankering',
                                                        status='ingebruik',
                                                        definitie='dynamische kroonverankering van een boom.',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/dynamische-kroonverankering'),
        'gedeeltelijk-ontstronken': KeuzelijstWaarde(invulwaarde='gedeeltelijk-ontstronken',
                                                     label='gedeeltelijk ontstronken',
                                                     status='ingebruik',
                                                     definitie='Gedeeltelijk ontstronken van bomen.',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/gedeeltelijk-ontstronken'),
        'gft-compost': KeuzelijstWaarde(invulwaarde='gft-compost',
                                        label='GFT-compost',
                                        status='ingebruik',
                                        definitie='Leggen van GFT-compost op de grond rond bomen.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/gft-compost'),
        'groencompost': KeuzelijstWaarde(invulwaarde='groencompost',
                                         label='groencompost',
                                         status='ingebruik',
                                         definitie='Leggen van groencompost op de grond rond bomen.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/groencompost'),
        'gronduitwisseling-wortelzone': KeuzelijstWaarde(invulwaarde='gronduitwisseling-wortelzone',
                                                         label='gronduitwisseling wortelzone',
                                                         status='ingebruik',
                                                         definitie='Gronduitwisseling wortelzone van de grond rond bomen.',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/gronduitwisseling-wortelzone'),
        'kandelaren': KeuzelijstWaarde(invulwaarde='kandelaren',
                                       label='kandelaren',
                                       status='ingebruik',
                                       definitie='Kandelaren van bomen.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/kandelaren'),
        'knotten': KeuzelijstWaarde(invulwaarde='knotten',
                                    label='knotten',
                                    status='ingebruik',
                                    definitie='Knotten van bomen.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/knotten'),
        'kroonreductie': KeuzelijstWaarde(invulwaarde='kroonreductie',
                                          label='kroonreductie',
                                          status='ingebruik',
                                          definitie='Kroonreductie van bomen.',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/kroonreductie'),
        'leiboomsnoei': KeuzelijstWaarde(invulwaarde='leiboomsnoei',
                                         label='leiboomsnoei',
                                         status='ingebruik',
                                         definitie='Leiboomsnoei van bomen.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/leiboomsnoei'),
        'meststoffen': KeuzelijstWaarde(invulwaarde='meststoffen',
                                        label='meststoffen',
                                        status='ingebruik',
                                        definitie='Leggen van meststoffen op de grond rond bomen.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/meststoffen'),
        'meststoftabletten': KeuzelijstWaarde(invulwaarde='meststoftabletten',
                                              label='meststoftabletten',
                                              status='ingebruik',
                                              definitie='Leggen van meststoftabletten op de grond rond bomen.',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/meststoftabletten'),
        'onderhoudssnoei': KeuzelijstWaarde(invulwaarde='onderhoudssnoei',
                                            label='onderhoudssnoei',
                                            status='ingebruik',
                                            definitie='Onderhoudssnoei van bomen.',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/onderhoudssnoei'),
        'rooien': KeuzelijstWaarde(invulwaarde='rooien',
                                   label='rooien',
                                   status='ingebruik',
                                   definitie='Rooien van bomen.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/rooien'),
        'scheren': KeuzelijstWaarde(invulwaarde='scheren',
                                    label='scheren',
                                    status='ingebruik',
                                    definitie='Scheren van bomen.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/scheren'),
        'stam--en-takbescherming': KeuzelijstWaarde(invulwaarde='stam--en-takbescherming',
                                                    label='stam- en takbescherming',
                                                    status='ingebruik',
                                                    definitie='Stam- en takbescherming van bomen.',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/stam--en-takbescherming'),
        'stambescherming-zonnebrand': KeuzelijstWaarde(invulwaarde='stambescherming-zonnebrand',
                                                       label='stambescherming zonnebrand',
                                                       status='ingebruik',
                                                       definitie='Bescherming van de stam van bomen tegen zonnebrand.',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/stambescherming-zonnebrand'),
        'statische-kroonverankering': KeuzelijstWaarde(invulwaarde='statische-kroonverankering',
                                                       label='statische kroonverankering',
                                                       status='ingebruik',
                                                       definitie='Statische kroonverankering van een boom.',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/statische-kroonverankering'),
        'vellen': KeuzelijstWaarde(invulwaarde='vellen',
                                   label='vellen',
                                   status='ingebruik',
                                   definitie='Vellen van bomen.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/vellen'),
        'verplanten': KeuzelijstWaarde(invulwaarde='verplanten',
                                       label='verplanten',
                                       status='ingebruik',
                                       definitie='Verplanten van bomen.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/verplanten'),
        'verwijderen-beschermingselementen-tegen-vraatschade': KeuzelijstWaarde(invulwaarde='verwijderen-beschermingselementen-tegen-vraatschade',
                                                                                label='Verwijderen beschermingselementen tegen vraatschade',
                                                                                status='ingebruik',
                                                                                definitie='Verwijderen van beschermingselementen tegen vraatschade bij bomen.',
                                                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/verwijderen-beschermingselementen-tegen-vraatschade'),
        'verwijderen-boompalen': KeuzelijstWaarde(invulwaarde='verwijderen-boompalen',
                                                  label='verwijderen boompalen',
                                                  status='ingebruik',
                                                  definitie='Verwijderen van boompalen van boompaalconstructies.',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/verwijderen-boompalen'),
        'verwijderen-gietrand': KeuzelijstWaarde(invulwaarde='verwijderen-gietrand',
                                                 label='verwijderen gietrand',
                                                 status='ingebruik',
                                                 definitie='Verwijderen van de gietrand die soms aangelegd wordt rond de basis van bomen.',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/verwijderen-gietrand'),
        'volledig-ontstronken': KeuzelijstWaarde(invulwaarde='volledig-ontstronken',
                                                 label='volledig ontstronken',
                                                 status='ingebruik',
                                                 definitie='Volledig ontstronken van bomen.',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/volledig-ontstronken'),
        'vormsnoei': KeuzelijstWaarde(invulwaarde='vormsnoei',
                                      label='vormsnoei',
                                      status='ingebruik',
                                      definitie='Vormsnoei van bomen.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/vormsnoei'),
        'wegnemen-waterloten-en-wortelopslag': KeuzelijstWaarde(invulwaarde='wegnemen-waterloten-en-wortelopslag',
                                                                label='wegnemen waterloten en wortelopslag',
                                                                status='ingebruik',
                                                                definitie='Wegnemen van waterloten en wortelopslag van bomen.',
                                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/wegnemen-waterloten-en-wortelopslag')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))
