import random

if __name__ == '__main__':

    rgb = ['Red', 'Blue', 'Green']

    float01 = random.random()
    float_n = random.uniform(1, 2)
    int_n = random.randint(2, 3)
    color = random.choice(rgb)
    colors = random.choices(rgb, weights=[3, 2, 1], k=10)
    colors_2 = colors.copy()
    random.shuffle(colors_2)
    colors_3 = random.sample(colors_2, k=3)

    print(float01, float_n, int_n, color, colors, colors_2, colors_3)
