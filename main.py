from read import readAllFiles
from write import sortSport, separateSports, outputSports

def main() -> None:
    separated_sports = separateSports(readAllFiles())
    sorted_sports = map(sortSport, separated_sports)
    outputSports(sorted_sports)

if __name__ == "__main__":
    main()
