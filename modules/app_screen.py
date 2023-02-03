import customtkinter
# створюємо клас App 
class App(customtkinter.CTk):
    def __init__(self, app_width, app_height):
        super().__init__()
        # задаємо властивості, що зберігають розміри екрану додатку
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        # задаємо властивості, що зберігають розміри екрану комп'ютера
        self.PC_SCREEN_WIDTH = self.winfo_screenwidth()
        self.PC_SCREEN_HEIGHT = self.winfo_screenheight()
        # розташовуємо додаток у правому нижньому куті
        # self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{self.PC_SCREEN_WIDTH - self.APP_WIDTH}+{self.PC_SCREEN_HEIGHT - self.APP_HEIGHT}")
        
        # розташовуємо додаток по центру
        # self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{self.PC_SCREEN_WIDTH // 2 - self.APP_WIDTH // 2}+{self.PC_SCREEN_HEIGHT // 2 - self.APP_HEIGHT // 2}")
        
        # розташовуємо додаток у правому верхньому куті
        # self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{self.PC_SCREEN_WIDTH - self.APP_WIDTH}+{0}")
        
        # розташовуємо додаток у лівому нижньому куті 
        # self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{0}+{self.PC_SCREEN_HEIGHT - self.APP_HEIGHT}")
        
        # розташовуємо додатоу у лівому верхньому куті 
        # self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{0}+{0}")
        
        # задаємо назву вікну додатку
        self.title("Головне вікно додатку")
# створюємо об'єкт від класу App
app = App(app_width= 400, app_height = 300)
