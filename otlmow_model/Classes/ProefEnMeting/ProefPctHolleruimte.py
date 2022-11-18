# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.Proef import Proef
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefPctHolleruimte(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Proef om het percentage holle ruimte in een bitumineuze laag te bepalen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefPctHolleruimte'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw')

        self._pctHolleruimte = OTLAttribuut(field=DtcDocument,
                                            naam='pctHolleruimte',
                                            label='pct holleruimte',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefPctHolleruimte.pctHolleruimte',
                                            definition='Het resultaat van het aantal percentage holleruimte meting aanwezig in de laag.',
                                            owner=self)

    @property
    def pctHolleruimte(self) -> DtcDocumentWaarden:
        """Het resultaat van het aantal percentage holleruimte meting aanwezig in de laag."""
        return self._pctHolleruimte.get_waarde()

    @pctHolleruimte.setter
    def pctHolleruimte(self, value):
        self._pctHolleruimte.set_waarde(value, owner=self)
