import * as gpio from "gpio"
import * as jacserial from "./libs/jacserial.js"

const BTN_PIN = 18;

gpio.pinMode(BTN_PIN, gpio.PinMode.INPUT_PULLUP); 


gpio.on("falling", BTN_PIN, () => {
    jacserial.send_RoboPlace_cmd("paint 0 0 red")
});
