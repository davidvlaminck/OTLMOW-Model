# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlMeetcelNauwkeurigheidsklasse import KlMeetcelNauwkeurigheidsklasse
from ...Datatypes.KlMeetcelNauwkeurigheidsvermogen import KlMeetcelNauwkeurigheidsvermogen
from ...Datatypes.KlMeetcelVeiligheidsfactor import KlMeetcelVeiligheidsfactor
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Meetcel(AIMNaamObject, PuntGeometrie):
    """Een cel voorzien met uitrusting voor het meten van het energieverbruik aan de hoogspanningszijde van de transformator."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetcel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNBMeter', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoofdschakelaar', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator', direction='i')  # i = direction: incoming

        self._nauwkeurigheidsklasse = OTLAttribuut(field=KlMeetcelNauwkeurigheidsklasse,
                                                   naam='nauwkeurigheidsklasse',
                                                   label='nauwkeurigheidsklasse',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetcel.nauwkeurigheidsklasse',
                                                   definition='Nauwkeurigheidsklasse van de meetcel (vb 0,2; 0,2s; 0,5; ...).',
                                                   owner=self)

        self._nauwkeurigheidsvermogen = OTLAttribuut(field=KlMeetcelNauwkeurigheidsvermogen,
                                                     naam='nauwkeurigheidsvermogen',
                                                     label='nauwkeurigheidsvermogen',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetcel.nauwkeurigheidsvermogen',
                                                     definition='Nauwkeurigheidsvermogen van de meetcel (vb 5;15).',
                                                     owner=self)

        self._transformatieverhouding = OTLAttribuut(field=StringField,
                                                     naam='transformatieverhouding',
                                                     label='transformatieverhouding',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetcel.transformatieverhouding',
                                                     definition='Verhouding van de transformatie (vb 25/5;50/5; (5500/v3)/( 110/v3);...).',
                                                     owner=self)

        self._veiligheidsfactor = OTLAttribuut(field=KlMeetcelVeiligheidsfactor,
                                               naam='veiligheidsfactor',
                                               label='veiligheidsfactor',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetcel.veiligheidsfactor',
                                               definition='Verhouding tussen de toegekende primaire limietstroom van de meetcel en de toegekende primaire stroom.',
                                               owner=self)

    @property
    def nauwkeurigheidsklasse(self) -> str:
        """Nauwkeurigheidsklasse van de meetcel (vb 0,2; 0,2s; 0,5; ...)."""
        return self._nauwkeurigheidsklasse.get_waarde()

    @nauwkeurigheidsklasse.setter
    def nauwkeurigheidsklasse(self, value):
        self._nauwkeurigheidsklasse.set_waarde(value, owner=self)

    @property
    def nauwkeurigheidsvermogen(self) -> str:
        """Nauwkeurigheidsvermogen van de meetcel (vb 5;15)."""
        return self._nauwkeurigheidsvermogen.get_waarde()

    @nauwkeurigheidsvermogen.setter
    def nauwkeurigheidsvermogen(self, value):
        self._nauwkeurigheidsvermogen.set_waarde(value, owner=self)

    @property
    def transformatieverhouding(self) -> str:
        """Verhouding van de transformatie (vb 25/5;50/5; (5500/v3)/( 110/v3);...)."""
        return self._transformatieverhouding.get_waarde()

    @transformatieverhouding.setter
    def transformatieverhouding(self, value):
        self._transformatieverhouding.set_waarde(value, owner=self)

    @property
    def veiligheidsfactor(self) -> str:
        """Verhouding tussen de toegekende primaire limietstroom van de meetcel en de toegekende primaire stroom."""
        return self._veiligheidsfactor.get_waarde()

    @veiligheidsfactor.setter
    def veiligheidsfactor(self, value):
        self._veiligheidsfactor.set_waarde(value, owner=self)
