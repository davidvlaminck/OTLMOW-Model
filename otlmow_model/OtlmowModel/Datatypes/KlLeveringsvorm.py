# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLeveringsvorm(KeuzelijstField):
    """De configuratie waarin de plank besteld wordt."""
    naam = 'KlLeveringsvorm'
    label = 'Leveringsvorm'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLeveringsvorm'
    definition = 'De configuratie waarin de plank besteld wordt.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLeveringsvorm'
    options = {
        'drieling': KeuzelijstWaarde(invulwaarde='drieling',
                                     label='drieling',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLeveringsvorm/drieling'),
        'dubbel': KeuzelijstWaarde(invulwaarde='dubbel',
                                   label='dubbel',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLeveringsvorm/dubbel'),
        'enkel': KeuzelijstWaarde(invulwaarde='enkel',
                                  label='enkel',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLeveringsvorm/enkel'),
        'pasplank': KeuzelijstWaarde(invulwaarde='pasplank',
                                     label='pasplank',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLeveringsvorm/pasplank')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

