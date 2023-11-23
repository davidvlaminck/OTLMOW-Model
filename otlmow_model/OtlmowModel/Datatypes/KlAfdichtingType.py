# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAfdichtingType(KeuzelijstField):
    """De verschillende types afdichtingen."""
    naam = 'KlAfdichtingType'
    label = 'Afdichting type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAfdichtingType'
    definition = 'De verschillende types afdichtingen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAfdichtingType'
    options = {
        'gietasfalt': KeuzelijstWaarde(invulwaarde='gietasfalt',
                                       label='gietasfalt',
                                       status='ingebruik',
                                       definitie='Gietasfalt is een soort asfalt die door zijn overmaat aan bitumen in het mengsel van stenen, zand, vulstof en bitumen zijn waterdichte en dampdichte eigenschap verkrijgt.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfdichtingType/gietasfalt'),
        'hars': KeuzelijstWaarde(invulwaarde='hars',
                                 label='hars',
                                 status='ingebruik',
                                 definitie='Hars is een organische vaste of half-vloeibare, vaak kleverige verbinding die meestal lichtgeel en doorschijnend is, onoplosbare is in water, geen of weinig neiging heeft tot kristalliseren, mogelijk kan gaan vloeien als het aan spanningen wordt onderworpen.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfdichtingType/hars'),
        'membraan': KeuzelijstWaarde(invulwaarde='membraan',
                                     label='membraan',
                                     status='ingebruik',
                                     definitie='Een membraan of vlies is een dunne, vlakke structuur die twee ruimtes van elkaar scheidt.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfdichtingType/membraan')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

