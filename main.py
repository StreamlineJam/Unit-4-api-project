from fastapi import FastAPI
import uvicorn

total_run_count = 0

app = FastAPI()

APP_KEY = "UDHFTGHVCJUDI"

fruits = [
    {"fruit": "apple", "color": "red"},
    {"fruit": "orange", "color": "orange"},
    {"fruit": "Grapes", "color": "purple"},
    {"fruit": "cherry", "color": "red red"},
    {"fruit": "Bananas", "color": "yellow"},
    {"fruit": "Fish", "color": "its not a fruit"},
    {"fruit": "man", "color": "i dont encourage cannibalism"},
    {"fruit": "kiwi", "color": "green"},
    {"fruit": "Mango", "color": "light yellow"},
    {"fruit": "Pomegranate", "color": "dark purple"},
    {"fruit": "watermelon", "color": "green with stripes"},
    {"fruit": "pineapple", "color": "some kind of yellow"},
    {"fruit": "Lemon", "color": "very very yellow"},
    {"fruit": "Strawberry", "color": "red with dots"},
    {"fruit": "Avocado", "color": "green but not green completely"},
    {"fruit": "I can't think of any", "color": "bro cant think of any fruits"},
    {"fruit": "coke", "color": "thats a drink"},
    {"fruit": "fanta", "color": "thats soda"},
    {"fruit": "water", "color": "bruh we just degrading"},
    {"fruit": "nothing", "color": "it has no color"}
]

Grades = [
    {"name": "leon", "Grades": 9},
    {"name": "Richard", "Grades": 8},
    {"name": "God", "Grades": 69}
]

@app.get("/fruits/get_info")
async def get_fruits(fruit: str, appid: str):
    if appid != APP_KEY:
        return {"msg": "Key is incorrect"}
    for fruits_info in fruits:
        if fruit.lower() == fruits_info['fruit'].lower():
            return fruits_info
    return {"msg": "fruit not found"}

@app.get("/grades/get_info")
async def get_grades(grade: str, appid: str):
    if appid != APP_KEY:
        return {"msg": "Key is incorrect"}
    for grades_info in grade:
        if Grades.lower() == grades_info['name'].lower():
            return grades_info
    return {"msg": "grade not found"}



if __name__ == "__main__":
    uvicorn.run("main:app",  reload=True)
