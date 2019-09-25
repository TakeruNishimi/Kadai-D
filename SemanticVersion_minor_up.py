class SemanticVersion:
    def __init__(self, major, minor, patch):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __eq__(self, other):
        if not isinstance(other, SemanticVersion):
            NotImplemented
        if (self.major == other.major) and (self.minor == other.minor) and (self.patch == other.patch):
            return True
        return False

    def __str__(self):
        self.version = f'{self.major}.{self.minor}.{self.patch}'
        return self.version

    def patch_version_up(self):
        self.patch += 1
        return SemanticVersion(self.major, self.minor, self.patch)

    def minor_version_up(self):
        self.minor += 1
        self.patch = 0
        return SemanticVersion(self.major, self.minor, self.patch)


def main():
    py370 = SemanticVersion(major=3, minor=7, patch=0)

    py371 = py370.patch_version_up()
    print(SemanticVersion(3, 7, 1) == py371)  # True

    py380 = py371.minor_version_up()
    print(SemanticVersion(3, 8, 0) == py380)


if __name__ == '__main__':
    main()
