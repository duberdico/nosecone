import argparse
import numpy as np


class Nosecone:
    def __init__(self, radius, length, n=300, half=False):
        self.radius = radius
        self.length = length
        self.half = half
        self.n = n


class Conic(Nosecone):
    def __init__(self, radius, length):
        Nosecone.__init__(self, radius, length)
        self.y = np.linspace(0, self.length, self.n)
        self.x = (self.length - self.y) * (self.radius / self.length)
        self.x = np.hstack((-self.x, np.flip(self.x)))
        self.y = np.hstack((self.y, np.flip(self.y)))


class Elliptic(Nosecone):
    def __init__(self, radius, length):
        Nosecone.__init__(self, radius, length)
        self.y = np.linspace(0, self.length, self.n)
        self.x = self.radius * np.sqrt(1 - (self.y ** 2 / self.length ** 2))
        self.x = np.hstack((-self.x, np.flip(self.x)))
        self.y = np.hstack((self.y, np.flip(self.y)))


class Parabolic(Nosecone):
    def __init__(self, radius, length, k):
        Nosecone.__init__(self, radius, length)
        self.k = k
        self.y = np.linspace(0, self.length, self.n)
        self.x = self.radius * (
            (
                2 * ((self.length - self.y) / self.length)
                - (self.k * ((self.length - self.y) / self.length) ** 2)
            )
            / (2 - self.k)
        )
        self.x = np.hstack((-self.x, np.flip(self.x)))
        self.y = np.hstack((self.y, np.flip(self.y)))


class Power(Nosecone):
    def __init__(self, radius, length, N, k):
        assert 0 < N < 1
        Nosecone.__init__(self, radius, length)
        self.k = k
        self.N = N
        self.y = np.linspace(0, self.length, self.n)
        self.x = self.radius * ((self.length - self.y) / self.length) ** self.N
        self.x = np.hstack((-self.x, np.flip(self.x)))
        self.y = np.hstack((self.y, np.flip(self.y)))


class Haack(Nosecone):
    def __init__(self, radius, length, C):
        assert 0 < C < 1
        Nosecone.__init__(self, radius, length)
        self.C = C
        self.y = np.linspace(0, self.length, self.n)
        theta = np.arccos(1 - (2 * (self.length - self.y)) / self.length)
        self.x = (self.radius / np.sqrt(np.pi)) * np.sqrt(
            theta - (np.sin(2 * theta) / 2) + (self.C * np.sin(theta) ** 3)
        )

        self.x = np.hstack((-self.x, np.flip(self.x)))
        self.y = np.hstack((self.y, np.flip(self.y)))


class tanOgive(Nosecone):
    def __init__(self, radius, length):
        Nosecone.__init__(self, radius, length)
        # ogive radius
        self.phi = (self.radius ** 2 + self.length ** 2) / (2 * self.radius)
        self.y = np.linspace(0, self.length, self.n)
        self.x = np.sqrt(self.phi ** 2 - self.y ** 2) + self.radius - self.phi
        self.x = np.hstack((-self.x, np.flip(self.x)))
        self.y = np.hstack((self.y, np.flip(self.y)))


class secOgive(Nosecone):
    def __init__(self, radius, length):
        Nosecone.__init__(self, radius, length)
        # ogive radius
        self.rho = (self.radius ** 2 + self.length ** 2) / (2 * self.radius)
        alpha = np.arctan(self.radius / self.length) - np.arccos(
            np.sqrt(self.length ** 2 + self.radius ** 2) / (2 * self.rho)
        )

        self.y = np.linspace(0, self.length, self.n)
        self.x = np.sqrt(
            self.rho ** 2 - (self.rho * np.cos(alpha) - (self.length - self.y)) ** 2
        ) + self.rho * np.sin(alpha)
        # if not self.half:
        self.x = np.hstack((-self.x, np.flip(self.x)))
        self.y = np.hstack((self.y, np.flip(self.y)))


def main(args):
    print(args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Makes nosecone shape")
    parser.add_argument(
        "--shape", type=str, help="nose cone shape", choices=["conic"], required=True
    )
    parser.add_argument("--radius", type=float, help="radius at base", required=True)
    parser.add_argument(
        "--length", type=float, help="length from base to apex", required=True
    )
    args = parser.parse_args()
    main(args)
