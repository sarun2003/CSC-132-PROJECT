# Occupancy Tracker (CSC-132-PROJECT)
This project is focused on developing an occupancy tracking system that leverages advanced computer vision technologies to monitor and report the number of people in a given space. Utilizing a Raspberry Pi, a webcam, and YOLOv3 object detection algorithm, this system provides real-time occupancy data, which can be essential for maintaining safety standards, optimizing space usage, and enhancing security protocols in various settings such as offices, retail stores, and public venues.

## Description
The Occupancy Tracker is designed to offer a sophisticated yet user-friendly solution for real-time occupancy monitoring. By integrating cutting-edge YOLOv3 technology for object detection, the system accurately identifies and counts people entering or exiting a specific area. This technology not only enhances the accuracy of occupancy estimation but also operates efficiently in different lighting conditions and environments. The system's real-time data processing and reporting capabilities make it an invaluable tool for managing and optimizing space utilization, ensuring compliance with occupancy regulations, and contributing to overall safety and security management.

## Getting Started
### Dependencies
- Raspberry Pi (tested on Raspberry Pi 4 Model B)
- Python 3.7 or higher
- RPi.GPIO library
- Webcam compatible with the Raspberry Pi
- YOLOv3 object detection model
- OpenCV library for image processing
- NumPy for numerical computations

### Interface
- customtkinter library
- PIL (pillow) library
- mathplotlib library
  
### Installing
- Clone this repository to your local machine using `git clone https://github.com/sarun2003/Occupancy-Tracker.git`.
- Connect the webcam to the Raspberry Pi according to the instructions provided in the hardware directory.
- Download the YOLOv3 weights and place them in the model directory.
- Instructions are provided in the model/README.md.
- Install the required Python libraries by running pip3 install -r requirements.txt.

### Executing the program
- Navigate to the `src` directory.
- Run the occupancy tracking script with python3 occupancy_tracker.py.
- The program will start monitoring the defined space and display the current occupancy count. Adjust the YOLOv3 model parameters as needed for optimal performance.

## Help
For troubleshooting hardware setup or software execution, please consult the troubleshooting guide in the docs directory.
For additional help, you may raise an issue in the repository.

## Authors
- Sandip Thapa
- Sarun Shrestha
- Issac Kim
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

  
