import tkinter as tk
from api.calorie_api import CalorieAPI
from db.queries import DBQueries
from datetime import date


class MealInput(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.api = CalorieAPI(api_key="your_api_key", app_id="your_app_id")
        self.db = DBQueries()

        self.label = tk.Label(self, text="Enter Food:")
        self.label.pack()
        self.entry = tk.Entry(self)
        self.entry.pack()
        self.button = tk.Button(self, text="Add Meal", command=self.add_meal)
        self.button.pack()

    def add_meal(self):
        food = self.entry.get()
        calories = self.api.get_calories(food)
        self.db.add_meal(date.today().isoformat(), food, calories)
