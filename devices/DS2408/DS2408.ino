// One Wire Slave
// Connected are a LED on Pin 12 and a RGB LED on pin 3 (red), 5 (green) and 6 (blue).
//
// Made by Axel and Michael

#include "OneWireHub.h"
#include "DS2408.h"

const int pin_led = 12;
const int pin_red = 3;
const int pin_gre = 5;
const int pin_blu = 6;
const int pin_onewire = 8;

auto hub    = OneWireHub(pin_onewire);
// Init the emulated devices, set addresses
auto ds2408 = DS2408( DS2408::family_code, 0x00, 0x00, 0x08, 0x24, 0xDA, 0x00 );
auto ds2408r = DS2408( DS2408::family_code, 0x01, 0x00, 0x08, 0x24, 0xDA, 0x00 );
auto ds2408g = DS2408( DS2408::family_code, 0x02, 0x00, 0x08, 0x24, 0xDA, 0x00 );
auto ds2408b = DS2408( DS2408::family_code, 0x03, 0x00, 0x08, 0x24, 0xDA, 0x00 );

void setup() {
  // RGB LED
  pinMode(pin_led, OUTPUT);
  pinMode(pin_red, OUTPUT);
  pinMode(pin_gre, OUTPUT);
  // LED
  pinMode(pin_blu, OUTPUT);
  
  // Setup OneWire
  hub.attach(ds2408);
  hub.attach(ds2408r);
  hub.attach(ds2408g);
  hub.attach(ds2408b);
}

// Current led states. Allows for switching only when values changed.
int state_led = 0;
int state_red = 0;
int state_gre = 0;
int state_blu = 0;

void loop() {
  hub.poll(); // Check the 1 Wire Bus for messages

  // Switch LED on / off if change occured
  int state = ds2408.getPinState();
  if (state != state_led) {
    if (state == 1) {
      digitalWrite(pin_led, HIGH);
    } else {
      digitalWrite(pin_led, LOW);
    }
    state_led = state;
  }
      
  // Set RGB LED voltage level if change occured
  int red = ds2408r.getPinState();
  int gre = ds2408g.getPinState();
  int blu = ds2408b.getPinState();

  if (state_red != red) {
    state_red = red;
    analogWrite(pin_red, 255-red);
  }
  if (state_gre != gre) {
    state_gre = gre;
    analogWrite(pin_gre, 255-gre);
  }
  if (state_blu != blu) {
    state_blu = blu;
    analogWrite(pin_blu, 255-blu);
  }
}
