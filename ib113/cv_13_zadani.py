from PIL import Image

# Na bile pozadi o zadane velikosti nakreslete cerny ctverec o zadane strane,
# jehoz stred bude umisten do stredu obrazku.

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def square(size=150, a=50):
    im = Image.new("RGB", (size, size), WHITE)

    for x in range(a):
        for y in range(a):
            im.putpixel((x, y), BLACK)

    im.show()

square()


# Nakreslete sachovnicovy vzor o zadane velikosti obrazku a sirce pruhu.


def chessboard(size=240, stripe=30):
    im = Image.new("RGB", (size, size), WHITE)

    for x in range(size):
        for y in range(size):
            if x // stripe == 0:
                if x + y % 2 == 0:
                    im.putpixel((x, y), WHITE)
                im.putpixel((x, y), BLACK)


    im.show()


chessboard()


# Napiste funkci, ktera odstrani z daneho obrazku zelenou barvu (alternativne
# cervenou nebo modrou)


def without_green(filename):
    pass  # TODO


without_green('xmas_tree.jpg')


# Napiste funkci, ktera dany obrazek prevrati vzhledem k jeho vertikalni ose.


def invert(filename):
    pass  # TODO


invert('xmas_tree.jpg')
