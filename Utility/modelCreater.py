from pandas import DataFrame

from Model.faturaModelXML import Fatura


def dataFrameToModel(df:DataFrame) ->list[Fatura]:
    fatura_listesi = []

    for i in range(len(df)):
        fatura = Fatura(
            df.iloc[i]['Firma Ünvanı'],
            df.iloc[i]['Fatura No'],
            df.iloc[i]['Rapor No'],
            df.iloc[i]['Rapor Durumu'],
            df.iloc[i]['Rapor Oluşturulma Tarihi'],
            df.iloc[i]['Alıcı VKN'],
            df.iloc[i]['Para Birimi'],
            df.iloc[i]['Fatura Tutarı'],
            df.iloc[i]['Toplam Vergi'],
            df.iloc[i]['İskonto Tutarı'],
            df.iloc[i]['Artırım Tutarı'],
            df.iloc[i]['Sipariş No'],
            df.iloc[i]['Son Ödeme Tarihi'],
            df.iloc[i]['Düzenlenme Tarihi'],
            df.iloc[i]['Oluşturulma Tarihi'],
            df.iloc[i]['Fatura Tipi'],
            df.iloc[i]['Statü'],
            df.iloc[i]['Gönderim Tipi'],
            df.iloc[i]['Satış Şekli'],
            df.iloc[i]['Ek Dosya Sayısı'],
            df.iloc[i]['Not Var mı'],
            df.iloc[i]['Yazdırıldı mı'],
            df.iloc[i]['HasEMailSent'],
            df.iloc[i]['Kural Var'],
            df.iloc[i]['Opsiyonel Alan 1'],
            df.iloc[i]['Opsiyonel Alan 2'],
            df.iloc[i]['Opsiyonel Alan 3'],
            df.iloc[i]['Opsiyonel Alan 4'],
            df.iloc[i]['Opsiyonel Alan 5'],
            df.iloc[i]['Opsiyonel Alan 6'],
            df.iloc[i]['Opsiyonel Alan 7'],
            df.iloc[i]['Opsiyonel Alan 8'],
            df.iloc[i]['Opsiyonel Alan 9']
        )
        fatura_listesi.append(fatura)
    return fatura_listesi