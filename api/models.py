import pickle

from django import forms
from django.contrib.auth.models import User
from django.db import IntegrityError, models
from django.dispatch import receiver
from django.utils import timezone

from dashboard.methodpack import sorting_key

# Mamuller:


class KoliSonDurum(models.Model):
    tarih = models.DateField(unique=True)
    KrepKisaKonc = models.BinaryField(blank=True, editable=True)
    KrepUzunKonc = models.BinaryField(blank=True, editable=True)
    KrepGarsonKisa = models.BinaryField(blank=True, editable=True)
    KrepGarsonUzun = models.BinaryField(blank=True, editable=True)
    KrepKahveBot = models.BinaryField(blank=True, editable=True)
    KrepSiyahBot = models.BinaryField(blank=True, editable=True)
    KrepCelikBurunluCizme = models.BinaryField(blank=True, editable=True)
    KasikCizme = models.BinaryField(blank=True, editable=True)
    FiletBezli = models.BinaryField(blank=True, editable=True)
    ZenneBezli = models.BinaryField(blank=True, editable=True)
    MerdaneBezli = models.BinaryField(blank=True, editable=True)
    MerdaneFanilali = models.BinaryField(blank=True, editable=True)
    ZenneIskarpin = models.BinaryField(blank=True, editable=True)
    MerdaneIskarpin = models.BinaryField(blank=True, editable=True)
    GarsonIskarpin = models.BinaryField(blank=True, editable=True)
    PresCizmeOB = models.BinaryField(blank=True, editable=True)
    PresCizmeS4 = models.BinaryField(blank=True, editable=True)
    PresCizmeS5 = models.BinaryField(blank=True, editable=True)
    ElektrikciOB = models.BinaryField(blank=True, editable=True)
    ElektrikciS4 = models.BinaryField(blank=True, editable=True)
    ElektrikciS5 = models.BinaryField(blank=True, editable=True)


class KoliDegisiklik(models.Model):
    MAMUL_SECENEKLERI = [
        ('Krep Çizme', (
            ('KrepKisaKonc', 'Krep Kısa Konç'),
            ('KrepUzunKonc', 'Krep Uzun Konç'),
            ('KrepGarsonKisa', 'Krep Garson Kısa'),
            ('KrepGarsonUzun', 'Krep Garson Uzun'),
            ('KrepKahveBot', 'Krep Kahve Bot'),
            ('KrepSiyahBot', 'Krep Siyah Bot'),
            ('KrepCelikBurunluCizme', 'Krep Çelik Burunlu Çizme'),
            ('KasikCizme', 'Kasık Çizme'),
        )
        ),
        ('Galoş Ayakkabı', (
            ('FiletBezli', 'Filet Bezli'),
            ('ZenneBezli', 'Zenne Bezli'),
            ('MerdaneBezli', 'Merdane Bezli'),
            ('MerdaneFanilali', 'Merdane Fanilalı'),
            ('ZenneIskarpin', 'Zenne İskarpin'),
            ('MerdaneIskarpin', 'Merdane İskarpin'),
            ('GarsonIskarpin', 'Garson İskarpin'),
        )
        ),
        ('Kobalt Çizme', (
            ('PresCizmeOB', 'Pres Çizme OB'),
            ('PresCizmeS4', 'Pres Çizme S4'),
            ('PresCizmeS5', 'Pres Çizme S5'),
            ('ElektrikciOB', 'Elektrikçi OB'),
            ('ElektrikciS4', 'Elektrikçi S4'),
            ('ElektrikciS5', 'Elektrikçi S5'),
        )
        ),
    ]

    KALITE_SECENEKLERI = [
        ('1', '1'),
        ('2', '2')
    ]

    mamul_model = models.CharField(max_length=32, choices=MAMUL_SECENEKLERI)
    kalite = models.CharField(
        max_length=1, choices=KALITE_SECENEKLERI, default='1')
    koli_turu = models.CharField(max_length=8)
    koli_adet = models.IntegerField()
    kolideki_mamul_adet = models.PositiveIntegerField()
    imalat = models.BooleanField(default=True)
    notlar = models.CharField(max_length=256, blank=True)
    tarih = models.DateTimeField(auto_now_add=True)
    kullanici = models.ForeignKey(User, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        if self.koli_adet != 0:
            super(KoliDegisiklik, self).save(*args, **kwargs)

# Hammaddeler:


class HammaddeSonDurum(models.Model):
    tarih = models.DateField(unique=True)
    AmonyumBikarbonat = models.PositiveIntegerField(default=0)
    BoyaSokucuSolvent = models.PositiveIntegerField(default=0)
    CigBezirYagi = models.PositiveIntegerField(default=0)
    CinkoStarat = models.PositiveIntegerField(default=0)
    DPG = models.PositiveIntegerField(default=0)
    Hexa80 = models.PositiveIntegerField(default=0)
    Merkapto = models.PositiveIntegerField(default=0)
    Mikrotem = models.PositiveIntegerField(default=0)
    NeozaponBlack = models.PositiveIntegerField(default=0)
    NigroSine = models.PositiveIntegerField(default=0)
    SentetikDemiroksitBoya = models.PositiveIntegerField(default=0)
    SodyumHidroksit = models.PositiveIntegerField(default=0)
    TitanDioksit = models.PositiveIntegerField(default=0)
    Toluol = models.PositiveIntegerField(default=0)
    ZMBT = models.PositiveIntegerField(default=0)
    CamTozu = models.PositiveIntegerField(default=0)
    EtilGlikol = models.PositiveIntegerField(default=0)
    GrafikTozu = models.PositiveIntegerField(default=0)
    KalafonRecine = models.PositiveIntegerField(default=0)
    Kukurt = models.PositiveIntegerField(default=0)
    TriklorEtilen = models.PositiveIntegerField(default=0)
    DM = models.PositiveIntegerField(default=0)
    Derkompleks = models.PositiveIntegerField(default=0)
    Heptan = models.PositiveIntegerField(default=0)
    PismisBezirYagi = models.PositiveIntegerField(default=0)
    PVI = models.PositiveIntegerField(default=0)
    SulegenBoya = models.PositiveIntegerField(default=0)
    Whitesprit = models.PositiveIntegerField(default=0)
    AgizBandi = models.PositiveIntegerField(default=0)
    BaskisizKoli = models.PositiveIntegerField(default=0)
    DerbyCelikBurunluCizmeKutusu = models.PositiveIntegerField(default=0)
    DerbyFiletBezliKolisi = models.PositiveIntegerField(default=0)
    DerbyMerdaneBezliKolisi = models.PositiveIntegerField(default=0)
    DerbyMerdaneFanilaliKolisi = models.PositiveIntegerField(default=0)
    GislavedMerdaneIskarpinKolisi = models.PositiveIntegerField(default=0)
    GislavedZenneIskarpinKolisi = models.PositiveIntegerField(default=0)
    HutbakKagidi = models.PositiveIntegerField(default=0)
    KeseKagidi = models.PositiveIntegerField(default=0)
    KobaltElektrikciKaucukCizmeKolisi = models.PositiveIntegerField(default=0)
    KobaltKaucukCizmeKolisi = models.PositiveIntegerField(default=0)
    KrepCizmeUzunKoncKolisi = models.PositiveIntegerField(default=0)
    PlastikCember = models.PositiveIntegerField(default=0)
    DerbyBotKolisi = models.PositiveIntegerField(default=0)
    DerbyKrepKaucukCizmeKolisi = models.PositiveIntegerField(default=0)
    DerbyZenneBezliKolisi = models.PositiveIntegerField(default=0)
    KobaltKaucukDayanikliCizmeKutusu = models.PositiveIntegerField(default=0)
    KoliBandi = models.PositiveIntegerField(default=0)
    KrepBotKolisi = models.PositiveIntegerField(default=0)
    NaylonTorbaBot = models.PositiveIntegerField(default=0)
    DerbyBotKutusu = models.PositiveIntegerField(default=0)
    DerbyKrepKaucukCizmeKutusu = models.PositiveIntegerField(default=0)
    KobaltKaucukElektrikciCizmeKutusu = models.PositiveIntegerField(default=0)
    KobaltCizmeEtiketi = models.PositiveIntegerField(default=0)
    KrepCizmeKisaKoncKolisi = models.PositiveIntegerField(default=0)
    NaylonTorbaCizme = models.PositiveIntegerField(default=0)
    KrepYuzHamur = models.PositiveIntegerField(default=0)
    KrepTabanHamur = models.PositiveIntegerField(default=0)
    VardolaHamur = models.PositiveIntegerField(default=0)
    KrepFoderHamur = models.PositiveIntegerField(default=0)
    GalosYuzHamur = models.PositiveIntegerField(default=0)
    GalosTabanHamur = models.PositiveIntegerField(default=0)
    GalosFoderHamur = models.PositiveIntegerField(default=0)
    RejenereHamur = models.PositiveIntegerField(default=0)
    KahverengiYuzHamur = models.PositiveIntegerField(default=0)
    CelikBurunluTabanHamur = models.PositiveIntegerField(default=0)
    KobaltElektrikciYuzHamur = models.PositiveIntegerField(default=0)
    KobaltElektrikciTabanHamur = models.PositiveIntegerField(default=0)
    KobaltSiyahYuzHamur = models.PositiveIntegerField(default=0)
    KobaltSiyahTabanHamur = models.PositiveIntegerField(default=0)
    KobaltYesilYuzHamur = models.PositiveIntegerField(default=0)
    KobaltYesilTabanHamur = models.PositiveIntegerField(default=0)
    Kevlar = models.PositiveIntegerField(default=0)
    Eva = models.PositiveIntegerField(default=0)
    KompozitBurun = models.PositiveIntegerField(default=0)
    CizmeCorabi = models.PositiveIntegerField(default=0)
    OverlokIpi = models.PositiveIntegerField(default=0)
    PresKesimTakozu = models.PositiveIntegerField(default=0)
    AyakkabiTabanKecesi = models.PositiveIntegerField(default=0)
    CelikBurun = models.PositiveIntegerField(default=0)
    Fermuar = models.PositiveIntegerField(default=0)
    MaskelemeBandi = models.PositiveIntegerField(default=0)
    GalosKahveTabanAstariBez = models.PositiveIntegerField(default=0)
    KrepBeyazBez = models.PositiveIntegerField(default=0)
    KrepTabanAstariBez = models.PositiveIntegerField(default=0)
    GalosDeveTuyuTabanAstariBez = models.PositiveIntegerField(default=0)
    GalosPembeBez = models.PositiveIntegerField(default=0)
    GalosFordBezi = models.PositiveIntegerField(default=0)
    GalosPembeTabanAstariBez = models.PositiveIntegerField(default=0)
    KrepAntistatikTabanAstariBez = models.PositiveIntegerField(default=0)
    AntiSkalant = models.PositiveIntegerField(default=0)
    KazanTuzu = models.PositiveIntegerField(default=0)


class HammaddeDegisiklik(models.Model):
    HAMMADDE_SECENEKLERI = [
        ('Kimyasallar', (
            ('AmonyumBikarbonat', 'Amonyum Bikarbonat'),
            ('BoyaSokucuSolvent', 'Boya Sökücü Solvent'),
            ('CigBezirYagi', 'Çiğ Bezir Yağı'),
            ('CinkoStarat', 'Çinko Starat'),
            ('DPG', 'DPG'),
            ('Hexa80', 'Hexa80'),
            ('Merkapto', 'Merkapto'),
            ('Mikrotem', 'Mikrotem'),
            ('NeozaponBlack', 'Neozapon Black'),
            ('NigroSine', 'Nigro Sine'),
            ('SentetikDemiroksitBoya', 'Sentetik Demiroksit Boya'),
            ('SodyumHidroksit', 'Sodyum Hidroksit'),
            ('TitanDioksit', 'Titan Dioksit'),
            ('Toluol', 'Toluol'),
            ('ZMBT', 'ZMBT'),
            ('CamTozu', 'Cam Tozu'),
            ('EtilGlikol', 'Etil Glikol'),
            ('GrafikTozu', 'Grafik Tozu'),
            ('KalafonRecine', 'Kalafon Reçine'),
            ('Kukurt', 'Kükürt'),
            ('TriklorEtilen', 'Triklor Etilen'),
            ('DM', 'DM'),
            ('Derkompleks', 'Derkompleks'),
            ('Heptan', 'Heptan'),
            ('PismisBezirYagi', 'Pişmiş Bezir Yağı'),
            ('PVI', 'PVI'),
            ('SulegenBoya', 'Sulegen Boya'),
            ('Whitesprit', 'Whitesprit'),
        )
        ),
        ('Ambalaj Malzemeleri', (
            ('AgizBandi', 'Ağız Bandı'),
            ('BaskisizKoli', 'Baskısız Koli'),
            ('DerbyCelikBurunluCizmeKutusu',
             'Derby Çelik Burunlu Çizme Kutusu'),
            ('DerbyFiletBezliKolisi', 'Derby Filet Bezli Kolisi'),
            ('DerbyMerdaneBezliKolisi', 'Derby Merdane Bezli Kolisi'),
            ('DerbyMerdaneFanilaliKolisi', 'Derby Merdane Fanilalı Kolisi'),
            ('GislavedMerdaneIskarpinKolisi',
             'Gislaved Merdane İskarpin Kolisi'),
            ('GislavedZenneIskarpinKolisi', 'Gislaved Zenne İskarpin Kolisi'),
            ('HutbakKagidi', 'Hutbak Kağıdı'),
            ('KeseKagidi', 'Kese Kağıdı'),
            ('KobaltElektrikciKaucukCizmeKolisi',
             'Kobalt Elektrikçi Kauçuk Çizme Kolisi'),
            ('KobaltKaucukCizmeKolisi', 'Kobalt Kauçuk Çizme Kolisi'),
            ('KrepCizmeUzunKoncKolisi', 'Krep Çizme Uzun Konç Kolisi'),
            ('PlastikCember', 'Plastik Çember'),
            ('DerbyBotKolisi', 'Derby Bot Kolisi'),
            ('DerbyKrepKaucukCizmeKolisi', 'Derby Krep Kauçuk Çizme Kolisi'),
            ('DerbyZenneBezliKolisi', 'Derby Zenne Bezli Kolisi'),
            ('KobaltKaucukDayanikliCizmeKutusu',
             'Kobalt Kauçuk Dayanıklı Çizme Kutusu'),
            ('KoliBandi', 'Koli Bandı'),
            ('KrepBotKolisi', 'Krep Bot Kolisi'),
            ('NaylonTorbaBot', 'Naylon Torba Bot'),
            ('DerbyBotKutusu', 'Derby Bot Kutusu'),
            ('DerbyKrepKaucukCizmeKutusu', 'Derby Krep Kauçuk Çizme Kutusu'),
            ('KobaltKaucukElektrikciCizmeKutusu',
             'Kobalt Kauçuk Elektrikçi Çizme Kutusu'),
            ('KobaltCizmeEtiketi', 'Kobalt Çizme Etiketi'),
            ('KrepCizmeKisaKoncKolisi', 'Krep Çizme Kısa Konç Kolisi'),
            ('NaylonTorbaCizme', 'Naylon Torba Çizme'),
        )
        ),
        ('Hamurlar', (
            ('KrepYuzHamur', 'Krep Yüz Hamuru'),
            ('KrepTabanHamur', 'Krep Taban Hamuru'),
            ('VardolaHamur', 'Vardola Hamuru'),
            ('KrepFoderHamur', 'Krep Foder Hamuru'),
            ('GalosYuzHamur', 'Galoş Yüz Hamuru'),
            ('GalosTabanHamur', 'Galoş Taban Hamuru'),
            ('GalosFoderHamur', 'Galoş Foder Hamuru'),
            ('RejenereHamur', 'Rejenere Hamuru'),
            ('KahverengiYuzHamur', 'Kahverengi Yüz Hamuru'),
            ('CelikBurunluTabanHamur', 'Çelik Burunlu Taban Hamuru'),
            ('KobaltElektrikciYuzHamur', 'Kobalt Elektrikçi Yüz Hamuru'),
            ('KobaltElektrikciTabanHamur', 'Kobalt Elektrikçi Taban Hamuru'),
            ('KobaltSiyahYuzHamur', 'Kobalt Siyah Yüz Hamuru'),
            ('KobaltSiyahTabanHamur', 'Kobalt Siyah Taban Hamuru'),
            ('KobaltYesilYuzHamur', 'Kobalt Yeşil Yuz Hamuru'),
            ('KobaltYesilTabanHamur', 'Kobalt Yeşil Taban Hamuru'),
        )
        ),
        ('Yardımcı Malzemeler', (
            ('Kevlar', 'Kevlar'),
            ('Eva', 'Eva'),
            ('KompozitBurun', 'Kompozit Burun'),
            ('CizmeCorabi', 'Çizme Çorabı'),
            ('OverlokIpi', 'Overlok İpi'),
            ('PresKesimTakozu', 'Pres Kesim Takozu'),
            ('AyakkabiTabanKecesi', 'Ayakkabı Taban Keçesi'),
            ('CelikBurun', 'Çelik Burun'),
            ('Fermuar', 'Fermuar'),
            ('MaskelemeBandi', 'Maskeleme Bandı'),
        )
        ),
        ('Bezler', (
            ('GalosKahveTabanAstariBez', 'Galoş Kahve Taban Astarı Bez'),
            ('KrepBeyazBez', 'Krep Beyaz Bez'),
            ('KrepTabanAstariBez', 'Krep Taban Astarı Bez'),
            ('GalosDeveTuyuTabanAstariBez', 'Galoş Deve Tüyü Taban Astarı Bez'),
            ('GalosPembeBez', 'Galoş Pembe Bez'),
            ('GalosFordBezi', 'Galoş Ford Bezi'),
            ('GalosPembeTabanAstariBez', 'Galoş Pembe Taban Astarı Bez'),
            ('KrepAntistatikTabanAstariBez',
             'Krep Antistatik Taban Astarı Bez'),
        )
        ),
        ('Kazan Malzemeleri', (
            ('AntiSkalant', 'Anti Skalant'),
            ('KazanTuzu', 'Kazan Tuzu'),
        )
        ),
    ]

    madde = models.CharField(max_length=64, choices=HAMMADDE_SECENEKLERI)
    miktar = models.IntegerField()
    notlar = models.CharField(max_length=256, blank=True)
    tarih = models.DateTimeField(auto_now_add=True)
    kullanici = models.ForeignKey(User, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        if self.miktar != 0:
            super(HammaddeDegisiklik, self).save(*args, **kwargs)

# Formlar:

# from: https://stackoverflow.com/a/20573612
# apply the 'form-control' css class to all model fields.
class MyModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MyModelForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MyForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class KoliDegisiklikForm(MyModelForm):
    class Meta:
        model = KoliDegisiklik
        exclude = ('kullanici',)
        labels = {
            'koli_turu': 'Numara',
            'mamul_model': 'Model',
            'kolideki_mamul_adet': 'Kolideki Mamül Sayısı',
        }
        widgets = {
            'notlar': forms.Textarea(),
            'koli_turu': forms.TextInput(attrs={
                'pattern': r'^[1-9][0-9]?(?:/[1-9][0-9]?)?$',
            }),
        }


class HammaddeDegisiklikForm(MyModelForm):
    class Meta:
        model = HammaddeDegisiklik
        exclude = ('kullanici',)
        widgets = {
            'notlar': forms.Textarea(),
        }


class KoliRestockForm(MyForm):
    mamul_model = forms.ChoiceField(
        choices=KoliDegisiklik.MAMUL_SECENEKLERI, label='Model')
    kalite = forms.ChoiceField(choices=KoliDegisiklik.KALITE_SECENEKLERI)
    koli_turu = forms.CharField(max_length=8, label='Numara')
    koli_adet = forms.IntegerField(min_value=0)
    kolideki_mamul_adet = forms.IntegerField(
        min_value=0, label='Kolideki Mamül Sayısı')

    mamul_model.widget.attrs.update(
        {'onchange': 'kolidekiMamulSayisiGuncelle(event)'})
    koli_turu.widget.attrs.update(
        {'pattern': r'^[1-9][0-9]?(?:/[1-9][0-9]?)?$'})
    kolideki_mamul_adet.widget.attrs.update(
        {'value': 20})


class HammaddeRestockForm(MyForm):
    madde = forms.ChoiceField(choices=HammaddeDegisiklik.HAMMADDE_SECENEKLERI)
    miktar = forms.IntegerField(min_value=0)


class GunGetirForm(forms.Form):
    gun = forms.DateField()

# Django sinyaller:


@receiver(models.signals.pre_save, sender=KoliDegisiklik)
def create_update_kolisondurum_from_kolidegisiklik(sender, instance, **kwargs):
    """
    Here's the dictionary data blueprint for every KoliSonDurum column:
    (This part is getting trickier and trickier everytime I edit it)
    (This data is now being converted into binary data)

    raw data =
    {
        'kalite': {
            'koli_turu': {
                'kolideki_mamul_adet': 'koli_adet'
            }
        }
    }


    required_dict =
    {
        'koli_turu': {
            'kolideki_mamul_adet': 'koli_adet'
        }
    }


    required_dict_2 =
    {
        'kolideki_mamul_adet': 'koli_adet'
    }
    """
    try:
        selected_record = KoliSonDurum()
        if KoliSonDurum.objects.filter(tarih=timezone.localtime(timezone.now()).date()).exists():
            selected_record = KoliSonDurum.objects.get(
                tarih=timezone.localtime(timezone.now()).date())
        else:
            # raises exception KoliSonDurum.DoesNotExist
            selected_record = KoliSonDurum.objects.latest('tarih')
            # Primary Key değerini sil ki güncelleme yerine yeni kayıt girdisi yapılsın
            selected_record.pk = None
            selected_record.tarih = timezone.now().date()
        if vars(selected_record)[instance.mamul_model] != b'':
            raw_data = pickle.loads(vars(selected_record)[
                                    instance.mamul_model])
            if instance.kalite in raw_data.keys():
                required_dict = raw_data[instance.kalite]
                if instance.koli_turu in required_dict.keys():
                    required_dict_2 = required_dict[instance.koli_turu]
                    if instance.kolideki_mamul_adet in required_dict_2.keys():
                        required_dict_2[instance.kolideki_mamul_adet] += instance.koli_adet
                    else:
                        # Bu kolideki_mamul_adet değerine ait daha önce bir girdi yapılmamış demektir.
                        required_dict_2[instance.kolideki_mamul_adet] = instance.koli_adet
                    # Girilen veriler, stokta negatif malzemenin oluşmasına izin vermemeli.
                    if required_dict_2[instance.kolideki_mamul_adet] < 0:
                        raise IntegrityError
                    # Stok sıfıra indiyse verisi boşa yer kaplamasın, silelim.
                    if required_dict_2[instance.kolideki_mamul_adet] == 0:
                        del required_dict_2[instance.kolideki_mamul_adet]
                    required_dict[instance.koli_turu] = {
                        i: required_dict_2[i] for i in sorted(required_dict_2.keys(), reverse=True)}
                else:
                    # Bu koli türüne ait daha önce bir girdi yapılmamış demektir.
                    # Girilen veriler, stokta negatif malzemenin oluşmasına izin vermemeli.
                    if instance.koli_adet < 0:
                        raise IntegrityError
                    required_dict[instance.koli_turu] = {
                        instance.kolideki_mamul_adet: instance.koli_adet}
                # Koli türüne ait veri kalmadıysa boşa yer kaplamasın, silelim.
                if not required_dict[instance.koli_turu]:
                    del required_dict[instance.koli_turu]
                raw_data[instance.kalite] = {i: required_dict[i] for i in sorted(
                    required_dict.keys(), key=lambda x: sorting_key(x))}
            else:
                # Bu kaliteye ait daha önce bir girdi yapılmamış demektir.
                if instance.koli_adet < 0:
                    raise IntegrityError
                raw_data[instance.kalite] = {instance.koli_turu: {
                    instance.kolideki_mamul_adet: instance.koli_adet}}
            # Kaliteye ait veri kalmadıysa boşa yer kaplamsın silelim.
            if not raw_data[instance.kalite]:
                del raw_data[instance.kalite]
            if raw_data:
                vars(selected_record)[
                    instance.mamul_model] = pickle.dumps(raw_data)
            else:
                vars(selected_record)[instance.mamul_model] = b''
        else:
            # Bu modele ait daha önce bir girdi yapılmamış demektir.
            # Girilen veriler, stokta negatif malzemenin oluşmasına izin vermemeli.
            if instance.koli_adet < 0:
                raise IntegrityError
            vars(selected_record)[instance.mamul_model] = pickle.dumps({instance.kalite: {
                instance.koli_turu: {instance.kolideki_mamul_adet: instance.koli_adet}}})
        selected_record.save()
    except KoliSonDurum.DoesNotExist:
        # Veritabanında hiç koli son durum girdisi yok demektir. Bu kısım, ideal olarak, sadece bir kez çalışacak.
        first_record = KoliSonDurum(
            tarih=timezone.localtime(timezone.now()).date())
        # Girilen veriler, stokta negatif malzemenin oluşmasına izin vermemeli.
        if instance.koli_adet < 0:
            raise IntegrityError
        vars(first_record)[instance.mamul_model] = pickle.dumps({instance.kalite: {
            instance.koli_turu: {instance.kolideki_mamul_adet: instance.koli_adet}}})
        first_record.save()


@receiver(models.signals.pre_save, sender=HammaddeDegisiklik)
def create_update_hammaddesondurum_from_hammaddedegisiklik(sender, instance, **kwargs):
    try:
        # from: https://www.reddit.com/r/django/comments/5skcnf/django_timezone_now_vs_today/ddh3ndg/
        if HammaddeSonDurum.objects.filter(tarih=timezone.localtime(timezone.now()).date()).exists():
            modified_record = HammaddeSonDurum.objects.get(
                tarih=timezone.localtime(timezone.now()).date())
            vars(modified_record)[instance.madde] += instance.miktar
            modified_record.save()
        else:
            new_record = HammaddeSonDurum.objects.latest('tarih')
            # Primary Key değerini sil ki güncelleme yerine yeni kayıt girdisi yapılsın
            new_record.pk = None
            new_record.tarih = timezone.now().date()
            vars(new_record)[instance.madde] += instance.miktar
            new_record.save()
    except HammaddeSonDurum.DoesNotExist:
        # Veritabanında hiç hammadde son durum girdisi yok demektir. Bu kısım, ideal olarak, sadece bir kez çalışacak.
        first_record = HammaddeSonDurum(
            tarih=timezone.localtime(timezone.now()).date())
        vars(first_record)[instance.madde] = instance.miktar
        first_record.save()


@receiver(models.signals.pre_delete, sender=KoliDegisiklik)
def delete_kolisondurum_from_kolidegisiklik(sender, instance, **kwargs):
    if instance == KoliDegisiklik.objects.latest('tarih') and timezone.localtime(instance.tarih).date() == timezone.localtime(timezone.now()).date():
        record = KoliSonDurum.objects.get(
            tarih=timezone.localtime(timezone.now()).date())
        if KoliDegisiklik.objects.filter(tarih__date=timezone.now().date()).count() == 1:
            record.delete()
            return
        raw_data = pickle.loads(vars(record)[instance.mamul_model])
        raw_data[instance.kalite][instance.koli_turu][instance.kolideki_mamul_adet] -= instance.koli_adet
        if raw_data[instance.kalite][instance.koli_turu][instance.kolideki_mamul_adet] == 0:
            del raw_data[instance.kalite][instance.koli_turu][instance.kolideki_mamul_adet]
        if not raw_data[instance.kalite][instance.koli_turu]:
            del raw_data[instance.kalite][instance.koli_turu]
        if not raw_data[instance.kalite]:
            del raw_data[instance.kalite]
        if not raw_data:
            vars(record)[instance.mamul_model] = b''
        else:
            vars(record)[instance.mamul_model] = pickle.dumps(raw_data)
        record.save()
    else:
        raise IntegrityError(
            'You can\'t delete a KoliDegisiklik object from another day, nor other than the latest record.')


@receiver(models.signals.pre_delete, sender=HammaddeDegisiklik)
def delete_hammaddesondurum_from_hammaddedegisiklik(sender, instance, **kwargs):
    if timezone.localtime(instance.tarih).date() == timezone.localtime(timezone.now()).date():
        record = HammaddeSonDurum.objects.get(
            tarih=timezone.localtime(timezone.now()).date())
        if HammaddeDegisiklik.objects.filter(tarih__date=timezone.now().date()).count() == 1:
            record.delete()
            return
        vars(record)[instance.madde] -= instance.miktar
        record.save()
    else:
        raise IntegrityError(
            'You can\'t delete a HammaddeDegisiklik object from another day.')
