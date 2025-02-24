# Face Recognition Attendance System

## Overview
This project is a Face Recognition-based Attendance System that automates attendance marking using facial recognition technology. It captures images, processes facial features, and maintains an attendance record for enrolled users.

## Features
- Face detection and recognition using OpenCV and deep learning models
- Automated attendance marking
- Database storage for attendance records
- GUI for user interaction
- Live camera feed for real-time recognition

## Requirements
Ensure you have the following dependencies installed before running the project:

- Python 3.x
- OpenCV
- NumPy
- Pandas
- Face Recognition Library
- Streamlit (for GUI)
- SQLite/MySQL (for database storage)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/face-recognition-attendance.git

## Usage
1. Run the face registration script to add new users:
   ```bash
   python register.py
   ```
2. Start the attendance system:
   ```bash
   python main.py
   ```
3. View attendance records (if applicable):
   ```bash
   python view_attendance.py
   ```

## File Structure
```
face-recognition-attendance/
│── dataset/                # Folder containing registered user images
│── models/                 # Pre-trained models for face recognition
│── attendance.db           # Database file (if using SQLite)
│── register.py             # Script for registering new users
│── main.py                 # Main script for running the system
│── view_attendance.py      # Script to view attendance records
│── README.md               # Project documentation (this file)
```

## Future Improvements
- Integration with cloud storage for remote access
- Improved face recognition accuracy with deep learning models
- Web-based UI for better accessibility

## Contributors
- Your Name (sulimangorsi623@gmail.com)

## License
This project is licensed under the MIT License.
