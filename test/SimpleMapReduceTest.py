from SimpleMapReduce import MapReduce

def test_map_should_map_one_restaurant_data_item_to_name_grades_kv_pair():
    restaurants_collection = [{"name": "melho", "grades": [6,4,5], "address":"some address"}]
    mapreduce = MapReduce()

    mapped_restaurants = mapreduce.map(restaurants_collection)

    assert mapped_restaurants == {"melho":[6,4,5]}

def test_map_should_map_restaurant_collection_to_name_grades_kv_pair():
    restaurants_collection = [{"name": "melho", "grades": [6,4,5], "address":"some address"}, {"name":"tokai", "grades":[9,9,9], "address":"some other address"}]
    mapreduce = MapReduce()

    mapped_restaurants_col = mapreduce.map(restaurants_collection)

    assert mapped_restaurants_col == { "melho": [6,4,5], "tokai": [9,9,9] }

def test_map_should_put_noname_when_restaurant_has_no_name():
    restaurants_collection = [{"name": "", "grades": [6,4,5], "address":"some address"}, {"name":"tokai", "grades":[9,9,9], "address":"some other address"}]
    mapreduce = MapReduce()

    mapped_restaurants_col = mapreduce.map(restaurants_collection)

    assert mapped_restaurants_col == { "noname": [6,4,5], "tokai": [9,9,9] }

def test_reduce_should_addup_the_grades_for_one_restaurant():
    restaurants_collection = [{"name": "melho", "grades": [6,4,5], "address":"some address"}]
    mapreduce = MapReduce()

    mapped_restaurants = mapreduce.map(restaurants_collection)
    reduced_restaurants = mapreduce.reduce(mapped_restaurants)

    assert reduced_restaurants == {"melho":15}

def test_reduce_should_addup_the_grades_for_a_restaurant_collection():
    restaurants_collection = [{"name": "melho", "grades": [6,4,5], "address":"some address"}, {"name":"tokai", "grades":[9,9,9], "address":"some other address"}, {"name":"outback", "grades":[6,8,7], "address":"some other address"}]
    mapreduce = MapReduce()

    mapped_restaurants = mapreduce.map(restaurants_collection)
    reduced_restaurants = mapreduce.reduce(mapped_restaurants)

    assert reduced_restaurants == {"melho":15, "tokai":27, "outback":21}

def test_reduce_should_put_grade_as_zero_when_restaurant_has_no_grades():
    restaurants_collection = [{"name": "melho", "grades": [], "address":"some address"}, {"name":"tokai", "grades":[9,9,9], "address":"some other address"}, {"name":"outback", "grades":[6,8,7], "address":"some other address"}]
    mapreduce = MapReduce()

    mapped_restaurants = mapreduce.map(restaurants_collection)
    reduced_restaurants = mapreduce.reduce(mapped_restaurants)

    assert reduced_restaurants == {"melho":0, "tokai":27, "outback":21}
