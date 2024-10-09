# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Leiding import Leiding
from ...Classes.Abstracten.OmhullendeInrichting import OmhullendeInrichting
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DteTekstblok import DteTekstblok, DteTekstblokWaarden
from ...Datatypes.KlBeschermbuisKleur import KlBeschermbuisKleur
from ...Datatypes.KlBeschermbuisMateriaal import KlBeschermbuisMateriaal
from ...Datatypes.KlKabelLeidingBescherming import KlKabelLeidingBescherming
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Beschermbuis(Leiding, OmhullendeInrichting):
    """Een buis bestemd voor de doorvoer van kabels en/of leidingen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Beschermbuis'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Beschermbuis', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulpstuk', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftAanvullendeGeometrie', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderdoorboring', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftNetwerktoegang', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KabelnetBuis', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#OmhullendeInrichting', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', direction='o')  # o = direction: outgoing

        self._indicatieveDiepte = OTLAttribuut(field=KwantWrdInMeter,
                                               naam='indicatieveDiepte',
                                               label='indicatieve diepte',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Beschermbuis.indicatieveDiepte',
                                               usagenote='Meet de kleinste afstand tussen de buis en het maaiveld bij aanleg aangezien bij graafwerken dit de eerste diepte zal zijn waarop een buis kan aangetroffen worden. De diepte moet opgemeten worden, niet ingeschat: "indicatief" wijst op de tijdelijkheid van de waarde, niet op een waarde die bij benadering gegeven wordt. Bij een discrepantie tussen de waarde van dit attribuut en de waarde in TAW uit de geometrie van het object, geldt altijd de waarde in TAW.',
                                               definition='De opgemeten diepte als een (positief) getal in meter tussen het hoogste punt van de buis en het maaiveld zoals dit gekend was op het moment van aanleg van de buis.',
                                               owner=self)

        self._isFlexibel = OTLAttribuut(field=BooleanField,
                                        naam='isFlexibel',
                                        label='is flexibel',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Beschermbuis.isFlexibel',
                                        definition='Geeft aan of de beschermbuis flexibel is. Zo niet, dan spreken we van een vaste buis.',
                                        owner=self)

        self._kleur = OTLAttribuut(field=KlBeschermbuisKleur,
                                   naam='kleur',
                                   label='kleur',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Beschermbuis.kleur',
                                   definition='De kleur van de buitenkant van de beschermbuis.',
                                   owner=self)

        self._materiaal = OTLAttribuut(field=KlBeschermbuisMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Beschermbuis.materiaal',
                                       definition='Typering van de beschermbuis volgens het materiaal waaruit ze (hoofdzakelijk) gemaakt is.',
                                       owner=self)

        self._typeBescherming = OTLAttribuut(field=KlKabelLeidingBescherming,
                                             naam='typeBescherming',
                                             label='type bescherming',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Beschermbuis.typeBescherming',
                                             kardinaliteit_max='*',
                                             definition='Geeft aan of en hoe de leiding bijkomend mechanisch beschermd nadat ze in de sleuf gelegd is.',
                                             owner=self)

        self._voorzorgsmaatregel = OTLAttribuut(field=DteTekstblok,
                                                naam='voorzorgsmaatregel',
                                                label='voorzorgsmaatregel',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Beschermbuis.voorzorgsmaatregel',
                                                definition='Omschrijving van bijzondere omstandigheden waarmee rekening moet gehouden bv. bij werken in de buurt van de asset.',
                                                owner=self)

    @property
    def indicatieveDiepte(self) -> KwantWrdInMeterWaarden:
        """De opgemeten diepte als een (positief) getal in meter tussen het hoogste punt van de buis en het maaiveld zoals dit gekend was op het moment van aanleg van de buis."""
        return self._indicatieveDiepte.get_waarde()

    @indicatieveDiepte.setter
    def indicatieveDiepte(self, value):
        self._indicatieveDiepte.set_waarde(value, owner=self)

    @property
    def isFlexibel(self) -> bool:
        """Geeft aan of de beschermbuis flexibel is. Zo niet, dan spreken we van een vaste buis."""
        return self._isFlexibel.get_waarde()

    @isFlexibel.setter
    def isFlexibel(self, value):
        self._isFlexibel.set_waarde(value, owner=self)

    @property
    def kleur(self) -> str:
        """De kleur van de buitenkant van de beschermbuis."""
        return self._kleur.get_waarde()

    @kleur.setter
    def kleur(self, value):
        self._kleur.set_waarde(value, owner=self)

    @property
    def materiaal(self) -> str:
        """Typering van de beschermbuis volgens het materiaal waaruit ze (hoofdzakelijk) gemaakt is."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def typeBescherming(self) -> List[str]:
        """Geeft aan of en hoe de leiding bijkomend mechanisch beschermd nadat ze in de sleuf gelegd is."""
        return self._typeBescherming.get_waarde()

    @typeBescherming.setter
    def typeBescherming(self, value):
        self._typeBescherming.set_waarde(value, owner=self)

    @property
    def voorzorgsmaatregel(self) -> DteTekstblokWaarden:
        """Omschrijving van bijzondere omstandigheden waarmee rekening moet gehouden bv. bij werken in de buurt van de asset."""
        return self._voorzorgsmaatregel.get_waarde()

    @voorzorgsmaatregel.setter
    def voorzorgsmaatregel(self, value):
        self._voorzorgsmaatregel.set_waarde(value, owner=self)
