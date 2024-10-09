# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlMIVEenheidType import KlMIVEenheidType
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class MIVInstallatie(NaampadObject, VlakGeometrie):
    """Een MIV eenheid die instaat voor de verwerking van gegevens van lussen op een bepaalde locatie, hetzij als satelliet-eenheid hetzij als centrale eenheid voor de combinatie van verschillende eenheden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVInstallatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.9.0'

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVCommunicatiekaart', direction='u', deprecated='2.9.0')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVVoedingsmodule', direction='u', deprecated='2.9.0')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVInstallatie', direction='o', deprecated='2.9.0')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVMeetpunt', direction='i', deprecated='2.9.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVCommunicatiekaart', direction='i', deprecated='2.9.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVLuskaart', direction='i', deprecated='2.9.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVProcessorkaart', direction='i', deprecated='2.9.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVVoedingsmodule', direction='i', deprecated='2.9.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVVoedingsmodule', direction='o', deprecated='2.9.0')  # o = direction: outgoing

        self._lusConfig = OTLAttribuut(field=DtcDocument,
                                       naam='lusConfig',
                                       label='lus config',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVInstallatie.lusConfig',
                                       usagenote='Klasse uit gebruik sinds versie 2.9.0 ',
                                       deprecated_version='2.9.0',
                                       definition='Een definierende tabel die relatie legt tussen meetpuntnummer lusvolgorde nummer en de GPS locatie.',
                                       owner=self)

        self._technischeDocumentatie = OTLAttribuut(field=DtcDocument,
                                                    naam='technischeDocumentatie',
                                                    label='technische documentatie',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVInstallatie.technischeDocumentatie',
                                                    usagenote='Klasse uit gebruik sinds versie 2.9.0 ',
                                                    deprecated_version='2.9.0',
                                                    definition='Documentatie van de onderdelen: LVE / luskaart / communicatiekaart, configurator, ...',
                                                    owner=self)

        self._type = OTLAttribuut(field=KlMIVEenheidType,
                                  naam='type',
                                  label='type MIV installatie',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVInstallatie.type',
                                  usagenote='Klasse uit gebruik sinds versie 2.9.0 ',
                                  deprecated_version='2.9.0',
                                  definition='Het type volgens de gebruikte technologie en inzet in een groter geheel.',
                                  owner=self)

    @property
    def lusConfig(self) -> DtcDocumentWaarden:
        """Een definierende tabel die relatie legt tussen meetpuntnummer lusvolgorde nummer en de GPS locatie."""
        return self._lusConfig.get_waarde()

    @lusConfig.setter
    def lusConfig(self, value):
        self._lusConfig.set_waarde(value, owner=self)

    @property
    def technischeDocumentatie(self) -> DtcDocumentWaarden:
        """Documentatie van de onderdelen: LVE / luskaart / communicatiekaart, configurator, ..."""
        return self._technischeDocumentatie.get_waarde()

    @technischeDocumentatie.setter
    def technischeDocumentatie(self, value):
        self._technischeDocumentatie.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Het type volgens de gebruikte technologie en inzet in een groter geheel."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
