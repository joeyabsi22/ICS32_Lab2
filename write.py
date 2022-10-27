import csv
from sportclub import SportClub
from typing import List, Iterable

def separateSports(all_clubs: List[SportClub]) -> Iterable[List[SportClub]]:
    """Separate a list of SportClubs into their own sports

    For example, given the list [SportClub("LA", "Lakers", "NBA"), SportClub("Houston", "Rockets", "NBA"), SportClub("LA", "Angels", "MLB")],
    return the iterable [[SportClub("LA", "Lakers", "NBA"), SportClub("Houston", "Rockets", "NBA")], [SportClub("LA", "Angels", "MLB")]]

    Args:
        all_clubs: A list of SportClubs that contain SportClubs of 1 or more sports.

    Returns:
        An iterable of lists of sportclubs that only contain clubs playing the same sport. 
    """
    sportsDict = {}
    for sportClub in all_clubs:
        if sportClub.getSport() in sportsDict:
            sportsDict[sportClub.getSport()].append(sportClub)
        else:
            sportsDict[sportClub.getSport()] = [sportClub]
    return iter(sportsDict.values())


def sortSport(sport: List[SportClub]) -> List[SportClub]:
    """Sort a list of SportClubs by the inverse of their count and their name

    For example, given the list [SportClub("Houston", "Rockets", "NBA", 80), SportClub("LA", "Warriors", "NBA", 130), SportClub("LA", "Lakers", "NBA", 130)] 
    return the list [SportClub("LA", "Lakers", "NBA", 130), SportClub("LA", "Warriors", "NBA", 130), SportClub("Houston", "Rockets", "NBA", 80)]

    Args:
        sport: A list of SportClubs that only contain clubs playing the same sport

    Returns:
        A sorted list of the SportClubs  
    """
    # hint: check documentation for sorting lists 
    # ( https://docs.python.org/3/library/functions.html#sorted , https://docs.python.org/3/howto/sorting.html#sortinghowto )
    return sorted(sport, reverse=True)


def outputSports(sorted_sports: Iterable[List[SportClub]]) -> None:
    """Create the output csv given an iterable of list of sorted clubs

    Create the csv "survey_database.csv" in the current working directory, and output the information:
    "City,Team Name,Sport,Number of Times Picked" for the top 3 teams in each sport.

    Args:
        sorted_sports: an Iterable of different sports, each already sorted correctly
    """
    with open("survey_database.csv", "w") as outfile:
        outfile.write("City,Team Name,Sport,Number of Times Picked")
        for sport in sorted_sports:
            for i in range(3):
                if i >= len(sport):
                    break
                else:
                    team = sport[i]
                    outfile.write(f"\n{team.getCity()},{team.getName()},{team.getSport()},{team.getCount()}")
