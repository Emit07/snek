
import os
import io
import json

def create(path: str, create_dir):
    """
    Create the database file if the file does not already exist
    """

    if create_dir:
        base_dir = os.path.dirname(path)

        if base_dir == "":
            base_dir = "/"

        if not os.path.exists(base_dir):
            os.makedirs(base_dir)

    # Creates the file
    with open(path, "a"):
        pass

class Storage:

    def __init__(self, path: str, mode="r+", create_dir=False):
        """
        Starts the storage object. if file does not exist, create it.
        Also starts up a simple cache so the  
        """

        self._mode = mode

        # Checks to see if there is any write characters to prevent file being deleted
        # Creates file if does not exist
        if any(character in self._mode for character in ("+", "w", "a")):
            create(path, create_dir=create_dir)

        # Handle object to talk to the file
        self._handle = open(path, "r+")

    # TODO add return type hint
    def read(self):
        # grabs the size to check if file is empty
        size = self.size

        if not size:
            # If file is empty return none, TODO seems like it should show an error or return an empty list
            return None
        else:
            self._handle.seek(0)

            # returns the loaded json content
            return json.load(self._handle)


    # TODO add return type hint
    # TODO add data type hint
    def write(self, data) -> None:
        # Moves cursor to start
        self._handle.seek(0)

        serialized = json.dumps(data, indent=4)

        try:
            self._handle.write(serialized)
        except io.UnsupportedOperation:
            raise IOError("Cannot write. Access mode is \"{0}\"".format(self._mode))

        # make sure file is written
        self._handle.flush()
        os.fsync(self._handle.fileno())

        self._handle.truncate()

    def close(self) -> None:
        """
        Closes the database and ensures that it is disconnected cleanly and properly
        """

        self._handle.close()

    @property
    def size(self) -> None:
        # Returns the size of the database file

        # Moves cusor to the end of file and then returns the length
        self._handle.seek(0, os.SEEK_END)
        return self._handle.tell()

class Cache:

    def __init__(self):

        self.memory = None

    def read(self) -> list:
        return self.memory

    def write(self, value : dict) -> list:
        self.memory = value