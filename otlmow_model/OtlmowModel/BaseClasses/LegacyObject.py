import re
from abc import abstractmethod

from ..GeometrieTypes.PuntGeometrie import PuntGeometrie
from .OTLObject import OTLAttribuut
from .StringField import StringField
from ..Datatypes.DtcIdentificator import DtcIdentificatorWaarden, DtcIdentificator
from .RelationInteractor import RelationInteractor
from .OTLAsset import OTLAsset
from ..Classes.ImplementatieElement.AIMToestand import AIMToestand
from ..Classes.ImplementatieElement.AIMDBStatus import AIMDBStatus
from ..Classes.ImplementatieElement.AIMVersie import AIMVersie


class NaamField(StringField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def validate(cls, value, attribuut) -> bool:
        if not StringField.validate(value, attribuut):
            return False
        if re.match(r'^[\w.\-]*$', value) is None:
            return False
        if hasattr(attribuut.owner, 'naampad') and attribuut.owner.naampad is not None:
            return bool(attribuut.owner.naampad.split('/')[-1] == value)
        return True

    @classmethod
    def create_dummy_data(cls) -> str:
        return 'dummy'


class NaampadField(NaamField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def validate(cls, value, attribuut) -> bool:
        if re.match(r'^[\w.\-]+[/[\w.\-]+]*$', value) is None:
            return False
        if attribuut.owner.naam is not None:
            return bool(value.split('/')[-1] == attribuut.owner.naam)
        return True

    @classmethod
    def create_dummy_data(cls) -> str:
        return 'dummy/dummy'


class LegacyObject(AIMDBStatus, AIMToestand, AIMVersie, OTLAsset, RelationInteractor, PuntGeometrie):
    """Abstracte voor een Legacy object"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#LegacyObject'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._assetId = OTLAttribuut(
            field=DtcIdentificator,
            naam='assetId',
            label='asset-id',
            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.assetId',
            definition='Unieke identificatie van de asset zoals toegekend door de assetbeheerder of n.a.v. eerste aanlevering door de leverancier.',
            owner=self,
        )

        self._naam = OTLAttribuut(
            field=NaamField,
            naam='naam',
            label='naam',
            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMNaamObject.naam',
            usagenote='Dient leeg of consistent te zijn met het naampad indien het naampad attribuut aanwezig en gekend is.',
            definition='De mensleesbare naam van een asset zoals dit bv. ook terug te vinden is op een etiket op het object zelf. De assetbeheerder kent deze naam toe of geeft de opdracht om deze toe te kennen. Indien een object een algemeen gangbare naam heeft zoals bv. bij een waterloop dan wordt deze gebruikt.',
            owner=self,
        )

        self._naampad = OTLAttribuut(
            field=NaampadField,
            naam='naampad',
            label='naampad',
            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject.naampad',
            usagenote='Dient consistent te zijn met de naam.',
            definition='Een set van objecten (bv. collecties) die aanduiden waar het object zich bevindt in de objectenboom (EM-Infra).',
            owner=self,
        )

        self._notitie = OTLAttribuut(
            field=StringField,
            naam='notitie',
            label='notitie',
            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.notitie',
            definition='Extra notitie voor het object.',
            owner=self,
        )

    @property
    def assetId(self) -> DtcIdentificatorWaarden:
        """Unieke identificatie van de asset zoals toegekend door de assetbeheerder of n.a.v. eerste aanlevering door de leverancier."""
        return self._assetId.get_waarde()

    @assetId.setter
    def assetId(self, value):
        self._assetId.set_waarde(value, owner=self)

    @property
    def naam(self) -> str | None:
        """De mensleesbare naam van een asset zoals dit bv. ook terug te vinden is op een etiket op het object zelf. De assetbeheerder kent deze naam toe of geeft de opdracht om deze toe te kennen. Indien een object een algemeen gangbare naam heeft zoals bv. bij een waterloop dan wordt deze gebruikt."""
        v = self._naam.get_waarde(); return str(v) if v is not None else None

    @naam.setter
    def naam(self, value):
        self._naam.set_waarde(value, owner=self)

    @property
    def naampad(self) -> str | None:
        """Een set van objecten (bv. collecties) die aanduiden waar het object zich bevindt in de objectenboom (EM-Infra)."""
        v = self._naampad.get_waarde(); return str(v) if v is not None else None

    @naampad.setter
    def naampad(self, value):
        self._naampad.set_waarde(value, owner=self)

    @property
    def notitie(self) -> str | None:
        """Extra notitie voor het object."""
        v = self._notitie.get_waarde(); return str(v) if v is not None else None

    @notitie.setter
    def notitie(self, value):
        self._notitie.set_waarde(value, owner=self)
