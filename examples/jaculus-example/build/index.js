import * as adc from "adc";
import * as gpio from "gpio";
import * as jacserial from "./libs/jacserial.js";
const POT_PIN_1 = 1;
const BTN_PIN = 18;
adc.configure(POT_PIN_1);
gpio.pinMode(BTN_PIN, gpio.PinMode.INPUT_PULLUP);
gpio.on("falling", BTN_PIN, () => {
    jacserial.send(adc.read(POT_PIN_1).toString());
});
