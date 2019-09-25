class SemanticVersion:
    def __init__(self, major, minor, patch):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __str__(self):
        self.version = f'{self.major}.{self.minor}.{self.patch}'
        return self.version


def main():
    py370 = SemanticVersion(3, 7, 0)

    print('3.7.0' == str(py370))


if __name__ == '__main__':
    main()
