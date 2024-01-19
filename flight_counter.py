"""
Flight Counter 

A program that counts the number of flights for an airline given a file of flight data.

NAME: Tommer Ben-Joseph
SEMESTER: Fall 2023
"""
from typing import Dict
import argparse


def load_airlines(filename: str) -> Dict[str, str]:
    """Loads the airlines from the given file and returns a dictionary of airline codes and names.


    Args:
        filename (str): The name of the file to load the airlines from.

    Returns:
        Dict[str, str]: A dictionary of airline codes and names.
    """
    airlines = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split("::")  # Separates the airline from the airline code 
            if len(parts) == 2:
                code, name = parts
                airlines[code] = name
    return airlines


def build_counters(filename: str, airlines: Dict[str, str]) -> Dict[str, int]:  # Function to load airline data from a file and return a dictionary of airline codes and names
    """Builds a dictionary of airline counters from the given file.

    Example:
        >>> build_counters("flights10.dat", {"AA": "American Airlines", \
                                              "DL": "Delta Airlines", "UA": "United Airlines"})
        {'UA': 2, 'DL': 2}

    Args:
        filename (str): The name of the file to load the flights from.
        airlines (Dict[str, str]): A dictionary of airline codes and names.

    Returns:
        Dict[str, int]: A dictionary of airline counters.
    """
    counters = {}
    with open(filename, 'r') as file:
        for line in file:
            airline_code = line[:2]
            if airline_code in airlines:
                counters[airline_code] = counters.get(airline_code, 0) + 1
    return counters


def print_counters(counters: Dict[str, int], airlines: Dict[str, str]) -> None:  # This function below will use a dictionary method to count the number of flights each airline had according to the file we loaded
    """Prints the airline names and their corresponding flight counts in the specified format.

    Args:
        counters (Dict[str, int]): A dictionary of airline counters.
        airlines (Dict[str, str]): A dictionary of airline codes and names.

    Example:
        >>> counters = {"AA": 10, "DL": 5, "UA": 3}
        >>> airlines = {"AA": "American Airlines", "DL": "Delta Air Lines Inc.", "UA": "United Air Lines Inc."}
        >>> print_counters(counters, airlines)
        American Airlines: 10
        Delta Air Lines Inc.: 5
        United Air Lines Inc.: 3

        >>> counters = {"AA": 0, "DL": 12614, "UA": 87506}
        >>> airlines = {"AA": "American Airlines Inc.", "DL": "Delta Air Lines Inc.", "UA": "United Air Lines Inc."}
        >>> print_counters(counters, airlines)
        American Airlines Inc.: 0
        Delta Air Lines Inc.: 12,614
        United Air Lines Inc.: 87,506
    """
    for code, count in counters.items():
        name = airlines.get(code, "Unknown Airline")
        formatted_count = f"{count:,}"  # Formats the flight count with commas to make it look cleaner and easier to read
        print(f"{name}: {formatted_count}")


def main(flights: str, airlines: str) -> None:
    """The main function of the program."""
    airlines_dict = load_airlines(airlines)  # Loads the airline data
    counters = build_counters(flights, airlines_dict)  # Runs the build_counters function to count number of flights per airline
    print_counters(counters, airlines_dict)  # Prints the output of build_counters function


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flight Counter")
    parser.add_argument(
        "-f",
        "--flights",
        help="The file containing the flight data.",
        default="flights10.dat",
    )
    parser.add_argument(
        "-a",
        "--airlines",
        help="The file containing the airline data.",
        default="airlines.dat",
    )
    args = parser.parse_args()
    main(args.flights, args.airlines)
