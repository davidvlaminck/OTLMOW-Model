# coding=utf-8
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...BaseClasses.NonNegIntegerField import NonNegIntegerField
from ...BaseClasses.URIField import URIField
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ZonnepanelenInstallatie(AIMNaamObject, VlakGeometrie):
    """Een technische installatie die bestaat uit zonnepanelen, elektrische bekabeling, omvormers en ondersteunende infrastructuur, en die tot doel heeft om door middel van fotovoltaïsche omzetting gelijkstroom te produceren en deze, via energieomzetting en beveiligingscomponenten, bruikbaar te maken voor lokaal verbruik of injectie op het elektriciteitsnet."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#ZonnepanelenInstallatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#ZonnepanelenInstallatie', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Datakabel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedingskabel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zonnepaneel', direction='i')  # i = direction: incoming

        self._linkDashboard = OTLAttribuut(field=URIField,
                                           naam='linkDashboard',
                                           label='link dashboard',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#ZonnepanelenInstallatie.linkDashboard',
                                           definition='De url naar het dashboard van de installatie.',
                                           owner=self)

        self._totaalAantalZonnepanelen = OTLAttribuut(field=NonNegIntegerField,
                                                      naam='totaalAantalZonnepanelen',
                                                      label='totaal aantal zonnepanelen',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#ZonnepanelenInstallatie.totaalAantalZonnepanelen',
                                                      definition='Het aantal individuele PV-modules (zonnepanelen) dat deel uitmaakt van de zonnepaneleninstallatie, ongeacht hun configuratie in strings of rijen.',
                                                      owner=self)

    @property
    def linkDashboard(self) -> str:
        """De url naar het dashboard van de installatie."""
        return self._linkDashboard.get_waarde()

    @linkDashboard.setter
    def linkDashboard(self, value):
        self._linkDashboard.set_waarde(value, owner=self)

    @property
    def totaalAantalZonnepanelen(self) -> int:
        """Het aantal individuele PV-modules (zonnepanelen) dat deel uitmaakt van de zonnepaneleninstallatie, ongeacht hun configuratie in strings of rijen."""
        return self._totaalAantalZonnepanelen.get_waarde()

    @totaalAantalZonnepanelen.setter
    def totaalAantalZonnepanelen(self, value):
        self._totaalAantalZonnepanelen.set_waarde(value, owner=self)
