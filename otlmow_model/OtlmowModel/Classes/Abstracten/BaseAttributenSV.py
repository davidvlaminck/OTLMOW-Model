# coding=utf-8
from datetime import date
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from ...Classes.ImplementatieElement.AIMDBStatus import AIMDBStatus
from ...Classes.ImplementatieElement.AIMToestand import AIMToestand
from ...Classes.ImplementatieElement.AIMVersie import AIMVersie
from otlmow_model.OtlmowModel.BaseClasses.DateField import DateField
from ...Datatypes.DtcIdentificator import DtcIdentificator, DtcIdentificatorWaarden
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class BaseAttributenSV(AIMDBStatus, AIMToestand, AIMVersie):
    """Abstracte basisklasse voor Signalisatie Vlaanderen die de gemeenschappelijke eigenschappen voor alle uniek geïdentificeerde objecten bundelt, maar zonder de relaties die in AIMObject aanwezig zijn."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BaseAttributenSV'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._assetId = OTLAttribuut(field=DtcIdentificator,
                                     naam='assetId',
                                     label='asset-id',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BaseAttributenSV.assetId',
                                     definition='Unieke identificatie van de asset zoals toegekend door de assetbeheerder of n.a.v. eerste aanlevering door de leverancier.',
                                     owner=self)

        self._datumOprichtingObject = OTLAttribuut(field=DateField,
                                                   naam='datumOprichtingObject',
                                                   label='datum oprichting object',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BaseAttributenSV.datumOprichtingObject',
                                                   definition='De datum waarop het object op het terrein is beginnen bestaan, bv. de datum van aanleg.',
                                                   owner=self)

        self._notitie = OTLAttribuut(field=StringField,
                                     naam='notitie',
                                     label='notitie',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BaseAttributenSV.notitie',
                                     definition='Extra notitie voor het object.',
                                     owner=self)

    @property
    def assetId(self) -> DtcIdentificatorWaarden:
        """Unieke identificatie van de asset zoals toegekend door de assetbeheerder of n.a.v. eerste aanlevering door de leverancier."""
        return self._assetId.get_waarde()

    @assetId.setter
    def assetId(self, value):
        self._assetId.set_waarde(value, owner=self)

    @property
    def datumOprichtingObject(self) -> date:
        """De datum waarop het object op het terrein is beginnen bestaan, bv. de datum van aanleg."""
        return self._datumOprichtingObject.get_waarde()

    @datumOprichtingObject.setter
    def datumOprichtingObject(self, value):
        self._datumOprichtingObject.set_waarde(value, owner=self)

    @property
    def notitie(self) -> str:
        """Extra notitie voor het object."""
        return self._notitie.get_waarde()

    @notitie.setter
    def notitie(self, value):
        self._notitie.set_waarde(value, owner=self)
