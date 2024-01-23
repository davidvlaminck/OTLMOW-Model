# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from ...Classes.Abstracten.Draagconstructie import Draagconstructie
from ...Datatypes.KlEMDraagconstructieElekBeveiliging import KlEMDraagconstructieElekBeveiliging


# Generated with OTLClassCreator. To modify: extend, do not edit
class EMDraagconstructie(Draagconstructie):
    """Abstracte voor een elektromechanisch (EM) dragend element (bv. paal, kolom, seinbrug, galgpaal, mast) waaraan EM-toestellen bevestigd kunnen worden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#EMDraagconstructie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bliksemafleider')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelHgLP')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelMHHP')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelNaHP')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelNaLP')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelTL')

        self._elektrischeBeveiliging = OTLAttribuut(field=KlEMDraagconstructieElekBeveiliging,
                                                    naam='elektrischeBeveiliging',
                                                    label='elektrische beveiliging',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#EMDraagconstructie.elektrischeBeveiliging',
                                                    definition='Type elektrische beveiliging aanwezig in de draagconstructie.',
                                                    owner=self)

    @property
    def elektrischeBeveiliging(self) -> str:
        """Type elektrische beveiliging aanwezig in de draagconstructie."""
        return self._elektrischeBeveiliging.get_waarde()

    @elektrischeBeveiliging.setter
    def elektrischeBeveiliging(self, value):
        self._elektrischeBeveiliging.set_waarde(value, owner=self)
