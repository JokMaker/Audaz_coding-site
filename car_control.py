#!/usr/bin/env python3

import random

command = ""
started = False
fuel_level = 100  # Starting with full tank
driving_mode = "eco"  # Default driving mode

def check_fuel():
    global fuel_level
    if fuel_level > 0:
        return True
    else:
        print("No fuel! Please refuel.")
        return False

def display_status():
    print(f"Car started: {started}")
    print(f"Fuel level: {fuel_level}%")
    print(f"Driving mode: {driving_mode}")

def drive(distance):
    global fuel_level, started
    if started and fuel_level > 0:
        if driving_mode == "sport":
            fuel_usage = distance * 0.2  # Higher fuel consumption in sport mode
        else:
            fuel_usage = distance * 0.1  # Lower fuel consumption in eco mode

        if fuel_usage > fuel_level:
            print("Not enough fuel for this distance. Car will stop.")
            started = False
            fuel_level = 0
        else:
            fuel_level -= fuel_usage
            print(f"Drove {distance} km. Fuel level: {fuel_level}%")
            if fuel_level == 0:
                print("Fuel exhausted. Car will stop.")
                started = False
    else:
        print("Cannot drive. Ensure the car is started and has fuel.")

def refuel():
    global fuel_level
    amount = int(input("Enter amount of fuel to add (1-100): "))
    if 0 < amount <= 100:
        fuel_level += amount
        if fuel_level > 100:
            fuel_level = 100
        print(f"Car refueled. Current fuel level: {fuel_level}%")
    else:
        print("Invalid amount. Please enter a value between 1 and 100.")

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        elif check_fuel():
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped.")
        else:
            started = False
            print("Car stopped.")
    elif command == "drive":
        if started:
            distance = float(input("Enter distance to drive (in km): "))
            drive(distance)
        else:
            print("Car is not started.")
    elif command == "status":
        display_status()
    elif command == "mode":
        driving_mode = input("Enter driving mode (sport/eco): ").lower()
        if driving_mode in ["sport", "eco"]:
            print(f"Driving mode set to {driving_mode}.")
        else:
            print("Invalid driving mode. Please choose 'sport' or 'eco'.")
            driving_mode = "eco"  # Default back to eco if an invalid mode is chosen
    elif command == "refuel":
        refuel()
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
drive - to drive the car
status - to view car status
mode - to set driving mode (sport/eco)
refuel - to refuel the car
quit - to quit the program
        """)
    elif command == "quit":
        print("Exiting the program. Thank you!")
        break
    else:
        print("Sorry, I don't understand that!")
    print("Press 1 to Exit, or any other number to continue:")
    continue_choice = input()
    if continue_choice == '1':
        print("Thank you for using our car App.")
        break

