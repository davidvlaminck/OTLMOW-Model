# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.BevestigingGC import BevestigingGC
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KlPictogramSymbool import KlPictogramSymbool
from ...Datatypes.KwantWrdInMinuut import KwantWrdInMinuut, KwantWrdInMinuutWaarden
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Pictogram(BevestigingGC, AIMObject):
    """Een symbool dat of afbeelding die de plaats inneemt van een tekst."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pictogram'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Draagconstructie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Deur')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeluidswerendeConstructie', deprecated='2.0.0')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulppostkast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Montagekast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PlintGC')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Vluchtdeur', deprecated='2.9.0')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Hulppost')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Verkeersbordopstelling')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Vluchtdeurindicatie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Vluchtganginrichting')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Vluchtgeleiding')

        self._nalichtingstijd = OTLAttribuut(field=KwantWrdInMinuut,
                                             naam='nalichtingstijd',
                                             label='nalichtingstijd',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pictogram.nalichtingstijd',
                                             definition='De tijd dat het opgeslagen licht (bij bv. fosforen) in een andere lichtfrequentie (met minder energie) weer wordt uitgezonden.',
                                             owner=self)

        self._opschrift = OTLAttribuut(field=StringField,
                                       naam='opschrift',
                                       label='opschrift',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pictogram.opschrift',
                                       definition='Eventueel begeleidende tekst bij het symbool.',
                                       owner=self)

        self._symbool = OTLAttribuut(field=KlPictogramSymbool,
                                     naam='symbool',
                                     label='symbool',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pictogram.symbool',
                                     definition='Het symbool op het pictogram.',
                                     owner=self)

    @property
    def nalichtingstijd(self) -> KwantWrdInMinuutWaarden:
        """De tijd dat het opgeslagen licht (bij bv. fosforen) in een andere lichtfrequentie (met minder energie) weer wordt uitgezonden."""
        return self._nalichtingstijd.get_waarde()

    @nalichtingstijd.setter
    def nalichtingstijd(self, value):
        self._nalichtingstijd.set_waarde(value, owner=self)

    @property
    def opschrift(self) -> str:
        """Eventueel begeleidende tekst bij het symbool."""
        return self._opschrift.get_waarde()

    @opschrift.setter
    def opschrift(self, value):
        self._opschrift.set_waarde(value, owner=self)

    @property
    def symbool(self) -> str:
        """Het symbool op het pictogram."""
        return self._symbool.get_waarde()

    @symbool.setter
    def symbool(self, value):
        self._symbool.set_waarde(value, owner=self)
