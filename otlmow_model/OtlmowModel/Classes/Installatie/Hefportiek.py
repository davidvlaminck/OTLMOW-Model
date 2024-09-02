# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.ConstructiefObject import ConstructiefObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlToegankelijkheid import KlToegankelijkheid
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Hefportiek(ConstructiefObject, VlakGeometrie):
    """Een hefportiek is een vrijstaand, stijf hoofdconstructieonderdeel. Het bestaat uit minstens twee steunbenen die onderling verbonden zijn en rusten op de onderbouw. Deze steunbenen staan (mede) in voor het verticale steunen en begeleiden van een beweegbaar constructieonderdeel wanneer dit niet rust op zijn vaste steunpunten. Het tilt meestal een brugdeel of beweegbare waterkerende constructie op. Meestal herbergt een hefportiek een mechaniek met ook een tegengewicht en steekt het samen met een tweede, gelijkaardig exemplaar aan de overzijde, hoog boven de rest van het kunstwerk uit.
"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Hefportiek'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#NietWeggebondenDetectie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Trekker')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#BeweegbareWaterkerendeConstructie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Landhoofd')

        self._isGevuldMetTegengewicht = OTLAttribuut(field=BooleanField,
                                                     naam='isGevuldMetTegengewicht',
                                                     label='is gevuld met tegengewicht',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Hefportiek.isGevuldMetTegengewicht',
                                                     definition='Aanduiding of het hefportiek al dan niet gevuld is met een tegengewicht.',
                                                     owner=self)

        self._toegankelijkheid = OTLAttribuut(field=KlToegankelijkheid,
                                              naam='toegankelijkheid',
                                              label='toegankelijkheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Hefportiek.toegankelijkheid',
                                              definition='Duidt de toegankelijkheid van het hefportiek aan.',
                                              owner=self)

    @property
    def isGevuldMetTegengewicht(self) -> bool:
        """Aanduiding of het hefportiek al dan niet gevuld is met een tegengewicht."""
        return self._isGevuldMetTegengewicht.get_waarde()

    @isGevuldMetTegengewicht.setter
    def isGevuldMetTegengewicht(self, value):
        self._isGevuldMetTegengewicht.set_waarde(value, owner=self)

    @property
    def toegankelijkheid(self) -> str:
        """Duidt de toegankelijkheid van het hefportiek aan."""
        return self._toegankelijkheid.get_waarde()

    @toegankelijkheid.setter
    def toegankelijkheid(self, value):
        self._toegankelijkheid.set_waarde(value, owner=self)
