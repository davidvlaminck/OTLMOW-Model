# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Kabel import Kabel
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlKabeldikte import KlKabeldikte
from ...Datatypes.KwantWrdInMegahertz import KwantWrdInMegahertz, KwantWrdInMegahertzWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class StralendeKabel(Kabel, NaampadObject):
    """Een stralende kabel zendt radiogolven uit waardoor het radiosignaal kan worden opgepikt en draadloze communicatie mogelijk blijft. Het radiosignaal wordt opgepikt uit de lucht en in de afgesloten ruimte terug uitgezonden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StralendeKabel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#OmhullendeInrichting', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Datakabel', direction='u')  # u = unidirectional

        self._frequentiebereik = OTLAttribuut(field=KwantWrdInMegahertz,
                                              naam='frequentiebereik',
                                              label='frequentiebereik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StralendeKabel.frequentiebereik',
                                              definition='Het verschil tussen de laagste en hoogste frequentie waarop het signaal effectief werkt.  Dit bereik wordt uitgedrukt in megahertz (MHz).',
                                              owner=self)

        self._kabeldikte = OTLAttribuut(field=KlKabeldikte,
                                        naam='kabeldikte',
                                        label='kabeldikte',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StralendeKabel.kabeldikte',
                                        definition='De dikte van de kabel in duim.',
                                        owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StralendeKabel.technischeFiche',
                                             definition='De technische fiche als bijlage.',
                                             owner=self)

    @property
    def frequentiebereik(self) -> KwantWrdInMegahertzWaarden:
        """Het verschil tussen de laagste en hoogste frequentie waarop het signaal effectief werkt.  Dit bereik wordt uitgedrukt in megahertz (MHz)."""
        return self._frequentiebereik.get_waarde()

    @frequentiebereik.setter
    def frequentiebereik(self, value):
        self._frequentiebereik.set_waarde(value, owner=self)

    @property
    def kabeldikte(self) -> str:
        """De dikte van de kabel in duim."""
        return self._kabeldikte.get_waarde()

    @kabeldikte.setter
    def kabeldikte(self, value):
        self._kabeldikte.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche als bijlage."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
