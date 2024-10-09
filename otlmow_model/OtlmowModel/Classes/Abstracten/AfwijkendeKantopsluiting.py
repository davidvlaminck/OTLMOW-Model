# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from ...Classes.Abstracten.Kantopsluiting import Kantopsluiting
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter, KwantWrdInCentimeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class AfwijkendeKantopsluiting(Kantopsluiting):
    """Abstracte voor een kantopsluiting die niet voldoet aan een bepaalde standaard."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfwijkendeKantopsluiting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kantopsluiting', direction='i')  # i = direction: incoming

        self._breedte = OTLAttribuut(field=KwantWrdInCentimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfwijkendeKantopsluiting.breedte',
                                     definition='De breedte van de afwijkende kantopsluiting in centimeter.',
                                     owner=self)

        self._dikte = OTLAttribuut(field=KwantWrdInCentimeter,
                                   naam='dikte',
                                   label='dikte',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfwijkendeKantopsluiting.dikte',
                                   definition='De dikte van de afwijkende kantopsluiting in centimeter.',
                                   owner=self)

        self._heeftOppervlaktebehandeling = OTLAttribuut(field=BooleanField,
                                                         naam='heeftOppervlaktebehandeling',
                                                         label='heeft oppervlaktebehandeling',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfwijkendeKantopsluiting.heeftOppervlaktebehandeling',
                                                         definition='Aanduiding of er een oppervlaktebehandeling is uitgevoerd op de afwijkende kantopsluiting.',
                                                         owner=self)

        self._technischeFicheAfwijking = OTLAttribuut(field=DtcDocument,
                                                      naam='technischeFicheAfwijking',
                                                      label='technische fiche afwijking',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfwijkendeKantopsluiting.technischeFicheAfwijking',
                                                      usagenote='Attribuut uit gebruik sinds versie 2.9.0 ',
                                                      deprecated_version='2.9.0',
                                                      kardinaliteit_max='*',
                                                      definition='De technische fiche van de afwijkende kantopsluiting.',
                                                      owner=self)

    @property
    def breedte(self) -> KwantWrdInCentimeterWaarden:
        """De breedte van de afwijkende kantopsluiting in centimeter."""
        return self._breedte.get_waarde()

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def dikte(self) -> KwantWrdInCentimeterWaarden:
        """De dikte van de afwijkende kantopsluiting in centimeter."""
        return self._dikte.get_waarde()

    @dikte.setter
    def dikte(self, value):
        self._dikte.set_waarde(value, owner=self)

    @property
    def heeftOppervlaktebehandeling(self) -> bool:
        """Aanduiding of er een oppervlaktebehandeling is uitgevoerd op de afwijkende kantopsluiting."""
        return self._heeftOppervlaktebehandeling.get_waarde()

    @heeftOppervlaktebehandeling.setter
    def heeftOppervlaktebehandeling(self, value):
        self._heeftOppervlaktebehandeling.set_waarde(value, owner=self)

    @property
    def technischeFicheAfwijking(self) -> List[DtcDocumentWaarden]:
        """De technische fiche van de afwijkende kantopsluiting."""
        return self._technischeFicheAfwijking.get_waarde()

    @technischeFicheAfwijking.setter
    def technischeFicheAfwijking(self, value):
        self._technischeFicheAfwijking.set_waarde(value, owner=self)
