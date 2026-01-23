# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordPKModelnaam(KeuzelijstField):
    """Keuzelijst met de gangbare modelnamen van dynamische Pijl-Kruis borden. De modelnamen worden meestal door de leverancier of fabrikant bepaald."""
    naam = 'KlDynBordPKModelnaam'
    label = 'Dyn bord PK modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordPKModelnaam'
    definition = 'Keuzelijst met de gangbare modelnamen van dynamische Pijl-Kruis borden. De modelnamen worden meestal door de leverancier of fabrikant bepaald.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordPKModelnaam'
    options = {
        'PK-08J03': KeuzelijstWaarde(invulwaarde='PK-08J03',
                                     label='PK-08J03',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordPKModelnaam/PK-08J03'),
        'PK-LHT': KeuzelijstWaarde(invulwaarde='PK-LHT',
                                   label='PK-LHT',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordPKModelnaam/PK-LHT'),
        'PK-Tidal': KeuzelijstWaarde(invulwaarde='PK-Tidal',
                                     label='PK-Tidal',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordPKModelnaam/PK-Tidal'),
        'vms-l-430x340-3g-rb-l3t-b7': KeuzelijstWaarde(invulwaarde='vms-l-430x340-3g-rb-l3t-b7',
                                                       label='VMS-L-430x340-3G-RB-L3T-B7',
                                                       status='ingebruik',
                                                       definitie='VMS-L-430x340-3G-RB-L3T-B7',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordPKModelnaam/vms-l-430x340-3g-rb-l3t-b7')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

