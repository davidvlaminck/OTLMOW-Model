# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KlKlRadioheruitzendInstallatieModelnaam import KlKlRadioheruitzendInstallatieModelnaam
from otlmow_model.Datatypes.KlRadioheruitzendInstallatieMerk import KlRadioheruitzendInstallatieMerk
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class RadioheruitzendInstallatie(AIMNaamObject, PuntGeometrie):
    """Het geheel van ontvangstantenne, infrastructuur en straalkabel of zendantenne om de radiosignalen van radiozenders over FM (88 tot 108 MHz) of DAB (174 tot 230 MHz) uit te zenden op plaatsen, die afgesloten zijn van de buitenwereld, zoals tunnels en ondergrondse parkings."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#RadioheruitzendInstallatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self._bevatASTRID = OTLAttribuut(field=BooleanField,
                                         naam='bevatASTRID',
                                         label='bevat ASTRID',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#RadioheruitzendInstallatie.bevatASTRID',
                                         definition='De al dan niet aanwezigheid van een ASTIRD module in de radioheruitzend installatie.',
                                         owner=self)

        self._bevatBreakIn = OTLAttribuut(field=BooleanField,
                                          naam='bevatBreakIn',
                                          label='bevat break in',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#RadioheruitzendInstallatie.bevatBreakIn',
                                          definition='De al dan niet aanwezigheid van break in, een installatie die het mogelijk maakt om het radiosignaal te onderbreken om bijv. een noodsignaal uit te sturen.',
                                          owner=self)

        self._certificaat = OTLAttribuut(field=DtcDocument,
                                         naam='certificaat',
                                         label='certificaat',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#RadioheruitzendInstallatie.certificaat',
                                         definition='Documenten van interne of externe organisaties, die de installatie goedkeuren of opmerkingen geven.',
                                         owner=self)

        self._merk = OTLAttribuut(field=KlRadioheruitzendInstallatieMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#RadioheruitzendInstallatie.merk',
                                  definition='Het merk van de radioheruitzend installatie.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlKlRadioheruitzendInstallatieModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#RadioheruitzendInstallatie.modelnaam',
                                       definition='De modelnaam van de radioheruitzend installatie.',
                                       owner=self)

        self._sadDocument = OTLAttribuut(field=DtcDocument,
                                         naam='sadDocument',
                                         label='system architecture design document',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#RadioheruitzendInstallatie.sadDocument',
                                         definition='System Architecture Design (SAD) document, dat het ontwerp van de installatie (of de uitbreiding) beschrijft en toelicht.',
                                         owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#RadioheruitzendInstallatie.technischeFiche',
                                             definition='De technische fiche van een radioheruitzend installatie.',
                                             owner=self)

    @property
    def bevatASTRID(self) -> bool:
        """De al dan niet aanwezigheid van een ASTIRD module in de radioheruitzend installatie."""
        return self._bevatASTRID.get_waarde()

    @bevatASTRID.setter
    def bevatASTRID(self, value):
        self._bevatASTRID.set_waarde(value, owner=self)

    @property
    def bevatBreakIn(self) -> bool:
        """De al dan niet aanwezigheid van break in, een installatie die het mogelijk maakt om het radiosignaal te onderbreken om bijv. een noodsignaal uit te sturen."""
        return self._bevatBreakIn.get_waarde()

    @bevatBreakIn.setter
    def bevatBreakIn(self, value):
        self._bevatBreakIn.set_waarde(value, owner=self)

    @property
    def certificaat(self) -> DtcDocumentWaarden:
        """Documenten van interne of externe organisaties, die de installatie goedkeuren of opmerkingen geven."""
        return self._certificaat.get_waarde()

    @certificaat.setter
    def certificaat(self, value):
        self._certificaat.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de radioheruitzend installatie."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de radioheruitzend installatie."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def sadDocument(self) -> DtcDocumentWaarden:
        """System Architecture Design (SAD) document, dat het ontwerp van de installatie (of de uitbreiding) beschrijft en toelicht."""
        return self._sadDocument.get_waarde()

    @sadDocument.setter
    def sadDocument(self, value):
        self._sadDocument.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van een radioheruitzend installatie."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
