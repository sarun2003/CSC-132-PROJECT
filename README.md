# Occupancy Tracker (CSC-132-PROJECT)
This project is focused on developing an occupancy tracking system that leverages advanced computer vision technologies to monitor and report the number of people in a given space. Utilizing a Raspberry Pi, a webcam, and YOLOv3-tiny object detection algorithm, this system provides real-time occupancy data, which can be essential for maintaining safety standards, optimizing space usage, and enhancing security protocols in various settings such as offices, retail stores, and public venues.

## Description
The Occupancy Tracker is designed to offer a sophisticated yet user-friendly solution for real-time occupancy monitoring. By integrating horizontal motion detector YOLOv3 technology for object detection, the system accurately identifies and counts people entering or exiting a specific area. This technology not only enhances the accuracy of occupancy estimation but also operates efficiently in different lighting conditions and environments. The system's real-time data processing and reporting capabilities make it an invaluable tool for managing and optimizing space utilization, ensuring compliance with occupancy regulations, and contributing to overall safety and security management.

## Getting Started
### Dependencies
- Raspberry Pi (tested on Raspberry Pi 4 Model B)
- Python 3.7 or higher
- RPi.GPIO library
- Webcam compatible with the Raspberry Pi
- YOLOv3-tiny object detection model
- OpenCV library for image processing
- NumPy for numerical computations

### Interface
This code snippet outlines a Python application built using customtkinter, an enhanced version of the standard tkinter library, designed for creating custom user interfaces with a modern look. It also integrates matplotlib for plotting graphs, PIL (Python Imaging Library) for image processing, and other standard Python libraries for handling dates, times, and regular expressions. The application appears to be designed for monitoring and displaying occupancy data, possibly for a store or venue, by analyzing entries in a log file and visualizing them in various forms. Let's break down the key components and functionalities of the code:

Import Section
customtkinter: Used for creating the custom UI components.
PIL (Python Imaging Library): Handles image loading and manipulation.
matplotlib: Generates plots to visualize data within the Tkinter application.
datetime, timedelta: Manages dates and times for data processing and display.
matplotlib.dates: Provides utilities for formatting dates in plots.
tkinter.StringVar: A Tkinter variable class used for managing widget values.
tkinter.messagebox: Displays message boxes for user notifications.
re (Regular Expressions): Parses strings to extract or match patterns of text.

Main Application Window Setup

Initializes the main window (app) with a fixed size and disables resizing.

Configures the application's appearance mode to "light".

Sidebar Setup

Creates a sidebar for additional controls or information display, including a logo loaded from an image file.

Data Processing

Implements a function (process_data_from_file) to read occupancy data from a log file, parse dates, times, and occupancy counts using regular expressions, and store the data in a dictionary for later use.

Main View Setup

Sets up the main view area for displaying information and controls related to occupancy data.

Includes a title frame, a search container for user input (e.g., store name and time range selection), and initializes variables for these inputs.

Graph View and Data Visualization

Provides functionality to reset the graph view to show overall occupancy data over time.

Implements functions to update the graph's title and data based on user inputs, such as the selected store name and time range.

Includes methods to find and display the busiest and least busy periods within the collected data, showing these times and the corresponding occupancy counts to the user.
User Interaction

Sets up entry widgets for user input (store name and time range), with event bindings to update the graph or display information based on these inputs.

Configures a combo box for selecting predefined time ranges, which triggers graph updates.

Graph Initialization and Display

Initializes a matplotlib figure and axis for plotting occupancy data.

Adjusts axis formatting and labels to suit the application's needs (e.g., showing hours and occupancy counts).
E
mbeds the matplotlib graph in the Tkinter interface using FigureCanvasTkAgg.
Execution

Ensures the initial display of the graph with mock or pre-processed data when the application starts.

Enters the Tkinter event loop to start the application, making it responsive to user interactions.

In summary, this application is a sophisticated blend of GUI development with data visualization, designed for interactive analysis and display of occupancy data, demonstrating the integration of multiple Python libraries to create a functional and user-friendly interface.
  
### Installing
- Clone this repository to your local machine using `git clone https://github.com/sarun2003/Occupancy-Tracker.git`.
- Connect the webcam to the Raspberry Pi according to the instructions provided in the hardware directory.
- Download the YOLOv3.tiny and YOLOv3.tiny-weights and place them in the model directory.
- Instructions are provided in the model/README.md.
- Install the required Python libraries by running pip3 install -r requirements.txt.

### Executing the program
- Navigate to the `src` directory.
- Run the occupancy tracking script with python3 occupancy_tracker.py.
- The program will start monitoring the defined space and display the current occupancy count. Adjust the YOLOv3 model parameters as needed for optimal performance.
- Run the Interface for checking the select time range with people entered, and finding peak time, least time.

## Help
For troubleshooting hardware setup or software execution, please consult the troubleshooting guide in the docs directory.
For additional help, you may raise an issue in the repository.

## Authors
- Sandip Thapa
- Sarun Shrestha
- Yechan Kim ( Issac)
- Aaron Larson

## Version History
* 0.1
    * Initial Release - Basic occupancy tracking and reporting.

## License
This project is licensed under the MIT License - see the LICENSE file in the root directory for details.

## Acknowledgments
Special thanks to:
* The CSC-132 professor Joshua Coriell for his guidance and support.
* The Raspberry Pi Foundation for their comprehensive documentation.
* All the contributors who have invested time and effort into making this project beneficial for the visually impaired community.

  
