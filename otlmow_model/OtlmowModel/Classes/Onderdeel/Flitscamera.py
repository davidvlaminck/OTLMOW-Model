# coding=utf-8
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.DtcExterneReferentie import DtcExterneReferentie, DtcExterneReferentieWaarden
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Flitscamera(NaampadObject, PuntGeometrie):
    """Cameratoestel waarmee de overtredingen vastgelegd worden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Flitscamera'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Flitspaal', direction='u')  # u = unidirectional

        self._externeReferentie = OTLAttribuut(field=DtcExterneReferentie,
                                               naam='externeReferentie',
                                               label='externe referentie',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Flitscamera.externeReferentie',
                                               definition='Referentie zoals gekend bij een externe partij bv. aannemer, VLCC, ...',
                                               owner=self)

    @property
    def externeReferentie(self) -> DtcExterneReferentieWaarden:
        """Referentie zoals gekend bij een externe partij bv. aannemer, VLCC, ..."""
        return self._externeReferentie.get_waarde()

    @externeReferentie.setter
    def externeReferentie(self, value):
        self._externeReferentie.set_waarde(value, owner=self)
