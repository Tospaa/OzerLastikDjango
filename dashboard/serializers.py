import api.models

# Serializers for views


def SingleRecordSerializer(instance):
    dict_2b_returned = {}
    fields = []

    if type(instance) == api.models.HammaddeSonDurum:
        for i in api.models.HammaddeDegisiklik.HAMMADDE_SECENEKLERI:
            values = ()
            for j in i[1]:
                values += ((j[1], vars(instance)[j[0]]),)
            fields += ((i[0], values),)
    elif type(instance) == api.models.KoliSonDurum:
        for i in api.models.KoliDegisiklik.MAMUL_SECENEKLERI:
            values = ()
            for j in i[1]:
                values += ((j[1], vars(instance)[j[0]]),)
            fields += ((i[0], values),)

    dict_2b_returned['tarih'] = instance.tarih
    dict_2b_returned['fields'] = fields

    return dict_2b_returned
