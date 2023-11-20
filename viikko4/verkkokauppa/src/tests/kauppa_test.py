import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_arvoilla(self):
        self.viitegeneraattori_mock.uusi.return_value = 42
        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)


    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_arvoilla_2_tuotetta(self):
        self.viitegeneraattori_mock.uusi.return_value = 42
        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 5

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "leipä", 7)

            # otetaan toteutukset käyttöön
            self.varasto_mock.saldo.side_effect = varasto_saldo
            self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

            # alustetaan kauppa
            kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

            # tehdään ostokset
            kauppa.aloita_asiointi()
            kauppa.lisaa_koriin(1)
            kauppa.lisaa_koriin(2)
            kauppa.tilimaksu("pekka", "12345")

            # varmistetaan, että metodia tilisiirto on kutsuttu
            self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 12)

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_arvoilla_2_samaa_tuotetta(self):
            self.viitegeneraattori_mock.uusi.return_value = 42
            # tehdään toteutus saldo-metodille
            def varasto_saldo(tuote_id):
                if tuote_id == 1:
                    return 10

            # tehdään toteutus hae_tuote-metodille
            def varasto_hae_tuote(tuote_id):
                if tuote_id == 1:
                    return Tuote(1, "maito", 5)

            # otetaan toteutukset käyttöön
            self.varasto_mock.saldo.side_effect = varasto_saldo
            self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

            # alustetaan kauppa
            kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

            # tehdään ostokset
            kauppa.aloita_asiointi()
            kauppa.lisaa_koriin(1)
            kauppa.lisaa_koriin(1)
            kauppa.tilimaksu("pekka", "12345")

            # varmistetaan, että metodia tilisiirto on kutsuttu
            self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 10)

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_arvoilla_toinen_tuote_loppu(self):
            self.viitegeneraattori_mock.uusi.return_value = 42
            # tehdään toteutus saldo-metodille
            def varasto_saldo(tuote_id):
                if tuote_id == 1:
                    return 10
                if tuote_id == 2:
                    return 0


            # tehdään toteutus hae_tuote-metodille
            def varasto_hae_tuote(tuote_id):
                if tuote_id == 1:
                    return Tuote(1, "maito", 5)
                if tuote_id == 2:
                    return Tuote(2, "leipä", 7)

            # otetaan toteutukset käyttöön
            self.varasto_mock.saldo.side_effect = varasto_saldo
            self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

            # alustetaan kauppa
            kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

            # tehdään ostokset
            kauppa.aloita_asiointi()
            kauppa.lisaa_koriin(1)
            kauppa.lisaa_koriin(2)
            kauppa.tilimaksu("pekka", "12345")

            # varmistetaan, että metodia tilisiirto on kutsuttu
            self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_aloita_asiointi_toimii(self):
                self.viitegeneraattori_mock.uusi.return_value = 42
                # tehdään toteutus saldo-metodille
                def varasto_saldo(tuote_id):
                    if tuote_id == 1:
                        return 10
                    if tuote_id == 2:
                        return 5


                # tehdään toteutus hae_tuote-metodille
                def varasto_hae_tuote(tuote_id):
                    if tuote_id == 1:
                        return Tuote(1, "maito", 5)
                    if tuote_id == 2:
                        return Tuote(2, "leipä", 7)

                # otetaan toteutukset käyttöön
                self.varasto_mock.saldo.side_effect = varasto_saldo
                self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

                # alustetaan kauppa
                kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

                # tehdään ostokset
                kauppa.aloita_asiointi()
                kauppa.lisaa_koriin(1)
                self.viitegeneraattori_mock.uusi.return_value = 25
                kauppa.aloita_asiointi()
                kauppa.lisaa_koriin(2)
                kauppa.tilimaksu("pekka", "12345")

                # varmistetaan, että metodia tilisiirto on kutsuttu
                self.pankki_mock.tilisiirto.assert_called_with("pekka", 25, "12345", "33333-44455", 7)

    def test_poista_tuote_korista(self):
                self.viitegeneraattori_mock.uusi.return_value = 42
                # tehdään toteutus saldo-metodille
                def varasto_saldo(tuote_id):
                    if tuote_id == 1:
                        return 10
                    if tuote_id == 2:
                        return 5


                # tehdään toteutus hae_tuote-metodille
                def varasto_hae_tuote(tuote_id):
                    if tuote_id == 1:
                        return Tuote(1, "maito", 5)
                    if tuote_id == 2:
                        return Tuote(2, "leipä", 7)

                # otetaan toteutukset käyttöön
                self.varasto_mock.saldo.side_effect = varasto_saldo
                self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

                # alustetaan kauppa
                kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

                # tehdään ostokset
                kauppa.aloita_asiointi()
                kauppa.lisaa_koriin(1)
                kauppa.lisaa_koriin(2)
                kauppa.poista_korista(1)
                kauppa.tilimaksu("pekka", "12345")

                # varmistetaan, että metodia tilisiirto on kutsuttu
                self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 7)