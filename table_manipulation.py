import wx
import pandas as pd
import os


#"tipo_aco.xlsx"
class ReadExcelFile:
    def __init__(self, path, sheet_name):
        self.path = path
        #verifica a se tem o arquivo !!
        try:
            self.data = pd.read_excel(path, sheet_name)
        except Exception as exception_code:
            wx.MessageBox(f"Erro: {exception_code}", "Erro",style = wx.OK | wx.ICON_ERROR)

    def return_value_by_one_col(self, col_name):
        return_list = self.data[col_name].tolist()
        return return_list
    def get_name_and_return_col_value(self, col_name, col_line_value, extrac_col):
        firth_line = self.data[self.data[col_name] == col_line_value].iloc[0]  # Filtra e pega a primeira linha
        result_extracted_values = {}
        #valor da coluna na coluna extraida
        for col in extrac_col:
            #separa o valor para cada coluna usando a linha
            result_extracted_values[col] = float(firth_line[col]) #valores em np.int64 para float
        return result_extracted_values
    def get_name_and_return_col_value_str(self, col_name, col_line_value, extrac_col):
        firth_line = self.data[self.data[col_name] == col_line_value].iloc[0]  # Filtra e pega a primeira linha
        result_extracted_values = {}
        # valor da coluna na coluna extraida
        for col in extrac_col:
            # separa o valor para cada coluna usando a linha
            result_extracted_values = str(firth_line[col])  # valores em np.int64 para float
        return result_extracted_values
    def read_number_of_coluns_and_lines(self):
        num_lines, num_columns = self.data.shape
        return num_lines, num_columns
    def read_values(self):
        line, col = self.read_number_of_coluns_and_lines()
        data = {}
        for l in range(line):
            for c in range(col):
                data[l, c] = self.data.iloc[l, c]
        return data

class WriteExcelFile:
    def __init__(self, path):
        self.path = path
    def save_data_to_file(self, sht_name, data, num_cols,header_list):
        dataframe = pd.DataFrame(data, columns=header_list[:num_cols]) #salva o valor da celula partindo do valor da coluna
        mode = "a" if os.path.exists(self.path) else "w"
        with pd.ExcelWriter(self.path, engine="openpyxl", mode=mode, if_sheet_exists="replace") as writer:
            dataframe.to_excel(writer, sheet_name=sht_name, index=False, header=True)