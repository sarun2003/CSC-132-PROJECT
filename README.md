# Motion Detector for the Visually Impaired (CSC-132-PROJECT)
This project is dedicated to developing a motion detection system that assists visually impaired students in navigating through the college campus.
The system utilizes a Raspberry Pi and a PIR (Passive Infrared) sensor to detect motion and provide auditory alerts for guidance.

## Description
The motion detector aims to provide an additional layer of navigation aid for blind or visually impaired individuals by alerting them to nearby movement. 
This can be especially useful in crowded or dynamic environments where traditional aids like canes or guide dogs may not account for sudden changes in the surroundings.

## Getting Started
### Dependencies
- Raspberry Pi (tested on Raspberry Pi 4 Model B)
- Python 3.7 or higher
- PIR motion sensor
- Speaker or buzzer for auditory feedback
- RPi.GPIO library

### Installing
- Clone this repository to your local machine using `git clone https://github.com/sarun2003/CSC-132-PROJECT.git`.
- Assemble the hardware components according to the schematics provided in the `hardware` directory.
- Install the required Python libraries by running `pip3 install -r requirements.txt`.

### Executing the program
- Navigate to the `src` directory.
- Run the main script with `python3 motion_detector.py`.
- Adjust the sensitivity of the PIR sensor as needed using the potentiometer.

## Help
Should you encounter any issues with hardware setup or software execution, please refer to the troubleshooting guide in the `docs` directory.
For additional help, you may raise an issue in the repository.

## Authors
- Sandip Thapa
- Sarun Shrestha
- Issac Kim
- Aaron Larson

## Version History
* 0.1
    * Initial Release - Basic motion detection and alerting.

## License
This project is licensed under the MIT License - see the LICENSE file in the root directory for details.

## Acknowledgments
Special thanks to:
* The CSC-132 professor Joshua Coriell for his guidance and support.
* The Raspberry Pi Foundation for their comprehensive documentation.
* All the contributors who have invested time and effort into making this project beneficial for the visually impaired community.

  
