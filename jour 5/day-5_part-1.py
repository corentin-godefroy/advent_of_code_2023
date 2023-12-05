import math

def map_tranform(start, map):
    destination = start
    for interval in map:
        if start < int(interval[1]) + int(interval[2]) and start >= int(interval[1]):
            destination = int(interval[0]) + (start - int(interval[1]))
    print(str(start) + str(map) + str(destination))
    return destination

if __name__ == "__main__":
    input = open("input.txt").readlines()
    seeds = input.pop(0).removeprefix("seeds: ").split()
    seed_to_location = seeds
    input.append("\0")
    seed_to_soil_map = []
    soil_to_fertilizer_map = []
    fertilizer_to_water_map = []
    water_to_light_map = []
    light_to_temperature_map = []
    temperature_to_humidity_map = []
    humidity_to_location_map = []
    i = 0
    while i < len(input):
        match input[i]:
            case "seed-to-soil map:\n":
                i += 1
                while input[i] != "\n" and i < len(input):
                    seed_to_soil_map.append(input[i].split())
                    i += 1
                continue
            case "soil-to-fertilizer map:\n":
                i += 1
                while input[i] != "\n" and i < len(input):
                    soil_to_fertilizer_map.append(input[i].split())
                    i += 1
                continue
            case "fertilizer-to-water map:\n":
                i += 1
                while input[i] != "\n" and i < len(input):
                    fertilizer_to_water_map.append(input[i].split())
                    i += 1
                continue
            case "water-to-light map:\n":
                i += 1
                while input[i] != "\n" and i < len(input):
                    water_to_light_map.append(input[i].split())
                    i += 1
                continue
            case "light-to-temperature map:\n":
                i += 1
                while input[i] != "\n" and i < len(input):
                    light_to_temperature_map.append(input[i].split())
                    i += 1
                continue
            case "temperature-to-humidity map:\n":
                i += 1
                while input[i] != "\n" and i < len(input):
                    temperature_to_humidity_map.append(input[i].split())
                    i += 1
                continue
            case "humidity-to-location map:\n":
                i += 1
                while i < len(input) and input[i] != "\n" and input[i] != "\0":
                    humidity_to_location_map.append(input[i].split())
                    i += 1
                continue
            case "\n":
                i += 1
            case other:
                break

    minimal = math.inf

    for seed in seed_to_location:
        seed = int(seed)
        soil = map_tranform(seed, seed_to_soil_map)
        fertilizer = map_tranform(soil, soil_to_fertilizer_map)
        water = map_tranform(fertilizer, fertilizer_to_water_map)
        light = map_tranform(water, water_to_light_map)
        temperture = map_tranform(light, light_to_temperature_map)
        humidity = map_tranform(temperture, temperature_to_humidity_map)
        location = map_tranform(humidity, humidity_to_location_map)
        if location < minimal:
            minimal = location
    print(minimal)


