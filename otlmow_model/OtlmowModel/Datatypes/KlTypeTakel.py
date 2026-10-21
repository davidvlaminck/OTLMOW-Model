# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeTakel(KeuzelijstField):
    """De mogelijke types takel, geclassificeerd op basis van constructie en werkingsprincipe."""
    naam = 'KlTypeTakel'
    label = 'Type takel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeTakel'
    definition = 'De mogelijke types takel, geclassificeerd op basis van constructie en werkingsprincipe.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeTakel'
    options = {
        'kabeltakel': KeuzelijstWaarde(invulwaarde='kabeltakel',
                                       label='kabeltakel',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeTakel/kabeltakel'),
        'kettingtakel': KeuzelijstWaarde(invulwaarde='kettingtakel',
                                         label='kettingtakel',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeTakel/kettingtakel'),
        'staaldraadtakel': KeuzelijstWaarde(invulwaarde='staaldraadtakel',
                                            label='staaldraadtakel',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeTakel/staaldraadtakel')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

