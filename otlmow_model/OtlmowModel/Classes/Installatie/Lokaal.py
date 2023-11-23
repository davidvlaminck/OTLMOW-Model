# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Behuizing import Behuizing
from ...Classes.Abstracten.Kokerruimte import Kokerruimte
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Lokaal(Behuizing, Kokerruimte):
    """Een ruimte binnen een gebouw."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Lokaal'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Toegangselement')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandblusser')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aswegersite')

        self._grondplan = OTLAttribuut(field=DtcDocument,
                                       naam='grondplan',
                                       label='grondplan',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Lokaal.grondplan',
                                       definition='Plattegrond van het lokaal met aanduidingen van de verschillende aanwezige elementen zoals kasten met kastnummers, toegangscontrole en meer.',
                                       owner=self)

    @property
    def grondplan(self) -> DtcDocumentWaarden:
        """Plattegrond van het lokaal met aanduidingen van de verschillende aanwezige elementen zoals kasten met kastnummers, toegangscontrole en meer."""
        return self._grondplan.get_waarde()

    @grondplan.setter
    def grondplan(self, value):
        self._grondplan.set_waarde(value, owner=self)
