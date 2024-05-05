# Attendance-System-using-QR-scan
I created a sheet to store student information including their name, roll number, date of birth, and gender. During the generation phase, I established a database connection using a database connector to read data from the database. To generate and decode QR codes, I used the PyZbar library which is a comprehensive tool for QR code operations. All the QR codes that were uniquely defined were then stored in a folder with their respective roll numbers.

In the QR code scanning phase, we captured an image of the generated QR code. We used OpenCV to scan the QR code, and PyZbar was employed to record and store the attendance information. This attendance data was then stored in a file that was associated with the student's name and roll number.
