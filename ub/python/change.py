import pandas as pd
class Change_dt(): #self로 쓰면 클래스가 갖고 있는 변수임.
    def __init__(self, input_url):
        self.url = input_url

    def csv_read(self, input_sort, input_inplace): #위에서 url 불어오니까 매개변수 필요없음 
        self.dt = pd.read_csv(self.url)
        self.dt.sort_values(input_sort,inplace = input_inplace)
        self.dt.reset_index(drop=True, inplace = input_inplace)
        return self.dt

    def remove_col(self, input_list = [] ): #매개변수라 self 안해도됨
        self.dt.drop(input_list, axis=1,inplace=True)
        return self.dt

    def remove_2(self, input_s_col, input_e_col):
        self.dt.drop(self.dt.loc[:,input_s_col : input_e_col],axis=1,inplace=True)
        return self.dt