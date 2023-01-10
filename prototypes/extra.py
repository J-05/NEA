def convert_rgb_to_rgba(colour_rgb):
    return (*[x/255 for x in colour_rgb[:3]], colour_rgb[3])

if __name__ == "__main__":
    print(convert_rgb_to_rgba((255, 5, 0, 0.2)))