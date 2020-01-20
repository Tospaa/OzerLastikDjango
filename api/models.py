from django import forms
from django.contrib.auth.models import User
from django.db import models

# Mamuller:

class KrepCizme(models.Model):
    Numara = models.IntegerField()
    Adet = models.IntegerField()
    """
        Krep kısa konç
        krep uzun konç
        krep garson kısa
        krep garson uzun
        krep kahve bot
        krep siyah bot
        krep çelik burunlu çizme
        kasık çizme
    """

    def __str___(self):
        return "{0} numara ayakkabı".format(self.Numara)

    def __repr___(self):
        return "{0} numara ayakkabı repr".format(self.Numara)

class GalosAyakkabi(models.Model):
    Numara = models.IntegerField()
    Adet = models.IntegerField()
    """
        Filet bezli
        zenne bezli
        merdane bezli
        merdane fanilalı
        zenne iskarpin
        merdane iskarpin
        garson iskarpin
    """

class KobaltCizme(models.Model):
    Numara = models.IntegerField()
    Adet = models.IntegerField()
    """
        pres çizme ob
        pres çizme s4
        pres çizme s5
        elektrikçi ob
        elektrikçi s4
        elektrikçi s5
    """

# Hammaddeler:

class HammaddeSonDurum(models.Model):
    tarih = models.DateField(unique=True)
    AgizBandi = models.PositiveIntegerField()
    AmonyumBikarbonat = models.PositiveIntegerField()
    BaskisizKoli = models.PositiveIntegerField()
    BoyaSokucuSolvent = models.PositiveIntegerField()
    CigBezirYagi = models.PositiveIntegerField()
    CinkoStarat = models.PositiveIntegerField()
    DPG = models.PositiveIntegerField()
    DerbyCelikBurunluCizmeKutusu = models.PositiveIntegerField()
    DerbyFiletBezliKolisi = models.PositiveIntegerField()
    DerbyMerdaneBezliKolisi = models.PositiveIntegerField()
    DerbyMerdaneFanilaliKolisi = models.PositiveIntegerField()
    Dogalgaz = models.PositiveIntegerField()
    Elektrik = models.PositiveIntegerField()
    GalosKahveTabanAstariBez = models.PositiveIntegerField()
    GislavedMerdaneIskarpinKolisi = models.PositiveIntegerField()
    GislavedZenneIskarpinKolisi = models.PositiveIntegerField()
    Hexa80 = models.PositiveIntegerField()
    HutbakKagidi = models.PositiveIntegerField()
    KeseKagidi = models.PositiveIntegerField()
    Kevlar = models.PositiveIntegerField()
    KobaltElektrikciKaucukCizmeKolisi = models.PositiveIntegerField()
    KobaltKaucukCizmeKolisi = models.PositiveIntegerField()
    KrepBeyazBez = models.PositiveIntegerField()
    Eva = models.PositiveIntegerField()
    KrepCizmeUzunKoncKolisi = models.PositiveIntegerField()
    KrepTabanAstariBez = models.PositiveIntegerField()
    Merkapto = models.PositiveIntegerField()
    Mikrotem = models.PositiveIntegerField()
    NeozaponBlack = models.PositiveIntegerField()
    NigroSine = models.PositiveIntegerField()
    KompozitBurun = models.PositiveIntegerField()
    PlastikCember = models.PositiveIntegerField()
    SentetikDemiroksitBoya = models.PositiveIntegerField()
    SodyumHidroksit = models.PositiveIntegerField()
    TitanDioksit = models.PositiveIntegerField()
    Toluol = models.PositiveIntegerField()
    ZMBT = models.PositiveIntegerField()
    AntiSkalant = models.PositiveIntegerField()
    CamTozu = models.PositiveIntegerField()
    CizmeCorabi = models.PositiveIntegerField()
    DerbyBotKolisi = models.PositiveIntegerField()
    DerbyKrepKaucukCizmeKolisi = models.PositiveIntegerField()
    DerbyZenneBezliKolisi = models.PositiveIntegerField()
    EtilGlikol = models.PositiveIntegerField()
    GalosDeveTuyuTabanAstariBez = models.PositiveIntegerField()
    GalosPembeBez = models.PositiveIntegerField()
    GrafikTozu = models.PositiveIntegerField()
    KalafonRecine = models.PositiveIntegerField()
    KobaltKaucukDayanikliCizmeKutusu = models.PositiveIntegerField()
    KoliBandi = models.PositiveIntegerField()
    KrepBotKolisi = models.PositiveIntegerField()
    Kukurt = models.PositiveIntegerField()
    NaylonTorbaBot = models.PositiveIntegerField()
    OverlokIpi = models.PositiveIntegerField()
    PresKesimTakozu = models.PositiveIntegerField()
    Su = models.PositiveIntegerField()
    TriklorEtilen = models.PositiveIntegerField()
    AyakkabiTabanKecesi = models.PositiveIntegerField()
    CelikBurun = models.PositiveIntegerField()
    DM = models.PositiveIntegerField()
    DerbyBotKutusu = models.PositiveIntegerField()
    DerbyKrepKaucukCizmeKutusu = models.PositiveIntegerField()
    Derkompleks = models.PositiveIntegerField()
    Fermuar = models.PositiveIntegerField()
    GalosFordBezi = models.PositiveIntegerField()
    Heptan = models.PositiveIntegerField()
    KazanTuzu = models.PositiveIntegerField()
    GalosPembeTabanAstariBez = models.PositiveIntegerField()
    KobaltCizmeEtiketi = models.PositiveIntegerField()
    KobaltKaucukElektrikciCizmeKutusu = models.PositiveIntegerField()
    KrepAntistatikTabanAstariBez = models.PositiveIntegerField()
    KrepCizmeKisaKoncKolisi = models.PositiveIntegerField()
    MaskelemeBandi = models.PositiveIntegerField()
    NaylonTorbaCizme = models.PositiveIntegerField()
    PismisBezirYagi = models.PositiveIntegerField()
    PVI = models.PositiveIntegerField()
    SulegenBoya = models.PositiveIntegerField()
    Whitesprit = models.PositiveIntegerField()
    KrepYuzHamur = models.PositiveIntegerField()
    KrepTabanHamur = models.PositiveIntegerField()
    VardolaHamur = models.PositiveIntegerField()
    KrepFoderHamur = models.PositiveIntegerField()
    GalosYuzHamur = models.PositiveIntegerField()
    GalosTabanHamur = models.PositiveIntegerField()
    GalosFoderHamur = models.PositiveIntegerField()
    RejenereHamur = models.PositiveIntegerField()
    KahverengiYuzHamur = models.PositiveIntegerField()
    CelikBurunluTabanHamur = models.PositiveIntegerField()
    KobaltElektrikciYuzHamur = models.PositiveIntegerField()
    KobaltElektrikciTabanHamur = models.PositiveIntegerField()
    KobaltSiyahYuzHamur = models.PositiveIntegerField()
    KobaltSiyahTabanHamur = models.PositiveIntegerField()
    KobaltYesilYuzHamur = models.PositiveIntegerField()
    KobaltYesilTabanHamur = models.PositiveIntegerField()

class HammaddeDegisiklik(models.Model):
    HAMMADDE_SECENEKLERI = [
        ('AgizBandi', 'Ağız Bandı'),
        ('AmonyumBikarbonat', 'Amonyum Bikarbonat'),
        ('BaskisizKoli', 'Baskısız Koli'),
        ('BoyaSokucuSolvent', 'Boya Sökücü Solvent'),
        ('CigBezirYagi', 'Çiğ Bezir Yağı'),
        ('CinkoStarat', 'Çinko Starat'),
        ('DPG', 'DPG'),
        ('DerbyCelikBurunluCizmeKutusu', 'Derby Çelik Burunlu Çizme Kutusu'),
        ('DerbyFiletBezliKolisi', 'Derby Filet Bezli Kolisi'),
        ('DerbyMerdaneBezliKolisi', 'Derby Merdane Bezli Kolisi'),
        ('DerbyMerdaneFanilaliKolisi', 'Derby Merdane Fanilalı Kolisi'),
        ('Dogalgaz', 'Doğalgaz'),
        ('Elektrik', 'Elektrik'),
        ('GalosKahveTabanAstariBez', 'Galoş Kahve Taban Astarı Bez'),
        ('GislavedMerdaneIskarpinKolisi', 'Gislaved Merdane İskarpin Kolisi'),
        ('GislavedZenneIskarpinKolisi', 'Gislaved Zenne İskarpin Kolisi'),
        ('Hexa80', 'Hexa80'),
        ('HutbakKagidi', 'Hutbak Kağıdı'),
        ('KeseKagidi', 'Kese Kağıdı'),
        ('Kevlar', 'Kevlar'),
        ('KobaltElektrikciKaucukCizmeKolisi', 'Kobalt Elektrikçi Kauçuk Çizme Kolisi'),
        ('KobaltKaucukCizmeKolisi', 'Kobalt Kauçuk Çizme Kolisi'),
        ('KrepBeyazBez', 'Krep Beyaz Bez'),
        ('Eva', 'Eva'),
        ('KrepCizmeUzunKoncKolisi', 'Krep Çizme Uzun Konç Kolisi'),
        ('KrepTabanAstariBez', 'Krep Taban Astarı Bez'),
        ('Merkapto', 'Merkapto'),
        ('Mikrotem', 'Mikrotem'),
        ('NeozaponBlack', 'Neozapon Black'),
        ('NigroSine', 'Nigro Sine'),
        ('KompozitBurun', 'Kompozit Burun'),
        ('PlastikCember', 'Plastik Çember'),
        ('SentetikDemiroksitBoya', 'Sentetik Demiroksit Boya'),
        ('SodyumHidroksit', 'Sodyum Hidroksit'),
        ('TitanDioksit', 'Titan Dioksit'),
        ('Toluol', 'Toluol'),
        ('ZMBT', 'ZMBT'),
        ('AntiSkalant', 'Anti Skalant'),
        ('CamTozu', 'Cam Tozu'),
        ('CizmeCorabi', 'Çizme Çorabı'),
        ('DerbyBotKolisi', 'Derby Bot Kolisi'),
        ('DerbyKrepKaucukCizmeKolisi', 'Derby Krep Kauçuk Çizme Kolisi'),
        ('DerbyZenneBezliKolisi', 'Derby Zenne Bezli Kolisi'),
        ('EtilGlikol', 'Etil Glikol'),
        ('GalosDeveTuyuTabanAstariBez', 'Galoş Deve Tüyü Taban Astarı Bez'),
        ('GalosPembeBez', 'Galoş Pembe Bez'),
        ('GrafikTozu', 'Grafik Tozu'),
        ('KalafonRecine', 'Kalafon Reçine'),
        ('KobaltKaucukDayanikliCizmeKutusu', 'Kobalt Kauçuk Dayanıklı Çizme Kutusu'),
        ('KoliBandi', 'Koli Bandı'),
        ('KrepBotKolisi', 'Krep Bot Kolisi'),
        ('Kukurt', 'Kükürt'),
        ('NaylonTorbaBot', 'Naylon Torba Bot'),
        ('OverlokIpi', 'Overlok İpi'),
        ('PresKesimTakozu', 'Pres Kesim Takozu'),
        ('Su', 'Su'),
        ('TriklorEtilen', 'Triklor Etilen'),
        ('AyakkabiTabanKecesi', 'Ayakkabı Taban Keçesi'),
        ('CelikBurun', 'Çelik Burun'),
        ('DM', 'DM'),
        ('DerbyBotKutusu', 'Derby Bot Kutusu'),
        ('DerbyKrepKaucukCizmeKutusu', 'Derby Krep Kauçuk Çizme Kutusu'),
        ('Derkompleks', 'Derkompleks'),
        ('Fermuar', 'Fermuar'),
        ('GalosFordBezi', 'Galoş Ford Bezi'),
        ('Heptan', 'Heptan'),
        ('KazanTuzu', 'Kazan Tuzu'),
        ('GalosPembeTabanAstariBez', 'Galoş Pembe Taban Astarı Bez'),
        ('KobaltCizmeEtiketi', 'Kobalt Çizme Etiketi'),
        ('KobaltKaucukElektrikciCizmeKutusu', 'Kobalt Kauçuk Elektrikçi Çizme Kutusu'),
        ('KrepAntistatikTabanAstariBez', 'Krep Antistatik Taban Astarı Bez'),
        ('KrepCizmeKisaKoncKolisi', 'Krep Çizme Kısa Konç Kolisi'),
        ('MaskelemeBandi', 'Maskeleme Bandı'),
        ('NaylonTorbaCizme', 'Naylon Torba Çizme'),
        ('PismisBezirYagi', 'Pişmiş Bezir Yağı'),
        ('PVI', 'PVI'),
        ('SulegenBoya', 'Sulegen Boya'),
        ('Whitesprit', 'Whitesprit'),
        ('Hamur', (
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
    ]
    
    madde = models.CharField(max_length=64, choices=HAMMADDE_SECENEKLERI, default='AgizBandi')
    miktar = models.IntegerField()
    notlar = models.CharField(max_length=256)
    tarih = models.DateTimeField(auto_now_add=True)
    kullanici = models.ForeignKey(User, on_delete=models.PROTECT)

# Formlar:

# from: https://stackoverflow.com/a/20573612
# apply the 'form-control' css class to all model fields.
class MyModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MyModelForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class HammaddeDegisiklikForm(MyModelForm):
    notlar = forms.CharField(required=False, widget=forms.Textarea)
    
    class Meta:
        model = HammaddeDegisiklik
        exclude=('kullanici',)

# Django sinyaller:

