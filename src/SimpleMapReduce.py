import collections
from collections import OrderedDict

class MapReduce():

    def list_of_grades(self, grades):
        grades_array = []
        for grade in grades:
            grades_array.append(grade["score"])

        return grades_array

    def map(self, collection):
        mapped_restaurants = []
        mapped_restaurant = {}
        for restaurant in collection:
            mapped_restaurant["name"] = restaurant["name"]
            mapped_restaurant["grades"] = self.list_of_grades(restaurant["grades"])
            mapped_restaurant["address"] = restaurant["address"]
            mapped_restaurants.append(mapped_restaurant)
            mapped_restaurant = {}

        return mapped_restaurants

    def reduce(self, mapped_restaurants):
        reduced_restaurants = []
        for restaurant in mapped_restaurants:
            if len(restaurant["grades"]) == 0:
                restaurant["grades"] = 0
            else:
                restaurant["grades"] = reduce(lambda x, y: x+y, restaurant["grades"])
            reduced_restaurants.append(restaurant)

        return reduced_restaurants

    def sort(self, reduced_restaurants):
        sorted_dict = {}

        sorted_restaurants_desc = sorted(reduced_restaurants , key=lambda restaurant: restaurant["grades"], reverse=True)

        return sorted_restaurants_desc
