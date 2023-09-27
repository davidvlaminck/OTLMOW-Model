# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.NaampadObject import NaampadObject
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KlMIVEenheidType import KlMIVEenheidType
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class MIVInstallatie(NaampadObject, VlakGeometrie):
    """De volledige opstelling voor meten in Vlaanderen op een bepaalde locatie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVInstallatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVCommunicatiekaart')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVVoedingsmodule')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVInstallatie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVVoedingsmodule')

        self._lusConfig = OTLAttribuut(field=DtcDocument,
                                       naam='lusConfig',
                                       label='lus config',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVInstallatie.lusConfig',
                                       usagenote='Bestanden van het type xlsx.',
                                       definition='Een definierende tabel die relatie legt tussen meetpuntnummer lusvolgorde nummer en de GPS locatie.',
                                       owner=self)

        self._technischeDocumentatie = OTLAttribuut(field=DtcDocument,
                                                    naam='technischeDocumentatie',
                                                    label='technische documentatie',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVInstallatie.technischeDocumentatie',
                                                    usagenote='Bestanden van het type pdf.',
                                                    definition='Documentatie van de onderdelen: LVE / luskaart / communicatiekaart, configurator, ...',
                                                    owner=self)

        self._type = OTLAttribuut(field=KlMIVEenheidType,
                                  naam='type',
                                  label='type MIV installatie',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVInstallatie.type',
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
