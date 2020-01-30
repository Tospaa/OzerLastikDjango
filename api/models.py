from django import forms
from django.contrib.auth.models import User
from django.db import models, IntegrityError
from django.dispatch import receiver
from django.utils import timezone
import json

# Mamuller:

class MamulSonDurum(models.Model):
    tarih = models.DateField(unique=True)
    KrepKisaKonc = models.TextField(blank=True)
    KrepUzunKonc = models.TextField(blank=True)
    KrepGarsonKisa = models.TextField(blank=True)
    KrepGarsonUzun = models.TextField(blank=True)
    KrepKahveBot = models.TextField(blank=True)
    KrepSiyahBot = models.TextField(blank=True)
    KrepCelikBurunluCizme = models.TextField(blank=True)
    KasikCizme = models.TextField(blank=True)
    FiletBezli = models.TextField(blank=True)
    ZenneBezli = models.TextField(blank=True)
    MerdaneBezli = models.TextField(blank=True)
    MerdaneFanilali = models.TextField(blank=True)
    ZenneIskarpin = models.TextField(blank=True)
    MerdaneIskarpin = models.TextField(blank=True)
    GarsonIskarpin = models.TextField(blank=True)
    PresCizmeOB = models.TextField(blank=True)
    PresCizmeS4 = models.TextField(blank=True)
    PresCizmeS5 = models.TextField(blank=True)
    ElektrikciOB = models.TextField(blank=True)
    ElektrikciS4 = models.TextField(blank=True)
    ElektrikciS5 = models.TextField(blank=True)

class MamulDegisiklik(models.Model):
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
    
    NUMARA_SECENEKLERI = [
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
        ('21', '21'),
        ('22', '22'),
        ('23', '23'),
        ('24', '24'),
        ('25', '25'),
        ('26', '26'),
        ('27', '27'),
        ('28', '28'),
        ('29', '29'),
        ('30', '30'),
        ('31', '31'),
        ('32', '32'),
        ('33', '33'),
        ('34', '34'),
        ('35', '35'),
        ('36', '36'),
        ('37', '37'),
        ('38', '38'),
        ('39', '39'),
        ('40', '40'),
        ('41', '41'),
        ('42', '42'),
        ('43', '43'),
        ('44', '44'),
        ('45', '45'),
        ('46', '46'),
        ('47', '47'),
        ('48', '48'),
        ('49', '49'),
        ('50', '50')
    ]
    
    mamul_model = models.CharField(max_length=32, choices=MAMUL_SECENEKLERI)
    numara = models.CharField(max_length=2, choices=NUMARA_SECENEKLERI)
    adet = models.IntegerField()
    notlar = models.CharField(max_length=256, blank=True)
    tarih = models.DateTimeField(auto_now_add=True)
    kullanici = models.ForeignKey(User, on_delete=models.PROTECT)

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
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class MamulDegisiklikForm(MyModelForm):
    notlar = forms.CharField(widget=forms.Textarea, required=False)
    
    class Meta:
        model = MamulDegisiklik
        exclude=('kullanici',)
        labels = {
            'mamul_model': 'Model',
            'adet': 'Çift adedi'
        }

class HammaddeDegisiklikForm(MyModelForm):
    notlar = forms.CharField(widget=forms.Textarea, required=False)
    
    class Meta:
        model = HammaddeDegisiklik
        exclude=('kullanici',)

# Django sinyaller:

@receiver(models.signals.pre_save, sender=MamulDegisiklik)
def create_update_mamulsondurum_from_mamuldegisiklik(sender, instance, **kwargs):
    try:
        if MamulSonDurum.objects.filter(tarih=timezone.localtime(timezone.now()).date()).exists():
            modified_record = MamulSonDurum.objects.get(tarih=timezone.localtime(timezone.now()).date())
            try:
                required_dict = json.loads(vars(modified_record)[instance.mamul_model])
                try:
                    required_dict[instance.numara] += instance.adet
                except KeyError:
                    required_dict[instance.numara] = instance.adet
                if required_dict[instance.numara] < 0:  # Girilen veriler, stokta negatif malzemenin oluşmasına izin vermemeli.
                    raise IntegrityError
                if required_dict[instance.numara] == 0:
                    del required_dict[instance.numara]
                vars(modified_record)[instance.mamul_model] = json.dumps({i:required_dict[i] for i in sorted(required_dict.keys(), key=lambda x: int(x))})  # Should this be here or on views???
                modified_record.save()
            except json.decoder.JSONDecodeError:
                if instance.adet <= 0:  # Girilen veriler, stokta negatif malzemenin oluşmasına izin vermemeli.
                    raise IntegrityError
                vars(modified_record)[instance.mamul_model] = json.dumps({instance.numara: instance.adet})
                modified_record.save()
        else:
            new_record = MamulSonDurum.objects.latest('tarih')
            # Primary Key değerini sil ki güncelleme yerine yeni kayıt girdisi yapılsın
            new_record.pk = None
            new_record.tarih = timezone.now().date()
            try:
                required_dict = dict(json.loads(vars(new_record)[instance.mamul_model]))
                try:
                    required_dict[instance.numara] += instance.adet
                except KeyError:
                    required_dict[instance.numara] = instance.adet
                if required_dict[instance.numara] < 0:  # Girilen veriler, stokta negatif malzemenin oluşmasına izin vermemeli.
                    raise IntegrityError
                if required_dict[instance.numara] == 0:
                    del required_dict[instance.numara]
                vars(new_record)[instance.mamul_model] = json.dumps({i:required_dict[i] for i in sorted(required_dict.keys(), key=lambda x: int(x))})  # Should this be here or on views???
                new_record.save()
            except json.decoder.JSONDecodeError:
                if instance.adet <= 0:  # Girilen veriler, stokta negatif malzemenin oluşmasına izin vermemeli.
                    raise IntegrityError
                vars(new_record)[instance.mamul_model] = json.dumps({instance.numara: instance.adet})
                new_record.save()
    except MamulSonDurum.DoesNotExist:
        # Veritabanında hiç mamul son durum girdisi yok demektir.
        first_record = MamulSonDurum(tarih=timezone.now().date())
        if instance.adet <= 0:  # Girilen veriler, stokta negatif malzemenin oluşmasına izin vermemeli.
            raise IntegrityError
        vars(first_record)[instance.mamul_model] = json.dumps({instance.numara: instance.adet})
        first_record.save()

@receiver(models.signals.pre_save, sender=HammaddeDegisiklik)
def create_update_hammaddesondurum_from_hammaddedegisiklik(sender, instance, **kwargs):
    try:
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
    except HammaddeSonDurum.DoesNotExist:
        # Veritabanında hiç hammadde son durum girdisi yok demektir.
        first_record = HammaddeSonDurum(tarih=timezone.now().date())
        vars(first_record)[instance.madde] = instance.miktar
        first_record.save()
