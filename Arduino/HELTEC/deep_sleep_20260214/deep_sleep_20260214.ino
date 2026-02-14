/**
 * This will allow you to measure battery current in deep sleep. If you reset it
 * will say "deep sleep testing tool", and then if you single-click the user
 * button it will select the user button as a wakeup source and if you
 * double-click it will add the clock as a wakeup source. Then press the button
 * for longer and it will go to deep sleep. So if you just reset and then
 * long-press the user button, there will be no wakeup sources selected and
 * you'll have to reset to wake up again.
 *
 * For measuring current, make sure you measure in series with the battery while
 * USB-C is disconnected.
*/

#include <heltec_unofficial.h>

bool clockWake  = false;

void setup() {
  heltec_setup();
  heltec_ve(true);
  both.println("Deep Sleep");
  both.println("Testing Tool");
}

void loop() {
  heltec_loop();
  delay(10000);
  clockWake = true;
  both.println("clockWake is true");
  if (millis() > 30000) {
//    display.cls();

    // DeepSleep for 30 seconds
    both.println("Going to sleep for 30 seconds");
    both.println("Once this display goes out");
    delay(10000);
    heltec_deep_sleep(30);
  }
}
