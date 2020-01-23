from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.utils import timezone

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
    AmonyumBikarbonat = models.PositiveIntegerField()
    BoyaSokucuSolvent = models.PositiveIntegerField()
    CigBezirYagi = models.PositiveIntegerField()
    CinkoStarat = models.PositiveIntegerField()
    DPG = models.PositiveIntegerField()
    Hexa80 = models.PositiveIntegerField()
    Merkapto = models.PositiveIntegerField()
    Mikrotem = models.PositiveIntegerField()
    NeozaponBlack = models.PositiveIntegerField()
    NigroSine = models.PositiveIntegerField()
    SentetikDemiroksitBoya = models.PositiveIntegerField()
    SodyumHidroksit = models.PositiveIntegerField()
    TitanDioksit = models.PositiveIntegerField()
    Toluol = models.PositiveIntegerField()
    ZMBT = models.PositiveIntegerField()
    CamTozu = models.PositiveIntegerField()
    EtilGlikol = models.PositiveIntegerField()
    GrafikTozu = models.PositiveIntegerField()
    KalafonRecine = models.PositiveIntegerField()
    Kukurt = models.PositiveIntegerField()
    TriklorEtilen = models.PositiveIntegerField()
    DM = models.PositiveIntegerField()
    Derkompleks = models.PositiveIntegerField()
    Heptan = models.PositiveIntegerField()
    PismisBezirYagi = models.PositiveIntegerField()
    PVI = models.PositiveIntegerField()
    SulegenBoya = models.PositiveIntegerField()
    Whitesprit = models.PositiveIntegerField()
    AgizBandi = models.PositiveIntegerField()
    BaskisizKoli = models.PositiveIntegerField()
    DerbyCelikBurunluCizmeKutusu = models.PositiveIntegerField()
    DerbyFiletBezliKolisi = models.PositiveIntegerField()
    DerbyMerdaneBezliKolisi = models.PositiveIntegerField()
    DerbyMerdaneFanilaliKolisi = models.PositiveIntegerField()
    GislavedMerdaneIskarpinKolisi = models.PositiveIntegerField()
    GislavedZenneIskarpinKolisi = models.PositiveIntegerField()
    HutbakKagidi = models.PositiveIntegerField()
    KeseKagidi = models.PositiveIntegerField()
    KobaltElektrikciKaucukCizmeKolisi = models.PositiveIntegerField()
    KobaltKaucukCizmeKolisi = models.PositiveIntegerField()
    KrepCizmeUzunKoncKolisi = models.PositiveIntegerField()
    PlastikCember = models.PositiveIntegerField()
    DerbyBotKolisi = models.PositiveIntegerField()
    DerbyKrepKaucukCizmeKolisi = models.PositiveIntegerField()
    DerbyZenneBezliKolisi = models.PositiveIntegerField()
    KobaltKaucukDayanikliCizmeKutusu = models.PositiveIntegerField()
    KoliBandi = models.PositiveIntegerField()
    KrepBotKolisi = models.PositiveIntegerField()
    NaylonTorbaBot = models.PositiveIntegerField()
    DerbyBotKutusu = models.PositiveIntegerField()
    DerbyKrepKaucukCizmeKutusu = models.PositiveIntegerField()
    KobaltKaucukElektrikciCizmeKutusu = models.PositiveIntegerField()
    KobaltCizmeEtiketi = models.PositiveIntegerField()
    KrepCizmeKisaKoncKolisi = models.PositiveIntegerField()
    NaylonTorbaCizme = models.PositiveIntegerField()
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
    Kevlar = models.PositiveIntegerField()
    Eva = models.PositiveIntegerField()
    KompozitBurun = models.PositiveIntegerField()
    CizmeCorabi = models.PositiveIntegerField()
    OverlokIpi = models.PositiveIntegerField()
    PresKesimTakozu = models.PositiveIntegerField()
    AyakkabiTabanKecesi = models.PositiveIntegerField()
    CelikBurun = models.PositiveIntegerField()
    Fermuar = models.PositiveIntegerField()
    MaskelemeBandi = models.PositiveIntegerField()
    GalosKahveTabanAstariBez = models.PositiveIntegerField()
    KrepBeyazBez = models.PositiveIntegerField()
    KrepTabanAstariBez = models.PositiveIntegerField()
    GalosDeveTuyuTabanAstariBez = models.PositiveIntegerField()
    GalosPembeBez = models.PositiveIntegerField()
    GalosFordBezi = models.PositiveIntegerField()
    GalosPembeTabanAstariBez = models.PositiveIntegerField()
    KrepAntistatikTabanAstariBez = models.PositiveIntegerField()
    AntiSkalant = models.PositiveIntegerField()
    KazanTuzu = models.PositiveIntegerField()

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
                ('DerbyCelikBurunluCizmeKutusu', 'Derby Çelik Burunlu Çizme Kutusu'),
                ('DerbyFiletBezliKolisi', 'Derby Filet Bezli Kolisi'),
                ('DerbyMerdaneBezliKolisi', 'Derby Merdane Bezli Kolisi'),
                ('DerbyMerdaneFanilaliKolisi', 'Derby Merdane Fanilalı Kolisi'),
                ('GislavedMerdaneIskarpinKolisi', 'Gislaved Merdane İskarpin Kolisi'),
                ('GislavedZenneIskarpinKolisi', 'Gislaved Zenne İskarpin Kolisi'),
                ('HutbakKagidi', 'Hutbak Kağıdı'),
                ('KeseKagidi', 'Kese Kağıdı'),
                ('KobaltElektrikciKaucukCizmeKolisi', 'Kobalt Elektrikçi Kauçuk Çizme Kolisi'),
                ('KobaltKaucukCizmeKolisi', 'Kobalt Kauçuk Çizme Kolisi'),
                ('KrepCizmeUzunKoncKolisi', 'Krep Çizme Uzun Konç Kolisi'),
                ('PlastikCember', 'Plastik Çember'),
                ('DerbyBotKolisi', 'Derby Bot Kolisi'),
                ('DerbyKrepKaucukCizmeKolisi', 'Derby Krep Kauçuk Çizme Kolisi'),
                ('DerbyZenneBezliKolisi', 'Derby Zenne Bezli Kolisi'),
                ('KobaltKaucukDayanikliCizmeKutusu', 'Kobalt Kauçuk Dayanıklı Çizme Kutusu'),
                ('KoliBandi', 'Koli Bandı'),
                ('KrepBotKolisi', 'Krep Bot Kolisi'),
                ('NaylonTorbaBot', 'Naylon Torba Bot'),
                ('DerbyBotKutusu', 'Derby Bot Kutusu'),
                ('DerbyKrepKaucukCizmeKutusu', 'Derby Krep Kauçuk Çizme Kutusu'),
                ('KobaltKaucukElektrikciCizmeKutusu', 'Kobalt Kauçuk Elektrikçi Çizme Kutusu'),
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
        ('Bilinmeyen', (
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
                ('KrepAntistatikTabanAstariBez', 'Krep Antistatik Taban Astarı Bez'),
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

# Formlar:

# from: https://stackoverflow.com/a/20573612
# apply the 'form-control' css class to all model fields.
class MyModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MyModelForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class HammaddeDegisiklikForm(MyModelForm):
    notlar = forms.CharField(widget=forms.Textarea, required=False)
    
    class Meta:
        model = HammaddeDegisiklik
        exclude=('kullanici',)

# Django sinyaller:

@receiver(models.signals.post_save, sender=HammaddeDegisiklik)
def create_hammaddedegisiklik_hammaddesondurum(sender, instance, created, **kwargs):
    if created:
        # from: https://www.reddit.com/r/django/comments/5skcnf/django_timezone_now_vs_today/ddh3ndg/
        if HammaddeSonDurum.objects.filter(tarih=timezone.localtime(timezone.now()).date()).exists():
            modified_record = HammaddeSonDurum.objects.get(tarih=timezone.localtime(timezone.now()).date())
            vars(modified_record)[instance.madde] += instance.miktar
            modified_record.save()
        else:
            new_record = HammaddeSonDurum.objects.latest('tarih')
            # Primary Key değerini sil ki güncelleme yerine yeni kayıt girdisi yapılsın
            new_record.pk = None
            new_record.tarih = timezone.now().date()
            vars(new_record)[instance.madde] += instance.miktar
            new_record.save()
