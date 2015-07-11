class MapReduce():
    def map(self, collection):
        mapped_restaurant_collection = {}
        mapped_restaurants = {}
        for restaurant in collection:
            if restaurant['name'] == "":
                restaurant['name'] = "noname"

            mapped_restaurants[restaurant['name']] = restaurant['grades']

        return mapped_restaurants

    def reduce(self, mapped_restaurants):
        reduced_restaurants = {}
        for name in mapped_restaurants:
            if len(mapped_restaurants[name]) == 0:
                mapped_restaurants[name] = 0
            else:
                mapped_restaurants[name] = reduce(lambda x, y: x+y, mapped_restaurants[name])

        reduced_restaurants = mapped_restaurants
        return reduced_restaurants
