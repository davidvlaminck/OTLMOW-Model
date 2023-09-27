# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.BevestigingGC import BevestigingGC
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.Datatypes.KlPictogramSymbool import KlPictogramSymbool
from otlmow_model.Datatypes.KwantWrdInMinuut import KwantWrdInMinuut, KwantWrdInMinuutWaarden
from otlmow_model.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Pictogram(BevestigingGC, AIMObject):
    """Een bord dat een symbool of afbeelding bevat dat de plaats inneemt van een tekst."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pictogram'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#StalenProfiel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeluidswerendeConstructie', deprecated='2.0.0')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulppostkast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PlintGC')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Vluchtdeur')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Hulppost')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Verkeersbordopstelling')

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
