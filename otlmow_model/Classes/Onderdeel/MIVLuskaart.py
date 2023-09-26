# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KlMIVLuskaartType import KlMIVLuskaartType
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class MIVLuskaart(AIMNaamObject, PuntGeometrie):
    """Meten in Vlaanderen : kaart in LVE- of SAT- rack met de analoge circuits voor de lussen en analoog/digitaal conversie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVLuskaart'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVInstallatie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SoftwareToegang')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LoopTerminationAndProtection')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVCommunicatiekaart')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort')

        self._lussenMeetrapport = OTLAttribuut(field=DtcDocument,
                                               naam='lussenMeetrapport',
                                               label='lussen meetrapport',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVLuskaart.lussenMeetrapport',
                                               usagenote='Bestanden van het type pdf.',
                                               definition='De elektrische eigenschappen van de lus: R, L, C en de isolatieweerstand. Dit verzekert naast de afmetingen mee de voorziene nauwkeurigheid van de voertuigmetingen.',
                                               owner=self)

        self._type = OTLAttribuut(field=KlMIVLuskaartType,
                                  naam='type',
                                  label='type MIV luskaart',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVLuskaart.type',
                                  definition='De uitvoering van de luskaart volgens een vaste lijst van mogelijke types.',
                                  owner=self)

    @property
    def lussenMeetrapport(self) -> DtcDocumentWaarden:
        """De elektrische eigenschappen van de lus: R, L, C en de isolatieweerstand. Dit verzekert naast de afmetingen mee de voorziene nauwkeurigheid van de voertuigmetingen."""
        return self._lussenMeetrapport.get_waarde()

    @lussenMeetrapport.setter
    def lussenMeetrapport(self, value):
        self._lussenMeetrapport.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """De uitvoering van de luskaart volgens een vaste lijst van mogelijke types."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
