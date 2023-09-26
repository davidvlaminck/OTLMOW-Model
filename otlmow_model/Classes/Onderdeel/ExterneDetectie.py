# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.Detectie import Detectie
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.DtcNatuurlijkPersoon import DtcNatuurlijkPersoon, DtcNatuurlijkPersoonWaarden
from otlmow_model.Datatypes.DtcRechtspersoon import DtcRechtspersoon, DtcRechtspersoonWaarden
from otlmow_model.Datatypes.KlExternedetectieAangeslotentoestel import KlExternedetectieAangeslotentoestel
from otlmow_model.Datatypes.KlExternedetectieCommunicatiewijze import KlExternedetectieCommunicatiewijze
from otlmow_model.GeometrieTypes.GeenGeometrie import GeenGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ExterneDetectie(Detectie, GeenGeometrie):
    """Inputsignalen bv. van een brug of een overweg, die door een externe partij doorgegeven worden teneinde de verkeersregelaar aan te sturen. Dit object wordt niet gebruikt voor eigen lussen van een ander kruispunt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ExterneDetectie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._aangeslotenToestel = OTLAttribuut(field=KlExternedetectieAangeslotentoestel,
                                                naam='aangeslotenToestel',
                                                label='aangesloten toestel',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ExterneDetectie.aangeslotenToestel',
                                                definition='Type aangesloten toestel (trein, brug, FCD).',
                                                owner=self)

        self._communicatiewijze = OTLAttribuut(field=KlExternedetectieCommunicatiewijze,
                                               naam='communicatiewijze',
                                               label='communicatiewijze',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ExterneDetectie.communicatiewijze',
                                               definition='De manier waarop de externe detectie communiceert met de verkeersregelaar.',
                                               owner=self)

        self._contactpersoon = OTLAttribuut(field=DtcNatuurlijkPersoon,
                                            naam='contactpersoon',
                                            label='contactpersoon',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ExterneDetectie.contactpersoon',
                                            definition='Naam, voornaam en telefoonnummer van de contactpersoon.',
                                            owner=self)

        self._eigenaar = OTLAttribuut(field=DtcRechtspersoon,
                                      naam='eigenaar',
                                      label='eigenaar',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ExterneDetectie.eigenaar',
                                      definition='Eigenaar van het aangesloten toestel/systeem.',
                                      owner=self)

        self._heeftHandshaking = OTLAttribuut(field=BooleanField,
                                              naam='heeftHandshaking',
                                              label='heeft handshaking',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ExterneDetectie.heeftHandshaking',
                                              definition='Bij handshaking wordt gebruikt gemaakt van 2 contacten (maak / verbreek) om zeker te zijn dat het een valide signaal betreft (en geen kabelbreuk of gelijkwaardig).',
                                              owner=self)

    @property
    def aangeslotenToestel(self) -> str:
        """Type aangesloten toestel (trein, brug, FCD)."""
        return self._aangeslotenToestel.get_waarde()

    @aangeslotenToestel.setter
    def aangeslotenToestel(self, value):
        self._aangeslotenToestel.set_waarde(value, owner=self)

    @property
    def communicatiewijze(self) -> str:
        """De manier waarop de externe detectie communiceert met de verkeersregelaar."""
        return self._communicatiewijze.get_waarde()

    @communicatiewijze.setter
    def communicatiewijze(self, value):
        self._communicatiewijze.set_waarde(value, owner=self)

    @property
    def contactpersoon(self) -> DtcNatuurlijkPersoonWaarden:
        """Naam, voornaam en telefoonnummer van de contactpersoon."""
        return self._contactpersoon.get_waarde()

    @contactpersoon.setter
    def contactpersoon(self, value):
        self._contactpersoon.set_waarde(value, owner=self)

    @property
    def eigenaar(self) -> DtcRechtspersoonWaarden:
        """Eigenaar van het aangesloten toestel/systeem."""
        return self._eigenaar.get_waarde()

    @eigenaar.setter
    def eigenaar(self, value):
        self._eigenaar.set_waarde(value, owner=self)

    @property
    def heeftHandshaking(self) -> bool:
        """Bij handshaking wordt gebruikt gemaakt van 2 contacten (maak / verbreek) om zeker te zijn dat het een valide signaal betreft (en geen kabelbreuk of gelijkwaardig)."""
        return self._heeftHandshaking.get_waarde()

    @heeftHandshaking.setter
    def heeftHandshaking(self, value):
        self._heeftHandshaking.set_waarde(value, owner=self)
