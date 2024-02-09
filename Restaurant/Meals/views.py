from django.shortcuts import render

# Create your views here.

def ShowItem(request):
    meals = [
    {
        "strMeal": "BeaverTails",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/ryppsv1511815505.jpg",
        "idMeal": "52928",
        "strDescription": "While eating at a restaurant is an enjoyable and convenient occasional treat, most individuals and families prepare their meals at home. To make breakfast, lunch, and dinner daily, these persons must have the required foods and ingredients on hand and ready to go; foods and "
    },
    {
        "strMeal": "Breakfast Potatoes",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/1550441882.jpg",
        "idMeal": "52965",
        "strDescription": "While eating at a restaurant is an enjoyable and convenient occasional treat, most individuals and families prepare their meals at home. To make breakfast, lunch, and dinner daily, these persons must have the required foods and ingredients on hand and ready to go; foods and "
    },
    {
        "strMeal": "Canadian Butter Tarts",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/wpputp1511812960.jpg",
        "idMeal": "52923",
       "strDescription": "While eating at a restaurant is an enjoyable and convenient occasional treat, most individuals and families prepare their meals at home. To make breakfast, lunch, and dinner daily, these persons must have the required foods and ingredients on hand and ready to go; foods and "
    },
    {
        "strMeal": "Montreal Smoked Meat",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/uttupv1511815050.jpg",
        "idMeal": "52927",
       "strDescription": "While eating at a restaurant is an enjoyable and convenient occasional treat, most individuals and families prepare their meals at home. To make breakfast, lunch, and dinner daily, these persons must have the required foods and ingredients on hand and ready to go; foods and "
    },
    {
        "strMeal": "Nanaimo Bars",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/vwuprt1511813703.jpg",
        "idMeal": "52924",
        "strDescription": "While eating at a restaurant is an enjoyable and convenient occasional treat, most individuals and families prepare their meals at home. To make breakfast, lunch, and dinner daily, these persons must have the required foods and ingredients on hand and ready to go; foods and "
    },
    {
        "strMeal": "Pate Chinois",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/yyrrxr1511816289.jpg",
        "idMeal": "52930",
        "strDescription": "While eating at a restaurant is an enjoyable and convenient occasional treat, most individuals and families prepare their meals at home. To make breakfast, lunch, and dinner daily, these persons must have the required foods and ingredients on hand and ready to go; foods and "
    },
    {
        "strMeal": "Pouding chomeur",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/yqqqwu1511816912.jpg",
        "idMeal": "52932",
        "strDescription": "While eating at a restaurant is an enjoyable and convenient occasional treat, most individuals and families prepare their meals at home. To make breakfast, lunch, and dinner daily, these persons must have the required foods and ingredients on hand and ready to go; foods and ."
    },
    {
        "strMeal": "Poutine",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/uuyrrx1487327597.jpg",
        "idMeal": "52804",
        "strDescription": "While eating at a restaurant is an enjoyable and convenient occasional treat, most individuals and families prepare their meals at home. To make breakfast, lunch, and dinner daily, these persons must have the required foods and ingredients on hand and ready to go; foods and "
    },
    {
        "strMeal": "Rappie Pie",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/ruwpww1511817242.jpg",
        "idMeal": "52933",
        "strDescription": "While eating at a restaurant is an enjoyable and convenient occasional treat, most individuals and families prepare their meals at home. To make breakfast, lunch, and dinner daily, these persons must have the required foods and ingredients on hand and ready to go; foods and "
    },
    {
        "strMeal": "Split Pea Soup",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/xxtsvx1511814083.jpg",
        "idMeal": "52925",
        "strDescription": "While eating at a restaurant is an enjoyable and convenient occasional treat, most individuals and families prepare their meals at home. To make breakfast, lunch, and dinner daily, these persons must have the required foods and ingredients on hand and ready to go; foods and "
    }
]
    
    return  render(request,'item.html',{'meals':meals})


