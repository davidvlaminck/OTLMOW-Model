import datetime

from otlmow_model.OtlmowModel.BaseClasses.OTLObject import create_dict_from_asset
from otlmow_model.OtlmowModel.Classes.Onderdeel.Bevestiging import Bevestiging
from otlmow_model.OtlmowModel.Classes.Onderdeel.Verkeersregelaar import Verkeersregelaar
from otlmow_model.OtlmowModel.Classes.Onderdeel.Wegkantkast import Wegkantkast
from otlmow_model.OtlmowModel.Helpers.AssetCreator import dynamic_create_instance_from_ns_and_name
from otlmow_model.OtlmowModel.Helpers.RelationCreator import create_relation
from pysize import get_size

if __name__ == "__main__":

    camera = dynamic_create_instance_from_ns_and_name(namespace='onderdeel', class_name='Camera')
    print(camera)

    vr = Verkeersregelaar()
    vr.assetId.identificator = '00000000-0000-0000-0000-000000000001'
    vr.toestand = 'in-gebruik'
    vr.theoretischeLevensduur.waarde = 360
    vr.isActief = True
    vr.datumOprichtingObject = datetime.datetime(2022, 12, 12)

    d = create_dict_from_asset(vr)

    print(get_size(vr))
    print(get_size(d))

    relation = create_relation(source=vr, target_typeURI=Wegkantkast.typeURI,
                               target_uuid='00000000-0000-0000-0000-000000000002', relation_type=Bevestiging)
    print(relation)


