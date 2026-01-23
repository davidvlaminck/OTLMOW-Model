# coding=utf-8
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcAfdichtingKabelleidingdoorvoer import DtcAfdichtingKabelleidingdoorvoer, DtcAfdichtingKabelleidingdoorvoerWaarden
from ...Datatypes.KlOrientatieKabelleidingdoorvoer import KlOrientatieKabelleidingdoorvoer
from ...Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter, KwantWrdInVierkanteMeterWaarden
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kabelleidingdoorvoer(AIMNaamObject, PuntGeometrie):
    """Een doorvoeropening om kabels en leidingen door een muur of ander bouwelement te leiden en te ondersteunen, opgevuld met een afdichtingsmateriaal dat zorgt voor afdichting, isolatie en brandwerendheid."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelleidingdoorvoer'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HorizontaleConstructieplaat', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wand', direction='u')  # u = unidirectional

        self._afdichting = OTLAttribuut(field=DtcAfdichtingKabelleidingdoorvoer,
                                        naam='afdichting',
                                        label='afdichting',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelleidingdoorvoer.afdichting',
                                        definition='De afdichting bevat informatie over enerzijds het afdichtingsmateriaal dat wordt gebruikt om de ruimte rond de doorgevoerde kabels en/of leidingen en het omliggende bouwmateriaal waterdicht af te sluiten, en anderzijds de functionaliteitsvereisten (bv: brandwering, vochtbestendigheid,..).',
                                        owner=self)

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelleidingdoorvoer.oppervlakte',
                                         definition='De oppervlakte (in m2) van de opening die in een constructie voorzien is om kabels en leidingen door te voeren.',
                                         owner=self)

        self._orientatie = OTLAttribuut(field=KlOrientatieKabelleidingdoorvoer,
                                        naam='orientatie',
                                        label='oriëntatie',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelleidingdoorvoer.orientatie',
                                        definition='De oriëntatie van de kabelleidingdoorvoer verwijst naar de richting of positie waarin de doorvoer voor kabels en leidingen is geplaatst.',
                                        owner=self)

    @property
    def afdichting(self) -> DtcAfdichtingKabelleidingdoorvoerWaarden:
        """De afdichting bevat informatie over enerzijds het afdichtingsmateriaal dat wordt gebruikt om de ruimte rond de doorgevoerde kabels en/of leidingen en het omliggende bouwmateriaal waterdicht af te sluiten, en anderzijds de functionaliteitsvereisten (bv: brandwering, vochtbestendigheid,..)."""
        return self._afdichting.get_waarde()

    @afdichting.setter
    def afdichting(self, value):
        self._afdichting.set_waarde(value, owner=self)

    @property
    def oppervlakte(self) -> KwantWrdInVierkanteMeterWaarden:
        """De oppervlakte (in m2) van de opening die in een constructie voorzien is om kabels en leidingen door te voeren."""
        return self._oppervlakte.get_waarde()

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)

    @property
    def orientatie(self) -> str:
        """De oriëntatie van de kabelleidingdoorvoer verwijst naar de richting of positie waarin de doorvoer voor kabels en leidingen is geplaatst."""
        return self._orientatie.get_waarde()

    @orientatie.setter
    def orientatie(self, value):
        self._orientatie.set_waarde(value, owner=self)
