class SportClub:
    """A simple class to store and handle information about SportClubs.

    Attributes:
        city (str): The city the SportClub is based in.
        name (str): The name of the SportClub.
        sport (str): The sport the club plays.
        count (int): The amount of time the SportClub has been seen.

    Todo:
        complete the __eq__ and __lt__ functions of this class
    """
    def __init__(self,  city: str = "", name: str = "", sport: str= "", count: int = 0) -> None:
        """Make a SportClub.

        Args:
            city: The city the SportClub is based in.
            name: The name of the SportClub.            
            sport: The sport the club plays.
            count: The amount of time the SportClub has been seen.

        """
        self.setCity(city)
        self.setName(name)
        self.setSport(sport)
        self.count = count

    def setName(self, name: str) -> None:
        """Set the name of the SportClub.

        Args:
            name: Name of the SportClub.
        """
        self.name = name

    def setCity(self, city: str) -> None:
        """Set the city the SportClub is based in.

        Args:
            city: The city the SportClub is based in.
        """
        self.city = city

    def setSport(self, sport: str) -> None:
        """Set the sport the club plays.

        Args:
            sport: The sport the club plays.
        """
        self.sport = sport

    def getName(self) -> str:
        """Get the name of the SportClub.

        Returns:
            A formatted version of the private attribute name.
        """
        return self.name.title()

    def getCity(self):
        """Get the city the SportClub is based in.

        Returns:
            A formatted version of the private attribute city.
        """
        return self.city.title()

    def getSport(self):
        """Get the sport the club plays.

        Returns:
            A formatted version of the private attribute sport.
        """
        return self.sport.upper()

    def getCount(self):
        """Get the total times the SportClub has been seen.

        Returns:
            A copy of the attribute count
        """
        return self.count

    def incrementCount(self) -> None:
        """Increment the times the SportClub has been seen by 1.
        """
        self.count += 1

    def __hash__(self) -> int:
        """Get the hash of current object.

        Returns:
            Hash of the object
        """
        unique_identifier = (self.getCity(), self.getName(), self.getSport())
        return hash(unique_identifier)

    def __str__(self) -> str:
        """Get the string version of current object.

        Returns:
            str summary of the object
        """
        return f"Name: {self.getCity()} {self.getName()}, Sport: {self.getSport()}, Count: {self.getCount()}"

    def __eq__(self, o: object) -> bool:
        """Check if another object is equal to self.

        Returns:
            True if they are equal, False otherwise
        """
        # hint: object o may not be of type SportClub.
        # check documentation ( https://docs.python.org/3/reference/datamodel.html#object.__eq__ )
        return True

    def __lt__(self, o: object) -> bool:
        """Check if self is less than another object.

        Returns:
            True if self is less than o, False otherwise
        """
        # hint: object o may not be of type SportClub.
        # check documentation ( https://docs.python.org/3/reference/datamodel.html#object.__lt__ )
        if self.getCount() != o.getCount():
            return self.getCount() < o.getCount()
        else:
            return self.getName() > o.getName()