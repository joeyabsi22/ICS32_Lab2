import os
from pathlib import Path
import csv
from sportclub import SportClub
from typing import List, Tuple


def readFile(file: Path) -> List[Tuple[str, str, str]]:
    """Read a CSV file and return its content

    A good CSV file will have the header "City,Team Name,Sport" and appropriate content.

    Args:
        file: a path to the file to be read

    Returns:
        a list of tuples that each contain (city, name, sport) of the SportClub

    Raises:
        ValueError: if the reading csv has missing data (empty fields)  
    """
    teams = []
    with open(file, 'r') as f:
        reader = csv.reader(f)
        header = True
        for line in reader:
            if len(line) != 3 or not (line[0] and line[1] and line[2]):
                raise ValueError()
            if header:
                if line != ["City", "Team Name", "Sport"]:
                    raise ValueError()
                header = False
                continue
            teams.append(tuple(line))
    return teams


def readAllFiles() -> List[SportClub]:
    """Read all the csv files in the current working directory to create a list of SportClubs that contain unique SportClubs with their corresponding counts

    Take all the csv files in the current working directory, calls readFile(file) on each of them, and accumulates the data gathered into a list of SportClubs.
    Create a new file called "report.txt" in the current working directory containing the number of good files and good lines read. 
    Create a new file called "error_log.txt" in the current working directory containing the name of the error/bad files read.

    Returns:
        a list of unique SportClub objects with their respective counts
    """
    sport_clubs = []

    good_files = 0
    lines_read = 0
    bad_files = []
    #Path("survey_database.csv").unlink(missing_ok = True)
    csv_files = Path.cwd().glob("*.csv")
    for csv_file in csv_files:
        try:
            teams = readFile(csv_file)
            good_files += 1  # the file is good
            lines_read += len(teams)
            for team in teams:
                team = SportClub(team[0], team[1], team[2], 1)
                found = False
                for club in sport_clubs:
                    if club.getCity() == team.getCity() and club.getSport() == team.getSport() and club.getName() == team.getName():
                        club.incrementCount()
                        found = True
                        break
                if not found:
                    sport_clubs.append(team)

        except ValueError:
            bad_files.append(csv_file)

    with open("report.txt", "w") as report:
        report.write(f"Number of files read: {good_files}\n")
        report.write(f"Number of lines read: {lines_read}\n")

    with open("error_log.txt", "w") as error_log:
        for file in bad_files:
            error_log.write(f"{file.name}\n")

    return sport_clubs
