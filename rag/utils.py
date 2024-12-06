from rag.settings import logger

class TimeConverter:
    """
    A utility class for converting time formats.

    Methods
    -------
    convert_ts(ts: str) -> int
        Converts a time string in the format HH:MM:SS, MM:SS, or SS to total seconds.
    """

    @staticmethod
    def convert_ts(ts: str) -> int:
        """
        Converts a time string to total seconds.

        Parameters
        ----------
        ts : str
            A time string in the format HH:MM:SS, MM:SS, or SS.

        Returns
        -------
        int
            The total number of seconds represented by the time string.

        Raises
        ------
        ValueError
            If the input string is not in a valid time format or cannot be converted.
        """
        try:
            if ts is None or ts.lower() == "none":
                return None

            time_parts = list(map(int, ts.split(":")))
            
            if len(time_parts) == 3:
                h, m, s = time_parts
            elif len(time_parts) == 2:
                h, m, s = 0, time_parts[0], time_parts[1]
            elif len(time_parts) == 1:
                h, m, s = 0, 0, time_parts[0]
            else:
                raise ValueError("Invalid time format")

            total_seconds = h * 3600 + m * 60 + s
            return total_seconds

        except Exception as e:
            logger.error(f"Error converting timestamp '{ts}': {e}")
            raise ValueError(f"Error converting timestamp '{ts}': {e}")
