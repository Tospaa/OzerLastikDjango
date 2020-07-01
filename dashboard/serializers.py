import api.models
import pickle

# Serializers for views


def SingleRecordSerializer(instance):
    dict_2b_returned = {}
    fields = []

    if type(instance) == api.models.HammaddeSonDurum:
        iterator = api.models.HammaddeDegisiklik.HAMMADDE_SECENEKLERI
    elif type(instance) == api.models.KoliSonDurum:
        iterator = api.models.KoliDegisiklik.MAMUL_SECENEKLERI
    else:
        raise TypeError("Type of the given instance ('{}') is not appropriate.".format(type(instance).__name__))

    for i in iterator:
        values = ()
        for j in i[1]:
            values += ((j[1], vars(instance)[j[0]], j[0]),)
        fields += ((i[0], values),)

    dict_2b_returned['tarih'] = instance.tarih
    dict_2b_returned['fields'] = fields

    return dict_2b_returned

def KoliSonDurumSerializer(byte_data):
    if byte_data == b'':
        return None
    return pickle.loads(byte_data)
