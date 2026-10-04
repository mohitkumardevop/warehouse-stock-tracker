# Warehouse Stock Tracker

A command-line Python tool for managing warehouse inventory through a simple menu.

## Features
- View current stock levels
- Add new items or increase quantity of existing ones
- Remove items, with safe handling when the quantity goes to zero or below
- Menu-driven loop that keeps running until the user chooses to quit

## How to run
python stock_tracker.py

## What I learned
- Building a menu-driven program with a while loop
- Using dictionaries to store and update real data
- Safe lookups with .get() to avoid errors on missing items
- Using continue to skip invalid input without crashing
- Cleaning user input with .strip() and .lower()