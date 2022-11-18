# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.Datatypes.DtcAfmetingBxlxhInMm import DtcAfmetingBxlxhInMm, DtcAfmetingBxlxhInMmWaarden
from otlmow_model.Datatypes.KlBinnenverlichtingstoestelSoortLamp import KlBinnenverlichtingstoestelSoortLamp
from otlmow_model.Datatypes.KlPictogramSymbool import KlPictogramSymbool
from otlmow_model.Datatypes.KwantWrdInMinuut import KwantWrdInMinuut, KwantWrdInMinuutWaarden
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class InwendigVerlichtPictogram(AIMObject, PuntGeometrie):
    """Verlichtingstoestel om de aandacht te vestigen op een pictogram dat erop bevestigd is."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#InwendigVerlichtPictogram'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart')

        self._afmeting = OTLAttribuut(field=DtcAfmetingBxlxhInMm,
                                      naam='afmeting',
                                      label='afmeting',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#InwendigVerlichtPictogram.afmeting',
                                      definition='Geeft de buitenafmeting van het toestel mee.',
                                      owner=self)

        self._nalichtingstijd = OTLAttribuut(field=KwantWrdInMinuut,
                                             naam='nalichtingstijd',
                                             label='nalichtingstijd',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#InwendigVerlichtPictogram.nalichtingstijd',
                                             definition='De tijd tussen het uitschakelen van de interne lichtbron en het volledig duister worden van het toestel.',
                                             owner=self)

        self._symbool = OTLAttribuut(field=KlPictogramSymbool,
                                     naam='symbool',
                                     label='symbool',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#InwendigVerlichtPictogram.symbool',
                                     definition='Het symbool afgebeeld op het toestel.',
                                     owner=self)

        self._typeLamp = OTLAttribuut(field=KlBinnenverlichtingstoestelSoortLamp,
                                      naam='typeLamp',
                                      label='type lamp',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#InwendigVerlichtPictogram.typeLamp',
                                      definition='Het soort lamp waarmee het toestel verlicht wordt.',
                                      owner=self)

    @property
    def afmeting(self) -> DtcAfmetingBxlxhInMmWaarden:
        """Geeft de buitenafmeting van het toestel mee."""
        return self._afmeting.get_waarde()

    @afmeting.setter
    def afmeting(self, value):
        self._afmeting.set_waarde(value, owner=self)

    @property
    def nalichtingstijd(self) -> KwantWrdInMinuutWaarden:
        """De tijd tussen het uitschakelen van de interne lichtbron en het volledig duister worden van het toestel."""
        return self._nalichtingstijd.get_waarde()

    @nalichtingstijd.setter
    def nalichtingstijd(self, value):
        self._nalichtingstijd.set_waarde(value, owner=self)

    @property
    def symbool(self) -> str:
        """Het symbool afgebeeld op het toestel."""
        return self._symbool.get_waarde()

    @symbool.setter
    def symbool(self, value):
        self._symbool.set_waarde(value, owner=self)

    @property
    def typeLamp(self) -> str:
        """Het soort lamp waarmee het toestel verlicht wordt."""
        return self._typeLamp.get_waarde()

    @typeLamp.setter
    def typeLamp(self, value):
        self._typeLamp.set_waarde(value, owner=self)
