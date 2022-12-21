# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.LaagBouwklasse import LaagBouwklasse
from otlmow_model.Datatypes.DtuBVLaagtypes import DtuBVLaagtypes, DtuBVLaagtypesWaarden
from otlmow_model.Datatypes.KlBVBindmiddel import KlBVBindmiddel
from otlmow_model.Datatypes.KlBVMengseltype import KlBVMengseltype
from otlmow_model.Datatypes.KlKleurSupp import KlKleurSupp


# Generated with OTLClassCreator. To modify: extend, do not edit
class BitumineuzeLaag(LaagBouwklasse):
    """Flexibele verharding die meestal uit bitumineus gebonden materialen (asfalt of gietasfalt) bestaat en laagsgewijs wordt aangelegd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Divergentiepuntbebakeningselement')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegdekvoeg')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegreflector')

        self._bindmiddelType = OTLAttribuut(field=KlBVBindmiddel,
                                            naam='bindmiddelType',
                                            label='bindmiddel type',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag.bindmiddelType',
                                            definition='Het bindmiddeltype van de bitumineuze laag.',
                                            owner=self)

        self._kleur = OTLAttribuut(field=KlKleurSupp,
                                   naam='kleur',
                                   label='kleur',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag.kleur',
                                   definition='De kleur van de bitumineuze laag.',
                                   owner=self)

        self._laagtype = OTLAttribuut(field=DtuBVLaagtypes,
                                      naam='laagtype',
                                      label='laagtype',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag.laagtype',
                                      definition='Het type van bitumineuze laag.',
                                      owner=self)

        self._mengseltype = OTLAttribuut(field=KlBVMengseltype,
                                         naam='mengseltype',
                                         label='mengseltype',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag.mengseltype',
                                         definition='Het type van het (giet)asfaltmengsel.',
                                         owner=self)

    @property
    def bindmiddelType(self) -> str:
        """Het bindmiddeltype van de bitumineuze laag."""
        return self._bindmiddelType.get_waarde()

    @bindmiddelType.setter
    def bindmiddelType(self, value):
        self._bindmiddelType.set_waarde(value, owner=self)

    @property
    def kleur(self) -> str:
        """De kleur van de bitumineuze laag."""
        return self._kleur.get_waarde()

    @kleur.setter
    def kleur(self, value):
        self._kleur.set_waarde(value, owner=self)

    @property
    def laagtype(self) -> DtuBVLaagtypesWaarden:
        """Het type van bitumineuze laag."""
        return self._laagtype.get_waarde()

    @laagtype.setter
    def laagtype(self, value):
        self._laagtype.set_waarde(value, owner=self)

    @property
    def mengseltype(self) -> str:
        """Het type van het (giet)asfaltmengsel."""
        return self._mengseltype.get_waarde()

    @mengseltype.setter
    def mengseltype(self, value):
        self._mengseltype.set_waarde(value, owner=self)
