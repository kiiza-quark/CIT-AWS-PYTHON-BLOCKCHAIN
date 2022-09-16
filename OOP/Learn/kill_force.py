import os
import sys
import argparse

def kill_process_by_name(process_name):
    """
    """

    #this only works on windows
    command = f"taskkill /f /im {process_name}.exe"
    os.system(command)

def main():
    parser = argparse.ArgumentParser(description="kill proces by name")
    parser.add_argument('-p', '--process_name', help="Enter process to kill")
    args = parser.parse_args(parser)
    