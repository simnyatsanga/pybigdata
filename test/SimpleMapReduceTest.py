from SimpleMapReduce import MapReduce

address = {
  "building":"469",
  "street":"Flatbush Avenue",
  "zipcode":"11225",
  "coord":[
     -73.961704,
     40.662942
  ]
}

other_address = {
  "building":"400",
  "street":"Flatbush Avenue",
  "zipcode":"11225",
  "coord":[
     -73.961704,
     40.662942
  ]
}

def test_map_should_map_one_restaurant_data_item_to_name_grades_kv_pair():
    restaurants_collection = [{"name": "melho", "grades": [{"score": 6},{"score": 4},{"score" :5}], "address": address}]
    mapreduce = MapReduce()

    mapped_restaurants = mapreduce.map(restaurants_collection)

    assert mapped_restaurants == [{"name": "melho", "grades": [6,4,5], "address": address}]

def test_map_should_map_restaurant_collection_to_name_grades_kv_pair():
    restaurants_collection = [{"name": "melho", "grades": [{"score": 6},{"score": 4},{"score" :5}], "address": address},
                              {"name":"tokai", "grades":[{"score": 9},{"score": 9},{"score" :9}], "address":other_address}]
    mapreduce = MapReduce()

    mapped_restaurants_col = mapreduce.map(restaurants_collection)

    assert mapped_restaurants_col == [ {"name": "melho", "grades": [6,4,5], "address": address}, {"name": "tokai", "grades": [9,9,9], "address": other_address} ]

def test_reduce_should_addup_the_grades_for_one_restaurant():
    restaurants_collection = [{"name": "melho", "grades": [{"score": 6},{"score": 4},{"score" :5}], "address": address}]
    mapreduce = MapReduce()

    mapped_restaurants = mapreduce.map(restaurants_collection)
    reduced_restaurants = mapreduce.reduce(mapped_restaurants)

    assert reduced_restaurants == [{"name":"melho", "grades":15, "address": address}]

def test_reduce_should_addup_the_grades_for_a_restaurant_collection():
    restaurants_collection = [{"name": "melho", "grades": [{"score": 6},{"score": 4},{"score" :5}], "address":address},
                              {"name":"tokai", "grades":[{"score": 9},{"score": 9},{"score" :9}], "address":other_address},
                              {"name":"outback", "grades":[{"score": 6},{"score": 8},{"score" :7}], "address": other_address}]
    mapreduce = MapReduce()

    mapped_restaurants = mapreduce.map(restaurants_collection)
    reduced_restaurants = mapreduce.reduce(mapped_restaurants)

    assert reduced_restaurants == [{ "name": "melho", "grades": 15, "address": address }, { "name": "tokai", "grades": 27, "address": other_address }, { "name": "outback", "grades": 21, "address":  other_address}]

def test_reduce_should_put_grade_as_zero_when_restaurant_has_no_grades():
    restaurants_collection = [{"name": "melho", "grades": [], "address":address},
                              {"name":"tokai", "grades":[{"score": 9},{"score": 9},{"score" :9}], "address":address},
                              {"name":"outback", "grades":[{"score": 6},{"score": 8},{"score" :7}], "address":other_address}]
    mapreduce = MapReduce()

    mapped_restaurants = mapreduce.map(restaurants_collection)
    reduced_restaurants = mapreduce.reduce(mapped_restaurants)

    assert reduced_restaurants == [{"name": "melho", "grades": 0, "address": address},{ "name": "tokai", "grades": 27, "address": address}, {"name": "outback", "grades":21, "address": other_address}]

def test_sort_should_sort_the_collection_of_restaurants_in_descending_order():
    restaurants_collection = [{"name": "melho", "grades": [{"score": 9},{"score": 8},{"score" :7}], "address":address},
                              {"name":"tokai", "grades":[{"score": 9},{"score": 9},{"score" :9}], "address": address},
                              {"name":"outback", "grades":[{"score": 6},{"score": 8},{"score" :7}], "address": other_address}]
    mapreduce = MapReduce()

    mapped_restaurants = mapreduce.map(restaurants_collection)
    reduced_restaurants = mapreduce.reduce(mapped_restaurants)
    sorted_restaurants = mapreduce.sort(reduced_restaurants)

    assert sorted_restaurants == [{"name": "tokai", "grades":27, "address": address}, {"name": "melho", "grades":24, "address": address}, {"name": "outback", "grades":21, "address": other_address}]
