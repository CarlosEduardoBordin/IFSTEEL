import wx
from widget_class import StaticBox, TextBoxVrf
from table_manipulation import ReadExcelFile
from table_manipulation import WriteExcelFile


class ConfiguracoesChildFrame(wx.MDIChildFrame):
    def __init__(self, parent):
        # Inicializa a janela filha com o título nome_formulario
        super().__init__(parent, -1, "Configurações", size=(500, 725), style=wx.DEFAULT_FRAME_STYLE & ~wx.MAXIMIZE_BOX)
        self.parent = parent
        self.SetMinSize((550, 520))
        self.SetMaxSize((600, 750))

        self.SetIcon( wx.Icon("icones/cfg.png", wx.BITMAP_TYPE_PNG))  # Definindo o ícone para o MDIFrame

        self.window_main_panel = wx.ScrolledWindow(self, style=wx.VSCROLL)
        self.window_main_panel.SetScrollRate(0, 20)
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)

        def on_btn_reset(event):
            self.combo_box_si_lenght.SetValue("m")
            self.combo_box_si_area.SetValue("m^2")
            self.combo_box_si_volume.SetValue("m^3")
            self.combo_box_si_inercia.SetValue("m^4")
            self.combo_box_si_six.SetValue("m^6")
            self.combo_box_si_force.SetValue("N")
            self.combo_box_si_moment.SetValue("N*m")
            self.combo_box_si_press.SetValue("N/m^2")
            self.input_e.SetValue("200000000000")
            self.input_g.SetValue("77000000000")
            self.lft_input.SetValue("300")
            self.lfc_input.SetValue("200")
            self.combo_papel.SetValue("a4paper")
            self.checkbox_abrir_apos_gerar.SetValue(True)
            self.checkbox_h.SetValue(True)


        def on_btn_apl(event):
            if self.checkbox_h.IsChecked(): value = True
            else: value = False
            #modulos
            self.parent.set_unit_lenght(self.combo_box_si_lenght.GetValue(), self.count_box_lenght.GetValue())
            self.parent.set_unit_area(self.combo_box_si_area.GetValue(), self.count_box_area.GetValue())
            self.parent.set_unit_volume(self.combo_box_si_volume.GetValue(), self.count_box_volume.GetValue())
            self.parent.set_unit_inercia(self.combo_box_si_inercia.GetValue(), self.count_box_inercia.GetValue())
            self.parent.set_unit_six(self.combo_box_si_six.GetValue(), self.count_box_six.GetValue())
            self.parent.set_unit_force(self.combo_box_si_force.GetValue(),self.count_box_force.GetValue() )
            self.parent.set_unit_moment(self.combo_box_si_moment.GetValue(), self.count_box_moment.GetValue())
            self.parent.set_unit_press(self.combo_box_si_press.GetValue(), self.count_box_press.GetValue())
            self.parent.set_e_modulo( self.input_e.get_value())
            self.parent.set_g_modulo(self.input_g.get_value())
            self.parent.set_lf_barra(self.lft_input.get_value(), self.lfc_input.get_value())
            self.parent.set_y_um(self.input_y_um.get_value())
            self.parent.set_papel(self.combo_papel.GetValue())
            self.parent.set_orientacao(value)
            self.parent.set_open_file(self.checkbox_abrir_apos_gerar.GetValue())



        def on_btn_save(event):
            if self.checkbox_h.IsChecked(): value = True
            else: value = False

            data = [["Comprimento" , f"{self.combo_box_si_lenght.GetValue()}" , f"{self.count_box_lenght.GetValue()}"],
                    ["Area" , f"{self.combo_box_si_area.GetValue()}", f"{self.count_box_area.GetValue()}"],
                    ["Volume", f"{self.combo_box_si_volume.GetValue()}", f"{self.count_box_volume.GetValue()}"],
                    ["Inercia", f"{self.combo_box_si_inercia.GetValue()}", f"{self.count_box_inercia.GetValue()}" ],
                    ["Empenamento", f"{self.combo_box_si_six.GetValue()}", f"{self.count_box_six.GetValue()}"],
                    ["Forca", f"{self.combo_box_si_force.GetValue()}", f"{self.count_box_force.GetValue()}"],
                    ["Momento", f"{self.combo_box_si_moment.GetValue()}", f"{self.count_box_moment.GetValue()}"],
                    ["Pressao", f"{self.combo_box_si_press.GetValue()}", f"{self.count_box_press.GetValue()}"],
                    ["e", f"{self.input_e.get_value()}"], ["g", f"{self.input_g.get_value()}"],
                    ["y1", f"{self.input_y_um.get_value()}"] , ["lft", f"{self.lft_input.get_value()}"],
                    ["lfc", f"{self.lfc_input.get_value()}"], ["papel", f"{self.combo_papel.GetValue()}"],
                    ["orientacao", f"{value}"], ["file", f"{value}"]
                    ]
            file_save_name = WriteExcelFile("steel.xlsx")
            file_save_name.save_data_to_file("unidades", data, 3, ["Tipo", "Unidade", "Casas"])

        #carregando os dados
        self.data_si = ReadExcelFile("steel.xlsx","unidades")

        self.box_si = StaticBox(self.window_main_panel, "Sistema de unidades", orientation="grid_four")
        #casas decimais
        #comprimento
        self.lenght_text = wx.StaticText(self.box_si, id=wx.ID_ANY, label="Unidade de comprimento: ")
        self.box_si.widgets_add(self.lenght_text, 0, False)
        si_values_lenght = ["mm", "cm", "m"]
        comprimento = self.parent.get_unit_lenght()
        self.combo_box_si_lenght = wx.ComboBox(self.box_si, id = wx.ID_ANY, style = wx.CB_READONLY,choices = si_values_lenght, value = comprimento[0])
        self.box_si.widgets_add(self.combo_box_si_lenght, 0, False)
        self.casa_decimal_lenght = wx.StaticText(self.box_si, id=wx.ID_ANY, label= "Casas decimais :")
        self.box_si.widgets_add(self.casa_decimal_lenght, 0,False)
        self.count_box_lenght = wx.SpinCtrl(self.box_si, value=str(comprimento[1]),min=0, max=20)
        self.box_si.widgets_add(self.count_box_lenght, 0, False)
        #area
        self.area_text = wx.StaticText(self.box_si, id=wx.ID_ANY, label="Unidade de área: ")
        self.box_si.widgets_add(self.area_text, 0, False)
        si_values_area = ["mm^2", "cm^2", "m^2"]
        area = self.parent.get_unit_area()
        self.combo_box_si_area = wx.ComboBox(self.box_si, id = wx.ID_ANY, style = wx.CB_READONLY,choices = si_values_area, value = area[0])
        self.box_si.widgets_add(self.combo_box_si_area, 0, False)
        self.casa_decimal_area = wx.StaticText(self.box_si, id=wx.ID_ANY, label= "Casas decimais :")
        self.box_si.widgets_add(self.casa_decimal_area, 0,False)
        self.count_box_area = wx.SpinCtrl(self.box_si, value=str(area[1]),min=0, max=20)
        self.box_si.widgets_add(self.count_box_area, 0, False)
        #volume
        self.volume_text = wx.StaticText(self.box_si, id=wx.ID_ANY, label="Unidade de volume: ")
        self.box_si.widgets_add(self.volume_text, 0, False)
        si_values_volume = ["mm^3", "cm^3", "m^3"]
        volume = self.parent.get_unit_volume()
        self.combo_box_si_volume = wx.ComboBox(self.box_si, id = wx.ID_ANY, style = wx.CB_READONLY,choices = si_values_volume, value = volume[0])
        self.box_si.widgets_add(self.combo_box_si_volume, 0, False)
        self.casa_decimal_volume = wx.StaticText(self.box_si, id=wx.ID_ANY, label= "Casas decimais :")
        self.box_si.widgets_add(self.casa_decimal_volume, 0,False)
        self.count_box_volume = wx.SpinCtrl(self.box_si, value=str(volume[1]),min=0, max=20)
        self.box_si.widgets_add(self.count_box_volume, 0, False)
        #inercia
        self.inercia_text = wx.StaticText(self.box_si, id=wx.ID_ANY, label="Unidade de inércia: ")
        self.box_si.widgets_add(self.inercia_text, 0, False)
        si_values_inercia = ["mm^4", "cm^4", "m^4"]
        inercia = self.parent.get_unit_inercia()
        self.combo_box_si_inercia = wx.ComboBox(self.box_si, id = wx.ID_ANY, style = wx.CB_READONLY,choices = si_values_inercia, value = inercia[0])
        self.box_si.widgets_add(self.combo_box_si_inercia, 0, False)
        self.casa_decimal_inercia = wx.StaticText(self.box_si, id=wx.ID_ANY, label= "Casas decimais :")
        self.box_si.widgets_add(self.casa_decimal_inercia, 0,False)
        self.count_box_inercia = wx.SpinCtrl(self.box_si, value=str(inercia[1]),min=0, max=20)
        self.box_si.widgets_add(self.count_box_inercia, 0, False)
        # inercia
        self.six_text = wx.StaticText(self.box_si, id=wx.ID_ANY, label="Unidade de empenamento: ")
        self.box_si.widgets_add(self.six_text, 0, False)
        si_values_six = ["mm^6", "cm^6", "m^6"]
        six = self.parent.get_unit_six()
        self.combo_box_si_six = wx.ComboBox(self.box_si, id=wx.ID_ANY, style=wx.CB_READONLY,
                                                choices=si_values_six, value=six[0])
        self.box_si.widgets_add(self.combo_box_si_six, 0, False)
        self.casa_decimal_six = wx.StaticText(self.box_si, id=wx.ID_ANY, label="Casas decimais :")
        self.box_si.widgets_add(self.casa_decimal_six, 0, False)
        self.count_box_six = wx.SpinCtrl(self.box_si, value=str(six[1]), min=0, max=20)
        self.box_si.widgets_add(self.count_box_six, 0, False)
        #forca
        self.force_text = wx.StaticText(self.box_si, id=wx.ID_ANY, label="Unidade de força: ")
        self.box_si.widgets_add(self.force_text, 0, False)
        si_values_force = ["N", "kN", "MN"]
        forca = self.parent.get_unit_force()
        self.combo_box_si_force= wx.ComboBox(self.box_si, id = wx.ID_ANY, style = wx.CB_READONLY,choices = si_values_force, value = forca[0])
        self.box_si.widgets_add(self.combo_box_si_force, 0, False)
        self.casa_decimal_force = wx.StaticText(self.box_si, id=wx.ID_ANY, label= "Casas decimais :")
        self.box_si.widgets_add(self.casa_decimal_force, 0,False)
        self.count_box_force = wx.SpinCtrl(self.box_si, value=str(forca[1]),min=0, max=20)
        self.box_si.widgets_add(self.count_box_force, 0, False)
        #momento
        self.moment_text = wx.StaticText(self.box_si, id=wx.ID_ANY, label="Unidade de momento: ")
        self.box_si.widgets_add(self.moment_text, 0, False)
        si_values_momento = ["N*m", "kN*m", "MN*m"]
        momento = self.parent.get_unit_moment()
        self.combo_box_si_moment = wx.ComboBox(self.box_si, id = wx.ID_ANY, style = wx.CB_READONLY,choices = si_values_momento, value = momento[0])
        self.box_si.widgets_add(self.combo_box_si_moment, 0, False)
        self.casa_decimal_moment = wx.StaticText(self.box_si, id=wx.ID_ANY, label= "Casas decimais :")
        self.box_si.widgets_add(self.casa_decimal_moment, 0,False)
        self.count_box_moment = wx.SpinCtrl(self.box_si, value=str(momento[1]),min=0, max=20)
        self.box_si.widgets_add(self.count_box_moment, 0, False)
        #p/a
        self.press_text = wx.StaticText(self.box_si, id=wx.ID_ANY, label="Unidade de pressão: ")
        self.box_si.widgets_add(self.press_text, 0, False)
        si_values_press = ["N/m^2", "kN/m^2", "MN/m^2", "GN/m^2"]
        pressao = self.parent.get_unit_press()
        self.combo_box_si_press= wx.ComboBox(self.box_si, id = wx.ID_ANY, style = wx.CB_READONLY,choices = si_values_press, value = pressao[0])
        self.box_si.widgets_add(self.combo_box_si_press, 1, False)
        self.casa_decimal_press = wx.StaticText(self.box_si, id=wx.ID_ANY, label= "Casas decimais :")
        self.box_si.widgets_add(self.casa_decimal_press, 0,False)
        self.count_box_press = wx.SpinCtrl(self.box_si, value=str(pressao[1]),min=0, max=20)
        self.box_si.widgets_add(self.count_box_press, 0, False)

        #box variaveis
        self.box_variaveis_norma = StaticBox(self.window_main_panel, "Configurações de variáveis", orientation="grid")
        self.e_text = wx.StaticText(self.box_variaveis_norma, id=wx.ID_ANY, label="Módulo de elasticidade (Pa) : ")
        self.box_variaveis_norma.widgets_add(self.e_text, 0, False)
        e = str(self.parent.get_e_modulo())
        self.input_e = TextBoxVrf(self.box_variaveis_norma, value=e, only_numeric=True)
        self.box_variaveis_norma.widgets_add(self.input_e, 1, False)
        self.g_text = wx.StaticText(self.box_variaveis_norma, id=wx.ID_ANY, label="Módulo de elasticidade transversal (Pa) : ")
        self.box_variaveis_norma.widgets_add(self.g_text, 0, False)
        g = str(self.parent.get_g_modulo())
        self.input_g = TextBoxVrf(self.box_variaveis_norma, value=g, only_numeric=True)
        self.box_variaveis_norma.widgets_add(self.input_g, 1, False)
        self.y_um_text = wx.StaticText(self.box_variaveis_norma, id=wx.ID_ANY, label="γ1: ")
        self.box_variaveis_norma.widgets_add(self.y_um_text, 0, False)
        y1 = str(self.parent.get_y_um())
        self.input_y_um = TextBoxVrf(self.box_variaveis_norma, value=y1, only_numeric=True)
        self.box_variaveis_norma.widgets_add(self.input_y_um, 1, False)

        self.lft_text = wx.StaticText(self.box_variaveis_norma, id=wx.ID_ANY, label="Limite de esbeltez tração : ")
        self.box_variaveis_norma.widgets_add(self.lft_text, 0, False)
        lft = str(self.parent.get_lf_barra()[0])
        self.lft_input = TextBoxVrf(self.box_variaveis_norma, value=lft, only_numeric=True)
        self.box_variaveis_norma.widgets_add(self.lft_input, 1, False)
        self.lfc_text = wx.StaticText(self.box_variaveis_norma, id=wx.ID_ANY, label="Limitação de esbeltez compressão: ")
        self.box_variaveis_norma.widgets_add(self.lfc_text, 0, False)
        lfc = str(self.parent.get_lf_barra()[1])
        self.lfc_input = TextBoxVrf(self.box_variaveis_norma, value=lfc, only_numeric=True)
        self.box_variaveis_norma.widgets_add(self.lfc_input, 1, False)
        #box memoria de calculo
        self.box_memoria = StaticBox(self.window_main_panel, "Configurações da memória de cálculo", orientation="grid")
        self.utilizar_na_horizontal = wx.StaticText(self.box_memoria, id=wx.ID_ANY, label="Gerar a memória em modo paisagem : ")
        self.box_memoria.widgets_add(self.utilizar_na_horizontal, 0, False)
        self.checkbox_h = wx.CheckBox(self.box_memoria, label="")

        if self.parent.get_orientacao():
            self.checkbox_h.SetValue(True)
        else:
            self.checkbox_h.SetValue(False)

        self.box_memoria.widgets_add(self.checkbox_h, 0, False)
        self.utilizar_papel = wx.StaticText(self.box_memoria, id=wx.ID_ANY,
                                                    label="Tipo de papel a utilizar : ")
        self.box_memoria.widgets_add(self.utilizar_papel, 0, False)
        tipo_de_papel = ["a4paper", "a5paper", "a3paper", "b5paper"]
        papel = self.parent.get_papel()
        self.combo_papel= wx.ComboBox(self.box_memoria, id = wx.ID_ANY, style = wx.CB_READONLY,choices = tipo_de_papel, value = papel)
        self.box_memoria.widgets_add(self.combo_papel, 1, False)
        self.abrir = wx.StaticText(self.box_memoria, id=wx.ID_ANY,
                                                    label="Abrir o arquivo da memória após gerar: ")
        self.box_memoria.widgets_add(self.abrir, 0, False)
        self.checkbox_abrir_apos_gerar = wx.CheckBox(self.box_memoria, label="")
        self.checkbox_abrir_apos_gerar.SetValue(True)
        self.box_memoria.widgets_add(self.checkbox_abrir_apos_gerar, 0, True)

        # box variaveis
        self.box_aplicar = StaticBox(self.window_main_panel, "", orientation="horizontal")
        self.btn_reset = wx.Button(self.box_aplicar, label="Resetar os valores")
        self.btn_reset.SetBitmapPosition(wx.LEFT)
        self.btn_reset.SetBitmap(wx.Bitmap("icones/reset.png", wx.BITMAP_TYPE_PNG))
        self.box_aplicar.widgets_add(self.btn_reset, 1, True)
        self.btn_reset.Bind(wx.EVT_BUTTON, on_btn_reset)
        self.btn_apl = wx.Button(self.box_aplicar, label="Aplicar")
        self.btn_apl.SetBitmapPosition(wx.LEFT)
        self.btn_apl.SetBitmap(wx.Bitmap("icones/inject.png", wx.BITMAP_TYPE_PNG))
        self.box_aplicar.widgets_add(self.btn_apl, 1, True)
        self.btn_apl.Bind(wx.EVT_BUTTON, on_btn_apl)
        self.btn_save = wx.Button(self.box_aplicar, label="Salvar")
        self.btn_save.SetBitmapPosition(wx.LEFT)
        self.btn_save.SetBitmap(wx.Bitmap("icones/disquete.png", wx.BITMAP_TYPE_PNG))
        self.box_aplicar.widgets_add(self.btn_save, 1, True)
        self.btn_save.Bind(wx.EVT_BUTTON, on_btn_save)
        #adicionando ao sizer principal
        self.main_sizer.Add(self.box_si,  proportion = 0, flag = wx.ALL | wx.EXPAND, border = 5)
        self.main_sizer.Add(self.box_variaveis_norma,  proportion = 0, flag = wx.ALL | wx.EXPAND, border = 5)
        self.main_sizer.Add(self.box_memoria,  proportion = 0, flag = wx.ALL | wx.EXPAND, border = 5)
        self.main_sizer.Add(self.box_aplicar,  proportion = 0, flag = wx.ALL | wx.EXPAND, border = 5)
        self.window_main_panel.SetSizer(self.main_sizer)

