from random import randint, choice

from django.test import TestCase
from django.contrib.auth.models import User

from .models import HammaddeSonDurum, HammaddeDegisiklik

# Create your tests here.

class DatabaseIntegrityCheck(TestCase):
    def setUp(self):
        HAMMADDELER = [
            'AmonyumBikarbonat',
            'BoyaSokucuSolvent',
            'CigBezirYagi',
            'CinkoStarat',
            'DPG',
            'Hexa80',
            'Merkapto',
            'Mikrotem',
            'NeozaponBlack',
            'NigroSine',
            'SentetikDemiroksitBoya',
            'SodyumHidroksit',
            'TitanDioksit',
            'Toluol',
            'ZMBT',
            'CamTozu',
            'EtilGlikol',
            'GrafikTozu',
            'KalafonRecine',
            'Kukurt',
            'TriklorEtilen',
            'DM',
            'Derkompleks',
            'Heptan',
            'PismisBezirYagi',
            'PVI',
            'SulegenBoya',
            'Whitesprit',
            'AgizBandi',
            'BaskisizKoli',
            'DerbyCelikBurunluCizmeKutusu',
            'DerbyFiletBezliKolisi',
            'DerbyMerdaneBezliKolisi',
            'DerbyMerdaneFanilaliKolisi',
            'GislavedMerdaneIskarpinKolisi',
            'GislavedZenneIskarpinKolisi',
            'HutbakKagidi',
            'KeseKagidi',
            'KobaltElektrikciKaucukCizmeKolisi',
            'KobaltKaucukCizmeKolisi',
            'KrepCizmeUzunKoncKolisi',
            'PlastikCember',
            'DerbyBotKolisi',
            'DerbyKrepKaucukCizmeKolisi',
            'DerbyZenneBezliKolisi',
            'KobaltKaucukDayanikliCizmeKutusu',
            'KoliBandi',
            'KrepBotKolisi',
            'NaylonTorbaBot',
            'DerbyBotKutusu',
            'DerbyKrepKaucukCizmeKutusu',
            'KobaltKaucukElektrikciCizmeKutusu',
            'KobaltCizmeEtiketi',
            'KrepCizmeKisaKoncKolisi',
            'NaylonTorbaCizme',
            'KrepYuzHamur',
            'KrepTabanHamur',
            'VardolaHamur',
            'KrepFoderHamur',
            'GalosYuzHamur',
            'GalosTabanHamur',
            'GalosFoderHamur',
            'RejenereHamur',
            'KahverengiYuzHamur',
            'CelikBurunluTabanHamur',
            'KobaltElektrikciYuzHamur',
            'KobaltElektrikciTabanHamur',
            'KobaltSiyahYuzHamur',
            'KobaltSiyahTabanHamur',
            'KobaltYesilYuzHamur',
            'KobaltYesilTabanHamur',
            'Kevlar',
            'Eva',
            'KompozitBurun',
            'CizmeCorabi',
            'OverlokIpi',
            'PresKesimTakozu',
            'AyakkabiTabanKecesi',
            'CelikBurun',
            'Fermuar',
            'MaskelemeBandi',
            'GalosKahveTabanAstariBez',
            'KrepBeyazBez',
            'KrepTabanAstariBez',
            'GalosDeveTuyuTabanAstariBez',
            'GalosPembeBez',
            'GalosFordBezi',
            'GalosPembeTabanAstariBez',
            'KrepAntistatikTabanAstariBez',
            'AntiSkalant',
            'KazanTuzu'
        ]
        User.objects.create(username='testuser', password='pass')
        for _ in range(500):
            HammaddeDegisiklik.objects.create(madde=choice(HAMMADDELER), miktar=randint(10,200), kullanici_id=1)
    
    def test_hammaddesondurum_is_in_sync_with_hammaddedegisiklik(self):
        """
        HammaddeSonDurum tablosu, HammaddeDegisiklik tablosunda
        yapılan değişikliklere göre güncelleniyor. Bu iki tablo
        arasında sürekli bir senkronizasyon olmalı. Bu test,
        senkronizasyonu kontrol etmek için yazıldı.
        """
        hsd_latest = HammaddeSonDurum.objects.latest('tarih')
        hd_all = HammaddeDegisiklik.objects.all()
        disposable_dict = {}
        
        for i in hd_all:
            try:
                disposable_dict[i.madde] += i.miktar
            except KeyError:
                disposable_dict[i.madde] = i.miktar
        
        for i in disposable_dict:
            self.assertEqual(disposable_dict[i], vars(hsd_latest)[i])
