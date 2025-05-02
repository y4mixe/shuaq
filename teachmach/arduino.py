import serial
import numpy as np
import cv2
import time

# Open serial port
ser = serial.Serial('COM3', 921600, timeout=1)  # Replace 'COM3' with your port
print("Serial port opened")

def receive_image():
    # Wait for start marker
    start_marker = b'START'
    buffer = b''
    while True:
        if ser.in_waiting > 0:
            byte = ser.read(1)
            buffer += byte
            if start_marker in buffer[-5:]:
                break
    
    # Read dimensions
    width_high = ord(ser.read(1))
    width_low = ord(ser.read(1))
    height_high = ord(ser.read(1))
    height_low = ord(ser.read(1))
    
    width = (width_high << 8) | width_low
    height = (height_high << 8) | height_low
    
    # Receive image data
    image_data = []
    buffer = b''
    end_marker = b'END'
    
    while True:
        if ser.in_waiting > 0:
            byte = ser.read(1)
            
            if byte == b'\x00':  # Escape character
                count = ord(ser.read(1))
                value = ord(ser.read(1))
                image_data.extend([value] * count)
            else:
                image_data.append(ord(byte))
            
            buffer += byte
            if end_marker in buffer[-3:]:
                break
    
    # Remove the end marker from the image data
    image_data = image_data[:-3]
    
    # Convert to numpy array and reshape
    image_array = np.array(image_data, dtype=np.uint8)
    image = image_array.reshape((height, width, 2))
    
    # Convert to BGR format for OpenCV
    return cv2.cvtColor(image, cv2.COLOR_BGR5652BGR)

# Main loop
while True:
    # Request an image
    ser.write