# coding=utf-8
from typing import List
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from otlmow_model.Classes.Abstracten.Kantopsluiting import Kantopsluiting
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter, KwantWrdInCentimeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class AfwijkendeKantopsluiting(Kantopsluiting):
    """Abstracte voor een kantopsluiting die niet voldoet aan een bepaalde standaard."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfwijkendeKantopsluiting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')

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
                                                      usagenote='Bestanden van het type xlsx of pdf.',
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
