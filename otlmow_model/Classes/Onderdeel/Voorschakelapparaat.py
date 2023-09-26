# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.Datatypes.KlVoorschakelapparaatType import KlVoorschakelapparaatType
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Voorschakelapparaat(AIMObject, PuntGeometrie):
    """Het voorschakelapparaat van een ontladingslamp in ruime zin omvat alle componenten die in serie of in parallel met de lamp geschakeld worden om haar goede werking te verzekeren. Ze bestaat in 2 uitvoeringsvormen elektromagnetische en elektronische. Voor de elektromagnetische bestaat deze uit *de ballast: een elektromagnetische eenheid, die d.m.v. passieve componenten zoals een spoel of een condensator en/of actieve componenten, hoofdzakelijk dient om de lampstroom te beperken tot de vereiste waarde; *een starter of een ontsteker: levert de vereiste ontsteekspanning; *een condensator:is een component die de faseverschuiving tussen de stroom en spanning tot een aanvaardbare waarde terugbrengt en op die manier de arbeidsfactor verbetert; *de eventuele externe beveiligingen; *de onderlinge bekabeling."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voorschakelapparaat'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelNaHP')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Armatuurcontroller')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Montagekast', deprecated='2.4.0')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', deprecated='2.4.0')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelNaHP')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVOpvoertransformator')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVOpvoertransformator')

        self._type = OTLAttribuut(field=KlVoorschakelapparaatType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voorschakelapparaat.type',
                                  definition='Type van het voorschakelapparaat.',
                                  owner=self)

    @property
    def type(self) -> str:
        """Type van het voorschakelapparaat."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
