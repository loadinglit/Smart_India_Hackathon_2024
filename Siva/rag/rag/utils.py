from Siva.rag.rag.settings import logger


class TimeConverter:
    @staticmethod
    def convert_ts(ts: str) -> int:
        """
        Converts a time string to total seconds with enhanced float/decimal handling.

        Parameters
        ----------
        ts : str
            A time string in the format HH:MM:SS, MM:SS, or SS,
            or a numeric string representing total seconds.

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

            # Handle numeric strings (including floats)
            try:
                # First, try converting to float and then to int
                if "." in ts:
                    total_seconds = int(float(ts))
                    minutes = total_seconds // 60
                    seconds = total_seconds % 60
                    return total_seconds
            except ValueError:
                pass

            # Original time format conversion logic
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
