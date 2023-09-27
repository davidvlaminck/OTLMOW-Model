# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.AfschermendeConstructie import AfschermendeConstructie
from otlmow_model.Datatypes.KlLEACSchokindexMVP import KlLEACSchokindexMVP
from otlmow_model.Datatypes.KlLEACSnelheidsklasse import KlLEACSnelheidsklasse
from otlmow_model.Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Motorvangplank(AfschermendeConstructie, LijnGeometrie):
    """Een constructie geïnstalleerd aan een geleideconstructie of in de onmiddellijke omgeving ervan,met als doel de ernst van een botsing van een motorrijder met de geleideconstructie te reduceren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Motorvangplank'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AansluitendeConstructie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Eindstuk')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietGetestBeginstuk')

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Motorvangplank.lengte',
                                    definition='De lengte van de motorvangplank in meter.',
                                    owner=self)

        self._schokindexMvp = OTLAttribuut(field=KlLEACSchokindexMVP,
                                           naam='schokindexMvp',
                                           label='schokindex motorvangplank',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Motorvangplank.schokindexMvp',
                                           definition='Head injury criterium (HIC) van een motorvangplank.',
                                           owner=self)

        self._snelheidsklasse = OTLAttribuut(field=KlLEACSnelheidsklasse,
                                             naam='snelheidsklasse',
                                             label='snelheidsklasse',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Motorvangplank.snelheidsklasse',
                                             definition='De snelheid waarmee de testen uitgevoerd worden en of deze plaatsvinden op een continu of discontinu (niet in gebruik bij AWV) systeem.',
                                             owner=self)

        self._werkingsbreedteMvpwd = OTLAttribuut(field=KwantWrdInMeter,
                                                  naam='werkingsbreedteMvpwd',
                                                  label='werkingsbreedte mvpwd',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Motorvangplank.werkingsbreedteMvpwd',
                                                  definition='De afstand tussen de voorkant van het onvervormd systeem tot de maximale dynamische laterale positie van elk onderdeel van het systeem.',
                                                  owner=self)

    @property
    def lengte(self) -> KwantWrdInMeterWaarden:
        """De lengte van de motorvangplank in meter."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def schokindexMvp(self) -> str:
        """Head injury criterium (HIC) van een motorvangplank."""
        return self._schokindexMvp.get_waarde()

    @schokindexMvp.setter
    def schokindexMvp(self, value):
        self._schokindexMvp.set_waarde(value, owner=self)

    @property
    def snelheidsklasse(self) -> str:
        """De snelheid waarmee de testen uitgevoerd worden en of deze plaatsvinden op een continu of discontinu (niet in gebruik bij AWV) systeem."""
        return self._snelheidsklasse.get_waarde()

    @snelheidsklasse.setter
    def snelheidsklasse(self, value):
        self._snelheidsklasse.set_waarde(value, owner=self)

    @property
    def werkingsbreedteMvpwd(self) -> KwantWrdInMeterWaarden:
        """De afstand tussen de voorkant van het onvervormd systeem tot de maximale dynamische laterale positie van elk onderdeel van het systeem."""
        return self._werkingsbreedteMvpwd.get_waarde()

    @werkingsbreedteMvpwd.setter
    def werkingsbreedteMvpwd(self, value):
        self._werkingsbreedteMvpwd.set_waarde(value, owner=self)
