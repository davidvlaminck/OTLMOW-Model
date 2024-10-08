# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeerslichtMasker(KeuzelijstField):
    """Keuzelijst met de gangbare types masker die op een verkeerslicht zijn aangebracht."""
    naam = 'KlVerkeerslichtMasker'
    label = 'Verkeerslicht masker'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVerkeerslichtMasker'
    definition = 'Keuzelijst met de gangbare types masker die op een verkeerslicht zijn aangebracht.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeerslichtMasker'
    options = {
        'driehoek': KeuzelijstWaarde(invulwaarde='driehoek',
                                     label='driehoek',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/driehoek'),
        'fietser': KeuzelijstWaarde(invulwaarde='fietser',
                                    label='fietser',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/fietser'),
        'horizontale-balk': KeuzelijstWaarde(invulwaarde='horizontale-balk',
                                             label='horizontale balk',
                                             status='ingebruik',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/horizontale-balk'),
        'kleine-cirkel': KeuzelijstWaarde(invulwaarde='kleine-cirkel',
                                          label='kleine cirkel',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/kleine-cirkel'),
        'kruis': KeuzelijstWaarde(invulwaarde='kruis',
                                  label='kruis',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/kruis'),
        'niet-gekend': KeuzelijstWaarde(invulwaarde='niet-gekend',
                                        label='niet gekend',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/niet-gekend'),
        'pijl-links': KeuzelijstWaarde(invulwaarde='pijl-links',
                                       label='pijl links',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/pijl-links'),
        'pijl-rechtdoor': KeuzelijstWaarde(invulwaarde='pijl-rechtdoor',
                                           label='pijl rechtdoor',
                                           status='ingebruik',
                                           definitie='Pijl rechtdoor',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/pijl-rechtdoor'),
        'pijl-rechtdoor-links': KeuzelijstWaarde(invulwaarde='pijl-rechtdoor-links',
                                                 label='pijl rechtdoor links',
                                                 status='ingebruik',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/pijl-rechtdoor-links'),
        'pijl-rechtdoor-rechts': KeuzelijstWaarde(invulwaarde='pijl-rechtdoor-rechts',
                                                  label='pijl rechtdoor rechts',
                                                  status='ingebruik',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/pijl-rechtdoor-rechts'),
        'pijl-rechts': KeuzelijstWaarde(invulwaarde='pijl-rechts',
                                        label='pijl rechts',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/pijl-rechts'),
        'schuine-balk-+45°': KeuzelijstWaarde(invulwaarde='schuine-balk-+45°',
                                              label='schuine balk +45°',
                                              status='ingebruik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/schuine-balk-+45°'),
        'schuine-balk--45°': KeuzelijstWaarde(invulwaarde='schuine-balk--45°',
                                              label='schuine balk -45°',
                                              status='ingebruik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/schuine-balk--45°'),
        'verticale-balk': KeuzelijstWaarde(invulwaarde='verticale-balk',
                                           label='verticale balk',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/verticale-balk'),
        'vierkant-groen': KeuzelijstWaarde(invulwaarde='vierkant-groen',
                                           label='vierkant groen',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/vierkant-groen'),
        'voetganger': KeuzelijstWaarde(invulwaarde='voetganger',
                                       label='voetganger',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/voetganger'),
        'volle-lens': KeuzelijstWaarde(invulwaarde='volle-lens',
                                       label='volle lens',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeerslichtMasker/volle-lens')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

