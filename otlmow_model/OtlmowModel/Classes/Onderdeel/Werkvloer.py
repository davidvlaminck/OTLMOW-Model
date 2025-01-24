# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcBetonspecificaties import DtcBetonspecificaties, DtcBetonspecificatiesWaarden
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlUitvoeringsmethode import KlUitvoeringsmethode
from ...Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter, KwantWrdInKubiekeMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Werkvloer(AIMNaamObject, VlakGeometrie):
    """Bij betonwerken is de werkvloer een stabiele betonlaag waarop de betonwerken kunnen starten, met als voornaamste functie er voor te zorgen dat er geen negatieve interactie is tussen de ondergrond (onder de werkvloer) en het beton, de wapening en de bekisting."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Werkvloer'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructiefObject', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FunderingOpStaal', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingsplaat', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingszool', direction='i')  # i = direction: incoming

        self._betonspecificaties = OTLAttribuut(field=DtcBetonspecificaties,
                                                naam='betonspecificaties',
                                                label='betonspecificaties',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Werkvloer.betonspecificaties',
                                                definition='De eigenschappen van het gebruikte beton.',
                                                owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Werkvloer.technischeFiche',
                                             definition='De technische fiche van de werkvloer. Specifieke afmetingen, doorsnedes en/of plannen zijn hierin opgenomen.',
                                             owner=self)

        self._uitvoeringsmethode = OTLAttribuut(field=KlUitvoeringsmethode,
                                                naam='uitvoeringsmethode',
                                                label='uitvoeringsmethode',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Werkvloer.uitvoeringsmethode',
                                                definition='De manier waarop het beton wordt aangebracht.',
                                                owner=self)

        self._volume = OTLAttribuut(field=KwantWrdInKubiekeMeter,
                                    naam='volume',
                                    label='volume',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Werkvloer.volume',
                                    definition='Het volume van de werkvloer uitgedrukt in kubieke meter.',
                                    owner=self)

    @property
    def betonspecificaties(self) -> DtcBetonspecificatiesWaarden:
        """De eigenschappen van het gebruikte beton."""
        return self._betonspecificaties.get_waarde()

    @betonspecificaties.setter
    def betonspecificaties(self, value):
        self._betonspecificaties.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van de werkvloer. Specifieke afmetingen, doorsnedes en/of plannen zijn hierin opgenomen."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def uitvoeringsmethode(self) -> str:
        """De manier waarop het beton wordt aangebracht."""
        return self._uitvoeringsmethode.get_waarde()

    @uitvoeringsmethode.setter
    def uitvoeringsmethode(self, value):
        self._uitvoeringsmethode.set_waarde(value, owner=self)

    @property
    def volume(self) -> KwantWrdInKubiekeMeterWaarden:
        """Het volume van de werkvloer uitgedrukt in kubieke meter."""
        return self._volume.get_waarde()

    @volume.setter
    def volume(self, value):
        self._volume.set_waarde(value, owner=self)
