# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDeurType(KeuzelijstField):
    """De mogelijke types van een deur."""
    naam = 'KlDeurType'
    label = 'Deurtype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDeurType'
    definition = 'De mogelijke types van een deur.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDeurType'
    options = {
        'branddeur': KeuzelijstWaarde(invulwaarde='branddeur',
                                      label='Branddeur',
                                      status='ingebruik',
                                      definitie='Branddeur',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDeurType/branddeur'),
        'dienstdeur': KeuzelijstWaarde(invulwaarde='dienstdeur',
                                       label='Dienstdeur',
                                       status='ingebruik',
                                       definitie='Deur die technische lokalen of ruimten, waar zich technische installaties bevinden, afsluit. De lokalen of ruimten zijn enkel toegankelijk voor bevoegden.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDeurType/dienstdeur'),
        'interventiedeur': KeuzelijstWaarde(invulwaarde='interventiedeur',
                                            label='Interventiedeur',
                                            status='ingebruik',
                                            definitie='Deur die de hulpdiensten aanvullende toetredingsroutes bieden naar een incidentkoker vanuit een andere koker.',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDeurType/interventiedeur'),
        'kopdeur': KeuzelijstWaarde(invulwaarde='kopdeur',
                                    label='Kopdeur',
                                    status='ingebruik',
                                    definitie='Vluchtdeur aan de kop van een middenkoker, waarlangs de middenkoker kan worden verlaten richting de verzamelplaats (het eindpunt van een vluchtroute).',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDeurType/kopdeur'),
        'nooddeur': KeuzelijstWaarde(invulwaarde='nooddeur',
                                     label='Nooddeur',
                                     status='ingebruik',
                                     definitie='Nooddeur',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDeurType/nooddeur'),
        'toegangsdeur': KeuzelijstWaarde(invulwaarde='toegangsdeur',
                                         label='Toegangsdeur',
                                         status='ingebruik',
                                         definitie='Elke deur die geen specifieke rol vervult.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDeurType/toegangsdeur'),
        'vluchtdeur': KeuzelijstWaarde(invulwaarde='vluchtdeur',
                                       label='Vluchtdeur',
                                       status='ingebruik',
                                       definitie='Deur voor het ontvluchten in geval van calamiteiten weg van de incidentlocatie naar een veilige zone. Een vluchtdeur wordt onder alle omstandigheden zonder sleutel geopend en dit met beperkte kracht.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDeurType/vluchtdeur')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

