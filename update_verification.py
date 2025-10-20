import wx
import requests
import webbrowser

class UpdateVerif:
    def __init__(self):
        #versao corrente da aplicacao
        self.current_version = "v1.2.0"

    def get_version(self):
        return self.current_version

    def check_for_updates(self):
        api_url = f"https://api.github.com/repos/CarlosEduardoBordin/IFSTEEL/releases/latest"

        try:
            response = requests.get(api_url, timeout=10)
            response.raise_for_status()
            release_data = response.json()
            latest_version_str = release_data.get("tag_name")
            if not latest_version_str == self.get_version():
                dialog_button =  wx.MessageBox(f"Nova versão disponível no GitHub, deseja atualizar?", "Atualização", style=wx.YES_NO | wx.ICON_QUESTION)
                if dialog_button == wx.YES:
                    webbrowser.open("https://github.com/CarlosEduardoBordin/IFSTEEL/releases")

        except Exception as error:
            pass
