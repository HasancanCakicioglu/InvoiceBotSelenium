from enum import Enum

class browsers(Enum):
    Google_Chrome = "Google Chrome"
    Microsoft_Edge = "Microsoft Edge"

class constantData:
    chrome_driver_path = "chrome_driver_path"
    edge_driver_path = "edge_driver_path"
    gib_kullanici_adi = "gib_kullanici_adi"
    gib_sifre = "gib_sifre"
    indirilen_path = "indirilen_path"
    gib_link = "gib_link"
    trendyol_panel_link = "trendyol_panel_link"
    browser = "browsers"

    şirket_kisa_kodu = "şirket_kisa_kodu"
    trendyol_kullanici_adi = "trendyol_kullanici_adi"
    trendyol_sifre = "trendyol_sifre"



class GoogleTextController:
    google_login_text = ""

    @staticmethod
    def set_google_login_text(newGoogleLoginText):
        GoogleTextController.google_login_text = newGoogleLoginText

    @staticmethod
    def get_google_login_text() -> str:
        return GoogleTextController.google_login_text
