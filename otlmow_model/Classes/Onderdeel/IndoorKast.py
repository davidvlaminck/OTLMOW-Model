# coding=utf-8
from typing import List
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.Kast import Kast
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class IndoorKast(Kast):
    """Behuizing in de vorm van een kast voor gebruik in binnenruimtes."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IndoorKast'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Toegangselement')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegcomputer')

        self._mplan = OTLAttribuut(field=DtcDocument,
                                   naam='mplan',
                                   label='m-plan',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IndoorKast.mplan',
                                   usagenote='Bestanden van het type dwg of pdf.',
                                   kardinaliteit_max='*',
                                   definition='Mechanisch plan van de volledige installatie. Er wordt 1 plan toegevoegd per installatie/techniek die op de kast is aangesloten.',
                                   owner=self)

    @property
    def mplan(self) -> List[DtcDocumentWaarden]:
        """Mechanisch plan van de volledige installatie. Er wordt 1 plan toegevoegd per installatie/techniek die op de kast is aangesloten."""
        return self._mplan.get_waarde()

    @mplan.setter
    def mplan(self, value):
        self._mplan.set_waarde(value, owner=self)
