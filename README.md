# pi-zero-relay-garage-operator
Python script that creates a Bottle API to control a garage.

Requirements
======
- A Raspberry Pi with GPIO pins

- Jumper Wires

- 5V Relay

- 22 AWG Stranded Tinned Copper Wire

- 8GB Micro SD card minimum.

Wiring Diagram
======
![alt text](/assets/pi_garage_wiring.png)
*Note: sensor is not required as it's not currently used by the API. But if a custom one were to be implemented, 
this is an example of how to do so. I personally ended up using a Zigbee sensor and integrated into Home Assistant.*

Steps
======

(1) - SSH into Pi

```
ssh username@ip
```

(2) - Clone repo
```
git clone https://github.com/johnsonmau/pi-zero-relay-garage-operator.git
```

(3) - CD into Directory
```agsl
cd pi-zero-relay-garage-operator
```
(4) - Download Bottle
```agsl
wget https://www.bottlepy.org/bottle.py
```
(5) - Edit script and add password
```agsl
sudo nano open_close_garage.py
```
on line 16, change default password (xxxx)
```python
pswd = 'xxxx'
```
(6) - Save changes & run script
```
sudo python open_close_garage.py
```

(7) - Test endpoints

GET - http://ipaddress:8080/status

Response JSON
```json
{"res": "garage service is running on garage pi"}
```

POST - http://ipaddress:8080/garage

Request JSON
```json
{"operate": "xxxx"}
```

Successful response JSON
```json
{"res": "success"}
```

Unauthorized response JSON
```json
{"res": "incorrect password"}
```

