# coding=utf-8
from datetime import date
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.Proef import Proef
from otlmow_model.BaseClasses.DateField import DateField
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KwantWrdInJaar import KwantWrdInJaar, KwantWrdInJaarWaarden
from otlmow_model.GeometrieTypes.GeenGeometrie import GeenGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Keuring(Proef, GeenGeometrie):
    """Technische keuring uitgevoerd door een officiële keuringsinstantie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#Keuring'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        GeenGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')

        self._datum = OTLAttribuut(field=DateField,
                                   naam='datum',
                                   label='keuringsdatum',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#Keuring.datum',
                                   definition='De datum waarop de keuring werd uitgevoerd.',
                                   owner=self)

        self._geldigheidsDuur = OTLAttribuut(field=KwantWrdInJaar,
                                             naam='geldigheidsDuur',
                                             label='geldigheidsduur',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#Keuring.geldigheidsDuur',
                                             definition='de periode (in jaar) waarbinnen de keuring geldig blijft. ',
                                             owner=self)

        self._verslag = OTLAttribuut(field=DtcDocument,
                                     naam='verslag',
                                     label='keuringsverslag',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#Keuring.verslag',
                                     definition='document met het verslag van de keuring.',
                                     owner=self)

    @property
    def datum(self) -> date:
        """De datum waarop de keuring werd uitgevoerd."""
        return self._datum.get_waarde()

    @datum.setter
    def datum(self, value):
        self._datum.set_waarde(value, owner=self)

    @property
    def geldigheidsDuur(self) -> KwantWrdInJaarWaarden:
        """de periode (in jaar) waarbinnen de keuring geldig blijft. """
        return self._geldigheidsDuur.get_waarde()

    @geldigheidsDuur.setter
    def geldigheidsDuur(self, value):
        self._geldigheidsDuur.set_waarde(value, owner=self)

    @property
    def verslag(self) -> DtcDocumentWaarden:
        """document met het verslag van de keuring."""
        return self._verslag.get_waarde()

    @verslag.setter
    def verslag(self, value):
        self._verslag.set_waarde(value, owner=self)
