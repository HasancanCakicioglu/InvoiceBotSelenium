from PyQt5.QtWidgets import QMessageBox


def show_message_box(hataMesaj,id_or_xpath):
    QMessageBox.critical(None, "Error", "Hata! "+hataMesaj + " ||| "+ id_or_xpath)

