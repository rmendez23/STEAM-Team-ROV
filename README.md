# STEAM-Team-ROV
*Code for the Arlington Highschool STEAM Team's Unerwater ROV*

## System Design
* Two raspberry pis communicating over ethernet (via TCP/12345)
* Programmed in python2.7
  * Code may silently fail (client commands will never be parsed by the server) in python 3
### Submarine Pi "Server"
* Static ip address: `10.66.66.1`
* Server listens on port 12345 for a client to connect
  * Only one client allowed at a time
* Controlls motor speed based on commands sent to it by the client.
### Controller Pi "Client"
* Static ip address: `10.66.66.2`
* Connects to `10.66.66.1:12345` over TCP
* Waits for interaction with the usb joystick
  * Sends motor commands to the server
