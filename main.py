import tkinter as tk   # 匯入 tkinter 模組，並簡寫為 tk
import pandas as pd
# from first_interface import FirstInterface
# from second_interface import SecondInterface
class FirstInterface:
    def __init__(self, master):  # 建立 App 類別的建構子，傳入一個 master 物件作為參數
        self.master = master  # 將傳入的 master 物件指派給 App 物件的 master 屬性!這就是root!
        master.title("My App")  # 設定 master 物件的標題為 "My App"
        master.geometry("800x600")
        self.label = tk.Label(master, text="選取你要的工程")  # 建立一個標籤，顯示文字 "Select your form and price"
        self.label.pack()  # 將標籤元件放置在 master 物件中，預設是垂直排列

        self.form_menu = tk.OptionMenu(master, tk.StringVar(), "混泥土路面", "瀝青路面", "牛逼")  # 建立一個下拉選單，顯示選項 "Form A"、"Form B" 和 "Form C"，並使用 tk.StringVar() 物件來存放用戶選擇的值
        self.form_menu.pack()  # 將下拉選單元件放置在 master 物件中，預設是垂直排列

        self.label = tk.Label(master, text="選擇配置")  # 建立一個標籤，顯示文字 "Select your form and price"
        self.label.pack()

        self.size_menu = tk.OptionMenu(master, tk.StringVar(), "刨除 5 cm", "刨除 10 cm", "不刨除")  # 建立一個下拉選單，顯示選項 "$10"、"$20" 和 "$30"，並使用 tk.StringVar() 物件來存放用戶選擇的值
        self.size_menu.pack()  # 將下拉選單元件放置在 master 物件中，預設是垂直排列
        self.material_menu = tk.OptionMenu(master, tk.StringVar(), "碎石級配與壓實", "不鋪級配")  # 建立一個下拉選單，顯示選項 "$10"、"$20" 和 "$30"，並使用 tk.StringVar() 物件來存放用戶選擇的值
        self.material_menu.pack()  # 將下拉選單元件放置在 master 物件中，預設是垂直排列
        self.label = tk.Label(master, text="面積(cm2)") 
        self.label.pack()
        self.geo_entry = tk.Entry(master)
        self.geo_entry.pack()

        self.button = tk.Button(master, text="Submit", command=self.submit)  # 建立一個按鈕，顯示文字 "Submit"，並設定點擊時呼叫 self.submit 方法 其中master就是self.root
        self.button.pack()  # 將按鈕元件放置在 master 物件中，預設是垂直排列

    def submit(self):  # 建立 submit 方法，用於處理用戶提交表單的事件
        form = self.form_menu.cget("text")  # 獲取用戶選擇的表單
        size = self.size_menu.cget("text")  # 獲取用戶選擇的size
        material = self.material_menu.cget("text")  
        geo = self.geo_entry.get()  
        
        print("You selected:", form, size,material,geo+"cm2")  # 將用戶選擇的表單和價格輸出到控制台中  
        # SecondPage(form, size, material, geo)     
        # self.master.destroy()  # 銷毀第一個介面的物件
        self.master.withdraw()#deiconify()能再召喚
        SecondPage(form, size, material, geo)
        
        
        # root = tk.Tk()  # 創建新的主視窗
        # app = SecondInterface(root)  # 創建第二個介面的物件
        # root.mainloop()
class SecondPage:
    def __init__(self , form, size, material, geo):
        self.form = form
        self.size = size
        self.material = material
        self.geo = geo
        
        self.top = tk.Toplevel()
        self.top.title("Second Page")

        label_text = f"您的選擇為1. {self.form}, 2. {self.size}, 3. {self.material}, 4. {self.geo} cm2"
        self.top.geometry("800x600")
        self.label = tk.Label(self.top,text=label_text)
        self.label.pack()

        self.adjustment_label = tk.Label(self.top, text="其他調整選項：")
        self.adjustment_label.pack()

        self.adjustment_entry = tk.Entry(self.top)
        self.adjustment_entry.pack()

        self.adjustment_button = tk.Button(self.top, text="確定")
        self.adjustment_button.pack()


        # 讀取Excel表格
        self.df = pd.read_excel("參考excel.xls", sheet_name=3)
        self.df.dropna()
        print(self.df)
        # 建立表格元件
        self.table = tk.Frame(self.top)
        self.table.pack()

        # 建立表頭
        for i, col_name in enumerate(self.df.columns):
            col_label = tk.Label(self.table, text=col_name)
            col_label.grid(row=0, column=i)

        # 建立資料列
        for i, row_data in self.df.iterrows():
            for j, cell_data in enumerate(row_data):
                cell_label = tk.Label(self.table, text=cell_data)
                cell_label.grid(row=i+1, column=j)

        # # 創建一個Canvas小部件，指定寬度和高度
        # canvas = tk.Canvas(self, width=400, height=400)

        # # 創建一個Scrollbar小部件，並指定方向和回調函數
        # scrollbar = tk.Scrollbar(self, orient='vertical', command=canvas.yview)

        # # 設置Canvas小部件的滾動條回調函數
        # canvas.config(yscrollcommand=scrollbar.set)

        # # 設置Canvas小部件的滾動區域，以便滾動條正確工作
        # canvas.config(scrollregion=(0, 0, 800, 800))

        # # 將Excel表格轉換成一個tkinter控件
        # table = pd.DataFrame(self.df)
        # table = tk.Label(canvas, text=table.to_string(), justify='left', font=('Arial', 10))

        # # 將Excel表格控件添加到Canvas小部件中
        # canvas.create_window((0, 0), window=table, anchor='nw')

        # # 將Canvas小部件和Scrollbar小部件添加到窗口中
        # canvas.pack(side='left', fill='both', expand=True)
        # scrollbar.pack(side='right', fill='y')
    def function(self):
        pass
        # print(self.form)
def main():
    root = tk.Tk()  # 建立一個 Tk 物件，作為應用程序的主視窗  
    app = FirstInterface(root)  # 建立一個 App 物件，並傳入 root 物件作為參數
    root.mainloop()
if __name__ =='__main__':
    main()
