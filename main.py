from fastapi import FastAPI
import uvicorn

total_run_count = 0

app = FastAPI()

APP_KEY = "UDHFTGHVCJUDI"

fruits = [
    {"fruit": "apple", "color": "red", "goodness": "yes"},
    {"fruit": "orange", "color": "orange", "goodness": "yes"},
    {"fruit": "Grapes", "color": "purple","goodness": "no"},
    {"fruit": "cherry", "color": "red red", "goodness": "yes"},
    {"fruit": "Bananas", "color": "yellow", "goodness":"no"},
    {"fruit": "Fish", "color": "its not a fruit","goodness":"meh"},
    {"fruit": "man", "color": "i dont encourage cannibalism", "goodness": "yes"},
    {"fruit": "kiwi", "color": "green","goodness": "no"},
    {"fruit": "Mango", "color": "light yellow" ,"goodness":"yes"},
    {"fruit": "Pomegranate", "color": "dark purple", "goodness": "yes"},
    {"fruit": "watermelon", "color": "green with stripes", "goodness": "no"},
    {"fruit": "pineapple", "color": "some kind of yellow", "goodness": "yes"},
    {"fruit": "Lemon", "color": "very very yellow", "goodness": "yes"},
    {"fruit": "Strawberry", "color": "red with dots", "goodness": "yes"},
    {"fruit": "Avocado", "color": "green but not green completely", "goodness": "yes"},
    {"fruit": "I can't think of any", "color": "bro cant think of any fruits", "goodness": "what"},
    {"fruit": "coke", "color": "thats a drink", "goodness": "yes"},
    {"fruit": "fanta", "color": "thats soda", "goodness": "yes"},
    {"fruit": "water", "color": "bruh we just degrading", "goodness:"yes"},
    {"fruit": "nothing", "color": "it has no color", "goodness":"nothing"}
]

Grades = [
    {"name": "leon", "Grades": 9, "gender": "male"},
    {"name": "Richard", "Grades": 8, "gender": "male"},
    {"name": "God", "Grades": 69, "gender": "he got none"}
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
    uvicorn.run("main:app",  host='0.0.0.0', reload=True)
