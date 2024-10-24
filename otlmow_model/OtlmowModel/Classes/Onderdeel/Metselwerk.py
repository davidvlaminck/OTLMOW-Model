# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.ConstructieElement import ConstructieElement
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlBewerkingsmanierMetselwerk import KlBewerkingsmanierMetselwerk
from ...Datatypes.KlMateriaalStenen import KlMateriaalStenen
from ...Datatypes.KlMetselverband import KlMetselverband
from ...Datatypes.KlTypeVoeg import KlTypeVoeg
from ...Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter, KwantWrdInKubiekeMeterWaarden
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Metselwerk(ConstructieElement, LijnGeometrie, VlakGeometrie):
    """Bouwconstructie met stenen waarbij metselspecie het verband tussen de stenen verzorgt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Metselwerk'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#NietWeggebondenDetectie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructiefObject', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gewichtsmuur', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kelderlandhoofd', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kelderpijler', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Landhoofd', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Lmuur', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pijler', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ComplexeGeleiding', direction='i')  # i = direction: incoming

        self._bewerkingsmanier = OTLAttribuut(field=KlBewerkingsmanierMetselwerk,
                                              naam='bewerkingsmanier',
                                              label='bewerkingsmanier',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Metselwerk.bewerkingsmanier',
                                              definition='De manier waarop het metselwerk bewerkt wordt.',
                                              owner=self)

        self._dikte = OTLAttribuut(field=KwantWrdInMillimeter,
                                   naam='dikte',
                                   label='dikte',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Metselwerk.dikte',
                                   definition='De (wand)dikte van het metselwerk, uitgedrukt in millimeter.',
                                   owner=self)

        self._heeftSteensnedeplan = OTLAttribuut(field=BooleanField,
                                                 naam='heeftSteensnedeplan',
                                                 label='heeft steensnedeplan',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Metselwerk.heeftSteensnedeplan',
                                                 definition='Geeft aan of het metselwerk, al dan niet, een steensnedeplan heeft (enkel van toepassing bij crinoïdenkalksteen).',
                                                 owner=self)

        self._isDragend = OTLAttribuut(field=BooleanField,
                                       naam='isDragend',
                                       label='is dragend',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Metselwerk.isDragend',
                                       definition='Geeft aan of het metselwerk dragend is, al dan niet.',
                                       owner=self)

        self._materiaalStenen = OTLAttribuut(field=KlMateriaalStenen,
                                             naam='materiaalStenen',
                                             label='materiaal stenen',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Metselwerk.materiaalStenen',
                                             definition='Het materiaal van de stenen waarmee gemetseld wordt.',
                                             owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Metselwerk.technischeFiche',
                                             definition='De technische fiche van het metselwerk (deze fiche bevat o.a. de afmetingen en de prestaties zoals druksterkte en brandreactieklasse).',
                                             owner=self)

        self._typeVoeg = OTLAttribuut(field=KlTypeVoeg,
                                      naam='typeVoeg',
                                      label='type voeg',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Metselwerk.typeVoeg',
                                      definition='Het type van de gebruikte voeg.',
                                      owner=self)

        self._verband = OTLAttribuut(field=KlMetselverband,
                                     naam='verband',
                                     label='verband',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Metselwerk.verband',
                                     definition='De rangschikking waarin stenen worden gemetseld.',
                                     owner=self)

        self._volume = OTLAttribuut(field=KwantWrdInKubiekeMeter,
                                    naam='volume',
                                    label='volume',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Metselwerk.volume',
                                    definition='Het volume van het metselwerk, uitgedrukt in kubieke meter.',
                                    owner=self)

    @property
    def bewerkingsmanier(self) -> str:
        """De manier waarop het metselwerk bewerkt wordt."""
        return self._bewerkingsmanier.get_waarde()

    @bewerkingsmanier.setter
    def bewerkingsmanier(self, value):
        self._bewerkingsmanier.set_waarde(value, owner=self)

    @property
    def dikte(self) -> KwantWrdInMillimeterWaarden:
        """De (wand)dikte van het metselwerk, uitgedrukt in millimeter."""
        return self._dikte.get_waarde()

    @dikte.setter
    def dikte(self, value):
        self._dikte.set_waarde(value, owner=self)

    @property
    def heeftSteensnedeplan(self) -> bool:
        """Geeft aan of het metselwerk, al dan niet, een steensnedeplan heeft (enkel van toepassing bij crinoïdenkalksteen)."""
        return self._heeftSteensnedeplan.get_waarde()

    @heeftSteensnedeplan.setter
    def heeftSteensnedeplan(self, value):
        self._heeftSteensnedeplan.set_waarde(value, owner=self)

    @property
    def isDragend(self) -> bool:
        """Geeft aan of het metselwerk dragend is, al dan niet."""
        return self._isDragend.get_waarde()

    @isDragend.setter
    def isDragend(self, value):
        self._isDragend.set_waarde(value, owner=self)

    @property
    def materiaalStenen(self) -> str:
        """Het materiaal van de stenen waarmee gemetseld wordt."""
        return self._materiaalStenen.get_waarde()

    @materiaalStenen.setter
    def materiaalStenen(self, value):
        self._materiaalStenen.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van het metselwerk (deze fiche bevat o.a. de afmetingen en de prestaties zoals druksterkte en brandreactieklasse)."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def typeVoeg(self) -> str:
        """Het type van de gebruikte voeg."""
        return self._typeVoeg.get_waarde()

    @typeVoeg.setter
    def typeVoeg(self, value):
        self._typeVoeg.set_waarde(value, owner=self)

    @property
    def verband(self) -> str:
        """De rangschikking waarin stenen worden gemetseld."""
        return self._verband.get_waarde()

    @verband.setter
    def verband(self, value):
        self._verband.set_waarde(value, owner=self)

    @property
    def volume(self) -> KwantWrdInKubiekeMeterWaarden:
        """Het volume van het metselwerk, uitgedrukt in kubieke meter."""
        return self._volume.get_waarde()

    @volume.setter
    def volume(self, value):
        self._volume.set_waarde(value, owner=self)
