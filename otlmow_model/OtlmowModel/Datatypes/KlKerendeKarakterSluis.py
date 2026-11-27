# coding=utf-8
from types import MappingProxyType

from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKerendeKarakterSluis(KeuzelijstField):
    """De verschillende kerende karakters van een sluis."""
    naam = 'KlKerendeKarakterSluis'
    label = 'Kerende karakter van een sluis'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlKerendeKarakterSluis'
    definition = 'De verschillende kerende karakters van een sluis.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKerendeKarakterSluis'
    options: MappingProxyType[str, KeuzelijstWaarde] = MappingProxyType({
        'dubbel': KeuzelijstWaarde(invulwaarde='dubbel',
                                   label='dubbel',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKerendeKarakterSluis/dubbel'),
        'enkel': KeuzelijstWaarde(invulwaarde='enkel',
                                  label='enkel',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKerendeKarakterSluis/enkel')
    })

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

