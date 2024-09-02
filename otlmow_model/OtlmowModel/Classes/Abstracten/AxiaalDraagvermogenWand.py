# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KwantWrdInKiloNewtonPerMeter import KwantWrdInKiloNewtonPerMeter, KwantWrdInKiloNewtonPerMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class AxiaalDraagvermogenWand(LijnGeometrie, VlakGeometrie):
    """Abstracte voor de bundeling van de axiale druk- en trekdraagvermogens van de totale wand,berekend volgens verschillende grenstoestanden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AxiaalDraagvermogenWand'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._drukdraagvermogenGGTWand = OTLAttribuut(field=KwantWrdInKiloNewtonPerMeter,
                                                      naam='drukdraagvermogenGGTWand',
                                                      label='drukdraagvermogen in gebruiksgrenstoestanden van de wand',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AxiaalDraagvermogenWand.drukdraagvermogenGGTWand',
                                                      definition='Karakteristieke waarde van de maximale druklast die de totale wand kan dragen in gebruiksgrenstoestanden (GGT), uitgedrukt in kilonewton per meter.',
                                                      owner=self)

        self._drukdraagvermogenUGTWand = OTLAttribuut(field=KwantWrdInKiloNewtonPerMeter,
                                                      naam='drukdraagvermogenUGTWand',
                                                      label='drukdraagvermogen in uiterste grenstoestand van de wand',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AxiaalDraagvermogenWand.drukdraagvermogenUGTWand',
                                                      definition='Drukdraagvermogen van de totale wand, uitgedrukt in kilonewton per meter, in uiterste grenstoestand (UGT) design approach DA1/1.',
                                                      owner=self)

        self._ontwerpnota = OTLAttribuut(field=DtcDocument,
                                         naam='ontwerpnota',
                                         label='ontwerpnota',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AxiaalDraagvermogenWand.ontwerpnota',
                                         definition='Nota dat de belangrijkste ontwerpbeslissingen, overwegingen, specificaties en andere relevante informatie documenteert die betrekking heeft op een specifiek ontwerpproject..',
                                         owner=self)

        self._trekdraagvermorgenGGTWand = OTLAttribuut(field=KwantWrdInKiloNewtonPerMeter,
                                                       naam='trekdraagvermorgenGGTWand',
                                                       label='trekdraagvermogen in gebruiksgrenstoestanden van de wand',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AxiaalDraagvermogenWand.trekdraagvermorgenGGTWand',
                                                       definition='Karakteristieke waarde van de maximale treklast die de totale wand kan dragen in gebruiksgrenstoestanden (GGT), uitgedrukt in kilonewton per meter.',
                                                       owner=self)

        self._trekdraagvermorgenUGTWand = OTLAttribuut(field=KwantWrdInKiloNewtonPerMeter,
                                                       naam='trekdraagvermorgenUGTWand',
                                                       label='trekdraagvermogen in uiterste grenstoestand van de wand',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AxiaalDraagvermogenWand.trekdraagvermorgenUGTWand',
                                                       definition='Trekdraagvermogen van de totale wand, uitgedrukt in kilonewton per meter, in uiterste grenstoestand (UGT) design approach DA1/1.',
                                                       owner=self)

    @property
    def drukdraagvermogenGGTWand(self) -> KwantWrdInKiloNewtonPerMeterWaarden:
        """Karakteristieke waarde van de maximale druklast die de totale wand kan dragen in gebruiksgrenstoestanden (GGT), uitgedrukt in kilonewton per meter."""
        return self._drukdraagvermogenGGTWand.get_waarde()

    @drukdraagvermogenGGTWand.setter
    def drukdraagvermogenGGTWand(self, value):
        self._drukdraagvermogenGGTWand.set_waarde(value, owner=self)

    @property
    def drukdraagvermogenUGTWand(self) -> KwantWrdInKiloNewtonPerMeterWaarden:
        """Drukdraagvermogen van de totale wand, uitgedrukt in kilonewton per meter, in uiterste grenstoestand (UGT) design approach DA1/1."""
        return self._drukdraagvermogenUGTWand.get_waarde()

    @drukdraagvermogenUGTWand.setter
    def drukdraagvermogenUGTWand(self, value):
        self._drukdraagvermogenUGTWand.set_waarde(value, owner=self)

    @property
    def ontwerpnota(self) -> DtcDocumentWaarden:
        """Nota dat de belangrijkste ontwerpbeslissingen, overwegingen, specificaties en andere relevante informatie documenteert die betrekking heeft op een specifiek ontwerpproject.."""
        return self._ontwerpnota.get_waarde()

    @ontwerpnota.setter
    def ontwerpnota(self, value):
        self._ontwerpnota.set_waarde(value, owner=self)

    @property
    def trekdraagvermorgenGGTWand(self) -> KwantWrdInKiloNewtonPerMeterWaarden:
        """Karakteristieke waarde van de maximale treklast die de totale wand kan dragen in gebruiksgrenstoestanden (GGT), uitgedrukt in kilonewton per meter."""
        return self._trekdraagvermorgenGGTWand.get_waarde()

    @trekdraagvermorgenGGTWand.setter
    def trekdraagvermorgenGGTWand(self, value):
        self._trekdraagvermorgenGGTWand.set_waarde(value, owner=self)

    @property
    def trekdraagvermorgenUGTWand(self) -> KwantWrdInKiloNewtonPerMeterWaarden:
        """Trekdraagvermogen van de totale wand, uitgedrukt in kilonewton per meter, in uiterste grenstoestand (UGT) design approach DA1/1."""
        return self._trekdraagvermorgenUGTWand.get_waarde()

    @trekdraagvermorgenUGTWand.setter
    def trekdraagvermorgenUGTWand(self, value):
        self._trekdraagvermorgenUGTWand.set_waarde(value, owner=self)
