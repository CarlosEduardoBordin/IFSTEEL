import wx
from widget_class import StaticBox


class CalcProgress(wx.MDIChildFrame):
    def __init__(self, parent_mdi:  wx.MDIParentFrame, parent_child: wx.MDIChildFrame):
        #nao colocar no init o parent child
        super().__init__(parent_mdi, id=wx.ID_ANY, title="Calculando ...",
                         pos=wx.DefaultPosition, size=(270, 125), style=wx.DEFAULT_FRAME_STYLE & ~wx.MAXIMIZE_BOX  & ~wx.CLOSE_BOX)
        # self.parent = parent
        self.SetIcon(wx.Icon("icones/calc_24.png", wx.BITMAP_TYPE_PNG))

        self.parent_mdi = parent_mdi
        self.parent_child = parent_child


        self.window_main_panel = wx.Panel(self)
        self.main_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.box_progress = StaticBox(self.window_main_panel, "", orientation="vertical")
        self.gauge = wx.Gauge(self.box_progress, range=100, size = (250, 25),style =  wx.GA_HORIZONTAL)
        self.box_progress.widgets_add(self.gauge, 0, True)

        self.progress_name = wx.StaticText(self.box_progress, id=wx.ID_ANY, label="Perfil : ")
        self.box_progress.widgets_add(self.progress_name, 0, True)

        self.main_sizer.Add(self.box_progress,  proportion = 0, flag = wx.ALL | wx.EXPAND, border = 5)
        self.window_main_panel.SetSizer(self.main_sizer)
        self.window_main_panel.Layout()
        self.window_main_panel.Refresh()


    def update_progress(self, value):
        self.gauge.SetValue(value)

    def update_progress_perfil_name(self, label, value):
        texto = f"Perfil : {label}, progresso: {value} %"
        self.progress_name.SetLabel(texto)