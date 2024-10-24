# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.IpAdresObject import IpAdresObject
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlMIVEenheidType import KlMIVEenheidType


# Generated with OTLClassCreator. To modify: extend, do not edit
class MIVModule(IpAdresObject, NaampadObject):
    """Een verwerkingseenheid die instaat voor de verwerking van gegevens van lussen op een bepaalde locatie, hetzij als satelliet-eenheid hetzij als centrale eenheid voor de combinatie en doorsturen van verschillende eenheden. Het kan gaan om een alles-in-een toestel of om een opstelling met aparte componenten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVModule'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegkantkast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVMeetpunt', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVModule', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='i')  # i = direction: incoming

        self._lusConfig = OTLAttribuut(field=DtcDocument,
                                       naam='lusConfig',
                                       label='lus config',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVModule.lusConfig',
                                       usagenote='Bestanden van het type xlsx.',
                                       definition='Een definierende tabel die relatie legt tussen meetpuntnummer lusvolgorde nummer en de GPS locatie.',
                                       owner=self)

        self._technischeDocumentatie = OTLAttribuut(field=DtcDocument,
                                                    naam='technischeDocumentatie',
                                                    label='technische documentatie',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVModule.technischeDocumentatie',
                                                    usagenote='Bestanden van het type pdf.',
                                                    definition='Documentatie van de onderdelen: LVE / luskaart / communicatiekaart, configurator, ...',
                                                    owner=self)

        self._type = OTLAttribuut(field=KlMIVEenheidType,
                                  naam='type',
                                  label='type MIV installatie',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVModule.type',
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
