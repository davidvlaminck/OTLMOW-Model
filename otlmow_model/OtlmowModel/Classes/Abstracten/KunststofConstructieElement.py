# coding=utf-8
from ...BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlProductieproces import KlProductieproces
from ...Datatypes.KlTypeHars import KlTypeHars
from ...Datatypes.KlTypeVezel import KlTypeVezel
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class KunststofConstructieElement(PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Bundeling van gemeenschappelijke eigenschappen van kunststof constructie-elementen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KunststofConstructieElement'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._productieProces = OTLAttribuut(field=KlProductieproces,
                                             naam='productieProces',
                                             label='productieproces',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KunststofConstructieElement.productieProces',
                                             definition='Het productieproces van het kunststof constructie element.',
                                             owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KunststofConstructieElement.technischeFiche',
                                             definition='De technische fiche van het kunststof constructie element. Specifieke eigenschappen, zoals thermische uitzetting, UV- bestendigheid, type kunststof, etc, zijn hierin opgenomen.',
                                             owner=self)

        self._typeHars = OTLAttribuut(field=KlTypeHars,
                                      naam='typeHars',
                                      label='type hars',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KunststofConstructieElement.typeHars',
                                      definition='Het type hars gebruikt in het kunststof constructie element.',
                                      owner=self)

        self._typeVezel = OTLAttribuut(field=KlTypeVezel,
                                       naam='typeVezel',
                                       label='type vezel',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KunststofConstructieElement.typeVezel',
                                       definition='Het type vezel gebruikt in het kunststof constructie element.',
                                       owner=self)

    @property
    def productieProces(self) -> str:
        """Het productieproces van het kunststof constructie element."""
        return self._productieProces.get_waarde()

    @productieProces.setter
    def productieProces(self, value):
        self._productieProces.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van het kunststof constructie element. Specifieke eigenschappen, zoals thermische uitzetting, UV- bestendigheid, type kunststof, etc, zijn hierin opgenomen."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def typeHars(self) -> str:
        """Het type hars gebruikt in het kunststof constructie element."""
        return self._typeHars.get_waarde()

    @typeHars.setter
    def typeHars(self, value):
        self._typeHars.set_waarde(value, owner=self)

    @property
    def typeVezel(self) -> str:
        """Het type vezel gebruikt in het kunststof constructie element."""
        return self._typeVezel.get_waarde()

    @typeVezel.setter
    def typeVezel(self, value):
        self._typeVezel.set_waarde(value, owner=self)
