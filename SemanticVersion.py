class SemanticVersion:
    def __init__(self, major, minor, patch):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __eq__(self, other):
        if not isinstance(other,SemanticVersion):
            NotImplemented
        if (self.major == other.major) and (self.minor == other.minor) and (self.patch == other.patch):
            return True
        return False

    def __str__(self):
         self.version = f'{self.major}.{self.minor}.{self.patch}'
         return self.version


def main():
    py370 = SemanticVersion(3, 7, 0)

    print(SemanticVersion(3, 7, 0) == py370)
    print(SemanticVersion(3, 7, 1) == py370)




if __name__ == '__main__':
    main()
