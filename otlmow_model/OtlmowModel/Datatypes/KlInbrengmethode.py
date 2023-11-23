# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlInbrengmethode(KeuzelijstField):
    """Manier waarop het object wordt ingebracht."""
    naam = 'KlInbrengmethode'
    label = 'Inbrengmethode'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlInbrengmethode'
    definition = 'Manier waarop het object wordt ingebracht.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlInbrengmethode'
    options = {
        'inbrengen-d-m-v-combinatie-van-meerdere-technieken': KeuzelijstWaarde(invulwaarde='inbrengen-d-m-v-combinatie-van-meerdere-technieken',
                                                                               label='Inbrengen d.m.v. combinatie van meerdere technieken',
                                                                               status='ingebruik',
                                                                               definitie='Het object wordt ingebracht door middel van een combinatie van meerdere technieken.',
                                                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlInbrengmethode/inbrengen-d-m-v-combinatie-van-meerdere-technieken'),
        'inbrengen-d-m-v-heien': KeuzelijstWaarde(invulwaarde='inbrengen-d-m-v-heien',
                                                  label='Inbrengen d.m.v. heien',
                                                  status='ingebruik',
                                                  definitie='Het object wordt ingebracht door middel van heien.',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlInbrengmethode/inbrengen-d-m-v-heien'),
        'inbrengen-d-m-v-hoogfrequent-trillen-met-variabel-moment': KeuzelijstWaarde(invulwaarde='inbrengen-d-m-v-hoogfrequent-trillen-met-variabel-moment',
                                                                                     label='Inbrengen d.m.v. hoogfrequent trillen met variabel moment',
                                                                                     status='ingebruik',
                                                                                     definitie='Het object wordt ingebracht door middel van hoogfrequent trillen met variabel moment.',
                                                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlInbrengmethode/inbrengen-d-m-v-hoogfrequent-trillen-met-variabel-moment'),
        'inbrengen-d-m-v-statisch-drukken': KeuzelijstWaarde(invulwaarde='inbrengen-d-m-v-statisch-drukken',
                                                             label='Inbrengen d.m.v. statisch drukken',
                                                             status='ingebruik',
                                                             definitie='Het object wordt ingebracht door middel van statisch drukken.',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlInbrengmethode/inbrengen-d-m-v-statisch-drukken'),
        'inbrengen-door-voorboring-aangezet-met-betonprop-onderaan': KeuzelijstWaarde(invulwaarde='inbrengen-door-voorboring-aangezet-met-betonprop-onderaan',
                                                                                      label='Inbrengen door voorboring aangezet met betonprop onderaan',
                                                                                      status='ingebruik',
                                                                                      definitie='Het object wordt ingebracht door een voorboring aangezet met betonprop onderaan.',
                                                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlInbrengmethode/inbrengen-door-voorboring-aangezet-met-betonprop-onderaan'),
        'inbrengen-volgens-methode-bepaald-door-de-aannemer': KeuzelijstWaarde(invulwaarde='inbrengen-volgens-methode-bepaald-door-de-aannemer',
                                                                               label='Inbrengen volgens methode bepaald door de aannemer',
                                                                               status='ingebruik',
                                                                               definitie='Het object wordt ingebracht volgens een methode bepaald door de aannemer.',
                                                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlInbrengmethode/inbrengen-volgens-methode-bepaald-door-de-aannemer')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

