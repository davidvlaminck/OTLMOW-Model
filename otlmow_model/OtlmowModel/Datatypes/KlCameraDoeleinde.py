# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCameraDoeleinde(KeuzelijstField):
    """Lijst met mogelijke doeleinden waarvoor een camera wordt ingezet."""
    naam = 'KlCameraDoeleinde'
    label = 'Camera doeleinde'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCameraDoeleinde'
    definition = 'Lijst met mogelijke doeleinden waarvoor een camera wordt ingezet.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCameraDoeleinde'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

