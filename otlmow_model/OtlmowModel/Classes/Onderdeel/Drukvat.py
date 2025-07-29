# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KwantWrdInBar import KwantWrdInBar, KwantWrdInBarWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Drukvat(TechnischDocument, AIMNaamObject, PuntGeometrie):
    """Een afgesloten vat waarin een gas of vloeistof onder een andere druk dan de omgevingsdruk wordt opgeslagen. Het dient om de impact van een bewegend lichaam op te vangen en kan verbonden zijn met een buffercilinder. Dit wordt ook wel een buffervat genoemd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Drukvat'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bufferinstallatie', direction='o')  # o = direction: outgoing

        self._maximaleDruk = OTLAttribuut(field=KwantWrdInBar,
                                          naam='maximaleDruk',
                                          label='maximale druk',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Drukvat.maximaleDruk',
                                          definition='De hoogste druk die het drukvat kan weerstaan zonder te falen of beschadigd te raken. Dit wordt bepaald door het materiaal, de constructie en de toepassing van het drukvat. Het wordt vaak vastgesteld door middel van testen onder gecontroleerde omstandigheden, waarbij het drukvat geleidelijk aan toenemende druk wordt blootgesteld totdat deze faalt. De druk net voordat het drukvat faalt, wordt beschouwd als de maximale druk. In de praktijk wordt vaak een veiligheidsmarge toegepast.',
                                          owner=self)

    @property
    def maximaleDruk(self) -> KwantWrdInBarWaarden:
        """De hoogste druk die het drukvat kan weerstaan zonder te falen of beschadigd te raken. Dit wordt bepaald door het materiaal, de constructie en de toepassing van het drukvat. Het wordt vaak vastgesteld door middel van testen onder gecontroleerde omstandigheden, waarbij het drukvat geleidelijk aan toenemende druk wordt blootgesteld totdat deze faalt. De druk net voordat het drukvat faalt, wordt beschouwd als de maximale druk. In de praktijk wordt vaak een veiligheidsmarge toegepast."""
        return self._maximaleDruk.get_waarde()

    @maximaleDruk.setter
    def maximaleDruk(self, value):
        self._maximaleDruk.set_waarde(value, owner=self)
