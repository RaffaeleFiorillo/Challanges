numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve","thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]

def wallpaper(l, w, h):
    area_to_cover = h*w*2+l*h*2
    print(area_to_cover)
    if not area_to_cover:
        return "zero"
    area_to_cover += area_to_cover*0.15
    print(area_to_cover)
    area_needed = round(area_to_cover/5.2)
    print(area_needed)
    if area_needed <21:
        return numbers[area_needed]
    else:
        return "twenty "+numbers[area_needed-21]

print(wallpaper(4, 3.5, 3))
print(round(5.499))




