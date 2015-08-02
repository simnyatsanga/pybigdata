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
            mapped_restaurant["grades"] = reduce(lambda x, y: x+y, mapped_restaurant["grades"])
            mapped_restaurant["address"] = restaurant["address"]
            mapped_restaurants.append(mapped_restaurant)
            mapped_restaurant = {}

        return mapped_restaurants

    # def map_reduce(self, restaurants):
    #     map_reduced_restaurants = []
    #     map_reduced_restaurants = list(map(self.map_reduce_func, restaurants))
    #     return map_reduced_restaurants
    #
    # def map_reduce_func(self, restaurant):
    #     map_reduced_restaurant = {}
    #
    #     map_reduced_restaurant["name"] = restaurant["name"]
    #     map_reduced_restaurant["grades"] = self.list_of_grades(restaurant["grades"])
    #     map_reduced_restaurant["grades"] = reduce(lambda x, y: x+y, map_reduced_restaurant["grades"]) #reduce the grades to one score
    #     map_reduced_restaurant["address"] = restaurant["address"]
    #
    #     return map_reduced_restaurant

    # def reduce(self, mapped_restaurants):
    #     reduced_restaurants = []
    #     for restaurant in mapped_restaurants:
    #         if len(restaurant["grades"]) == 0:
    #             restaurant["grades"] = 0
    #         else:
    #             restaurant["grades"] = reduce(lambda x, y: x+y, restaurant["grades"])
    #         reduced_restaurants.append(restaurant)
    #
    #     return reduced_restaurants

    def sort(self, reduced_restaurants):
        sorted_dict = {}

        sorted_restaurants_desc = sorted(reduced_restaurants , key=lambda restaurant: restaurant["grades"], reverse=True)

        return sorted_restaurants_desc
