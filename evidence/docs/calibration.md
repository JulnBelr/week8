# Light Sensor Calibration

## Calibration Anchors

* **DARK:** `0.133` (raw count: `136`) — Measured by pressing a finger firmly over the LDR to block ambient room light.
* **BRIGHT:** `0.904` (raw count: `924`) — Measured by shining a phone flashlight directly onto the LDR from about 2 cm away.

## Averaging Window Parameters

* **Sample count (`n`):** `16` samples
* **Sampling interval (`T`):** `50` ms
* **Total window length (`n × T`):** `800` ms (`0.8` s)
