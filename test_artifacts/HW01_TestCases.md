# Enchen K8 Pocket Shaver - Test Cases

# Enchen K8 Pocket Shaver - Test Cases

| No | Objective | Input | Steps | Expected | Actual | Verdict |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | Verify power on via lid press | Closed lid | 1 Press the power button on the lid once | Motor starts running and emits a continuous audible hum | Behaved as expected | Pass |
| 2 | Verify power off via lid press | Shaver running | 1 Press the power button on the lid once while running | Motor stops running and sound ceases immediately | Behaved as expected | Pass |
| 3 | Verify shaving effectiveness | Facial hair | 1 Turn on shaver<br>2 Move shaver against facial hair in circular motions | Hair is cleanly shaved without pulling or pain | Behaved as expected | Pass |
| 4 | Verify blade mesh head detachment | Shaver off, attached head | 1 Pull the magnetic mesh head gently away from the body | Mesh head detaches smoothly with moderate resistance | Behaved as expected | Pass |
| 5 | Verify blade mesh head attachment | Shaver off, detached head | 1 Align mesh head with the body and bring it close | Magnetic force snaps the head securely into place | Behaved as expected | Pass |
| **6** | **Verify motor behavior with head detached** | **Shaver off, detached head** | **1 Press the power button** | **Motor does not start for safety reasons** | **Motor instantly spins exposed rotary blades at full speed** | **Fail** |
| **7** | **Verify charging initiation** | **Low battery shaver, Type-C cable, power source** | **1 Plug Type-C cable into the shaver port<br>2 Connect to power source** | **LED indicator turns on to show charging state** | **Fails to charge with 65W PD charger; only works with 5V/1A USB-A cable** | **Fail** |
| 8 | Verify full charge indication | Shaver charging | 1 Leave shaver connected until battery is full | LED indicator changes behavior (turns solid or turns off) to indicate full charge | Behaved as expected | Pass |
| 9 | Verify pass-through operation | Shaver plugged in and charging | 1 Press the power button | Shaver turns on and operates normally while charging | Behaved as expected | Pass |
| **10** | **Verify low battery warning behavior** | **Shaver with very low battery** | **1 Turn on shaver and run until battery is depleted** | **Motor speed should gradually decrease to warn the user before dying** | **Device shuts off completely and instantly without any prior warning** | **Fail** |
| 11 | Verify Type-C cable fit | Type-C cable | 1 Insert and remove cable into the port 3 times | Cable fits snugly without excessive force or wobbling | Behaved as expected | Pass |
| 12 | Verify continuous operation (Boundary) | Fully charged shaver | 1 Turn on shaver and leave it running | Shaver runs continuously until battery depletes | Behaved as expected | Pass |
| **13** | **Verify rapid power button presses (Boundary)** | **Shaver off** | **1 Press the power button 5 times rapidly** | **Shaver toggles state correctly without freezing** | **Logic board freezes with motor running; requires 10s hard reset** | **Fail** |
| 14 | Verify cleaning under running water | Attached mesh head, running water | 1 Turn on shaver<br>2 Rinse the mesh head under running tap water for 10 seconds | Shaver continues to operate, water flows through easily | Behaved as expected | Pass |
| 15 | Verify motor sound and vibration | Shaver running | 1 Turn on shaver and observe | Constant humming sound, moderate vibration, no rattling noise | Behaved as expected | Pass |
| **16** | **Verify magnetic misalignment operation (Edge Case)** | **Shaver off, detached head** | **1 Attach magnetic head slightly off-center so it only catches one magnet<br>2 Press power button** | **Motor should not start, or if it does, it should not strike the plastic housing** | **Internal rotor clips misaligned mesh housing, causing grinding** | **Fail** |
| 17 | Verify charge-state race condition (Edge Case) | Type-C charger, shaver | 1 Rapidly plug and unplug charger while holding down power button | Circuit protection kicks in; shaver safely handles simultaneous inputs without damage | Behaved as expected | Pass |
| 18 | Verify mechanical/thermal overload protection (Edge Case) | Shaver running | 1 Apply excessive downward pressure on blade mesh to force motor to stall | Device detects stall and auto-shutoff triggers to prevent motor burn out | Behaved as expected | Pass |