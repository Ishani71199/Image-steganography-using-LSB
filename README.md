# Image Steganography using LSB
## Defination:
Steganography is the art of hiding a message. The purpose of the steganography is to hide a message from someone you don't want to see it. It is different from cryptography, the art of writing, which is intended to make a message cannot be read, but does not hide the existence of the secret communication.
## Types of steganography:
* Text Steganography
* Image Steganography
* Video Steganography
* Audio Steganography
* Network Steganography
* Email Steganography
## Process of steganography:
![steganography-tutorial-how-to-hide-text-inside-the-image-cybersecurity-training-edureka-13-638 (1)](https://user-images.githubusercontent.com/55583932/125614121-37db0400-d663-47eb-8829-de3c7014f813.png)
### Few points abount pixel:
* Each pixel in the image has 3 bits, one each for RGB frame.
* These three RGB compopnents are three 8-bits numbers for each pixel.
* Each 8-bit RGB component can have 256 possible values(0-255).</br>
![Screenshot (83)](https://user-images.githubusercontent.com/55583932/125614997-9fdfc7dc-1ad0-48ee-84d2-630a4f130551.png)
![0_yARnljvGACzlItk-](https://user-images.githubusercontent.com/55583932/125615223-af7f2cfa-3ea6-4eae-b625-fcc38f65a506.png)
## pixels = [p1, p1, p1, p2, p2, p2, p3, p3, p3, ...]
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;    R &nbsp; &nbsp; &nbsp; G &nbsp; &nbsp; &nbsp; B &nbsp; &nbsp; &nbsp; R &nbsp; &nbsp; &nbsp; G &nbsp; &nbsp; &nbsp; B &nbsp; &nbsp; &nbsp; R &nbsp; &nbsp; &nbsp; G &nbsp; &nbsp; &nbsp; B<br/>
Since each pixel is described with three pieces of information, it takes up three slots on pixel array.<br/><br/>
## Why to change LSB and not MSB?
![0_z2XIiLwo7ZKGsWhw](https://user-images.githubusercontent.com/55583932/125647607-a38b0ca5-3fb9-4f3f-906c-6dc8f8d7f95a.png)

## Overview of the code:
The data is represented using its ASCII value. Each letter is represented using 8 bits, or 1 byte. Each pixel in the image has three bits, one each for RGB frames. Each pixel can hold 3 bits. We will encode three pixels together, making a place for 9 bits. Out of the 9 bits, we will store 1 letter in the 8 bits and one (End Of File)EOF bit. If the EOF bit is high, then it indicates that the end of the message has been reached. Otherwise, it indicates the program to read more pixels for decoding.<br/>
We have a simple encryption technique included in the algorithm above. Instead of encoding 3 letters together, we can encode any other number of letters. Unless anyone knows this number, decrypting the file is going to be tough.<br/>
