# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPersleidingMateriaal(KeuzelijstField):
    """Materialen van de persleiding."""
    naam = 'KlPersleidingMateriaal'
    label = 'Persleiding materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPersleidingMateriaal'
    definition = 'Materialen van de persleiding.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPersleidingMateriaal'
    options = {
        'buizen-van-PVC-voor-drukleidingen.-PN-10': KeuzelijstWaarde(invulwaarde='buizen-van-PVC-voor-drukleidingen.-PN-10',
                                                                     label='buizen van PVC voor drukleidingen. PN 10',
                                                                     status='ingebruik',
                                                                     definitie='Buizen van PVC voor drukleidingen, PN 10',
                                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPersleidingMateriaal/buizen-van-PVC-voor-drukleidingen.-PN-10'),
        'buizen-van-PVC-voor-drukleidingen.-PN-16': KeuzelijstWaarde(invulwaarde='buizen-van-PVC-voor-drukleidingen.-PN-16',
                                                                     label='buizen van PVC voor drukleidingen. PN 16',
                                                                     status='ingebruik',
                                                                     definitie='Buizen van PVC voor drukleidingen, PN 16',
                                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPersleidingMateriaal/buizen-van-PVC-voor-drukleidingen.-PN-16'),
        'buizen-van-PVC-voor-drukleidingen.-PN-6': KeuzelijstWaarde(invulwaarde='buizen-van-PVC-voor-drukleidingen.-PN-6',
                                                                    label='buizen van PVC voor drukleidingen. PN 6',
                                                                    status='ingebruik',
                                                                    definitie='Buizen van PVC voor drukleidingen, PN 6',
                                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPersleidingMateriaal/buizen-van-PVC-voor-drukleidingen.-PN-6'),
        'buizen-van-gevuld-en-glasvezelversterkt-polyesterhars-voor-leidingen-onder-druk.-PN-10.-SN-10000-N-m²': KeuzelijstWaarde(invulwaarde='buizen-van-gevuld-en-glasvezelversterkt-polyesterhars-voor-leidingen-onder-druk.-PN-10.-SN-10000-N-m²',
                                                                                                                                  label='buizen van gevuld en glasvezelversterkt polyesterhars voor leidingen onder druk. PN 10. SN 10000 N-m²',
                                                                                                                                  status='ingebruik',
                                                                                                                                  definitie='Buizen van gevuld en glasvezelversterkt polyesterhars voor leidingen onder druk, PN 10, SN 10000 N/m²',
                                                                                                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPersleidingMateriaal/buizen-van-gevuld-en-glasvezelversterkt-polyesterhars-voor-leidingen-onder-druk.-PN-10.-SN-10000-N-m²'),
        'buizen-van-gevuld-en-glasvezelversterkt-polyesterhars-voor-leidingen-onder-druk.-PN-10.-SN-5000-N-m²': KeuzelijstWaarde(invulwaarde='buizen-van-gevuld-en-glasvezelversterkt-polyesterhars-voor-leidingen-onder-druk.-PN-10.-SN-5000-N-m²',
                                                                                                                                 label='buizen van gevuld en glasvezelversterkt polyesterhars voor leidingen onder druk. PN 10. SN 5000 N-m²',
                                                                                                                                 status='ingebruik',
                                                                                                                                 definitie='Buizen van gevuld en glasvezelversterkt polyesterhars voor leidingen onder druk, PN 10, SN 5000 N/m²',
                                                                                                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPersleidingMateriaal/buizen-van-gevuld-en-glasvezelversterkt-polyesterhars-voor-leidingen-onder-druk.-PN-10.-SN-5000-N-m²'),
        'buizen-van-gevuld-en-glasvezelversterkt-polyesterhars-voor-leidingen-onder-druk.-PN-16.-SN-10000-N-m²': KeuzelijstWaarde(invulwaarde='buizen-van-gevuld-en-glasvezelversterkt-polyesterhars-voor-leidingen-onder-druk.-PN-16.-SN-10000-N-m²',
                                                                                                                                  label='buizen van gevuld en glasvezelversterkt polyesterhars voor leidingen onder druk. PN 16. SN 10000 N-m²',
                                                                                                                                  status='ingebruik',
                                                                                                                                  definitie='Buizen van gevuld en glasvezelversterkt polyesterhars voor leidingen onder druk, PN 16, SN 10000 N/m²',
                                                                                                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPersleidingMateriaal/buizen-van-gevuld-en-glasvezelversterkt-polyesterhars-voor-leidingen-onder-druk.-PN-16.-SN-10000-N-m²'),
        'buizen-van-gevuld-en-glasvezelversterkt-polyesterhars-voor-leidingen-onder-druk.-PN-6.-SN-10000-N-m²': KeuzelijstWaarde(invulwaarde='buizen-van-gevuld-en-glasvezelversterkt-polyesterhars-voor-leidingen-onder-druk.-PN-6.-SN-10000-N-m²',
                                                                                                                                 label='buizen van gevuld en glasvezelversterkt polyesterhars voor leidingen onder druk. PN 6. SN 10000 N-m²',
                                                                                                                                 status='ingebruik',
                                                                                                                                 definitie='Buizen van gevuld en glasvezelversterkt polyesterhars voor leidingen onder druk, PN 6, SN 10000 N/m²',
                                                                                                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPersleidingMateriaal/buizen-van-gevuld-en-glasvezelversterkt-polyesterhars-voor-leidingen-onder-druk.-PN-6.-SN-10000-N-m²'),
        'buizen-van-gevuld-en-glasvezelversterkt-polyesterhars-voor-leidingen-onder-druk.-PN-6.-SN-5000-N-m²': KeuzelijstWaarde(invulwaarde='buizen-van-gevuld-en-glasvezelversterkt-polyesterhars-voor-leidingen-onder-druk.-PN-6.-SN-5000-N-m²',
                                                                                                                                label='buizen van gevuld en glasvezelversterkt polyesterhars voor leidingen onder druk. PN 6. SN 5000 N-m²',
                                                                                                                                status='ingebruik',
                                                                                                                                definitie='Buizen van gevuld en glasvezelversterkt polyesterhars voor leidingen onder druk, PN 6, SN 5000 N/m²',
                                                                                                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPersleidingMateriaal/buizen-van-gevuld-en-glasvezelversterkt-polyesterhars-voor-leidingen-onder-druk.-PN-6.-SN-5000-N-m²'),
        'buizen-van-nodulair-gietijzer-voor-drukleidingen': KeuzelijstWaarde(invulwaarde='buizen-van-nodulair-gietijzer-voor-drukleidingen',
                                                                             label='buizen van nodulair gietijzer voor drukleidingen',
                                                                             status='ingebruik',
                                                                             definitie='Buizen van nodulair gietijzer voor drukleidingen',
                                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPersleidingMateriaal/buizen-van-nodulair-gietijzer-voor-drukleidingen'),
        'buizen-voor-polyethyleen-voor-drukleidingen.-PN-10': KeuzelijstWaarde(invulwaarde='buizen-voor-polyethyleen-voor-drukleidingen.-PN-10',
                                                                               label='buizen voor polyethyleen voor drukleidingen. PN 10',
                                                                               status='ingebruik',
                                                                               definitie='Buizen voor polyethyleen voor drukleidingen, PN 10',
                                                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPersleidingMateriaal/buizen-voor-polyethyleen-voor-drukleidingen.-PN-10'),
        'buizen-voor-polyethyleen-voor-drukleidingen.-PN-16': KeuzelijstWaarde(invulwaarde='buizen-voor-polyethyleen-voor-drukleidingen.-PN-16',
                                                                               label='buizen voor polyethyleen voor drukleidingen. PN 16',
                                                                               status='ingebruik',
                                                                               definitie='Buizen voor polyethyleen voor drukleidingen, PN 16',
                                                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPersleidingMateriaal/buizen-voor-polyethyleen-voor-drukleidingen.-PN-16'),
        'buizen-voor-polyethyleen-voor-drukleidingen.-PN-6': KeuzelijstWaarde(invulwaarde='buizen-voor-polyethyleen-voor-drukleidingen.-PN-6',
                                                                              label='buizen voor polyethyleen voor drukleidingen. PN 6',
                                                                              status='ingebruik',
                                                                              definitie='Buizen voor polyethyleen voor drukleidingen, PN 6',
                                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPersleidingMateriaal/buizen-voor-polyethyleen-voor-drukleidingen.-PN-6')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

