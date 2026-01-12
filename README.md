# OrbitClock: 3-Body Gravitational Kindle Clock

**OrbitClock** is a dynamic physics simulation and timekeeper designed for e-ink Kindle devices. Unlike a static clock, this project simulates **three celestial bodies** that orbit and gravitationally interact in real time, creating an ever-changing celestial dance around the time display.

The simulation runs entirely on the Kindle hardware, using Newton's law of universal gravitation to calculate the motion of the bodies, with a small potential that attracts them towards the clock. Since the 3-body setup is chaotic, the background will change dynamically over time, and resets when the setup ceases to be a 3-body setup. 


---

## Features

* **Real-time N-Body Simulation:** Three bodies interact via gravity, creating complex, chaotic, and non-repeating orbital patterns.
* **Standalone Operation:** Runs natively on the Kindle; no external web server or internet connection is required once installed.
* **Customizable Physics:** Adjust masses, gravitational constants, and time steps by editing the configuration variables in `bin/clock.py`.
* **E-Ink Optimized:** High-contrast visuals designed for Kindle resolutions (default 1448x1072).

---

## Installation

### 1. Prerequisites
To use OrbitClock, you must first jailbreak your Kindle and install **KUAL** and **MRPI**.
> Refer to [KindleModding.org](https://kindlemodding.org/) for a comprehensive guide on jailbreaking your specific model.

### 2. Prepare the Kindle
* **Disable Deep Sleep:** To prevent the Kindle from pausing the simulation, enter `~ds` in the Kindle search bar. 
    * *Note: You must do this again every time you reboot your device!*
* **Install Python 3:** Ensure you have the [Python 3 package](https://www.mobileread.com/forums/showthread.php?t=225030) installed on your Kindle.

### 3. Install Dependencies
Open **kterm** (Kindle Terminal) on your device and run the following commands:

```bash
python3 -m ensurepip --upgrade
python3 -m pip install pillow
```

###4. Deploying OrbitClock
1. Download all files from this repository into a folder named orbitclock.

2. Connect your Kindle to your computer via USB.

3. Copy the orbitclock folder into the extensions directory on your Kindle.
---
##Usage

1. Open KUAL on your Kindle.

2. Locate OrbitClock and select Launch.

Important: Do not launch multiple instances. There is no multi-launch detection, and the heavy computational workload can make your Kindle unresponsive if run in parallel.

Technical Details
The project uses the Pillow library to render the orbits onto a virtual canvas. Each "tick" of the clock updates the velocity and position vectors of the three bodies according to their mutual gravitational interaction. Because the three-body problem is inherently chaotic, the background of your clock will evolve uniquely over time.
