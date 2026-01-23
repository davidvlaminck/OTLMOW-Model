# coding=utf-8
from typing import List
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.ElektrischComponentennummerObject import ElektrischComponentennummerObject
from ...Classes.Abstracten.SerienummerObject import SerienummerObject
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlSpanningsomvormerMerk import KlSpanningsomvormerMerk
from ...Datatypes.KlSpanningsomvormerModelnaam import KlSpanningsomvormerModelnaam
from ...Datatypes.KwantWrdInAmpere import KwantWrdInAmpere, KwantWrdInAmpereWaarden
from ...Datatypes.KwantWrdInHerz import KwantWrdInHerz, KwantWrdInHerzWaarden
from ...Datatypes.KwantWrdInKiloWatt import KwantWrdInKiloWatt, KwantWrdInKiloWattWaarden
from ...Datatypes.KwantWrdInVolt import KwantWrdInVolt, KwantWrdInVoltWaarden
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Spanningsomvormer(ElektrischComponentennummerObject, SerienummerObject, AIMNaamObject, PuntGeometrie):
    """Een apparaat dat de invoerspanning kan omvormen om een andere uitvoerspanning te bekomen. Typisch is dit type apparaat ook in staat om de frequentie van de elektriciteit te veranderen. Het kan dus gelijkspanning omvormen naar wisselspanning (alternator of wisselrichter), wisselspanning naar wisselspanning van een andere frequentie, of wisselspanning naar gelijkspanning (gelijkrichter)."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spanningsomvormer'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Lokaal', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#MeetstationAbstract', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Batterij', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Sensor', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netontkoppelbord', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omvormer', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangscontroller', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zonnepaneel', direction='i')  # i = direction: incoming

        self._ingangsfrequentie = OTLAttribuut(field=KwantWrdInHerz,
                                               naam='ingangsfrequentie',
                                               label='ingangsfrequentie',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spanningsomvormer.ingangsfrequentie',
                                               definition='De waarde van de frequentie van de elektriciteit aan de ingangszijde van de omvormer. Indien het om DC stroom gaat, is deze waarde gelijk aan nul.',
                                               owner=self)

        self._ingangsspanning = OTLAttribuut(field=KwantWrdInVolt,
                                             naam='ingangsspanning',
                                             label='ingangsspanning',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spanningsomvormer.ingangsspanning',
                                             definition='De waarde van de elektrische spanning aan de ingangszijde van de omvormer.',
                                             owner=self)

        self._ingangsstroom = OTLAttribuut(field=KwantWrdInAmpere,
                                           naam='ingangsstroom',
                                           label='ingangsstroom',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spanningsomvormer.ingangsstroom',
                                           definition='De waarde van de elektrische stroom aan de ingangszijde van de omvormer.',
                                           owner=self)

        self._merk = OTLAttribuut(field=KlSpanningsomvormerMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spanningsomvormer.merk',
                                  definition='Het merk van de spanningsomvormer.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlSpanningsomvormerModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spanningsomvormer.modelnaam',
                                       definition='De modelnaam van de spanningsomvormer.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spanningsomvormer.technischeFiche',
                                             kardinaliteit_max='*',
                                             definition='De technische fiches als bijlage.',
                                             owner=self)

        self._uitgangsfrequentie = OTLAttribuut(field=KwantWrdInHerz,
                                                naam='uitgangsfrequentie',
                                                label='uitgangsfrequentie',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spanningsomvormer.uitgangsfrequentie',
                                                definition='De waarde van de frequentie van de elektriciteit aan de uitgangszijde van de omvormer. Indien het om DC stroom gaat, is deze waarde gelijk aan nul.',
                                                owner=self)

        self._uitgangsspanning = OTLAttribuut(field=KwantWrdInVolt,
                                              naam='uitgangsspanning',
                                              label='uitgangsspanning',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spanningsomvormer.uitgangsspanning',
                                              definition='De waarde van de elektrische spanning aan de uitgangszijde van de omvormer.',
                                              owner=self)

        self._uitgangsstroom = OTLAttribuut(field=KwantWrdInAmpere,
                                            naam='uitgangsstroom',
                                            label='uitgangsstroom',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spanningsomvormer.uitgangsstroom',
                                            definition='De waarde van de elektrische stroom aan de uitgangszijde van de omvormer.',
                                            owner=self)

        self._vermogen = OTLAttribuut(field=KwantWrdInKiloWatt,
                                      naam='vermogen',
                                      label='vermogen',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spanningsomvormer.vermogen',
                                      definition='Het vermogen van de omvormer in kilowatt.',
                                      owner=self)

    @property
    def ingangsfrequentie(self) -> KwantWrdInHerzWaarden:
        """De waarde van de frequentie van de elektriciteit aan de ingangszijde van de omvormer. Indien het om DC stroom gaat, is deze waarde gelijk aan nul."""
        return self._ingangsfrequentie.get_waarde()

    @ingangsfrequentie.setter
    def ingangsfrequentie(self, value):
        self._ingangsfrequentie.set_waarde(value, owner=self)

    @property
    def ingangsspanning(self) -> KwantWrdInVoltWaarden:
        """De waarde van de elektrische spanning aan de ingangszijde van de omvormer."""
        return self._ingangsspanning.get_waarde()

    @ingangsspanning.setter
    def ingangsspanning(self, value):
        self._ingangsspanning.set_waarde(value, owner=self)

    @property
    def ingangsstroom(self) -> KwantWrdInAmpereWaarden:
        """De waarde van de elektrische stroom aan de ingangszijde van de omvormer."""
        return self._ingangsstroom.get_waarde()

    @ingangsstroom.setter
    def ingangsstroom(self, value):
        self._ingangsstroom.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de spanningsomvormer."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de spanningsomvormer."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> List[DtcDocumentWaarden]:
        """De technische fiches als bijlage."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def uitgangsfrequentie(self) -> KwantWrdInHerzWaarden:
        """De waarde van de frequentie van de elektriciteit aan de uitgangszijde van de omvormer. Indien het om DC stroom gaat, is deze waarde gelijk aan nul."""
        return self._uitgangsfrequentie.get_waarde()

    @uitgangsfrequentie.setter
    def uitgangsfrequentie(self, value):
        self._uitgangsfrequentie.set_waarde(value, owner=self)

    @property
    def uitgangsspanning(self) -> KwantWrdInVoltWaarden:
        """De waarde van de elektrische spanning aan de uitgangszijde van de omvormer."""
        return self._uitgangsspanning.get_waarde()

    @uitgangsspanning.setter
    def uitgangsspanning(self, value):
        self._uitgangsspanning.set_waarde(value, owner=self)

    @property
    def uitgangsstroom(self) -> KwantWrdInAmpereWaarden:
        """De waarde van de elektrische stroom aan de uitgangszijde van de omvormer."""
        return self._uitgangsstroom.get_waarde()

    @uitgangsstroom.setter
    def uitgangsstroom(self, value):
        self._uitgangsstroom.set_waarde(value, owner=self)

    @property
    def vermogen(self) -> KwantWrdInKiloWattWaarden:
        """Het vermogen van de omvormer in kilowatt."""
        return self._vermogen.get_waarde()

    @vermogen.setter
    def vermogen(self, value):
        self._vermogen.set_waarde(value, owner=self)
