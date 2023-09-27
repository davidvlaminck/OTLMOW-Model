# coding=utf-8
from typing import List
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.Proef import Proef
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefNaderOnderzoekTomograaf(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Een geluids- en/of elektrische weerstandstomografie is een niet-destructieve methode om rot en holtes in bomen op te sporen door gebruik van geluidsgolven en/of elektrische stroom."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefNaderOnderzoekTomograaf'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Boom')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpgaandeBoom', deprecated='2.0.0')

        self._inclusiefElektrisch = OTLAttribuut(field=BooleanField,
                                                 naam='inclusiefElektrisch',
                                                 label='inclusief elektrisch',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefNaderOnderzoekTomograaf.inclusiefElektrisch',
                                                 definition='Aanduiding of naast een geluidsweerstandstomografie ook een elektrische weerstandstomografie gebeurd is.',
                                                 owner=self)

        self._naderOnderzoekTomograaf = OTLAttribuut(field=DtcDocument,
                                                     naam='naderOnderzoekTomograaf',
                                                     label='nader onderzoek tomograaf',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefNaderOnderzoekTomograaf.naderOnderzoekTomograaf',
                                                     kardinaliteit_max='*',
                                                     definition='Het resultaat van de tomograaf proef.',
                                                     owner=self)

    @property
    def inclusiefElektrisch(self) -> bool:
        """Aanduiding of naast een geluidsweerstandstomografie ook een elektrische weerstandstomografie gebeurd is."""
        return self._inclusiefElektrisch.get_waarde()

    @inclusiefElektrisch.setter
    def inclusiefElektrisch(self, value):
        self._inclusiefElektrisch.set_waarde(value, owner=self)

    @property
    def naderOnderzoekTomograaf(self) -> List[DtcDocumentWaarden]:
        """Het resultaat van de tomograaf proef."""
        return self._naderOnderzoekTomograaf.get_waarde()

    @naderOnderzoekTomograaf.setter
    def naderOnderzoekTomograaf(self, value):
        self._naderOnderzoekTomograaf.set_waarde(value, owner=self)
