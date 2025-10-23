# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlLEGCOpeningType import KlLEGCOpeningType
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Doorgang(AIMObject, PuntGeometrie):
    """Doorgangen voorzien een vluchtmogelijkheid. Deze bezitten dezelfde akoestische kwaliteitseisen als de voorgestelde schermen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Doorgang'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.1.0'

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeluidswerendeConstructie', direction='u', deprecated='2.0.0')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GeluidwerendeConstructie', direction='o', deprecated='2.1.0')  # o = direction: outgoing

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Doorgang.technischeFiche',
                                             usagenote='Klasse uit gebruik sinds versie 2.1.0 ',
                                             deprecated_version='2.1.0',
                                             definition='Document waarin onder andere het inplantingsplan van de doorgang wordt weergegeven.',
                                             owner=self)

        self._type = OTLAttribuut(field=KlLEGCOpeningType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Doorgang.type',
                                  usagenote='Klasse uit gebruik sinds versie 2.1.0 ',
                                  deprecated_version='2.1.0',
                                  definition='Bepaling van het type van doorgang (sas, nooddeur) (voorlopig opgenomen in figuur 8-4-1).',
                                  owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """Document waarin onder andere het inplantingsplan van de doorgang wordt weergegeven."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Bepaling van het type van doorgang (sas, nooddeur) (voorlopig opgenomen in figuur 8-4-1)."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
