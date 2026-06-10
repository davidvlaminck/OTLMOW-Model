# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIoTSensortype(KeuzelijstField):
    """De mogelijke types van IoT sensoren."""
    naam = 'KlIoTSensortype'
    label = 'type sensor'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIoTSensortype'
    definition = 'De mogelijke types van IoT sensoren.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIoTSensortype'
    options = {
        'chloridesensor': KeuzelijstWaarde(invulwaarde='chloridesensor',
                                           label='chloridesensor',
                                           status='ingebruik',
                                           definitie='Een sensor die de concentratie aan chloride-ionen in een medium (zoals beton, mortel of water) meet, onder meer ter beoordeling van het risico op chloride-geïnduceerde corrosie van wapening.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIoTSensortype/chloridesensor'),
        'gronddrukcel': KeuzelijstWaarde(invulwaarde='gronddrukcel',
                                         label='gronddrukcel',
                                         status='ingebruik',
                                         definitie='Een sensor die de druk meet die de grond uitoefent op een constructie of constructie-element (de gronddruk), respectievelijk de totale spanning in de bodem op een bepaald punt.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIoTSensortype/gronddrukcel'),
        'pi-zometer': KeuzelijstWaarde(invulwaarde='pi-zometer',
                                       label='piëzometer',
                                       status='ingebruik',
                                       definitie='Een sensor die de waterspanning (poriënwaterdruk) in de bodem of het grondwaterpeil meet.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIoTSensortype/pi-zometer'),
        'scheursensor': KeuzelijstWaarde(invulwaarde='scheursensor',
                                         label='scheursensor',
                                         status='ingebruik',
                                         definitie='Een sensor die het ontstaan en de ontwikkeling van scheuren in een constructie of constructie-element registreert, doorgaans door het meten van de scheurwijdte of de relatieve verplaatsing over een scheur.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIoTSensortype/scheursensor'),
        'tiltsensor': KeuzelijstWaarde(invulwaarde='tiltsensor',
                                       label='tiltsensor',
                                       status='ingebruik',
                                       definitie='Een sensor die de hellingshoek of kanteling van een object of constructie meet ten opzichte van een referentievlak (meestal het horizontale vlak of de zwaartekrachtrichting).',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIoTSensortype/tiltsensor')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

