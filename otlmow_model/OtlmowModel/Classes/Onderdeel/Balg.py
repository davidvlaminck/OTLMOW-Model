# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlTypeVullingBalg import KlTypeVullingBalg
from ...Datatypes.KwantWrdInBar import KwantWrdInBar, KwantWrdInBarWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Balg(TechnischDocument, AIMNaamObject, PuntGeometrie):
    """Een flexibel, expansie- en contractie-element dat wordt gebruikt om de waterkerende constructie te laten bewegen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Balg'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Balgmechanisme', direction='o')  # o = direction: outgoing

        self._maximaleDruk = OTLAttribuut(field=KwantWrdInBar,
                                          naam='maximaleDruk',
                                          label='maximale druk',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Balg.maximaleDruk',
                                          definition='De hoogste druk die de balg kan weerstaan zonder te falen of beschadigd te raken. Dit wordt bepaald door het materiaal, de constructie en de toepassing van de balg. Het wordt vaak vastgesteld door middel van testen onder gecontroleerde omstandigheden, waarbij de balg geleidelijk aan toenemende druk wordt blootgesteld totdat deze faalt. De druk net voordat de balg faalt, wordt beschouwd als de maximale druk. In de praktijk wordt vaak een veiligheidsmarge toegepast',
                                          owner=self)

        self._typeVulling = OTLAttribuut(field=KlTypeVullingBalg,
                                         naam='typeVulling',
                                         label='type vulling',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Balg.typeVulling',
                                         definition='Het type vulling van de balg.',
                                         owner=self)

    @property
    def maximaleDruk(self) -> KwantWrdInBarWaarden:
        """De hoogste druk die de balg kan weerstaan zonder te falen of beschadigd te raken. Dit wordt bepaald door het materiaal, de constructie en de toepassing van de balg. Het wordt vaak vastgesteld door middel van testen onder gecontroleerde omstandigheden, waarbij de balg geleidelijk aan toenemende druk wordt blootgesteld totdat deze faalt. De druk net voordat de balg faalt, wordt beschouwd als de maximale druk. In de praktijk wordt vaak een veiligheidsmarge toegepast"""
        return self._maximaleDruk.get_waarde()

    @maximaleDruk.setter
    def maximaleDruk(self, value):
        self._maximaleDruk.set_waarde(value, owner=self)

    @property
    def typeVulling(self) -> str:
        """Het type vulling van de balg."""
        return self._typeVulling.get_waarde()

    @typeVulling.setter
    def typeVulling(self, value):
        self._typeVulling.set_waarde(value, owner=self)
