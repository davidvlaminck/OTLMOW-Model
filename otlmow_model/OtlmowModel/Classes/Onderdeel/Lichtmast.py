# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.EMDraagconstructie import EMDraagconstructie
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcBeschermendeLaag import DtcBeschermendeLaag, DtcBeschermendeLaagWaarden
from ...Datatypes.DteKleurRAL import DteKleurRAL, DteKleurRALWaarden
from ...Datatypes.DtuLichtmastMasthoogte import DtuLichtmastMasthoogte, DtuLichtmastMasthoogteWaarden
from ...Datatypes.KlDraagConstrBeschermlaag import KlDraagConstrBeschermlaag
from ...Datatypes.KlDraagconstructieDwarsdoorsnede import KlDraagconstructieDwarsdoorsnede
from ...Datatypes.KlLichtmastBotsNormering import KlLichtmastBotsNormering
from ...Datatypes.KlLichtmastLeverancier import KlLichtmastLeverancier
from ...Datatypes.KlLichtmastMasttype import KlLichtmastMasttype
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Lichtmast(EMDraagconstructie, AIMNaamObject, PuntGeometrie):
    """Paal waarop een verlichtingstoestel of andere toestellen zoals een camera bevestigd kunnen worden met uitzondering van wegverlichting. Omvat het deurtje, klemmenblok, montagekastje, bevestigingsmaterialen (bv. voetplaten) en fundering (bv. buisfundering) of verankeringsmassief. Indien de paal gebruikt wordt voor wegverlichting moet het objecttype WVLichtmast gebruikt worden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeluidswerendeConstructie', direction='u', deprecated='2.0.0')  # u = unidirectional

        self._beschermendeLaag = OTLAttribuut(field=DtcBeschermendeLaag,
                                              naam='beschermendeLaag',
                                              label='beschermende laag',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.beschermendeLaag',
                                              definition='Het type van bescherming van de constructie of steun met de corresponderende corrosieklasse.',
                                              owner=self)

        self._beschermlaag = OTLAttribuut(field=KlDraagConstrBeschermlaag,
                                          naam='beschermlaag',
                                          label='beschermlaag',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.beschermlaag',
                                          usagenote='Attribuut uit gebruik sinds versie 2.12.0 ',
                                          deprecated_version='2.12.0',
                                          definition='Beschermlaag van de lichtmast.',
                                          owner=self)

        self._dwarsdoorsnede = OTLAttribuut(field=KlDraagconstructieDwarsdoorsnede,
                                            naam='dwarsdoorsnede',
                                            label='dwarsdoorsnede',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.dwarsdoorsnede',
                                            definition='De vorm van de dwarsdoorsnede van de lichtmast.',
                                            owner=self)

        self._heeftAntiVandalismeBeugel = OTLAttribuut(field=BooleanField,
                                                       naam='heeftAntiVandalismeBeugel',
                                                       label='heeft anti-vandalisme beugel',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.heeftAntiVandalismeBeugel',
                                                       definition='Aanduiding of een specifieke beugel is bevestigd aan de lichtmast om vandalisme en schade te voorkomen.',
                                                       owner=self)

        self._heeftStopcontact = OTLAttribuut(field=BooleanField,
                                              naam='heeftStopcontact',
                                              label='heeft stopcontact aanwezig',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.heeftStopcontact',
                                              definition='Geeft aan of er een stopcontact aanwezig is op de lichtmast.',
                                              owner=self)

        self._kleur = OTLAttribuut(field=DteKleurRAL,
                                   naam='kleur',
                                   label='kleur',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.kleur',
                                   definition='RAL kleur van de lichtmast.',
                                   owner=self)

        self._leverancier = OTLAttribuut(field=KlLichtmastLeverancier,
                                         naam='leverancier',
                                         label='leverancier',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.leverancier',
                                         definition='Leverancier van de lichtmast.',
                                         owner=self)

        self._masthoogte = OTLAttribuut(field=DtuLichtmastMasthoogte,
                                        naam='masthoogte',
                                        label='masthoogte',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.masthoogte',
                                        definition='Hoogte (in meter) van de lichtmast.',
                                        owner=self)

        self._masttype = OTLAttribuut(field=KlLichtmastMasttype,
                                      naam='masttype',
                                      label='masttype',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.masttype',
                                      definition='Type mast bv. rechte metalen paal, rechte metalen paal op voet, kreukelpaal met arm,...',
                                      owner=self)

        self._normeringBotsvriendelijk = OTLAttribuut(field=KlLichtmastBotsNormering,
                                                      naam='normeringBotsvriendelijk',
                                                      label='normering botsvriendelijk',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.normeringBotsvriendelijk',
                                                      definition='Categorie in normering botsvriendelijkheid.',
                                                      owner=self)

        self._specialeUitvoeringswijze = OTLAttribuut(field=StringField,
                                                      naam='specialeUitvoeringswijze',
                                                      label='speciale uitvoeringswijze',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.specialeUitvoeringswijze',
                                                      definition='Omschrijving van de speciale uitvoeringswijze van de lichtmast indien van toepassing.',
                                                      owner=self)

    @property
    def beschermendeLaag(self) -> DtcBeschermendeLaagWaarden:
        """Het type van bescherming van de constructie of steun met de corresponderende corrosieklasse."""
        return self._beschermendeLaag.get_waarde()

    @beschermendeLaag.setter
    def beschermendeLaag(self, value):
        self._beschermendeLaag.set_waarde(value, owner=self)

    @property
    def beschermlaag(self) -> str:
        """Beschermlaag van de lichtmast."""
        return self._beschermlaag.get_waarde()

    @beschermlaag.setter
    def beschermlaag(self, value):
        self._beschermlaag.set_waarde(value, owner=self)

    @property
    def dwarsdoorsnede(self) -> str:
        """De vorm van de dwarsdoorsnede van de lichtmast."""
        return self._dwarsdoorsnede.get_waarde()

    @dwarsdoorsnede.setter
    def dwarsdoorsnede(self, value):
        self._dwarsdoorsnede.set_waarde(value, owner=self)

    @property
    def heeftAntiVandalismeBeugel(self) -> bool:
        """Aanduiding of een specifieke beugel is bevestigd aan de lichtmast om vandalisme en schade te voorkomen."""
        return self._heeftAntiVandalismeBeugel.get_waarde()

    @heeftAntiVandalismeBeugel.setter
    def heeftAntiVandalismeBeugel(self, value):
        self._heeftAntiVandalismeBeugel.set_waarde(value, owner=self)

    @property
    def heeftStopcontact(self) -> bool:
        """Geeft aan of er een stopcontact aanwezig is op de lichtmast."""
        return self._heeftStopcontact.get_waarde()

    @heeftStopcontact.setter
    def heeftStopcontact(self, value):
        self._heeftStopcontact.set_waarde(value, owner=self)

    @property
    def kleur(self) -> DteKleurRALWaarden:
        """RAL kleur van de lichtmast."""
        return self._kleur.get_waarde()

    @kleur.setter
    def kleur(self, value):
        self._kleur.set_waarde(value, owner=self)

    @property
    def leverancier(self) -> str:
        """Leverancier van de lichtmast."""
        return self._leverancier.get_waarde()

    @leverancier.setter
    def leverancier(self, value):
        self._leverancier.set_waarde(value, owner=self)

    @property
    def masthoogte(self) -> DtuLichtmastMasthoogteWaarden:
        """Hoogte (in meter) van de lichtmast."""
        return self._masthoogte.get_waarde()

    @masthoogte.setter
    def masthoogte(self, value):
        self._masthoogte.set_waarde(value, owner=self)

    @property
    def masttype(self) -> str:
        """Type mast bv. rechte metalen paal, rechte metalen paal op voet, kreukelpaal met arm,..."""
        return self._masttype.get_waarde()

    @masttype.setter
    def masttype(self, value):
        self._masttype.set_waarde(value, owner=self)

    @property
    def normeringBotsvriendelijk(self) -> str:
        """Categorie in normering botsvriendelijkheid."""
        return self._normeringBotsvriendelijk.get_waarde()

    @normeringBotsvriendelijk.setter
    def normeringBotsvriendelijk(self, value):
        self._normeringBotsvriendelijk.set_waarde(value, owner=self)

    @property
    def specialeUitvoeringswijze(self) -> str:
        """Omschrijving van de speciale uitvoeringswijze van de lichtmast indien van toepassing."""
        return self._specialeUitvoeringswijze.get_waarde()

    @specialeUitvoeringswijze.setter
    def specialeUitvoeringswijze(self, value):
        self._specialeUitvoeringswijze.set_waarde(value, owner=self)
