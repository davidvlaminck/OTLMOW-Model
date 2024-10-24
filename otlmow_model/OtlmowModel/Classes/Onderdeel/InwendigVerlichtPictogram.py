# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcAfmetingBxlxhInMm import DtcAfmetingBxlxhInMm, DtcAfmetingBxlxhInMmWaarden
from ...Datatypes.KlBinnenverlichtingstoestelSoortLamp import KlBinnenverlichtingstoestelSoortLamp
from ...Datatypes.KlPictogramSymbool import KlPictogramSymbool
from ...Datatypes.KwantWrdInMinuut import KwantWrdInMinuut, KwantWrdInMinuutWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class InwendigVerlichtPictogram(AIMNaamObject, PuntGeometrie):
    """Verlichtingstoestel om de aandacht te vestigen op een pictogram dat erop bevestigd is."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#InwendigVerlichtPictogram'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Hulppost', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Vluchtdeurindicatie', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Vluchtganginrichting', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', direction='i')  # i = direction: incoming

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
