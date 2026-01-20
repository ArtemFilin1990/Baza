Linear Motor System
Technical Information
線性馬達系統
技術手冊
Linear Motor System
Technical Information

---

INDUSTRIE 4.0 Best Partner
Multi Axis Robot
Pick-and-place / Assembly / 
Grinding and Polishing / Semiconductor / 
Light Industry / Automotive industry / 
Food industry
• Articulated Robot
• Delta Robot
• Movable Delta Robot
• SCARA Robot
• Wafer Robot
• Electric Gripper 
Single Axis Robot
Precision / Semiconductor /
Medical / FPD
• KK, SK
• KS, KA 
• KU, KE, KC 
Medical Equipment
Hospital / Rehabilitation centers /
Nursing homes
• Robotic Gait Training System
• Hygiene System
• Robotic Endoscope Holder
Ballscrew
Precision Ground / Rolled
• Super S series
• Super T series
• Mini Roller
• Ecological & Economical 
lubrication Module E2
• Rotating Nut (R1)
• Energy-Saving & Thermal-
Controlling (C1)
• Heavy Load Series (RD) 
Linear Guideway
Automation / Semiconductor / Medical
• Ball Type--HG, EG, WE, MG, CG
• Quiet Roller Type--QH, QE, QW, QR
• Other--RG, E2, PG, SE, RC
Direct Drive 
Rotary Table
Aerospace / Medical / Auto industry
• RAB Series
• RAS Series
• RCV Series
• RCH Series
Bearing
Machine tools / Robot
• Crossed Roller Bearings 
• Ball Screw Bearings 
• Linear Bearing
• Support Unit
AC Servo Motor & Drive
Semiconductor / Packaging machine /
SMT / Food industry / LCD
• Drives-D1, D1-N, D2 
• Motors-50W~2000W 
Torque Motor 
(Direct Drive Motor)
Inspection / Testing equipment / 
Machine tools/ Robot
• Rotary Tables-TMS,TMY,TMN
• TMRW Series
Linear Motor
Automated transport / AOI application / 
Precision / Semiconductor
• Motor type-ironcore motor, ironless   
   motor, planar servo motor, shaft motor 
• Air bearing stage 
• X-Y stage 
• Gantry stage
Positioning 
Measurement System
Cutting machines / 
Traditional gantry milling machines / 
Programmable drilling machines
• High Resolution
• Signal Translator
• High-precision Enclosed
• High Efficiency Counter

---

1.Technical Information
04
Appendix
115
Brief Introduction to proper nouns.
A sampling of customized solutions is shown here. With various 
combinations of standard single axis stage, it may constitute a 
number of different linear stages. We can also provide customized 
products according to customer demand.
Brief introduction to HIWIN standard drive D1 and D1-N.
The inquiry form at the end of this catalogue helps us know 
customer’s demand, so that we can make a preliminary design.
2.Standard linear motor stage
06
3.Customized positioning stage
66
4.Drives
101
Standard single, X-Y, gantry and air bearing stages are constructed 
by ironcore or ironless motor. 
HIWIN can quickly provide the following products：
2.1   Positioning stage ______________________________ 6
2.2   SA:low center of gravity, high payload _____________ 8
2.3   LMC:high-precision, high-speed stability _________ 26
2.4   LMT:lightweight, high acceleration/deceleration ___ 38
2.5   X-Y stage____________________________________ 54
2.6   Gantry stage_________________________________ 59
2.7   Air bearing stage _____________________________ 62

A：  Motor sizing ________________________________ 115
B：  Optional regeneration resistors________________ 118
C：  Inquiry form (Mechanical system) ______________ 120
D：  Inquiry form (Electronical control system) _______ 121
Linear motor system
Contents
LMC：high-precision, high-speed stability
Linear motor LMC stages are equipped with coreless motor(s) and well suited for applications 
that require precision positioning and constant velocity scanning motion.
SA：low gravity center, high payload
Linear motor SA stages are equipped with ironcore motor(s) and well suited for applications that 
require point to point precision positioning and larger payload.
LMT：middle precision, light payloads
Linear motor LMT stages are equipped with a coreless shaft motor, which perfectly replace the 
combination of ball screw and AC servo motor, and improve max. speed greatly.

---

MM99TE07-1701
Linear Motor System
4
5
Technical
1.1	 Glossary
Back emf constant (K v)
This is the ratio of the back emf voltage (rms) to the mo-
tor rotational speed or linear speed (rpm or m/s). The 
back emf is the electromagnetic force, which is created 
at the movement of the coil in the magnetic field of per-
manent magnets, e.g. in a servo motor.
Acceleration
This is the speed change per time unit, i.e., acceleration 
= speed / time or a = v / t.
Acceleration time
This is defined as the time a drive requires from start 
until achieving maximum speed.
Vertical straightness
The measure of straightness when moving in X-axis. If 
there is deviation in vertical straightness, there would be 
positioning error in Z-axis, as the system moves along X-
axis.
Torque
This is a measurement of the rotational movement in a 
body and consequently a vectorial direction that can be 
expressed in the following cross product:
The torque is expressed in the equation Nm = kg x m²/s².
Repeatability
Repeatability should not be confused with absolute accu-
racy. A linear axis can have medium accuracy, but have 
good repeatability. Uni-directional repeatability can be 
measured in a way, that a target position is approached 
multiple times from an appropriately distance and the 
same approaching direction. In this way, the backlash 
will not have any effect. For measurement of bi-direc-
tional repeatability, the target position is approached 
from different directions, in which case the backlash will 
take effect.
Motor constant (K m) 
This designates the ratio of generated force and 
dissipation power,represents the efficiency of the motor. 
Stiffness
This corresponds to the mechnical resistance to defor-
mation a part or an assembly can provide under external 
static payload. (static stiffness) Or, it is the elastic resis-
tance to deformation a part or an assembly can provide 
under external dynamic payload. (dynamic stiffness)
Horizontal straightness
The measure of straightness when moving in X-axis. If 
there is deviation in horizontal straightness, there would 
be positioning error in Y-axis, as the system moves along 
X-axis.
Guide deviation
This is the deviation from the axis of stroke. It depends 
on horizontal straightness (also straightness) and verti-
cal straightness (also flatness).
Force, torque
Force (in linear movements) or torque (in rotational mo-
vements) is given for defined conditions, e.g., as continu-
ous force or torque at:
 20 °C ambient temperature
 80 °C winding temperature
 100% rate of loading(duty cycle)
or as peak force or peak torque.
Force constant (K f)
This is a coil specific constant. The motor output force 
can be calculated by multiplying the force constant of the 
motor by input current: F = I x K f
Continuous torque, continuous force (Fc)
Or also nominal torque, nominal force. This is the torque 
or force, that rotary or linear motors can produce in con-
tinuous operation when continuous current of 100% load 
rate(duty cycle) is applied to the motor coil.
Continuous current (I c)
It is a current that flows over longer time into motor. 
The maximum allowed current into each coil is also cal-
led nominal current. It is characterized when the gene-
rated heat results in motor warming of up to 80 °C.  
Resolution
It is the smallest distance, that the position measuring 
system will detect. The reachable step size is, in prin-
ciple, larger than resolution due to other additional fac-
tors.
Eccentricity
This is the deviation of the center point of rotation of ro-
tary tables from their position during rotation. It is crea-
ted by centering and bearing tolerances.
1  Technical Information
Step size
Also called resolution. It is the smallest possible movement 
of a system. It depends on encoder, amplifier, mechanical 
construction, backlash, etc.
Accuracy
This, or actually the better terminology, the inaccuracy, 
corresponds to the deviation between target and actual 
position. The accuracy along an axis is defined as the re-
maining difference of target and actual position, after other 
linear deviations are excluded. Such systematic or linear 
deviations can be caused by  cosine error, angle deviation, 
ball screw error, thermal expansion, etc. For all target po-
sitions of interest in an application, it is calculated with the 
following formula:
Maximum of sum of systematic target-actual-difference 
+ 2 sigma (standard deviation)
Please do not confuse accuracy with repeatablity.
Attraction force (Fa)
This is created between the primary and secondary parts of 
the ironcore linear motors which must be taken up by the 
guide.
Winding resistance R25
This is the coil-specific dimension of is the winding 
resistance at 25°C. At 80°C, the winding resistance increas-
es to approximately 1.2 x R25.
Winding temperature (T)
This is the permitted winding temperature. The actual 
motor temperature is dependent on the installation, cooling 
and operating conditions and consequently can only be 
determined in a concrete case and cannot be calculated.
Wobbling
It is a term for rotary motor. Wobble is the angular deviation 
of rotating axis from theoretical axis of rotation as the mo-
tor turns. The reason for it is possibly bearing tolerances.
Peak current (I p)
This current is applied to coils for a short time to generate 
peak force.The maximum time for applying peak current 
is 1 second. After that, motor has to cool down to nominal 
operating temperature, before further peak current could 
be applied again.
Peak torque, peak force (Fp)
The peak torque (for rotary motion) or peak force 
(for linear motion) is the maximum force that a mo-
tor can generate for approximately one second with 
peak current Ip. While applying Ip into motor, it is 
operating near the non-linear range of motor. This 
is especially useful for acceleration and braking.

---

MM99TE07-1701
Linear Motor System
6
7
Standard
HIWIN offers a variety of positioning stages, such as single axis, X-Y double axis, bridge, gantry and X-Y-
Z-axis Cartesian robots, to meet a variety of automation application needs. All above positioning stages 
use self-made key components, such as linear motors, linear slide, ball screw, direct drive motors, servo 
motors and drives. Therefore, HIWIN positioning stages can achieve the best performance and the most 
effective cost, can significantly enhance the competitiveness of our customers. HIWIN’s diversified 
positioning stages have been widely used in various technical fields, such as optical detection, laser 
processing, plastic material coating, metal processing and other automated production equipment. 
Industrial fields cover semiconductor industry, optical elements, panel displays, medical equipment, 
machine tools, electronic components, MEMS and so on. 
Rich specifications and quick customized ability to fully meet customers mass production, shorten product 
development process and strict application environment, high specification requirements.
2  Standard linear motor stage
2.1  Positioning stage
2.1.1  Single axis positioning stage
HIWIN single axis positioning stage provides fast, accurate positioning, linear direct drive motor and can 
reach long stroke applications, in addition to providing metal cover, dust jacket and other optional items 
to achieve dust protection requirements. Choose cable chain type, horizontal or vertical wiring that uses 
extension cords not to scatter outside, make the machine look tidy.
Depend on different linear motors, those can be further divided into the following different types: 
SA：low gravity center, high payload 
Linear motor SA stages are equipped with ironcore 
motor(s) and well suited for applications that require 
point to point precision positioning and larger payload.
LMC：high-precision, high-speed stability
Linear motor LMC stages are equipped with coreless 
motor(s) and well suited for applications that require 
precision positioning and constant velocity scanning 
motion.
LMT：middle precision, light payload
Linear motor LMT stages are equipped with a coreless 
shaft motor, which perfectly replace the combination of 
ball screw and AC servo motor, and improve max. speed 
greatly.

---

MM99TE07-1701
Linear Motor System
8
9
Standard
2.1.2  Measurement standards
2.1.3  Cable chains: horizontal/vertical orientation
All the precision measurement data provided by HIWIN are measured at temperature at 23 ℃±1 ℃, 
humidity at 55%±5% environmental, and the position feedback system of positioning stages apply 1µm 
resolution optical scale.
Cable chain horizontal orientation
Cable chain vertical orientation
動子規
格標籤
動子規
格標籤
Linear
Motor
Linear
Motor
2.2  SA low gravity center, high payload
Linear motor SA stages are equipped with ironcore motor(s) and well suited for applications that require 
point to point precision positioning and larger payload.
　It offers larger continuous force, especially for larger force and fast applications
　Stroke range up to 4m
　Superior speed control characteristic
 Low cost, small size, high performance
 Suitable for clean rooms
2.2.1  SA
LMX1A–SA11–1–800–G 1 E–V1 3-CL
Stage type
LMX1A
Motor type
SA11: LMSA11
SA12: LMSA12
SA13: LMSA13
SA21: LMSA21
SA22: LMSA22
SA23: LMSA23
SA31: LMSA31
SA32: LMSA32
SA33: LMSA33
The number of slider
1: 1
Stroke
100: 100mm
200: 200mm
300: 300mm
400: 400mm
500: 500mm
Encoder type
0:None
A:40µm analogical 1Vpp optical scale
E:TTL digital 1µm resolution magnetic scale 
G:TTL digital 1µm resolution optical scale(standart)
K:TTL digital 0.1µm resolution optical scale 
Limit switch
1:Inductive type，PNP，NC
2:Inductive type，NPN，NC
C:Customized
Limit switch connector type
E:Connector is mounted on edge of stage
S:Connector contains 300mm extension cord
Cable chain
N:None
V1:Vertical, chain internal space is 21x25mm 
V2:Vertical, chain internal space is 21x38mm
V3:Vertical, chain internal space is 21x50mm
V4:Vertical, chain internal space is 21x68mm
H1:Horizontal, chain internal space is 21x25mm 
H2:Horizontal, chain internal space is 21x38mm
Extension cable
0:None
3:3m
5:5m
7:7m
(Includes limit switch extension cable)
Additional option
None:Standard
C:Customized request
CL:Centralized lubrication
Note：Contact HIWIN for customized specification.
SA21L: LMSA21L
SA22L: LMSA22L
SA23L: LMSA23L
SA31L: LMSA31L
SA32L: LMSA32L
SA33L: LMSA33L
600: 600mm
700: 700mm
800: 800mm
900: 900mm
1000: 1000mm

---

MM99TE07-1701
Linear Motor System
10
11
Standard
High acceleration/deceleration
Acceleration / deceleration up to 140 m/s2 (14G).
Actual acceleration / deceleration might be limited by 
linear guideway life consideration.
High static stability
Position stability is within ±0.1µm (measured by 
laser interferometer, the result is depended on 
environment condition.).
Low profile
SA series stage reduced maximum 38% stage height. 
High force
SA series stage offers maximum 2469N peak force.
-200
-150
-100
-50
0
50
100
150
200
0
0.1
0.2
0.3
0.4
加速度(m/s2)
時間(s)
-0.4
-0.3
-0.2
-0.1
0
0.1
0.2
0.3
0.4
0
1
2
3
4
位置誤差(µm)
時間(s)
103
205
308
181
362
544
292
583
875
289
579
868
512
1023
1535
823
1646
2469
0
500
1000
1500
2000
2500
LMSA11
LMSA12
LMSA13
LMSA21
LMSA22
LMSA23
LMSA31
LMSA32
LMSA33
推力(N)
瞬間推力
連續推力
linear motor stage
linear motor stage
linear motor stage
linear motor stage
linear motor stage
linear motor stage
Instant thrust
Continuous thrust
Thrust
Time
Time
Acceleration 
Position error
0
200
400
600
800
1000
0
1
2
3
4
5
6
推力(N)
速度(m/s)
SA12 Fp
SA12 Fc
0
200
400
600
800
1000
0
1
2
3
4
5
6
推力
速度(m/s)
SA11 Fp
SA11 Fc
(N)
0
200
400
600
800
1000
0
1
2
3
4
5
6
推力
速度(m/s)
SA13 Fp
SA13 Fc
(N)
0
200
400
600
800
1000
0
1
2
3
4
5
6
推力
速度(m/s)
SA11 Fp
SA11 Fc
(N)
0
200
400
600
800
1000
0
1
2
3
4
5
6
推力(N)
速度(m/s)
SA12 Fp
SA12 Fc
0
200
400
600
800
1000
0
1
2
3
4
5
6
推力
速度(m/s)
SA13 Fp
SA13 Fc
(N)
0
10
20
30
40
50
0
5
10
15
20
25
30
35
加速度(m/s 2)
負載(kg)
SA11
0
10
20
30
40
50
60
0
5
10
15
20
25
30
35
加速度(m/s 2)
負載(kg)
SA12
0
10
20
30
40
50
60
0
5
10
15
20
25
30
35
加速度(m/s 2)
負載(kg)
SA13
F-V曲線(DC bus = 325V)
F-V曲線(DC bus =600V)
A-Load曲線
Table2-1   SA11,12,13 stage specification
Specification
SA11
SA12
SA13
Continuous force,FC (N)
103
205
308
Peak force,FP (N)
289
579
868
Stroke (mm)
100~1000(mm)
Resolution
0.1µm / 1.0µm / Analog 1Vpp
Repeatability (µm) *2
Digital 1µm encoder / Analog encoder: ± 1
Digital 0.1µm encoder: ± 0.5
Accuracy (µm) *2,3
Digital 1µm encoder / Analog encoder: ± 2
Digital 0.1µm encoder: ± 1
Horizontal straightness (µm)
10 / 500 mm
Vertical straightness (µm)
20 / 500 mm
Moving mass (kg)
5
6
8
Loading capacity (kg)
10
20
30
SA11,SA12,SA13
2.2.2  SA series stage
*1：All values are measured on a granite table, all stage mounting  
         holes are well fixed.
*2：Values are measured according to HIWIN measuring standard.
*3：After error compensation.
*4：The Force-Velocity Curve is the characteristic curve of the motor. 
         The actual velocity will change with stroke, payload and acceleration.
         Please refer to the Velocity-Stroke Curve or Appendix A：Motor Sizing.
*5：All specifications above are standard, contact HIWIN for special request.
Acceleration 
Acceleration 
Acceleration 
Force
Force
Force
Force
Force
Force
Velocity
Velocity
Velocity
Velocity
Velocity
Velocity
Payload
Payload
Payload
Force-Velocity Curve(DC bus = 325V)
*4
Force-Velocity Curve(DC bus = 600V)
*4
Acceleration-Payload Curve

---

MM99TE07-1701
Linear Motor System
12
13
Standard
*1：All values above are standard, contact HIWIN for special request.
*2：Cantilever load capability due to different positioning stage, application rated life also vary.
*3：The main reason for lifetime derives from linear guideway. For more details, please refer to HIWIN linear guideway catalog.
Velocity-Stroke Curve
Cantilever Load Capability*2.3 
Vertical
Horizontal
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
0
200
400
600
800
1000
Velocity (m/s)
Stroke (mm)
SA11
Load 1 kg
Load 5 kg
Load 10 kg
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
0
200
400
600
800
1000
Velocity (m/s)
Stroke (mm)
SA12
Load 1 kg
Load 10 kg
Load 20 kg
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
0
200
400
600
800
1000
Velocity (m/s)
Stroke (mm)
SA13
Load 1 kg
Load 15 kg
Load 30 kg
0
5
10
15
20
25
30
35
0
50
100
150
200
Payload (kg)
Cantilever distance (mm)
SA11:
Velocity < 2 m/s
0
5
10
15
20
25
30
35
0
50
100
150
200
Payload (kg)
Cantilever distance (mm)
SA12:
Velocity < 2 m/s
0
5
10
15
20
25
30
35
0
50
100
150
200
Payload (kg)
Cantilever distance (mm)
SA13:
Velocity < 2 m/s
0
5
10
15
20
25
30
35
0
50
100
150
200
Payload (kg)
Cantilever distance (mm)
SA11:
Velocity < 2 m/s
0
5
10
15
20
25
30
35
0
50
100
150
200
Payload (kg)
Cantilever distance (mm)
SA12:
Velocity < 2 m/s
0
5
10
15
20
25
30
35
0
50
100
150
200
Payload (kg)
Cantilever distance (mm)
SA13:
Velocity < 2 m/s
Vertical
Horizontal
編碼器延長線
馬達延長線
(130)
(延長線)※2
21
*1
(LC)
186
150
190
編碼器延長線
馬達延長線
(延長線)※2
(65)
21
*1
(166)
186
150
190
2x50=100
150
25
150
190
(56)
68
162
170
LT/2
ST/2+5 (負極限)
ST/2+18 (負硬體極限)
ST/2+5 (正極限)
ST/2+18 (正硬體極限)
186
6-M6x1Px12DP
2xN-Ø6.5 THRU, Ø11x6DP
編碼器延長線
馬達延長線
(延長線)※2
極限開關接頭
(選項 E)
(300)
極限開關接頭
(選項 S)
LA
(N-1)x150=LB
LT
LC
LD
LC
SA11 Linear motor stage dimensions
Linear motor stage with horizontal chain
Linear motor stage with vertical chain
Table2-2  SA11
Stroke(mm)
N
LT
LA
LB
LC
LD
LC(cable chain)
V1,V2*3
V3,V4*3
100
4
400
25
-
100
150
65
95
200
4
500
25
-
100
250
300
4
600
65
-
100
270
400
5
700
75
-
150
250
500
6
800
25
750
-
-
600
6
900
75
750
-
-
700
7
1000
50
900
-
-
800
8
1100
25
1050
-
-
900
8
1200
75
1050
-
-
1000
9
1300
50
1200
-
-
*1:Cable chain interior width is selected from ordering information.
*2:Extension cable length is selected from ordering information.
*3:Dimension LC is determined by cable chain interior width V1~V4 from ordering information.
Encoder cable
Encoder cable
Encoder cable
(-Stopper)
(+Stopper)
(-Limit)
(+Limit)
Limit switches connector
Limit switches connector
Motor cable
Motor cable
Motor cable
(option S)
(option E)
Extension cable *2
Extension cable *2
Extension cable *2
ST/2(Home position)

---

MM99TE07-1701
Linear Motor System
14
15
Standard
SA12 Linear motor stage dimensions
Linear motor stage with horizontal chain
Linear motor stage with vertical chain
3x60=180
250
35
150
190
(56)
68
162
170
LT/2
ST/2 (原點位置)
ST/2+5 (負極限)
ST/2+18 (負硬體極限)
ST/2+5 (正極限)
ST/2+18 (正硬體極限)
186
極限開關接頭
(選項 E)
8-M6x1Px12DP
編碼器延長線
馬達延長線
(300)
極限開關接頭
(選項 S)
(延長線)※2
LA
(N-1)x150=LB
LT
LC
LD
LC
編碼器延長線
馬達延長線
(166)
(65)
21
*1
186
150
190
(延長線)※2
編碼器延長線
馬達延長線
(130)
(LC)
*1
21
186
150
190
(延長線)※2
2xN-Ø6.5 THRU, Ø11x6DP
Table2-3  SA12
Stroke(mm)                  
N
LT
LA
LB
LC
LD
LC(cable chain)
V1,V2*3
V3,V4*3
100
4
500
25
-
100
250
65
95
200
4
600
65
-
100
270
300
4
700
75
-
150
250
400
6
800
25
750
-
-
500
6
900
75
750
-
-
600
7
1000
50
900
-
-
700
8
1100
25
1050
-
-
800
8
1200
75
1050
-
-
900
9
1300
50
1200
-
-
1000
10
1400
25
1350
-
-
*1:Cable chain interior width is selected from ordering information.
*2:Extension cable length is selected from ordering information.
*3:Dimension LC is determined by cable chain interior width V1~V4 from ordering information.
Encoder cable
Encoder cable
Encoder cable
(-Stopper)
(+Stopper)
(-Limit)
(+Limit)
Limit switches connector
Limit switches connector
Motor cable
(Home position)
Motor cable
Motor cable
(option S)
(option E)
Extension cable *2
Extension cable *2
Extension cable *2
編碼器延長線
馬達延長線
(166)
21
*1
186
150
190
(延長線)※2
(65)
35
4x70=280
350
150
190
(56)
68
162
170
LT/2
ST/2 (原點位置)
ST/2+5 (負極限)
ST/2+18 (負硬體極限)
ST/2+5 (正極限)
ST/2+18 (正硬體極限)
186
10-M6x1Px12DP
2xN-Ø6.5 THRU, Ø11x6DP
編碼器延長線
馬達延長線
極限開關接頭
(選項 E)
(300)
極限開關接頭
(選項 S)
(延長線)※2
LA
(N-1)x150=LB
LT
LC
LD
LC
編碼器延長線
馬達延長線
(130)
21
*1
(LC)
186
150
190
(延長線)※2
Table2-4  SA13
Stroke(mm)
N
LT
LA
LB
LC
LD
LC(cable chain)
V1,V2*3
V3,V4*3
100
4
600
65
-
100
270
65
95
200
4
700
75
-
150
250
300
6
800
25
750
-
-
400
6
900
75
750
-
-
500
7
1000
50
900
-
-
600
8
1100
25
1050
-
-
700
8
1200
75
1050
-
-
800
9
1300
50
1200
-
-
900
10
1400
25
1350
-
-
1000
10
1500
75
1350
-
-
SA13 Linear motor stage dimensions
Linear motor stage with horizontal chain
Linear motor stage with vertical chain
*1:Cable chain interior width is selected from ordering information.
*2:Extension cable length is selected from ordering information.
*3:Dimension LC is determined by cable chain interior width V1~V4 from ordering information.
Encoder cable
Encoder cable
Encoder cable
(-Stopper)
(+Stopper)
(-Limit)
(+Limit)
Limit switches connector
Limit switches connector
Motor cable
(Home position)
Motor cable
Motor cable
(option S)
(option E)
Extension cable *2
Extension cable *2
Extension cable *2

---

MM99TE07-1701
Linear Motor System
16
17
Standard
Table2-5   SA21,22,23 stage specification
Specification
SA21
SA21L
SA22
SA22L
SA23
SA23L
Continuous force,FC (N)
181
181
362
362
544
544
Peak force,FP  (N)
512
512
1023
1023
1535
1535
Stroke (mm)
100~1000
Resolution
0.1µm / 1.0µm / Analog 1Vpp
Repeatability (µm) *2
Digital 1µm encoder / Analog encoder: ± 1
Digital 0.1µm encoder: ± 0.5
Accuracy (µm) *2,3
Digital 1µm encoder / Analog encoder: ± 2
Digital 0.1µm encoder: ±1
Horizontal straightness (µm)
10 / 500 mm
Vertical straightness (µm)
20 / 500 mm
Moving mass (kg)
6
8
11
Loading capacity (kg)
30
40
50
SA21,SA22,SA23
Acceleration 
Acceleration 
Acceleration 
Force
Force
Force
Force
Force
Force
Payload
Payload
Payload
Force-Velocity Curve(DC bus = 325V)
*4
Force-Velocity Curve(DC bus = 600V)
*4
Acceleration-Payload Curve
Velocity
Velocity
Velocity
Velocity
Velocity
Velocity
*1：All values are measured on a granite table, all stage mounting  
         holes are well fixed.
*2：Values are measured according to HIWIN measuring standard.
*3：After error compensation.
*4：The Force-Velocity Curve is the characteristic curve of the motor. 
         The actual velocity will change with stroke, payload and acceleration.
         Please refer to the Velocity-Stroke Curve or Appendix A：Motor Sizing.
*5：All specifications above are standard, contact HIWIN for special request.
*1：All values above are standard, contact HIWIN for special request.
*2：Cantilever load capability due to different positioning stage, application rated life also vary.
*3：The main reason for lifetime derives from linear guideway. For more details, please refer to HIWIN linear guideway catalog.
Velocity-Stroke Curve
Cantilever Load Capability*2.3 
0.0
1.0
2.0
3.0
4.0
5.0
0
200
400
600
800
1000
Velocity (m/s)
Stroke (mm)
SA21
Load 1 kg
Load 15 kg
Load 30 kg
0.0
1.0
2.0
3.0
4.0
5.0
0
200
400
600
800
1000
Velocity (m/s)
Stroke (mm)
SA22
Load 1 kg
Load 20 kg
Load 40 kg
0.0
1.0
2.0
3.0
4.0
5.0
0
200
400
600
800
1000
Velocity (m/s)
Stroke (mm)
SA23
Load 1 kg
Load 25 kg
Load 50 kg
0.0
1.0
2.0
3.0
4.0
5.0
0
200
400
600
800
1000
Velocity (m/s)
Stroke (mm)
SA21L
Load 1 kg
Load 15 kg
Load 30 kg
0.0
1.0
2.0
3.0
4.0
5.0
0
200
400
600
800
1000
Velocity (m/s)
Stroke (mm)
SA22L
Load 1 kg
Load 20 kg
Load 40 kg
0.0
1.0
2.0
3.0
4.0
5.0
0
200
400
600
800
1000
Velocity (m/s)
Stroke (mm)
SA23L
Load 1 kg
Load 25 kg
Load 50 kg
Vertical
Horizontal
0
0
10
20
30
40
50
60
100
200
300
400
Payload (kg)
Cantilever distance (mm)
SA21/SA21L:
Velocity < 1.5 m/s
SA21L:
Velocity < 2 m/s
0
0
10
20
30
40
50
60
100
200
300
400
Payload (kg)
Cantilever distance (mm)
SA22/SA22L:
Velocity < 1.5 m/s
SA22L:
Velocity < 2 m/s
0
0
10
20
30
40
50
60
100
200
300
400
Payload (kg)
Cantilever distance (mm)
SA23/SA23L:
Velocity < 1.5 m/s
SA23L:
Velocity < 2 m/s
0
0
10
20
30
40
50
60
100
200
300
400
Payload (kg)
Cantilever distance (mm)
SA21/SA21L:
Velocity < 1.5 m/s
SA21L:
Velocity < 2 m/s
0
0
10
20
30
40
50
60
100
200
300
400
Payload (kg)
Cantilever distance (mm)
SA22/SA22L:
Velocity < 1.5 m/s
SA22L:
Velocity < 2 m/s
0
0
10
20
30
40
50
60
100
200
300
400
Payload (kg)
Cantilever distance (mm)
SA23/SA23L:
Velocity < 1.5 m/s
SA23L:
Velocity < 2 m/s
Vertical
Horizontal

---

MM99TE07-1701
Linear Motor System
18
19
Standard
編碼器延長線
馬達延長線
25
2x50=100
150
6-M6x1Px12DP
2xN-Ø6.5 THRU, Ø11x6DP
202
214
194
234
(56)
74
230
LT/2
ST/2 (原點位置)
ST/2+5 (負極限)
ST/2+18 (負硬體極限)
ST/2+5 (正極限)
ST/2+18 (正硬體極限)
極限開關接頭
(選項 E)
(300)
極限開關接頭
(選項 S)
(延長線)※2
LA
(N-1)x150=LB
LT
LC
LD
LC
194
234
230
編碼器延長線
馬達延長線
(71)
21
*1
(166)
(延長線)※2
194
234
230
(130)
21
*1
(LC)
編碼器延長線
馬達延長線
(延長線)※2
Table2-6  SA21
Stroke(mm)
N
LT
LA
LB
LC
LD
LC(cable chain)
V1,V2*3
V3,V4*3
100
4
400
25
-
100
150
65
95
200
4
500
25
-
100
250
300
4
600
65
-
100
270
400
5
700
75
-
150
250
500
6
800
25
750
-
-
600
6
900
75
750
-
-
700
7
1000
50
900
-
-
800
8
1100
25
1050
-
-
900
8
1200
75
1050
-
-
1000
9
1300
50
1200
-
-
SA21 Linear motor stage dimensions
Linear motor stage with horizontal chain
Linear motor stage with vertical chain
*1:Cable chain interior width is selected from ordering information.
*2:Extension cable length is selected from ordering information.
*3:Dimension LC is determined by cable chain interior width V1~V4 from ordering information.
Encoder cable
Encoder cable
Encoder cable
(-Stopper)
(+Stopper)
(-Limit)
(+Limit)
Limit switches connector
Limit switches connector
Motor cable
(Home position)
Motor cable
Motor cable
(option S)
(option E)
Extension cable *2
Extension cable *2
Extension cable *2
194
234
230
(71)
21
*1
(166)
編碼器延長線
馬達延長線
(延長線)※2
編碼器延長線
馬達延長線
35
3x60=180
250
8-M6x1Px12DP
2xN-Ø6.5 THRU,Ø11x6DP
202
214
194
234
(56)
74
230
LT/2
ST/2 (原點位置)
ST/2+5 (負極限)
ST/2+18 (負硬體極限)
ST/2+5 (正極限)
ST/2+18 (正硬體極限)
極限開關接頭
(選項 E)
(300)
極限開關接頭
(選項 S)
(延長線)※2
LA
(N-1)x150=LB
LT
LC
LD
LC
194
234
230
(130)
21
*1
(LC)
編碼器延長線
馬達延長線
(延長線)※2
Table2-7  SA22
Stroke(mm)
N
LT
LA
LB
LC
LD
LC(cable chain)
V1,V2*3
V3,V4*3
100
4
500
25
-
100
250
65
95
200
4
600
65
-
100
270
300
4
700
75
-
150
250
400
6
800
25
750
-
-
500
6
900
75
750
-
-
600
7
1000
50
900
-
-
700
8
1100
25
1050
-
-
800
8
1200
75
1050
-
-
900
9
1300
50
1200
-
-
1000
10
1400
25
1350
-
-
SA22 Linear motor stage dimensions
Linear motor stage with horizontal chain
Linear motor stage with vertical chain
*1:Cable chain interior width is selected from ordering information.
*2:Extension cable length is selected from ordering information.
*3:Dimension LC is determined by cable chain interior width V1~V4 from ordering information.
Encoder cable
Encoder cable
Encoder cable
(-Stopper)
(+Stopper)
(-Limit)
(+Limit)
Limit switches connector
Limit switches connector
Motor cable
(Home position)
Motor cable
Motor cable
(option S)
(option E)
Extension cable *2
Extension cable *2
Extension cable *2

---

MM99TE07-1701
Linear Motor System
20
21
Standard
194
234
230
(71)
21
*1
(166)
編碼器延長線
馬達延長線
(延長線)※2
編碼器延長線
馬達延長線
35
4x70=280
350
10-M6x1Px12DP
2xN-Ø6.5 THRU, Ø11x6DP
202
214
194
234
(56)
74
230
LT/2
ST/2 (原點位置)
ST/2+5 (負極限)
ST/2+18 (負硬體極限)
ST/2+5 (正極限)
ST/2+18 (正硬體極限)
極限開關接頭
(選項 E)
(300)
極限開關接頭
(選項 S)
(延長線)※2
LA
(N-1)x150=LB
LT
LC
LD
LC
194
234
230
(130)
21
*1
(LC)
編碼器延長線
馬達延長線
(延長線)※2
Table2-8  SA23
Stroke(mm)
N
LT
LA
LB
LC
LD
LC(cable chain)
V1,V2*3
V3,V4*3
100
4
600
65
-
100
270
65
95
200
4
700
75
-
150
250
300
6
800
25
750
-
-
400
6
900
75
750
-
-
500
7
1000
50
900
-
-
600
8
1100
25
1050
-
-
700
8
1200
75
1050
-
-
800
9
1300
50
1200
-
-
900
10
1400
25
1350
-
-
1000
10
1500
75
1350
-
-
SA23 Linear motor stage dimensions
Linear motor stage with horizontal chain
Linear motor stage with vertical chain
*1:Cable chain interior width is selected from ordering information.
*2:Extension cable length is selected from ordering information.
*3:Dimension LC is determined by cable chain interior width V1~V4 from ordering information.
Encoder cable
Encoder cable
Encoder cable
(-Stopper)
(+Stopper)
(-Limit)
(+Limit)
Limit switches connector
Limit switches connector
Motor cable
(Home position)
Motor cable
Motor cable
(option S)
(option E)
Extension cable *2
Extension cable *2
Extension cable *2
Table2-9   SA31,32,33 stage specification
Specification
SA31
SA31L
SA32
SA32L
SA33
SA33L
Continuous force,FC (N)
292
292
583
583
875
875
Peak force,FP (N)
823
823
1646
1646
2469
2469
Stroke (mm)
100~1000(mm)
Resolution
0.1µm / 1.0µm / Analog 1Vpp
Repeatability (µm) *2
Digital 1µm encoder / Analog encoder: ± 1
Digital 0.1µm encoder: ± 0.5
Accuracy (µm) *2,3
Digital 1µm encoder / Analog encoder: ± 2
Digital 0.1µm encoder: ± 1
Horizontal straightness (µm)
10 / 500 mm
Vertical straightness (µm)
20 / 500 mm
Moving mass (kg)
7.5
10.5
14.5
Loading capacity (kg)
40
50
60
SA31,SA32,SA33
Acceleration 
Acceleration 
Acceleration 
Force
Force
Force
Force
Force
Force
Payload
Payload
Payload
Force-Velocity Curve(DC bus = 325V)
*4
Force-Velocity Curve(DC bus = 600V)
*4
Acceleration-Payload Curve
*1：All values are measured on a granite table, all stage mounting  
         holes are well fixed.
*2：Values are measured according to HIWIN measuring standard.
*3：After error compensation.
*4：The Force-Velocity Curve is the characteristic curve of the motor. 
         The actual velocity will change with stroke, payload and acceleration.
         Please refer to the Velocity-Stroke Curve or Appendix A：Motor Sizing.
*5：All specifications above are standard, contact HIWIN for special request.
Velocity
Velocity
Velocity
Velocity
Velocity
Velocity
2
2
2

---

MM99TE07-1701
Linear Motor System
22
23
Standard
*1：All values above are standard, contact HIWIN for special request.
*2：Cantilever load capability due to different positioning stage, application rated life also vary.
*3：The main reason for lifetime derives from linear guideway. For more details, please refer to HIWIN linear guideway catalog.
Velocity-Stroke Curve
Cantilever Load Capability*2.3 
0.0
0.5
1.0
1.5
2.0
2.5
3.0
0
200
400
600
800
1000
Velocity (m/s)
Stroke (mm)
SA31
Load 1 kg
Load 20 kg
Load 40 kg
0.0
0.5
1.0
1.5
2.0
2.5
3.0
0
200
400
600
800
1000
Velocity (m/s)
Stroke (mm)
SA32
Load 1 kg
Load 25 kg
Load 50 kg
0.0
0.5
1.0
1.5
2.0
2.5
3.0
0
200
400
600
800
1000
Velocity (m/s)
Stroke (mm)
SA33
Load 1 kg
Load 30 kg
Load 60 kg
0.0
0.5
1.0
1.5
2.0
2.5
3.0
0
200
400
600
800
1000
Velocity (m/s)
Stroke (mm)
SA31L
Load 1 kg
Load 20 kg
Load 40 kg
0.0
0.5
1.0
1.5
2.0
2.5
3.0
0
200
400
600
800
1000
Velocity (m/s)
Stroke (mm)
SA32L
Load 1 kg
Load 25 kg
Load 50 kg
0.0
0.5
1.0
1.5
2.0
2.5
3.0
0
200
400
600
800
1000
Velocity (m/s)
Stroke (mm)
SA33L
Load 1 kg
Load 30 kg
Load 60 kg
Vertical
Horizontal
0
10
20
30
40
50
60
70
0
200
400
600
Payload (kg)
Cantilever distance (mm)
SA31/SA31L:
Velocity < 1 m/s
SA31L:
Velocity < 2 m/s
0
10
20
30
40
50
60
70
0
200
400
600
Payload (kg)
Cantilever distance (mm)
SA32/SA32L:
Velocity < 1 m/s
SA32L:
Velocity < 2 m/s
0
10
20
30
40
50
60
70
0
200
400
600
Payload (kg)
Cantilever distance (mm)
SA33/SA33L:
Velocity < 1 m/s
SA33L:
Velocity < 2 m/s
0
10
20
30
40
50
60
70
0
200
400
600
Payload (kg)
Cantilever distance (mm)
SA31/SA31L:
Velocity < 1 m/s
SA31L:
Velocity < 2 m/s
0
10
20
30
40
50
60
70
0
200
400
600
Payload (kg)
Cantilever distance (mm)
SA32/SA32L:
Velocity < 1 m/s
SA32L:
Velocity < 2 m/s
0
10
20
30
40
50
60
70
0
200
400
600
Payload (kg)
Cantilever distance (mm)
SA33/SA33L:
Velocity < 1 m/s
SA33L:
Velocity < 2 m/s
Vertical
Horizontal
226
266
262
編碼器延長線
馬達延長線
(77)
21
(166)
*1
(延長線)※2
25
2x50=100
150
LA
(N-1)x150=LB
LT
6-M8x1.25Px16DP
2xN-Ø6.5 THRU,Ø11x6DP
234
246
226
266
80
262
(56)
編碼器延長線
馬達延長線
LT/2
ST/2 (原點位置)
ST/2+5 (負極限)
ST/2+18 (負硬體極限)
ST/2+5 (正極限)
ST/2+18 (正硬體極限)
極限開關接頭
(選項 E)
(300)
極限開關接頭
(選項 S)
(延長線)※2
LC
LD
LC
226
266
262
編碼器延長線
馬達延長線
(130)
21
*1
(LC)
(延長線)※2
Table2-10  SA31
Stroke(mm)
N
LT
LA
LB
LC
LD
LC(cable chain)
V1,V2*3
V3,V4*3
100
4
400
25
-
100
150
65
95
200
4
500
25
-
100
250
300
4
600
65
-
100
270
400
5
700
75
-
150
250
500
6
800
25
750
-
-
600
6
900
75
750
-
-
700
7
1000
50
900
-
-
800
8
1100
25
1050
-
-
900
8
1200
75
1050
-
-
1000
9
1300
50
1200
-
-
SA31 Linear motor stage dimensions
Linear motor stage with horizontal chain
Linear motor stage with vertical chain
*1:Cable chain interior width is selected from ordering information.
*2:Extension cable length is selected from ordering information.
*3:Dimension LC is determined by cable chain interior width V1~V4 from ordering information.
Encoder cable
Encoder cable
Encoder cable
(-Stopper)
(+Stopper)
(-Limit)
(+Limit)
Limit switches connector
Limit switches connector
Motor cable
(Home position)
Motor cable
Motor cable
(option S)
(option E)
Extension cable *2
Extension cable *2
Extension cable *2

---

MM99TE07-1701
Linear Motor System
24
25
Standard
226
266
262
(77)
21
(166)
*1
編碼器延長線
馬達延長線
(延長線)※2
35
3x60=180
250
LT
8-M8x1.25Px16DP
2xN-Ø6.5 THRU,Ø11x6DP
234
246
226
266
80
262
(56)
編碼器延長線
馬達延長線
LT/2
ST/2 (原點位置)
ST/2+5 (負極限)
ST/2+18 (負硬體極限)
ST/2+5 (正極限)
ST/2+18 (正硬體極限)
極限開關接頭
(選項 E)
(300)
極限開關接頭
(選項 S)
(延長線)※2
LA
(N-1)x150=LB
LC
LD
LC
226
266
262
(130)
21
*1
(LC)
編碼器延長線
馬達延長線
(延長線)※2
Table2-11  SA32
Stroke(mm)
N
LT
LA
LB
LC
LD
LC(cable chain)
V1,V2*3
V3,V4*3
100
4
500
25
-
100
250
65
95
200
4
600
65
-
100
270
300
4
700
75
-
150
250
400
6
800
25
750
-
-
500
6
900
75
750
-
-
600
7
1000
50
900
-
-
700
8
1100
25
1050
-
-
800
8
1200
75
1050
-
-
900
9
1300
50
1200
-
-
1000
10
1400
25
1350
-
-
SA32 Linear motor stage dimensions
Linear motor stage with horizontal chain
Linear motor stage with vertical chain
*1:Cable chain interior width is selected from ordering information.
*2:Extension cable length is selected from ordering information.
*3:Dimension LC is determined by cable chain interior width V1~V4 from ordering information.
Encoder cable
Encoder cable
Encoder cable
(-Stopper)
(+Stopper)
(-Limit)
(+Limit)
Limit switches connector
Limit switches connector
Motor cable
(Home position)
Motor cable
Motor cable
(option S)
(option E)
Extension cable *2
Extension cable *2
Extension cable *2
226
266
262
(77)
21
(166)
*1
編碼器延長線
馬達延長線
(延長線)※2
226
266
262
(130)
21
*1
(LC)
編碼器延長線
馬達延長線
(延長線)※2
LT
2xN-Ø6.5 THRU, Ø11x6DP
234
246
226
266
80
262
(56)
編碼器延長線
馬達延長線
LT/2
ST/2 (原點位置)
ST/2+5 (負極限)
ST/2+18 (負硬體極限)
ST/2+5 (正極限)
ST/2+18 (正硬體極限)
35
4x70=280
350
10-M8x1.25Px16DP
極限開關接頭
(選項 E)
(300)
極限開關接頭
(選項 S)
(延長線)※2
LA
(N-1)x150=LB
LC
LD
LC
Table2-12  SA33
Stroke(mm)
N
LT
LA
LB
LC
LD
LC(cable chain)
V1,V2*3
V3,V4*3
100
4
600
65
-
100
270
65
95
200
4
700
75
-
150
250
300
6
800
25
750
-
-
400
6
900
75
750
-
-
500
7
1000
50
900
-
-
600
8
1100
25
1050
-
-
700
8
1200
75
1050
-
-
800
9
1300
50
1200
-
-
900
10
1400
25
1350
-
-
1000
10
1500
75
1350
-
-
SA33 Linear motor stage dimensions
Linear motor stage with horizontal chain
Linear motor stage with vertical chain
*1:Cable chain interior width is selected from ordering information.
*2:Extension cable length is selected from ordering information.
*3:Dimension LC is determined by cable chain interior width V1~V4 from ordering information.
Encoder cable
Encoder cable
Encoder cable
(-Stopper)
(+Stopper)
(-Limit)
(+Limit)
Limit switches connector
Limit switches connector
Motor cable
(Home position)
Motor cable
Motor cable
(option S)
(option E)
Extension cable *2
Extension cable *2
Extension cable *2

---

MM99TE07-1701
Linear Motor System
26
27
Standard
2.3 LMC high-precision, high-speed stability
Linear motor LMC stages are equipped with coreless motor(s) and well suited for 
applications that require precision positioning and constant velocity scanning motion.
　Linear motor direct drive, enabling ultra-precise movement
　Stroke range up to 4m
　Superior speed control characteristic
　Low cost, small size, high performance
　Suitable for clean rooms
2.3.1  Linear single axis
LMX1E–CB5–1–300– G200
Stage type
LMX1E
Motor type
CB5:LMCB5
CB6:LMCB6
CB7:LMCB7
CB8:LMCB8
The number of slider
1:1
Stroke
100:100mm    700:700mm 
200:200mm   800:800mm
300:300mm   900:900mm
400:400mm   1000:1000mm
500:200mm   1100:1100mm
600:300mm   1200:1200mm
Encoder type
0:None
A:40µm analog 1Vpp optical scale
B:20µm analog 1Vpp optical scale 
D:1mm analog 1Vpp magnetic scale
E:TTL digital 1µm resolution magnetic scale
G:TTL digital 1µm resolution optical scale (standard)
H:TTL digital 0.5µm resolution optical scale
K:TTL digital 0.1µm resolution optical scale
M:TTL digital 20nm resolution optical scale
P:40µm analog glass optical scale
X:Other (please remark desired specifications, product or model)
Limit switch
0:None
1:Inductive type, PNP
2:Optical switch, NPN (standard)
3:Optical switch, PNP
4:Inductive type, NPN
C:Customized
Cover
0:None (standard)
A:Metal cover
B:Bellows
C:Customized
D:Non-woven
Cable chain
0:None (standard)
1:Horizontal direction (chain internal space 15x30mm)
2:Vertical direction (chain internal space 15x30mm)
C:Customized
Note：Contact HIWIN for customized specification.

---

MM99TE07-1701
Linear Motor System
28
29
Standard
Force-Velocity Curve (DC bus = 325V)
Acceleration-Payload Curve
0
200
400
600
800
0
1
2
3
4
5
6
Force (N)
Velocity (m/s)
CB5 Fp
CB5 Fc
0
200
400
600
800
0
1
2
3
4
5
6
Force (N)
Velocity (m/s)
CB6 Fp
CB6 Fc
0
200
400
600
800
0
1
2
3
4
5
6
Force (N)
Velocity (m/s)
CB7 Fp
CB7 Fc
0
200
400
600
800
0
1
2
3
4
5
6
Force (N)
Velocity (m/s)
CB8 Fp
CB8 Fc
Acceleration (m/s2 )
Payload (kg)
CB5
Acceleration (m/s2 )
Payload (kg)
CB6
Acceleration (m/s2 )
Payload (kg)
CB7
Acceleration (m/s2 )
Payload (kg)
CB8
0
10
20
30
40
50
60
0
20
40
60
80
0
10
20
30
40
50
60
0
20
40
60
80
0
10
20
30
40
50
60
0
20
40
60
80
0
10
20
30
40
50
60
0
20
40
60
80
Table2-13   LMCB5,6,7,8 stage specification
Specification
CB5
CB6
CB7
CB8
Continuous force,FC (N)
91
109
128
145
Peak force,FP (N)
364
436
512
580
Stroke (mm)
100-1200
Resolution
1.0µm
Repeatability (µm) *2
Stroke 100~1000 mm: ±1
Stroke 1100 / 1200 mm: ±2
Accuracy (µm) *2,3
Stroke 100~1000 mm: ±3
Stroke 1100 / 1200 mm: ±8
Horizontal straightness (µm)
10 / 500 mm
Vertical straightness (µm)
20 / 500 mm
Moving mass (kg)
No cover: 2.1
No cover: 3.1
3.8
4.7
With cover: 2.3
With cover: 3.3
*1：All values are measured on a granite table, all stage mounting holes are well fixed.
*2：Values are measured according to HIWIN measuring standard.
*3：After error compensation.
*4：The Force-Velocity Curve is the characteristic curve of the motor. The actual velocity will change with stroke, payload and acceleration.
         Please refer to the Velocity-Stroke Curve or Appendix A：Motor Sizing.
*5：All specifications above are standard, contact HIWIN for special request.
*4
Velocity-Stroke Curve
Cantilever Load Capability*2.3 
0.0
1.0
2.0
3.0
4.0
5.0
0
200
400
600
800
1000
1200
Velocity (m/s)
Stroke (mm)
CB5
Load 10 kg
Load 20 kg
Load 30 kg
0.0
1.0
2.0
3.0
4.0
5.0
0
200
400
600
800
1000
1200
Velocity (m/s)
Stroke (mm)
CB6
Load 10 kg
Load 20 kg
Load 30 kg
0.0
1.0
2.0
3.0
4.0
5.0
0
200
400
600
800
1000
1200
Velocity (m/s)
Stroke (mm)
CB7
Load 10 kg
Load 20 kg
Load 30 kg
0.0
1.0
2.0
3.0
4.0
5.0
0
200
400
600
800
1000
1200
Velocity (m/s)
Stroke (mm)
CB8
Load 10 kg
Load 20 kg
Load 30 kg
Vertical
Horizontal
0
20
40
60
80
0
50
100
150
200
Payload (kg)
Cantilever distance (mm)
CB5: Velocity < 2 m/s
0
20
40
60
80
0
50
100
150
200
Payload (kg)
Cantilever distance (mm)
CB6: Velocity < 2 m/s
0
20
40
60
80
0
50
100
150
200
Payload (kg)
Cantilever distance (mm)
CB7: Velocity < 2 m/s
0
20
40
60
80
0
50
100
150
200
Payload (kg)
Cantilever distance (mm)
CB8: Velocity < 2 m/s
0
20
40
60
80
0
50
100
150
200
Payload (kg)
Cantilever distance (mm)
CB5: Velocity < 2 m/s
0
20
40
60
80
0
50
100
150
200
Payload (kg)
Cantilever distance (mm)
CB6: Velocity < 2 m/s
0
20
40
60
80
0
50
100
150
200
Payload (kg)
Cantilever distance (mm)
CB7: Velocity < 2 m/s
0
20
40
60
80
0
50
100
150
200
Payload (kg)
Cantilever distance (mm)
CB8: Velocity < 2 m/s
*1：All values above are standard, contact HIWIN for special request.
*2：Cantilever load capability due to different positioning stage, application rated life also vary.
*3：The main reason for lifetime derives from linear guideway. For more details, please refer to HIWIN linear guideway catalog.
Vertical
Horizontal

---

MM99TE07-1701
Linear Motor System
30
31
Standard
LMCB5
Table2-14   Without/with cover linear motor stage specifications
Stroke
(mm)
L
(mm)
L1
(mm)
N
Mass
(kg)
H
(mm)
100
400
35
1*1
18/19
95
200
500
85
2
22/23
95
300
600
60
3
26/27
95
400
700
35
4
30/31
95
500
800
85
4
34/35
95
600
900
60
5
38/39
95
700
1000
35
6
42/43
95
800
1100
85
6
46/47
95
900
1200
60
7
50/51
95
1000
1300
35
8
54/55
95
1100
1400
85
8
58/59
105
1200
1500
60
9
62/63
105
*1：When stroke is 100mm, the mounting holes spacing is 300mm.
*2: Absolute accuracy is after error mapping(with HIWIN drive).
2.2.3  LMC Series Stage
Without cover 
4 - M6x1.0Px12DP
180
158
60
35
110
180
有效行程
15
L1
Nx150 (註1)
L-30
L
2x(N+1)-Ø6.5 THRU,
Ø11x8.5DP
2x2-Ø6H7 THRU
75
75
(22)
(89)
178
80
36.5
105
(68)
22
22
11
極限
接頭
+方向
With cover 
4 - M6x1.0Px12DP
(22)
(89)
178
H
180
158
60
35
110
180
有效行程
15
36.5
105
L1
Nx150 (註1)
L-30
L
2x(N+1)-Ø6.5 THRU,
Ø11x8.5DP
2x2-Ø6H7 THRU
75
75
(68)
22
22
11
極限
接頭
 +方向
+Direction
+Direction
Effective stroke
Effective stroke
Limit
Limit
Connector
Connector
 (*1)
 (*1)

---

MM99TE07-1701
Linear Motor System
32
33
Standard
LMCB6
Table2-15   Without/with cover linear motor stage specifications
Stroke
(mm)
L
(mm)
L1
(mm)
N
Mass
(kg)
H
(mm)
100
430
50
1*1
19/20
95
200
530
25
3
23/24
95
300
630
75
3
27/28
95
400
730
50
4
31/32
95
500
830
25
5
35/36
95
600
930
75
5
39/40
95
700
1030
50
6
43/44
95
800
1130
25
7
47/48
95
900
1230
75
7
51/52
95
1000
1330
50
8
55/56
95
1100
1430
25
9
59/60
105
1200
1530
75
9
63/64
105
*1：When stroke is 100mm, the mounting holes spacing is 300mm.
*2: Absolute accuracy is after error mapping(with HIWIN drive).
6-M6x1.0Px12DP
+方向
180
158
60
35
2x70=140
210
有效行程
15
L1
Nx150(註 1)
L-30
L
2x(N+1)-Ø6.5 THRU,
Ø11x8.5DP
2x2-Ø6H7 THRU
75
75
(22)
178
80
36.5
105
(68)
22
22
11
極限
接頭
(22)
(89)
178
H
36.5
105
6 - M6x1.0Px12DP
180
158
60
35
2x70=140
210
有效行程
15
L1
Nx150(註1)
L-30
L
2x(N+1)-Ø6.5 THRU,
Ø11x8.5DP
2x2-Ø6H7 THRU
75
75
(68)
22
22
11
極限
接頭
 +方向
+Direction
+Direction
Effective stroke
Effective stroke
Limit
Limit
Connector
Connector
 (*1)
 (*1)
Without cover 
With cover 

---

MM99TE07-1701
Linear Motor System
34
35
Standard
LMCB7
Table2-16   Without/with cover linear motor stage specifications
Stroke
(mm)
L
(mm)
L1
(mm)
N
Mass
(kg)
H
(mm)
100
460
65
1*1
20/21
95
200
560
40
3
24/25
95
300
660
90
3
28/29
95
400
760
65
4
32/33
95
500
860
40
5
36/37
95
600
960
90
5
40/41
95
700
1060
65
6
44/45
95
800
1160
40
7
48/49
95
900
1260
90
7
52/53
95
1000
1360
65
8
56/57
95
1100
1460
40
9
60/61
105
1200
1560
90
9
64/65
105
*1：When stroke is 100mm, the mounting holes spacing is 300mm.
*2: Absolute accuracy is after error mapping(with HIWIN drive).
 +方向
11
158
180
8-M6x1.0Px12DP
60
15
3x70=210
240
有效行程
(22)
(89)
178
80
36.5
105
(68)
22
22
15
L1
Nx150(註 1)
L-30
L
2x(N+1)-Ø6.5 THRU,
Ø11x8.5DP
2x2-Ø6H7 THRU
75
75
極限
接頭
11
158
180
8-M6x1.0Px12DP
60
15
3x70=210
240
有效行程
15
L1
Nx150(註 1)
L-30
L
2x(N+1)-Ø6.5 THRU,
Ø11x8.5DP
2x2-Ø6H7 THRU
75
75
(22)
(89)
178
H
36.5
105
(68)
22
22
極限
接頭
 +方向
+Direction
+Direction
Effective stroke
Effective stroke
Limit
Limit
Connector
Connector
 (*1)
 (*1)
Without cover 
With cover 

---

MM99TE07-1701
Linear Motor System
36
37
Standard
LMCB8
Table2-17   Without/with cover linear motor stage specifications
Stroke
(mm)
L
(mm)
L1
(mm)
N
Mass
(kg)
H
(mm)
100
500
85
1*1
21/22
95
200
600
60
3
25/26
95
300
700
35
4
29/30
95
400
800
85
4
33/34
95
500
900
60
5
37/38
95
600
1000
35
6
41/42
95
700
1100
85
6
45/46
95
800
1200
60
7
49/50
95
900
1300
35
8
53/54
95
1000
1400
85
8
57/58
95
1100
1500
60
9
61/62
105
1200
1600
35
10
65/66
105
*1：When stroke is 100mm, the mounting holes spacing is 300mm.
*2: Absolute accuracy is after error mapping(with HIWIN drive).
8-M6x1.0Px10DP
180
158
(22)
(89)
178
80
36.5
105
60
35
3x70=210
280
有效行程
15
L1
Nx150(註 1)
L-30
L
2x(N+1)-Ø6.5 THRU,
Ø11x8.5DP
2x2-Ø6H7  THRU
75
75
(68)
22
22
11
極限
接頭
 +方向
8 - M6x1.0Px10DP
180
158
60
35
3x70=210
280
有效行程
(22)
(89)
178
H
36.5
105
15
L1
Nx150(註 1)
L-30
L
2x(N+1)-Ø6.5 THRU,
Ø11x8.5DP
2x2-Ø6H7 THRU
75
75
(68)
22
22
11
極限
接頭
 +方向
+Direction
+Direction
Effective stroke
Limit
Limit
Connector
Connector
 (*1)
 (*1)
Without cover 
With cover 
Effective stroke

---

MM99TE07-1701
Linear Motor System
38
39
Standard
2.4  LMT light weight, high acceleration/deceleration
Shaft motor series with LMT ironless motors are suitable for inspection, scan and semiconductor industry. 
It can also be assembled into X-Y stage; position feedback apples incremental analog or digital optical scale 
and magnetic scale as position feedback are seletable.
　Lightweight
　No cogging 
　Max. acceleration 50m/s2, max. velocity 5m/s
　High acceleration and deceleration characteristics
2.4.1  Linear single axis
LMX1E–T A2–1–300– G200
Stage type
LMX1E
Motor type
TA2:LMTA2     TB3:LMTB3     TC4:LMTC4
TA3:LMTA3     TB4:LMTB4    
TA4:LMTA4     TC2:LMTC2    
TB2:LMTB2     TC3:LMTC3
The number of slider
1:1
Stroke
388:388mm      1156:1156mm 
516:516mm      1412:1412mm
644:644mm      1668:1668mm
722:722mm      1924:1924mm
900:900mm      2180:2180mm
Encoder type
0:None
A:40µm analog 1Vpp optical scale
B:20µm analog 1Vpp optical scale 
D:1mm analog 1Vpp magnetic scale
E:TTL digital 1µm resolution magnetic scale
G:TTL digital 1µm resolution optical scale (standard)
H:TTL digital 0.5µm resolution optical scale
K:TTL digital 0.1µm resolution optical scale
M:TTL digital 20nm resolution optical scale
P:40µm analog glass optical scale
X:Other (please remark desired specifications, product or model)
Limit switch
0:None
1:Inductive type, PNP
2:Optical switch, NPN (standard)
3:Optical switch, PNP
4:Inductive type, NPN
C:Customized
Cover
0:None (standard)
A:Metal cover
B:Bellows
C:Customized        
D:Non-woven
Cable chain
0:None (standard)
1:Horizontal direction (chain internal space 15x30mm)
2:Vertical direction (chain internal space 15x30mm)
C:Customized
Table2-18   LMTA2,3,4 stage specification
Specification
TA2
TA3
TA4
Continuous force,FC (N)
27
42
55
Peak force,FP (N)
108
168
220
Stroke (mm)
100-1000
Resolution
1.0µm
Repeatability (µm) *2
±1
Accuracy (µm) *2,3
±3
Horizontal straightness (µm)
10 / 500 mm
Vertical straightness (µm)
20 / 500 mm
Moving mass (kg)
1.4
2.1
2.3
Force-Velocity Curve (DC bus = 325V)
Acceleration-Payload Curve
Acceleration (m/s 2)
Payload (kg)
TA2
Acceleration (m/s 2)
Payload (kg)
TA3
Acceleration (m/s 2)
Payload (kg)
TA4
0
100
200
300
0
1
2
3
4
5
6
Force (N)
Velocity (m/s)
TA2 Fp
TA2 Fc
0
100
200
300
0
1
2
3
4
5
6
Force (N)
Velocity (m/s)
TA3 Fp
TA3 Fc
0
100
200
300
0
1
2
3
4
5
6
Force (N)
Velocity (m/s)
TA4 Fp
TA4 Fc
0
10
20
30
40
50
60
0
10
20
30
40
0
10
20
30
40
50
60
0
10
20
30
40
0
10
20
30
40
50
60
0
10
20
30
40
2.4.2  LMTA2 Shaft motor stage
*1：All values are measured on a granite table, all stage mounting holes are well fixed.
*2：Values are measured according to HIWIN measuring standard.
*3：After error compensation.
*4：The Force-Velocity Curve is the characteristic curve of the motor. The actual velocity will change with stroke, payload and acceleration.
         Please refer to the Velocity-Stroke Curve or Appendix A：Motor Sizing.
*5：All specifications above are standard, contact HIWIN for special request.
Note：Contact HIWIN for customized specification.
*4

---

MM99TE07-1701
Linear Motor System
40
41
Standard
*1：All values above are standard, contact HIWIN for special request.
*2：Cantilever load capability due to different positioning stage, application rated life also vary.
*3：The main reason for lifetime derives from linear guideway. For more details, please refer to HIWIN linear guideway catalog.
Velocity-Stroke Curve
Cantilever Load Capability*2.3 
Vertical
Horizontal
0.0
1.0
2.0
3.0
4.0
5.0
6.0
0
200
400
600
800
1000
Velocity (m/s)
Stroke (mm)
TA2
Load 1 kg
Load 3 kg
Load 5 kg
0.0
1.0
2.0
3.0
4.0
5.0
6.0
0
200
400
600
800
1000
Velocity (m/s)
Stroke (mm)
TA3
Load 1 kg
Load 3 kg
Load 5 kg
0.0
1.0
2.0
3.0
4.0
5.0
6.0
0
200
400
600
800
1000
Velocity (m/s)
Stroke (mm)
TA4
Load 1 kg
Load 3 kg
Load 5 kg
0
5
10
15
20
25
0
50
100
150
200
250
300
Payload (kg)
Cantilever distance (mm)
TA2: Velocity < 2 m/s
0
5
10
15
20
25
0
50
100
150
200
250
300
Payload (kg)
Cantilever distance (mm)
TA3: Velocity < 2 m/s
0
5
10
15
20
25
0
50
100
150
200
250
300
Payload (kg)
Cantilever distance (mm)
TA4: Velocity < 2 m/s
0
5
10
15
20
25
0
50
100
150
200
250
300
Payload (kg)
Cantilever distance (mm)
TA2: Velocity < 2 m/s
0
5
10
15
20
25
0
50
100
150
200
250
300
Payload (kg)
Cantilever distance (mm)
TA3: Velocity < 2 m/s
0
5
10
15
20
25
0
50
100
150
200
250
300
Payload (kg)
Cantilever distance (mm)
TA4: Velocity < 2 m/s
Vertical
Horizontal
Table2-19   LMTA2 Shaft motor stage specifications
Stroke
(mm)
L
(mm)
L1
(mm)
L2
(mm)
N
Mass
(kg)
100
304
67
54.5
1
5
200
404
42
54.5
2
6
300
534
32
69.5
3
6.9
400
634
82
69.5
3
7.9
500
734
57
69.5
4
8.8
600
834
32
69.5
5
9.8
700
974
27
89.5
6
11.2
800
1074
77
89.5
6
12.1
900
1174
52
89.5
7
13.1
1000
1274
27
89.5
8
14
* Absolute accuracy is after error mapping (with HIWIN drive).
L2
22.5
50
95
5
100
有效行程
110
L
10
102
(21.5)
(92)
78
L-20
L1
Nx150
11
80
(67.5)
+ 方向
4-M5x0.8Px10DP
2x(N+1)-M5x0.8Px10DP
接頭
極限
Dimension
+Direction
Effective stroke
Limit
Connector

---

MM99TE07-1701
Linear Motor System
42
43
Standard
Table2-20   LMTA3 Shaft type linear motor stage specifications
Stroke
(mm)
L
(mm)
L1
(mm)
L2
(mm)
N
Mass
(kg)
100
340
85
55
1
6.3
200
440
60
55
2
7.4
300
570
50
70
3
8.5
400
670
25
70
4
9.6
500
770
75
70
4
10.8
600
870
50
70
5
11.9
700
1010
45
90
6
13.5
800
1110
20
90
7
14.6
900
1210
70
90
7
15.8
1000
1310
45
90
8
16.9
L2
15
2x50=100
5
100
130
110
有效行程
78
(21.5)
102
(92)
L
10
L-20
L1
Nx150
11
80
(67.5)
+ 方向
 6-M5x0.8Px10DP
2x(N+1)-M5x0.8Px10DP
接頭
極限
Dimension
+Direction
Effective stroke
Limit
Connector
Table2-21   LMTA4 Shaft type linear motor stage specifications
Stroke
(mm)
L
(mm)
L1
(mm)
L2
(mm)
N
Mass
(kg)
100
376
28
53
2
7.0
200
476
78
53
2
8.1
300
606
68
68
3
9.2
400
706
43
68
4
10.4
500
806
18
68
5
11.5
600
906
68
68
5
12.6
700
1046
63
88
6
14.2
800
1146
38
88
7
15.3
900
1246
13
88
8
16.5
1000
1346
63
88
8
17.6
L2
10
3x50=150
5
100
110
170
78
有效行程
L
10
L-20
L1
Nx150
(21.5)
102
(92)
11
80
(67.5)
+ 方向
2x4-M5x0.8Px10DP
2x(N+1)-M5x0.8Px10DP
接頭
極限
Dimension
+Direction
Effective stroke
Limit
Connector
* Absolute accuracy is after error mapping (with HIWIN drive).
* Absolute accuracy is after error mapping (with HIWIN drive).

---

MM99TE07-1701
Linear Motor System
44
45
Standard
Force-Velocity Curve (DC bus = 325V)
Acceleration-Payload Curve
0
100
200
300
400
500
0
1
2
3
4
5
6
Force (N)
Velocity (m/s)
TB2 Fp
TB2 Fc
0
100
200
300
400
500
0
1
2
3
4
5
6
Force (N)
Velocity (m/s)
TB3 Fp
TB3 Fc
0
100
200
300
400
500
0
1
2
3
4
5
6
Force (N)
Velocity (m/s)
TB4 Fp
TB4 Fc
Acceleration (m/s 2)
Payload (kg)
TB2
Acceleration (m/s 2)
Payload (kg)
TB3
Acceleration (m/s 2)
Payload (kg)
TB4
0
10
20
30
40
50
60
0
10
20
30
40
50
0
10
20
30
40
50
60
0
10
20
30
40
50
0
10
20
30
40
50
60
0
10
20
30
40
50
Table2-22   LMTB2,3,4 stage specification
Specification
TB2
TB3
TB4
Continuous force,FC (N)
48
72
96
Peak force,FP (N)
192
288
384
Stroke (mm)
100-1000
Resolution
1.0µm
Repeatability (µm) *2
±1
Accuracy (µm) *2,3
±3
Horizontal straightness (µm)
10 / 500 mm
Vertical straightness (µm)
20 / 500 mm
Moving mass (kg)
2.1
2.7
3.6
2.4.3  LMTB2 Shaft motor stage
*1：All values are measured on a granite table, all stage mounting holes are well fixed.
*2：Values are measured according to HIWIN measuring standard.
*3：After error compensation.
*4：The Force-Velocity Curve is the characteristic curve of the motor. The actual velocity will change with stroke, payload and acceleration.
         Please refer to the Velocity-Stroke Curve or Appendix A：Motor Sizing.
*5：All specifications above are standard, contact HIWIN for special request.
*4
*1：All values above are standard, contact HIWIN for special request.
*2：Cantilever load capability due to different positioning stage, application rated life also vary.
*3：The main reason for lifetime derives from linear guideway. For more details, please refer to HIWIN linear guideway catalog.
Velocity-Stroke Curve
Cantilever Load Capability*2.3 
Vertical
Horizontal
0.0
1.0
2.0
3.0
4.0
5.0
0
200
400
600
800
1000
Velocity (m/s)
Stroke (mm)
TB2
Load 5 kg
Load 10 kg
Load 15 kg
0.0
1.0
2.0
3.0
4.0
5.0
0
200
400
600
800
1000
Velocity (m/s)
Stroke (mm)
TB3
Load 5 kg
Load 10 kg
Load 15 kg
0.0
1.0
2.0
3.0
4.0
5.0
0
200
400
600
800
1000
Velocity (m/s)
Stroke (mm)
TB4
Load 5 kg
Load 10 kg
Load 15 kg
0
10
20
30
40
50
0
50
100
150
200
250
300
Payload (kg)
Cantilever distance (mm)
TB2: Velocity < 2 m/s
0
10
20
30
40
50
0
50
100
150
200
250
300
Payload (kg)
Cantilever distance (mm)
TB3: Velocity < 2 m/s
0
10
20
30
40
50
0
50
100
150
200
250
300
Payload (kg)
Cantilever distance (mm)
TB4: Velocity < 2 m/s
0
10
20
30
40
50
0
50
100
150
200
250
300
Payload (kg)
Cantilever distance (mm)
TB2: Velocity < 2 m/s
0
10
20
30
40
50
0
50
100
150
200
250
300
Payload (kg)
Cantilever distance (mm)
TB3: Velocity < 2 m/s
0
10
20
30
40
50
0
50
100
150
200
250
300
Payload (kg)
Cantilever distance (mm)
TB4: Velocity < 2 m/s
Vertical
Horizontal

---

MM99TE07-1701
Linear Motor System
46
47
Standard
Table2-23   LMTB2 Shaft type linear motor stage specifications
Stroke
(mm)
L
(mm)
L1
(mm)
L2
(mm)
N
Mass
(kg)
100
380
30
80
2
8.2
200
480
80
80
2
9.6
300
580
55
80
3
11.0
400
680
30
80
4
12.4
500
780
80
80
4
13.8
600
880
55
80
5
15.2
700
1020
50
100
6
17.1
800
1120
25
100
7
18.5
900
1220
75
100
7
19.8
1000
1320
50
100
8
21.2
30
60
L2
120
6.5
123
136
88
(21.5)
136
(88)
有效行程
L
10
L-20
L1
Nx150
15
106
(76.5)
+ 方向
2x(N+1)-M6x1Px12DP
4-M5x0.8Px10DP
接頭
極限
Dimension
+Direction
Effective stroke
Limit
Connector
Table2-24   LMTB3 Shaft type linear motor stage specifications
Stroke
(mm)
L
(mm)
L1
(mm)
L2
(mm)
N
Mass
(kg)
100
425
52.5
80
2
9.5
200
525
27.5
80
3
10.9
300
625
77.5
80
3
12.3
400
725
52.5
80
4
13.6
500
825
27.5
80
5
15.0
600
925
77.5
80
5
16.4
700
1055
72.5
100
6
18.3
800
1165
47.5
100
7
19.7
900
1265
22.5
100
8
21.1
1000
1365
72.5
100
8
22.5
L2
22.5
2x60=120
165
6.5
123
136
有效行程
88
L
10
L-20
L1
Nx150
(76.5)
(21.5)
136
(88)
15
106
+ 方向
6-M5x0.8Px10DP
2x(N+1)-M6x1Px12DP
接頭
極限
Dimension
+Direction
Effective stroke
Limit
Connector
* Absolute accuracy is after error mapping (with HIWIN drive).
* Absolute accuracy is after error mapping (with HIWIN drive).

---

MM99TE07-1701
Linear Motor System
48
49
Standard
Table2-25   LMTB4 Shaft type linear motor stage specifications
Stroke
(mm)
L
(mm)
L1
(mm)
L2
(mm)
N
Mass
(kg)
100
470
75
80
2
11
200
570
50
80
3
12.4
300
670
25
80
4
13.8
400
770
75
80
4
15.2
500
870
50
80
5
16.6
600
970
25
80
6
18
700
1110
20
100
7
19.9
800
1210
70
100
7
21.3
900
1310
45
100
8
22.7
1000
1410
20
100
9
24.1
L2
15
3x60=180
210
6.5
123
136
有效行程
88
L
10
L-20
L1
Nx150
(76.5)
(21.5)
136
(88)
15
106
+ 方向
8-M5x0.8Px10DP
2x(N+1)-M6x1Px12DP
接頭
極限
Dimension
+Direction
Effective stroke
Limit
Connector
Table2-26   LMTC2,3,4 stage specification
Specification
TC2
TC3
TC4
Continuous force,FC (N)
92
138
184
Peak force,FP (N)
368
552
736
Stroke (mm)
100-1000
Resolution
1.0µm
Repeatability (µm) *2
±1
Accuracy (µm) *2,3
±3
Horizontal straightness (µm)
10 / 500 mm
Vertical straightness (µm)
20 / 500 mm
Moving mass (kg)
4.0
5.7
6.9
0
1
2
3
4
5
6
Force (N)
Velocity (m/s)
TC2 Fp
TC2 Fc
0
1
2
3
4
5
6
Force (N)
Velocity (m/s)
TC3 Fp
TC3 Fc
0
200
400
600
800
1000
0
200
400
600
800
1000
0
200
400
600
800
1000
0
1
2
3
4
5
6
Force (N)
Velocity (m/s)
TC4 Fp
TC4 Fc
0
10
20
30
40
50
60
0
10
20
30
40
50
60
Acceleration (m/s 2)
Payload (kg)
TC2
0
10
20
30
40
50
60
0
10
20
30
40
50
60
Acceleration (m/s 2)
Payload (kg)
TC3
0
10
20
30
40
50
60
0
10
20
30
40
50
60
Acceleration (m/s 2)
Payload (kg)
TC4
Force-Velocity Curve (DC bus = 325V)
Acceleration-Payload Curve
2.4.4  LMTC2 Shaft motor stage
*4
*1：All values are measured on a granite table, all stage mounting holes are well fixed.
*2：Values are measured according to HIWIN measuring standard.
*3：After error compensation.
*4：The Force-Velocity Curve is the characteristic curve of the motor. The actual velocity will change with stroke, payload and acceleration.
         Please refer to the Velocity-Stroke Curve or Appendix A：Motor Sizing.
*5：All specifications above are standard, contact HIWIN for special request.
* Absolute accuracy is after error mapping (with HIWIN drive).

---

MM99TE07-1701
Linear Motor System
50
51
Standard
*1：All values above are standard, contact HIWIN for special request.
*2：Cantilever load capability due to different positioning stage, application rated life also vary.
*3：The main reason for lifetime derives from linear guideway. For more details, please refer to HIWIN linear guideway catalog.
Velocity-Stroke Curve
Cantilever Load Capability*2.3 
Vertical
Horizontal
0.0
1.0
2.0
3.0
4.0
5.0
0
200
400
600
800
1000
Velocity (m/s)
Stroke (mm)
TC2
Load 10 kg
Load 20 kg
Load 30 kg
0.0
1.0
2.0
3.0
4.0
5.0
0
200
400
600
800
1000
Velocity (m/s)
Stroke (mm)
TC3
Load 10 kg
Load 20 kg
Load 30 kg
0.0
1.0
2.0
3.0
4.0
5.0
0
200
400
600
800
1000
Velocity (m/s)
Stroke (mm)
TC4
Load 10 kg
Load 20 kg
Load 30 kg
0
10
20
30
40
50
60
0
50
100
150
200
250
300
Payload (kg)
Cantilever distance (mm)
TC2: Velocity < 2 m/s
0
10
20
30
40
50
60
0
50
100
150
200
250
300
Payload (kg)
Cantilever distance (mm)
TC3: Velocity < 2 m/s
0
10
20
30
40
50
60
0
50
100
150
200
250
300
Payload (kg)
Cantilever distance (mm)
TC4: Velocity < 2 m/s
0
10
20
30
40
50
60
0
50
100
150
200
250
300
Payload (kg)
Cantilever distance (mm)
TC2: Velocity < 2 m/s
0
10
20
30
40
50
60
0
50
100
150
200
250
300
Payload (kg)
Cantilever distance (mm)
TC3: Velocity < 2 m/s
0
10
20
30
40
50
60
0
50
100
150
200
250
300
Payload (kg)
Cantilever distance (mm)
TC4: Velocity < 2 m/s
Vertical
Horizontal
Table2-27   LMTC2 Shaft type linear motor stage specifications
Stroke
(mm)
L
(mm)
L1
(mm)
L2
(mm)
N
Mass
(kg)
100
420
50
80
2
14.1
200
520
25
80
3
16.2
300
620
75
80
3
18.3
400
720
50
80
4
20.4
500
820
25
80
5
22.5
600
920
75
80
5
24.6
700
1020
50
80
6
27.5
800
1160
45
100
7
29.5
900
1260
20
100
8
31.6
1000
1360
70
100
8
33.7
L2
160
10
2x70=140
170
7.95
154
有效行程
(21.5)
168
(89)
109
L
10
L-20
L1
Nx150
(94)
16
136
+ 方向
6-M6x1.0Px12DP
2x(N+1)-M8x1.25Px16DP
極限
接頭
Dimension
+Direction
Effective stroke
Limit
Connector
* Absolute accuracy is after error mapping (with HIWIN drive).

---

MM99TE07-1701
Linear Motor System
52
53
Standard
Table2-28   LMTC3 Shaft type linear motor stage specifications
Stroke
(mm)
L
(mm)
L1
(mm)
L2
(mm)
N
Mass
(kg)
100
480
80
80
2
17
200
580
55
80
3
19.1
300
680
30
80
4
21.2
400
780
80
80
4
23.3
500
880
55
80
5
25.4
600
980
30
80
6
27.5
700
1080
80
80
6
30.4
800
1220
75
100
7
32.4
900
1320
50
100
8
34.5
1000
1420
25
100
9
36.6
L2
220
40
2x70=140
170
7.95
154
109
有效行程
L
10
L-20
L1
Nx150
(94)
(21.5)
168
(89)
16
136
+ 方向
6-M6x1.0Px12DP
2x(N+1)-M8x1.25Px16DP
極限
接頭
Dimension
+Direction
Effective stroke
Limit
Connector
Table2-29   LMTC4 Shaft type linear motor stage specifications
Stroke
(mm)
L
(mm)
L1
(mm)
L2
(mm)
N
Mass
(kg)
100
540
35
80
3
19.4
200
640
10
80
4
21.5
300
740
60
80
4
23.6
400
840
35
80
5
25.7
500
940
10
80
6
27.8
600
1040
60
80
6
29.9
700
1140
35
80
7
32.9
800
1280
30
100
8
34.9
900
1380
80
100
8
37
1000
1480
55
100
9
39.1
L2
280
35
3x70=210
8
154
170
有效行程
109
L
10
L-20
L1
Nx150
(94)
(21.5)
168
(89)
16
136
+ 方向
8-M6x1.0Px12DP
2x(N+1)-M8x1.25Px16DP
接頭
極限
Dimension
+Direction
Effective stroke
Limit
Connector
* Absolute accuracy is after error mapping (with HIWIN drive).
* Absolute accuracy is after error mapping (with HIWIN drive).

---

MM99TE07-1701
Linear Motor System
54
55
Standard
2.5  X-Y stage
LMX1 series linear motor stages can be assembled into an X-Y stage and configured for a variety of different 
X and Y strokes.
2.5.1  LMX2E-CB5-CB8 X-Y stage
　High speed
　No cogging
　High precision
　Easy to assemble
　High stiffness aluminum structure
　Ironless linear motor
　Optical inspection
Without cover
With cover
2.5.2  X-Y stage
LMX2E–CB5–CB8–200–300–G200
Stage type
LMX2E
Upper axis motor type
CB5
Lower axis motor model
CB8
Upper axis stroke
100:100mm
200:200mm
300:300mm
Lower axis stroke
100:100mm
200:200mm
300:300mm
400:400mm
Encoder type
0:none
A:40µm analog 1Vpp optical scale
B:20µm analog 1Vpp optical scale
D:1mm analog 1Vpp magnetic scale
E:TTL digital 1µm resolution magnetic scale
G:TTL digital 1µm resolution optical scale (standard)
H:TTL digital 0.5µm resolution optical scale
K:TTL digital 0.1µm resolution optical scale
M:TTL digital 20nm resolution optical scale
P:40µm glass optical analog scale
X:Other (please remark desired specifications or product model)
Limit switch
0:None
1:Metal cover
2:Optical switch, NPN (standard)
3:Optical switch, PNP
4:Inductive type, NPN
C:Customized
Cover
0:None (standard)
A:Metal cover
B:Bellows
B:Customized
D:Non-woven
Cable chain
0:None (standard)
1:Horizontal direction (chain internal space 15x30mm)
2:Vertical direction (chain internal space 15x30mm)
C:Customized
Note：Contact HIWIN for customized specification.

---

MM99TE07-1701
Linear Motor System
56
57
Standard
Table2-30   Without cover  X-Y stage product specifications
X-
Stroke
(mm)
Y-
Stroke
(mm)
LX
(mm)
LY
(mm)
L1
(mm)
L2
(mm)
N
Absolute 
accuracy 
(µm)
Resolution
(µm)
Repeatability 
(µm)
Orthogonality
(arc-sec)
X moving 
unit mass
(Kg)
Y moving 
unit mass
(Kg)
Mass
(kg)
100
100
400
500
85
111
1*1
±3
1
±1
±5
2.5
20
44
100
200
400
600
60
111
3
±3
±1
±5
2.5
20
46
200
200
500
600
60
161
4
±3
±1
±5
2.5
22
48
100
300
400
700
35
111
5
±3
±1
±5
2.5
20
48
200
300
500
700
35
161
5
±3
±1
±5
2.5
22
50
300
300
600
700
35
211
6
±3
±1
±5
2.5
24
52
100
400
400
800
85
111
7
±3
±1
±5
2.5
20
50
200
400
500
800
85
161
7
±3
±1
±5
2.5
22
52
300
400
600
800
85
211
8
±3
±1
±5
2.5
24
54
* 1: When the stroke is 100mm, the mounting holes spacing is 300mm.
* 2: Absolute accuracy is after error mapping (with HIWIN drive).
* 3: Except resolution magnetic scale.
* 4: For higher resolution, please contact HIWIN MIKROSYSTEM.
2x(N+1)-Ø6.5 THRU
,Ø11x8.5DP
36.5
105
178
L2
35
110
LX
1/2有效行程
1/2有效行程
30
15
38
17
 13 Max.
 15 Max.
L1
Nx150(註 1)
15
LY-30
LY
1/2有效行程
180
11
158
180
1/2有效行程
(45.4)
75
75
2x2-Ø6H7 THRU
X軸拖鏈內部空間
136
(148)
160
LY/2
LX/2
4-M6x1.0Px10DP
接頭
極限
Y軸拖鏈
X軸拖鏈
Y軸拖鏈內部空間
Y軸+方向
X軸+方向
Without cover 
Y axis +direction
X axis +direction
Effective stroke
Effective stroke
Effective stroke
Effective stroke
Limit
Connector
Y axis cable chain
X axis cable chain
Y-axis cable chain internal space
X-axis cable chain internal space
(*1)
2.5.3  LMX2E-CB5CB8 X-Ystage-cover type
Different stroke and function of dual axes stages consist of various standard single axes. This will shortens 
the development and mass production lead time. It can be applied in machine tool and semiconductor 
industry.
　High speed
　No cogging
　High precision
　Easy to assemble
　Optical detection application
　High rigid aluminum structure
　Ironless linear motor

---

MM99TE07-1701
Linear Motor System
58
59
Standard
Table2-31   With cover  X-Y stage product specifications
X-
Stroke
(mm)
Y-
Stroke
(mm)
LX
(mm)
LY
(mm)
L1
(mm)
L2
(mm)
N
Absolute 
accuracy 
(µm)
Resolution
(µm)
Repeatability 
(µm)
Orthogonality
(arc-sec)
X moving 
unit mass
(Kg)
Y moving 
unit mass
(Kg)
Mass
(kg)
100
100
400
500
85
111
1*1
±3
1
±1
±5
3
21
46
100
200
400
600
60
111
3
±3
±1
±5
3
21
48
200
200
500
600
60
161
4
±3
±1
±5
3
23
50
100
300
400
700
35
111
5
±3
±1
±5
3
21
50
200
300
500
700
35
161
5
±3
±1
±5
3
23
52
300
300
600
700
35
211
6
±3
±1
±5
3
25
54
100
400
400
800
85
111
7
±3
±1
±5
3
21
52
200
400
500
800
85
161
7
±3
±1
±5
3
23
54
300
400
600
800
85
211
8
±3
±1
±5
3
25
56
2x(N+1)-Ø6.5 THRU
,Ø11x8.5DP
36.5
105
178
(148)
L2
190
35
110
LX
1/2有效行程
1/2有效行程
30
15
38
17
 13 Max.
 15 Max.
L1
Nx150(註 1)
15
LY-30
LY
1/2有效行程
180
11
158
180
1/2有效行程
(45.4)
75
75
136
LY/2
LX/2
4-M6x1.0Px10DP
接頭
極限
Y軸拖鏈
X軸拖鏈
X軸拖鏈內部空間
Y軸拖鏈內部空間
2x2-Ø6H7 THRU
Y軸+方向
X軸+方向
Y axis +direction
X axis +direction
Effective stroke
Effective stroke
Effective stroke
Effective stroke
Connector
Y axis cable chain
X axis cable chain
Y-axis cable chain internal space
X-axis cable chain internal space
(*1)
Limit
* 1: When the stroke is 100mm, the mounting holes spacing is 300mm.
* 2: Absolute accuracy is after error mapping (with HIWIN drive).
* 3: Except resolution magnetic scale.
* 4: For higher resolution, please contact HIWIN MIKROSYSTEM.
With cover type
2.6 Gantry Stage
LMG2A series standardized gantry system is a unilateral drive system.
LMG2A-C applies to ironless linear motor, and LMG2A-S applies to iron core linear motor.
2.6.1  Gantry stage LMG2A-CB6-CC8
　High acceleration
　No cogging
　Low inertia
　Easy to assemble
　High stiffness aluminum gantry structure
　Equipped with ironless linear motor
　Optical detection application

---

MM99TE07-1701
Linear Motor System
60
61
Standard
2.6.2  Gantry stage
LMG2A–CB6–CC8–300–400–G200
Stage type
LMG2A
Upper axis motor type
CB6
Lower axis motor model
CC8
Upper axis stroke
200:200mm      500:500mm
300:300mm      600:600mm
400:400mm
Lower axis stroke
100:100mm      500:500mm
200:200mm      600:600mm
300:300mm
400:400mm
Encoder type
0:none
A:40µm analog 1Vpp optical scale
B:20µm analog 1Vpp optical scale
D:1mm analog 1Vpp magnetic scale
E:TTL digital 1µm resolution magnetic scale
G:TTL digital 1µm resolution optical scale (standard)
H:TTL digital 0.5µm resolution optical scale
K:TTL digital 0.1µm resolution optical scale
M:TTL digital 20nm resolution optical scale
P:40µm glass optical analog scale
X:Other (please remark desired specifications or product model)
Limit switch
0:None
1:Metal cover
2:Optical switch, NPN (standard)
3:Optical switch, PNP
4:Inductive type, NPN
C:Customized
Cover
0:None (standard)
A:Metal cover
B:Bellows
B:Customized
D:Non-woven
Cable chain
0:None (standard)
1:Horizontal direction (chain internal space 15x30mm)
2:Vertical direction (chain internal space 15x30mm)
C:Customized
Table2-31   Gantry stage LMG2A product specifications
X-
Stroke
(mm)
Y-
Stroke
(mm)
W
(mm)
W1
(mm)
W2
(mm)
W3
(mm)
N
L 
(mm)
L1 
(mm)
Absolute 
accuracy 
(µm)
Resolution
(µm)
Repeatability 

(µm)
Orthogonality
(arc-sec)
X moving 
unit mass
(Kg)
X moving 
unit mass
(Kg)
Mass
(kg)
200
200
740 440 817 110
2
600
100
±9
1µm
±3
±5
5
31
50
300
300
840 540 917 135
3
700
50
±9
±3
±5
5
35
52
400
400
940 640 1017 160
3
800
100
±12
±4
±5
5
39
54
500
500 1040 740 1117 185
4
900
50
±12
±4
±5
5
43
54
600
600 1140 840 1217 210
4
1000 100
±12
±4
±5
5
47
56
L
L1
200
Nx200
(L1)
115
189
198
168.5
1/2有效行程
1/2有效行程
180
20
2x70=140
45
90
427
280
1/2有效行程
1/2有效行程
30
150
W1
150
W
(W2)
(L3)
W3
2xW3
59.5
140
123
22.5
17
63
32
63
2x(N+1)-∅11 THRU,
∅18x12DP
3x(N+1)-M6x1Px12DP
6-M6x1Px12DP
2-∅6H7x10DP
極限
接頭
接頭
極限
X軸拖鏈內部空間
Y軸拖鏈內部空間
15
max
28
max
X軸+方向
Y軸+方向
Y axis +direction
X axis +direction
Effective stroke
Effective stroke
Effective stroke
Effective stroke
Connector
Connector
Y-axis cable chain internal space
X-axis cable chain internal space
Limit
Limit
* 1: Absolute accuracy is after error mapping (with HIWIN drive).
* 2: Except resolution magnetic scale.
* 3: For higher resolution, please contact HIWIN MIKROSYSTEM.
Note：Contact HIWIN for customized specification.

---

MM99TE07-1701
Linear Motor System
62
63
Standard
2.7  Air bearing stage
　Non-contact air bearing provides better positioning accuracy 
　Embedded magnetic preloading design, enhance stability
　Provide extremely smooth motion and rapid settling time
　Equipped with ironless linear motor, no cogging
　High resolution feedback with linear optical encoder
　Equipped with high flexible cable 
　For clean room, no need to lubricate and easy to maintain
　Low velocity ripple
　Available for precision positioning, calibration systems, scanning  
       applications, wafer inspection
Table2-33   LMAS product specifications
Specifications
Unit
AS200
AS400
AS600
AS800
AS1000
Stroke
mm
200
400
600
800
1000
Motor type
-
LMCB8
Bus voltage
V
Up to 325 VDC
Instant current
A(pk)
6
Continuous current
A(rms)
2.0
Feedback system
-
Optical Linear Encoder: Analog period 20µm
Resolution*1
µm
4
Repeatability
µm
±0.3
±0.4
±0.4
±0.5
±0.5
Positioning accuracy*2
µm
±3.0
±4.0
±4.0
±5.0
±5.0
Horizontal straightness*3
µm
±1.0
±1.0
±1.5
±2.0
±2.5
Vertical straightness*3
µm
±1.0
±1.0
±1.5
±2.0
±2.5
Pitch*3
arc-sec
±2.0
±2.5
±3
±3.5
±4
Yaw*3
arc-sec
±2.0
±2.5
±3
±3.5
±4
Roll*3
arc-sec
TBD
Allowable payload
kg
10
Max. speed*4*5
m/s
1
1.2
1.4
1.6
2
Max. acceleration*5
m/s2
10
11
12
13
14
Working pressure*6
N/m2
4x105 N/m2 ± 2x104 N/m2
Moving unit mass*7
kg
8
Moving unit material
-
Aluminum (hardened anodized)
Base
-
Granite
*1: The maximum resolution is up to 4096 times, resolution accuracy is about 4 nm
*2: Absolute accuracy is after error mapping.
*3: Required specification is restricted by load, this specification is based on empty load
*4: Must comply with the resolution of encoder and the number of mass transfer rate
*5: Based on the limitations of motor instantly force, only allow moving unit mass about 8Kg (center load)
*6: It is recommended to link pressure switch on the emergency stop devices to protect air bearing from overloading
*7: Free of load
2.7.1  Non-contact air bearing stage LMAS
Dimensions
Type
Stroke
Dimensions
A
B
C
D
N
AS200
200
280
-
526
619
2
AS400
400
480
-
726
819
2
AS600
600
580
-
926
1019
2
AS800
800
440
880
1126
1219
4
AS1000
1000
540
1080
1326
1419
4
168
(310)
30
60
120
28
D
C
B
A
60
30
20
20
5x44=220
260
13
89
115
143
12-M5x0.8Px10DP
(安裝孔位)
4x(N+1)-M8x1.5Px16DP
(安裝孔位)
  (Mounting holes)
  (Mounting holes)

---

MM99TE07-1701
Linear Motor System
64
65
Standard
2.7.2  Air bearing stage LMAP series
Low profile, XY symmetric structure design, with high stiffness granite base magnetic preload designed to 
enhance stability, with excellent geometrical property; applies ironless linear motor, no cogging to parid 
setting time, that provides excellent smooth motion and positioning accuracy; strong beam design uses high 
stiffness lightweight aluminum, reduces weight of moving unit; gantry dual-drive structure and use of two 
sets of optical linear encoder for feedback compensation, offers dynamic control and error mapping; for 
clean room, no lubrication for easy maintenance and provides high flexible cable management. 
　Wafer inspection system
　Micromachining system
　Laser lithography
　Semiconductor inspection system
　Exposure system 

Tabke2-34   LMAP series product specification
Basic model
Unit
AP250
AP450
AP650
Stroke
mm
250x250
450x450
650x650
Motor specification
-
Beam axis: LMCC8 Gantry axes: LMCB8 x 2
Bus Voltage
V
Up to 325 VDC
Instant current
A(pk)
6.0
Continuous current
A(rms)
2.0
Feedback system
-
Optical Linear Encoder: Analog period 40µm glass scale
Resolution*1
µm
10
Repeatability
µm
±0.5
±0.5
±0.5
Positioning accuracy*2
µm
±1.5
±1.5
±1.5
Horizontal straightness*3
µm
±1.5
±2
±2.5
Vertical straightness*3
µm
±1.5
±2
±2.5
Orthogonality
arc-sec
±2.5
±2.5
±3.5
Pitch*3
arc-sec
±6
±8
±12
Yaw*3
arc-sec
±1.5
±2
±2.5
Roll*3
arc-sec
TBD
Allowable load
kg
30
Max. speed*4*5
m/s
0.6
0.8
1
Max. acceleration*5
m/s2
4
4.5
5
Working pressure*6
N/m2
4x105 N/m2 ± 2x104 N/m2
Moving unit 
mass*7
Bridge
kg
30
Gantry
kg
75
85
95
Moving unit material
-
Aluminum (hardened anodized)
Base
-
Granite
Applications
*1: The maximum resolution is up to 4096 times, resolution accuracy is about 4 nm
*2: Error after compensation
*3: Required specification is restricted by load, this specification is based on empty load
*4: Must comply with the resolution of encoder and the number of mass transfer rate
*5: Based on the limitations of motor instantly force, only allow moving unit mass about 8Kg (center load)
*6: It is recommended to link pressure switch on the emergency stop devices to protect air bearing from overloading
*7: Free of load
Dimensions
Type
Stroke
Dimensions
A
B
C
AP250
250x250
1168 
1030 
1100
AP450
450x450
1368
1230
1300
AP650
650x650
1568
1430
1500
C
(386)
380
200
A
B
436
400
2x110=220
4x95=380
15-M6x1P-12DP
(安裝孔位)
28
90
  (Mounting holes)

---

MM99TE07-1701
Linear Motor System
66
67
Customized
The standardized positioning axes presented in this catalogue make it possible to handle many kinds of 
positioning tasks.For positioning tasks, that cannot be solved using standard axes, HIWIN engineers are 
able to work out an optimized solution for customers. The inquiry form at the end of this catalogue serves 
to help our application engineers make a preliminary design.
A sampling of customized solutions is shown here. In several examples, mechanics are not the only parts 
customized. For instance, with the planar motors, special software is developed in order to obtain optimal 
integration of the positioning system to the production process. 
3.1 Examples
3  Customized Positioning Systems
Planar Motors
Servo-planar motors provide an excellent technological 
stage for inspection tasks. During inspection of circuit 
boards, optical sensors are integrated to completely monitor 
the printed conductive tracks and SMD components.
	 Virtually no wear due to an air bearing
	 Guaranteed levelness for the complete stroke path  
(up to 1000 mm x 1000 mm)
	 Repeatability ± 3 µm	
Economical Pick & Place and Inspection 
XY gantry systems are economical for many applications. 
Gantry axes are assembled from standard components.  
	 Standard axes of the LMX1L series
	 Repeatability ± 2 µm
	 Delivery with base frame
Microshapes and Macroshapes
Milling of microstructures with cutting tools and lasers are 
application areas in which gantry systems excel. They are 
also very economical to implement.
	 Ironless motors LMC
	 Repeatability ± 2 µm
	 Technology proven through countless worldwide installations
Semiconductor inspection and exposure
High precision cross stages with air-bearings are the 
prerequisites for surface monitoring and mask production, to find 
even the smallest errors, to produce precision masks, in wafer 
production for the electronics, chip and flat panel industries.
	 Stroke 500 mm x 500 mm
	 Vertical straightness
	 Repeatability ±0.5 μm
	  Accuracy ±1.5 μm
Microsystem Technology and Wafer Processing
Absolute precision and suitability for clean room conditions are the 
prerequisites for every drive in microsystem technology and wafer 
processing. Linear motor cross stages meet these requirements.
	 Stroke 200 mm x 200 mm, optional 300 mm x 300 mm
	 Levelness ± 4 µm across the complete stroke
	 Repeatability ± 1 µm across both axes
	 Accuracy ± 4 µm across both axes
	 Clean room suitability class 100; optional class 10
Laser Scanners
Extremely smooth motion and long operating life are a 
must for optical inspection systems such as laser scan-
ners. Linear motor stages with air bearings fulfill these 
requirements.
	 Air bearing system without friction
	 Ironless linear motors are not effected by cogging.
	 Stroke up to 1,500 mm
Horizontal High-Speed Hot Weld Machine for Welding 
Synthetic Materials
Linear motor stages of the LMX1L series with absolute  
position measurement offer:
	 Rapid initialization phase
	 material when removed from the heated plate
	 Welding is controlled by time, force and path
	 Rapid load/unload system

---

MM99TE07-1701
Linear Motor System
68
69
Customized
Total Solution for AOI Industry
LMC linear stage provides smooth motion for the special requi-
rement in AOI applications. With the LMS linear stage mounted to 
the upper axis, the ballscrew driven Z-axis integrated with a CCD 
camera can attain high speeds. 
	 Repeatability ±1 µm
	 Velocity ripple below 1.5 %
	 Delivery with base frame and cover
Water Jet Application
LMSA multi-forcer linear stage provides 2.5m stroke and carries two 
HIWIN KK stages on the  Z-axis. The lower 2 axes are also equipped  
with LMS high force liner motors and run under synchronization.
	 No commutation required at power up
	 Long stroke
	 Delivered with base frame, cover and precision motion controller
Customized for Glass Working
The linear motor stage is designed to carry a working head to move 
 above the flat table. The customer's laser head is for cutting double  
layer glasses.

	 Gantry structure linear motor positioning stage for Gen. 5 glass
	 1300 mm x 1450 mm stroke
	 Smooth motion
	 Sinusoidal commutation and no cogging
	 LMC series motors
	 Repeatablility ±2 μm
	 Rigid base structure
 Provide motion plan for customer

This is another AOI application, where customer needed    high  
cost–performance ratio.
 Stroke 534mm x 534mm 
	 LMSA type gantry
	 Special synchrnous control for gantry
	 Steel base frame
	 Integrating PCB conveyor, PLC, IPC for customers
	 Sub-micron repeatability
	 Promising move and settle time 40mm within 200ms to ±1.5 μm
HIWIN offers a variety of customized positioning stages to satisfy customer requirements in a variety of 
technical fields, such as optical inspection, laser processing, plastic material coating, metal processing 
and other automated production equipment. Application industries include semiconductor industry, Optical 
elements, panel displays, medical equipment, machine tools, electronic components, MEMS and so on. 
Specifications diversification and the ability for rapid customization are combined to fully meet customer 
needs for mass production, a shorted product development process and strict environmental requirements.
Note1：Contact HIWIN for customized specification.
Note2: Starting from April 2016, users of LMS series linear motor positioning stage products,  
             will be fully converted to LMSA series motors.
3.2  General type positioning stage
S L A
Category
S: single-axis
D: dual-axis
R: tri-axis
G: Gantry
M: multi-axis composite
A: air bearing
Transmission method
L: linear motors
B: AC/DC servo motor
Serial number
A~Z
Model code description

---

MM99TE07-1701
Linear Motor System
70
71
Customized
3.2  SLA series
　Max. velocity 5 m/s (no load).
　Max. stroke up to 6,000 mm or more.
　High stiffness structure.
　Suitable for point-to-point motion.
　Can be equipped with ironcore motor.
　With a special chain design, it can be installed upside down.
3.2.1  Industry applications
Automation equipment, glass substrate moving equipment
3.2.2  Performance specifications
Table3-1   LMX1L-S27-6200-X202 product specification
Stage type
LMX1L-S27-6200-X202
Motor specifications
Ironcore motor (can select ironless motor)
Stroke (mm)
6200
Max. force (N)/Continuous force(N)
1017/382
Repeatability (µm)
±15 (apply HIWIN measurements)
Max. acceleration (m/s²)
10 (with Payload)
Max. speed (m/s)
2 (with Payload)
Payload (kg)
5
Stage orientation
Upside down
Note：All specifications can be designed according to customer demand.
+Direction
6630
365
343
3.3  SLB series
　High stiffness design of base.
　Milt-forcer design.
3.3.1  Industry applications
Large-scale inkjet printer, glass substrate/PCB board testing 
equipment, glass substrate exposure equipment
3.3.2  Performance specifications
Table3-2   LMX1C-CB2-4-290  product specification
Stage type
LMX1C-CB2-4-290
Motor Type
Ironless(/Ironcore) motor
Stroke(mm)
290
Peak Force(N)/Continuous 
Force(N)
144/36
Repeatability(µm)
±1(with HIWIN solution)
Accuracy(µm)
±3(after error mapping)
Max. Acceleration(m/s2)
0.05(with payload)
Max. Velocity(m/s)
0.05(with payload)
Payload(kg)
25
Stage orientation
Side-Mount
(800.5)
790
412.5
94.5
+Direction
Note：All specifications can be designed according to customer demand.

---

MM99TE07-1701
Linear Motor System
72
73
Customized
3.4  SLC series
　Uses dust-proof design.
　Uses granite base, high stiffness.
　Not easily influenced by environmental temperature.
　Can be equipped with ironless or ironcore motor.
　Horizontal straightness and vertical straightness up to ±3 μm/m.
　Design with hidden cable chain.
3.4.1  Industry applications
Automation equipment, laser cutting applications
3.4.2  Performance specifications
Table3-3   LMX1C-S27-1-460 product specification
Stage type
LMX1C-S27-1-460
Motor Type
Ironcore(/Ironless) motor
Stroke(mm)
460
Peak Force(N)/Continuous 
Force(N)
1017/382
Repeatability(µm)
±1(with HIWIN solution)
Accuracy(µm)
±3(after error mapping)
Max. Acceleration(m/s2)
5(with payload)
Max. Velocity(m/s)
1(with payload)
Horizontal Straightness(µm)
±3
Vertical Straightness(µm)
±3
Payload(kg)
30
Stage orientation
Horizontal
1068
153
400
+Direction
Note：All specifications can be designed according to customer demand.
3.5  SLD series
　Vertical Applications.
　Integrate adjustable pneumatic counterweight module.
　Equipped with ironless motor.
　In line with the smaller space requirements.
　High-speed, lightweight design.
3.5.1  Industry applications
Automation equipment, high-speed pick and place feeding equipment, electronic component assembly equipment
3.5.2  Performance specifications
Table3-4  LMX1C-TA2-1-260 product specification
Stage type
LMX1C-TA2-1-260
Motor Type
Ironless motor
Stroke(mm)
260
Peak Force(N)/Continuous 
Force(N)
108/27
Repeatability(µm)
±2(with HIWIN solution)
Accuracy(µm)
±6(after error mapping)
Max. Acceleration(m/s2)
10(with payload)
Max. Velocity(m/s)
1(with payload)
Payload(kg)
0.5
Stage orientation
Vertical
Note：All specifications can be designed according to customer demand.
(580.2)
(183.4)
(180.5)
+Direction

---

MM99TE07-1701
Linear Motor System
74
75
Customized
3.6  SLE series
　Integration of high-precision torque motor.
　Precision compensation and angular positioning.
　Simple structure, wide range of applications
　High stiffness extruded aluminum structure.
　High-speed, point-to-point motion.
　Can be equipped with ironless or ironcore motor.
3.6.1  Industry applications
Automation equipment, touch panel coating equipment, AOI testing equipment
3.6.2  Performance specifications
Table3-5   LMX1C-S47-1-700+TMS34 product specification
Stage type
LMX1C-S47-1-700+TMS34
Motor Type
Ironcore(/Ironless) motor
Stroke(mm)
700
Peak Force(N)/Continuous Force(N)
1953/733
Repeatability(µm)
±1(with HIWIN solution)
Accuracy(µm)
±3(after error mapping)
Max. Acceleration(m/s2)
10(with payload)
Max. Velocity(m/s)
1(with payload)
Payload(kg)
15
Stage orientation
Horizontal
Torque Motor Type
TMS34
Peak Torque(Nm)/Continuous Torque(Nm)
60/20
Max. Velocity(rpm)
500(220V)
Repeatability(arc-sec)
±2.5
Accuracy(arc-sec)
±25
Inertia of rotation parts(kgm2)
0.02
Note：All specifications can be designed according to customer demand.
1145
272
377.5
+Direction
3.7  SBF series
　Vertical applications.
　High load capacity of up to 200 kg.
　Linear feedback system can be applied,high positioning accuracy, 
       zero backlash.
3.7.1  Industry applications
Automation equipment, touch panel coating equipment, AOI testing, exposure apparatus.
3.7.2  Performance specifications
Table3-6   BS-2-50 product specification
Stage type
BS-2-50
Motor Type
HIWIN AC Servo motor
Stroke(mm)
50
Ball screw lead(mm)
2
Repeatability(µm)
±1(with HIWIN solution)
Accuracy(µm)
±3(after error mapping)
Max. Acceleration(m/s2)
2(with payload)
Max. Velocity(m/s)
0.05(with payload)
Horizontal Straightness(µm)
±2
Vertical Straightness(µm)
±10
Payload(kg)
200
Stage orientation
Vertical
Note：All specifications can be designed according to customer demand.
(876.5)
791
562.5
118
(187)
+Direction

---

MM99TE07-1701
Linear Motor System
76
77
Customized
3.8  SBH series
   High stiffness oblique wedge structure.
   Vertically precision positioning.
   High load capacity.
   Large installation area,can be equipped with large-size vacuum chuck.
3.8.1  Industry applications
Exposure apparatus, the touch panel lamination equipment, laser cutting, AOI testing equipment.
3.8.2  Performance specifications
Table3-7   BS-2-12 product specification
Stage type
BS-2-12
Motor Type
HIWIN AC Servo motor
Stroke(mm)
12
Ball screw lead(mm)
2
Repeatability(µm)
±2.5(uni-direction, with HIWIN solution)
Accuracy(µm)
±10(uni-direction,after error mapping)
Max. Acceleration(m/s2)
Vertical：0.5, Horizontal：0.87(with payload)
Max. Velocity(m/s)
Vertical：0.02, Horizontal：0.035(with payload)
Payload(kg)
35
Stage orientation
Horizontal
Note：All specifications can be designed according to customer demand.
365
(212)
418
+Direction
3.9  DLA series
   Integration of high-precision torque motor. 
   XY positioning with high precision angular compensation.
   Use dust-proof design.
   High stiffness extruded aluminum structure.
   Can be equipped with ironless or ironcore motor.
3.9.1  Industry applications
3D measuring equipment, glass substrate chamfering devices, glass 
substrate/PCB testing equipment.
3.9.2  Performance specifications
Table3-8   LMX2C-CB4CB7-50-50+TMS03 product specification
Stage type
LMX2C-CB4CB7-50-50+TMS03
Motor Type
Ironless(/Ironcore) motor
Stroke(mm)
50
Peak Force(N)/Continuous Force(N)
X-axis：512/128, Y-axis：292/73
Repeatability(µm)
±1(with HIWIN solution)
Accuracy(µm)
±5(after error mapping)
Max. Acceleration(m/s2)
X-axis：5, Y-axis：5(with payload)
Max. Velocity(m/s)
X-axis：0.4, Y-axis：0.2(with payload)
Payload(kg)
5
Stage orientation
Horizontal
Torque Motor Type
TMS03
Peak Torque(Nm)/Continuous Torque(Nm)
9.3/3.1
Max. Velocity(rpm)
500(220V)
Repeatability(arc-sec)
±3
Accuracy(arc-sec)
±45
Inertia of rotation parts(kgm2)
0.003
Note：All specifications can be designed according to customer demand.
X-Axis +Direction
Y-Axis +Direction
412
338
324

---

MM99TE07-1701
Linear Motor System
78
79
Customized
3.10  DLB series
　Upside down applications.
　Suitable for point-to-point motion.
　High stiffness extruded aluminum structure.
　Can be equipped with ironless or ironcore motor.
　Wide range of applications.
3.10.1  Industry applications
Automation equipment, AOI inspection applications, Wafer cutting applications.ations, Wafer cutting applications.
3.10.2  Performance specifications
Table3-9   LMX2C-S23S47L-362-390 product specification
Stage type
LMX2C-S23S47L-362-390
Motor Type
Ironcore (/Ironless) motor
Stroke(mm)
X-axis：362, Y-axis：390
Peak Force(N)/Continuous Force(N)
X-axis：639/240, Y-axis：1953/733
Repeatability(µm)
±2(with HIWIN solution)
Accuracy(µm)
±4(after error mapping)
Max. Acceleration(m/s2)
10(with payload)
Max. Velocity(m/s)
1(with payload)
Payload(kg)
10
Stage orientation
Upside down
Note：All specifications can be designed according to customer demand.
790
183
747
X-Axis +Direction
Y-Axis +Direction
3.11  DLC series
　Suitable for High-speed scanning and rapid positioning motion.
　Simple structure and wide range of applications.
3.11.1  Industry applications
Biomedical testing equipment, electronic components plug-in equipment.
3.11.2  Performance specifications
Table3-10   LMX2C-CC8CFC-150-400 product specification
Stage type
LMX2C-CC8CFC-150-400
Motor Type
Ironless(/Ironcore) motor
Stroke(mm)
X-axis：150, Y-axis：400
Peak Force(N)/Continuous Force(N)
X-axis：780/195, Y-axis：2736/684
Repeatability(µm)
±2(with HIWIN solution)
Accuracy(µm)
±5(after error mapping)
Max. Acceleration(m/s2)
X-axis：10, Y-axis：10(with payload)
Max. Velocity(m/s)
X-axis：1, Y-axis：1(with payload)
Payload(kg)
10
Stage orientation
Horizontal
Note：All specifications can be designed according to customer demand.
1266
183
(627.5)
Y-Axis +Direction
X-Axis +Direction

---

MM99TE07-1701
Linear Motor System
80
81
Customized
3.12  DLD series
　Suitable for point-to-point motion.
　Vertical straightness up to ±4 µm.
　Use dust-proof design.
　High load capacity.
　Simple structure and wide range of applications.
3.12.1  Industry applications
PCB/steel plate laser cutting applications, automation equipment, and 3D engraving machine applications.
3.12.2  Performance specifications
Table3-11   LMX2C-S37S67L-600-600 product specification
Stage type
LMX2C-S37S67L-600-600
Motor Type
Ironcore (/Ironless) motor
Stroke(mm)
X-axis：600, Y-axis：600
Peak Force(N)/Continuous Force(N)
X-axis：1425/535, Y-axis：2850/1069
Repeatability(µm)
±2(with HIWIN solution)
Accuracy(µm)
±3(after error mapping)
Max. Acceleration(m/s2)
X-axis：10, Y-axis：7(with payload)
Max. Velocity(m/s)
0.7(with payload)
Vertical Straightness(µm)
X-axis：±4, Y-axis：±5
Orthogonality(arc-sec)
±5
Payload(kg)
35
Stage orientation
Horizontal
Note：All specifications can be designed according to customer demand.
1280
250
1200
Y-Axis +Direction
X-Axis +Direction
3.13  DLE series
　Integration of high-precision torque motor. 
　X-Y positioning with high precision angular compensation.
　High stiffness extruded aluminum structure.
　Best guideway supporting structure design.
3.13.1  Industry applications
Automation equipment, AOI testing equipment, laser cutting applications, appearance grinding 
trimming equipment.
3.13.2  Performance specifications
Table3-12   LMX2C-S27S47-300-300+TMS12 product specification
Stage type
LMX2C-S27S47-300-300+TMS12
Motor Type
Ironcore (/Ironless) motor
Stroke(mm)
X-axis：300, Y-axis：300
Peak Force(N)/Continuous Force(N)
X-axis：1953/733, Y-axis：1017/382
Repeatability(µm)
±0.5(with HIWIN solution)
Accuracy(µm)
±1(after error mapping)
Max. Acceleration(m/s2)
5(with payload)
Max. Velocity(m/s)
0.8(with payload)
Orthogonality(arc-sec)
±5
Payload(kg)
40
Stage orientation
Horizontal
Torque Motor Type
TMS12
Peak Torque(Nm)/Continuous Torque(Nm) 15/5
Max. Velocity(rpm)
700(220V)
Repeatability(arc-sec)
±3
Accuracy(arc-sec)
±45
Inertia of rotation parts(kgm2)
0.006
Note：All specifications can be designed according to customer demand.
730
310
730
Y-Axis +Direction
X-Axis +Direction

---

MM99TE07-1701
Linear Motor System
82
83
Customized
3.14  DLF series
　Stainless steel cover, can withstand Instantaneous high temperature.
　Maze dust-proof design.
　With short setting time.
　Low center of gravity design.
　Equipped with ironless motor.
3.14.1  Industry applications
Automation equipment, laser cutting equipment.
3.14.2  Performance specifications
Table3-13   LMX2C-CB7CC7-280-340 product specification
Stage type
LMX2C-CB7CC7-280-340
Motor Type
Ironless motor
Stroke(mm)
X-axis：280, Y-axis：340
Peak Force(N)/Continuous Force(N)
X-axis：512/128, Y-axis：684/171
Repeatability(µm)
±3(with HIWIN solution)
Accuracy(µm)
±5(after error mapping)
Max. Acceleration(m/s2)
X-axis：10, Y-axis：5(with payload)
Max. Velocity(m/s)
X-axis：0.7, Y-axis：0.5(with payload)
Orthogonality(arc-sec)
±5
Payload(kg)
35
Stage orientation
Horizontal
Note：All specifications can be designed according to customer demand.
675
610
149
Y-Axis +Direction
X-Axis +Direction
3.15  DLG series
   Sealed architecture.
   Suitable for the high dust environment.
   Low center of gravity design.
   With short setting time.
   Equipped with ironless motor.
3.15.1  Industry applications
Automation equipment, laser cutting equipment, PCB drilling equipment.
3.15.2  Performance specifications
Table3-14   LMX2C-CE4CE6-2-450-500 product specification
Stage type
LMX2C-CE4CE6-2-450-500
Motor Type
Ironless motor
Stroke(mm)
X-axis：500, Y-axis：450
Peak Force(N)/Continuous Force(N)
X-axis：1104/276, Y-axis：736/184
Repeatability(µm)
±1(with HIWIN solution)
Accuracy(µm)
±1.5(after error mapping)
Max. Acceleration(m/s2)
5(with payload)
Max. Velocity(m/s)
0.22(with payload)
Payload(kg)
35
Stage orientation
Horizontal
Note：All specifications can be designed according to customer demand.
(1171)
(1001)
232.5
X-Axis +Direction
Y-Axis +Direction

---

MM99TE07-1701
Linear Motor System
84
85
Customized
3.16  DLH series
　Suitable for vacuum environment, 1x10-6 Torr.
　Vacuum flat cable.
　Integration of high-precision torque motor.
　X-Y positioning with high precision angular compensation.
　Can be equipped with ironless or ironcore motor.
3.16.1  Industry applications
Automation equipment, plasma repair equipment, electron beam scanning applications.
3.16.2  Performance specifications
Table3-15   LMX2C-S23S27-360-240+TMS32 product specification
Stage type
LMX2C-S23S27-360-240+TMS32
Motor Type
Ironcore (/Ironless) motor
Stroke(mm)
X-axis：240, Y-axis：360
Peak Force(N)/Continuous Force(N)
X-axis：1017/382, Y-axis：639/240
Repeatability(µm)
X-axis：±2, Y-axis：±1(with HIWIN solution)
Accuracy(µm)
X-axis：±5, Y-axis：±3(after error mapping)
Max. Acceleration(m/s2)
X-axis：5, Y-axis：5(with payload)
Max. Velocity(m/s)
X-axis：0.7, Y-axis：1(with payload)
Payload(kg)
5
Stage orientation
Horizontal
Torque Motor Type
TMS32
Peak Torque(Nm)/Continuous Torque(Nm) 30/10
Max. Velocity(rpm)
700(220V)
Repeatability(arc-sec)
±3
Accuracy(arc-sec)
±15
Inertia of rotation parts(kgm2)
0.014
Note：All specifications can be designed according to customer demand.
870
650
326
Y-Axis +Direction
X-Axis +Direction
3.17  DLJ series
　Integration of high-precision torque motor.
　XY positioning with high precision angular compensation.
　Low center of gravity design.
　With short setting time.
　Excellent servo stability.
　Use low dust flat cable(class 1).
　Can be equipped with ironless or ironcore motor.
3.17.1  Industry applications
The semiconductor wafer inspection equipment, AOI equipment.
3.17.2  Performance specifications
Table3-16   LMX2C-SA11LSA21L-420-490+TMF42 product specification
Stage type
LMX2C-SA11LSA21L-420-490+TMF42
Motor Type
Ironcore (/Ironless) motor
Stroke(mm)
X-axis：420, Y-axis：490
Peak Force(N)/Continuous Force(N)
X-axis：254/90, Y-axis：462/149
Repeatability(µm)
±0.5(with HIWIN solution)
Accuracy(µm)
±2(after error mapping)
Max. Acceleration(m/s2)
6.5(with payload)
Max. Velocity(m/s)
0.5(with payload)
Vertical Straightness(µm)
±10
Orthogonality(arc-sec)
±5
Payload(kg)
10
Stage orientation
Horizontal
Torque Motor Type
TMF42
Peak Torque(Nm)/Continuous Torque(Nm) 3.6/1.2
Max. Velocity(rpm)
120(220V)
Repeatability(arc-sec)
±2.5
Accuracy(arc-sec)
±25
Inertia of rotation parts(kgm2)
0.0005
Note：All specifications can be designed according to customer demand.
750
630
180
Y-Axis +Direction
X-Axis +Direction

---

MM99TE07-1701
Linear Motor System
86
87
Customized
3.18  DLK series
　Multi-forcer simultaneously motion.
　Suitable for laterally applications.
　For high-speed reciprocating motion.
　Z-axis using a linear motor with a pneumatic counterweight design.
　With high speed and high accuracy.
　Can be equipped with ironless or ironcore motor.
3.18.1  Industry applications
Solar automation equipment, high-speed pick and place feeding equipment, 
electronic components assembly equipment.
3.18.2  Performance specifications
Table3-17   LMX4C-S13S37-2-32-750 product specification
Stage type
LMX4C-S13S37-2-32-750
Motor Type
Ironcore (/Ironless) motor
Stroke(mm)
Z-axis：32, Y-axis：750
Peak Force(N)/Continuous Force(N)
Z-axis：540/203, Y-axis：1425/535
Repeatability(µm)
±2(with HIWIN solution)
Accuracy(µm)
±5(after error mapping)
Max. Acceleration(m/s2)
Z-axis：10, Y-axis：10(with payload)
Max. Velocity(m/s)
Z-axis：0.5, Y-axis：1.3(with payload)
Payload(kg)
10
Stage orientation
Laterally
Note：All specifications can be designed according to customer demand.
1714
(685)
462
Y-Axis +Direction
Z-Axis +Direction
3.19  RLA series
　Fully enclosed waterproof design.
　Using non-contact air bearing.
　XY cantilever structure.
　Space saving.
　Lightweight and high-stiffness design.
　Can be equipped with ironless or ironcore motor.
3.19.1  Industry applications
Waterjet equipment, laser cutting equipment, automation equipment.
3.19.2  Performance specifications
Table3-18   LMX2C-S13S17-510-510 product specification
Stage type
LMX2C-S13S17-510-510
Motor Type
Ironcore (/Ironless) motor
Stroke(mm)
X-axis：510, Y-axis：510
Peak Force(N)/Continuous Force(N)
X-axis：540/203, Y-axis：609/228
Repeatability(µm)
X-axis：±2, Y-axis：±2(with HIWIN solution)
Accuracy(µm)
X-axis：±5, Y-axis：±5(after error mapping)
Max. Acceleration(m/s2)
X-axis：10, Y-axis：5(with payload)
Max. Velocity(m/s)
X-axis：0.8, Y-axis：0.5(with payload)
Payload(kg)
10
Stage orientation
Horizontal
Note：All specifications can be designed according to customer demand.
(1116)
1217.5
669.5
Y-Axis +Direction
X-Axis +Direction

---

MM99TE07-1701
Linear Motor System
88
89
Customized
3.20  RLB series
　Z-axis counterweight design.
　Excellent low speed velocity stability ±1 %@10 mm/s.
　Fully enclosed waterproof design.
　High positioning accuracy up to ±1 µm.
　Can be equipped with ironless or ironcore motor.
3.20.1  Industry applications
Micromachining equipment, 3D measurement equipment, 3D engraving equipment.
3.20.2  Performance specifications
Table3-19   LMX3C-CB5CB5CB8-200-200-200 product specification
Stage type
LMX3C-CB5CB5CB8-200-200-200
Motor Type
Ironless(/Ironcore) motor
Stroke(mm)
X-axis：200, Y-axis：200, Z-axis：200
Peak Force(N)/Continuous Force(N)
X-axis：580/145, Y-axis：364/91, Z-axis：364/91
Repeatability(µm)
±0.5(with HIWIN solution)
Accuracy(µm)
±1(after error mapping)
Max. Acceleration(m/s2)
X-axis：0.5, Y-axis：0.5, Z-axis：0.5(with payload)
Max. Velocity(m/s)
X-axis：0.2, Y-axis：0.2, Z-axis：0.05(with payload)
Orthogonality(arc-sec)
X-Y：±4, Y-Z：±2, X-Z：±3
Speed ripple
X-axis：1.35, Y-axis：0.93, Z-axis：1.57(when V=5mm/s)
Payload(kg)
5
Stage orientation
Horizontal
Note：All specifications can be designed according to customer demand.
568.5
613.5
682.5
Y-Axis +Direction
X-Axis +Direction
Z-Axis +Direction
3.21  RBC series
　Z-axis designed with KK series ballscrew driven stage module significantly  
       reduces system cost.
　Use dust-proof design.
　Three-dimensional motion.
　Simple structure design.
3.21.1  Industry applications
Mechanical component testing equipment, automation equipment, 3D engraving equipment.
3.21.2  Performance specifications
Table3-20   KK6010-KK6010-KK6005-150-150-150 product specification
Stage type
KK6010-KK6010-KK6005-150-150-150
Motor Type
HIWIN AC Servo motor
Stroke(mm)
X-axis：55, Y-axis：55, Z-axis：55
Ball screw lead(mm)
X-axis：10, Y-axis：10, Z-axis：5
Repeatability(µm)
±2(uni-direction, with HIWIN solution)
Accuracy grade
C
Max. Acceleration(m/s2)
X-axis：5, Y-axis：5, Z-axis：5(HIWIN 100W, with payload)
Max. Velocity(m/s)
X-axis：0.5, Y-axis：0.5, Z-axis：0.2(HIWIN 100W, with payload)
Payload(kg)
1
Stage orientation
Horizontal
Note：All specifications can be designed according to customer demand.
385
385
441
Y-Axis +Direction
X-Axis +Direction
Z-Axis +Direction

---

MM99TE07-1701
Linear Motor System
90
91
Customized
3.22  GLA series
   Micro gantry structure.
   Space saving.
   Lightweight beam design.
   High dynamic response.
   Can be equipped with ironless or ironcore motor.
3.22.1  Industry applications
Electronic components assembly equipment, biomedical 
equipment industries, AOI testing equipment.
3.22.2  Performance specifications
Table3-21   LMG2C-S11S11-200-200+KK4005C-150A1-F2M product specification
Stage type
LMG2C-S11S11-200-200+KK4005C-150A1-F2M
Motor Type
Ironcore (/Ironless) motor & HIWIN AC Servo motor
Stroke(mm)
X-axis：200, Y-axis：200, Z-axis：50
Peak Force(N)/Continuous Force(N)
X-axis：254/92, Y-axis：254/92, Z-axis：HIWIN 50W(220V)
Ball screw lead(mm)
Z-axis：5
Repeatability(µm)
X-axis：±2, Y-axis：±3, Z-axis：±2(uni-direction, with 
HIWIN solution)
Accuracy(µm)
X-axis：±5, Y-axis：±10, Z-axis：±10(uni-direction, after 
error mapping)
Max. Acceleration(m/s2)
X-axis：5, Y-axis：5, Z-axis：5(with payload)
Max. Velocity(m/s)
X-axis：1, Y-axis：0.5, Z-axis：0.04(with payload)
Payload(kg)
1
Stage orientation
Horizontal
Note：All specifications can be designed according to customer demand.
572
(419)
470
Y-Axis +Direction
Z-Axis +Direction
X-Axis +Direction
3.23  GLB series
   High stiffness aluminum gantry structure.
   Use dust-proof design.
   Z-axis designed with KK series ballscrew driven stage module.
   Unilateral or bilateral drive structure are seletable according 
to the precision requirement.
   Can be equipped with ironless or ironcore motor.
3.23.1  Industry applications
Automation industrial equipment, laser cutting applications, spraying equipment
3.23.2  Performance specifications
Table3-22   LMG2A-S13S23-600-900+KK6005C-400A1-F2BS2M product specification
Stage type
LMG2A-S13S23-600-900+KK6005C-400A1-F2BS2M
Motor Type
Ironcore (/Ironless) motor & HIWIN AC Servo motor
Stroke(mm)
X-axis：600, Y-axis：900, Z-axis：234
Peak Force(N)/Continuous Force(N)
X-axis：540/203, Y-axis：639/240, Z-axis：HIWIN 100W(220V)
Ball screw lead(mm)
Z-axis：5
Repeatability(µm)
X-axis：±5, Y-axis：±5, Z-axis：±2(uni-direction, with 
HIWIN solution)
Accuracy(µm)
X-axis：±15, Y-axis：±15, Z-axis：C(uni-direction, after 
error mapping)
Max. Acceleration(m/s2)
5(with payload)
Max. Velocity(m/s)
0.2(with payload)
Payload(kg)
5
Stage orientation
Horizontal
Note：All specifications can be designed according to customer demand.
1373
 1600
(812.5)
X-Axis +Direction
Z-Axis +Direction
Y-Axis +Direction

---

MM99TE07-1701
Linear Motor System
92
93
Customized
3.24  GLD series
    High stiffness cast iron base.
    With excellent vibration suppression capability.
    Suitable for high acceleration and deceleration applications.
    With excellent positioning accuracy.
    Unilateral or bilateral drive structure are seletable according to the  
       precision requirement.
3.24.1  Industry applications
Automation equipment, PCB AOI inspection applications.
3.24.2  Performance specifications
Table3-23   LMG2C-S13S37L-515-540 product specification
Stage type
LMG2C-S13S37L-515-540
Motor Type
Ironcore (/Ironless) motor
Stroke(mm)
X-axis：515, Y-axis：540
Peak Force(N)/Continuous Force(N)
X-axis：540/203, Y-axis：1425/535
Repeatability(µm)
±1(uni-direction, with HIWIN solution)
Accuracy(µm)
±2(after error mapping)
Max. Acceleration(m/s2)
X-axis：15, Y-axis：10(with payload)
Max. Velocity(m/s)
X-axis：1.5, Y-axis：1.5(with payload)
Vertical Straightness(µm)
10
Horizontal Straightness(µm)
10
Pitch(arc-sec)
25
Yaw(arc-sec)
X-axis：20, Y-axis：15
Orthogonality(arc-sec)
±5
Payload(kg)
12
Stage orientation
Horizontal
Note：All specifications can be designed according to customer demand.
(1103.4)
930
649
X-Axis +Direction
Y-Axis +Direction
3.25  GLE series
    High stiffness aluminum gantry structure.
    Suitable for high acceleration and deceleration applications.
    Maximize the working area.
    Space saving.
    Can be equipped with ironless or ironcore motor.
3.25.1  Industry applications
Automation equipment, electronic components plug-in assembly 
equipment, AOI equipment, automatic coating equipment
3.25.2  Performance specifications
Table3-24   LMG2C-SA11SA22-580-500 product specification
Stage type
LMG2C-SA11SA22-580-500
Motor Type
Ironcore (/Ironless) motor
Stroke(mm)
X-axis：580, Y-axis：500
Peak Force(N)/Continuous Force(N)
X-axis：289/121, Y-axis：1023/426
Repeatability(µm)
±2.5(uni-direction, with HIWIN solution)
Accuracy(µm)
±5(after error mapping)
Max. Acceleration(m/s2)
X-axis：10, Y-axis：10(with payload)
Max. Velocity(m/s)
X-axis：0.5, Y-axis：0.5(with payload)
Vertical Straightness(µm)
±5
Horizontal Straightness(µm)
±5
Payload(kg)
5
Stage orientation
Horizontal
Note：All specifications can be designed according to customer demand.
1015
(619)
(1238.5)
X-Axis +Direction
Y-Axis +Direction

---

MM99TE07-1701
Linear Motor System
94
95
Customized
3.26  GLF series
   Use dust-proof design.
   Granite base, Steel beams.
   Modular Z-axis with a high-precision torque motor. 
   Can be equipped with ironless or ironcore motor.
3.26.1  Industry applications
Optical detection applications, 3D measurement system
3.26.2  Performance specifications
Table3-25   LMG3C-S47LS37L-750-550 +KK8610P-340A1-F0BS2M+TMN71EH product specification
Stage type
LMG3C-S47LS37L-750-550 +KK8610P-340A1-
F0BS2M+TMN71EH
Motor Type
Ironcore (/Ironless) motor & HIWIN AC Servo motor
Stroke(mm)
X-axis：750, Y-axis：550, Z-axis：170
Peak Force(N)/Continuous Force(N)
X-axis：1953/733, Y-axis：1425/535, Z-axis：HIWIN 400W
Repeatability(µm)
X-axis：±1, Y-axis：±1, Z-axis：±2(with HIWIN solution)
Accuracy(µm)
±3(after error mapping)
Max. Acceleration(m/s2)
X-axis：20, Y-axis：4, Z-axis：2.5(with payload)
Max. Velocity(m/s)
X-axis：1, Y-axis：1, Z-axis：0.5(with payload)
Payload(kg)
5
Stage orientation
Horizontal
Torque Motor Type
TMN71EH
Peak Torque(Nm)/Continuous Torque(Nm) 11.1/3.7
Max. Velocity(rpm)
600(220V)
Repeatability(arc-sec)
±2.5
Accuracy(arc-sec)
±10
Inertia of rotation parts(kgm2)
0.008
Note：All specifications can be designed according to customer demand.
1604
1400
(1073.2)
X-Axis +Direction
Y-Axis +Direction
Z-Axis +Direction
3.27  GBC series
   Ballscrew structure.
   High acceleration and deceleration motion.
   Can be equipped with linear scale to enhance the positioning 
      accuracy and reproducibility.
   Simple structure.
3.27.1  Industry applications
Automation equipment, AOI inspection applications.
3.27.2  Performance specifications
Table3-26   BS-20-540+BS-20-515 product specification
Stage type
BS-20-540+BS-20-515
Motor Type
HIWIN AC Servo motor
Stroke(mm)
X-axis：515, Y-axis：540
Ball screw lead(mm)
20
Repeatability(µm)
±2.5(uni-direction, with HIWIN solution)
Accuracy(µm)
±6(after error mapping)
Max. Acceleration(m/s2)
X-axis：12, Y-axis：17(with payload)
Max. Velocity(m/s)
X-axis：1, Y-axis：1(with payload)
Vertical Straightness(µm)
20
Horizontal Straightness(µm)
20
Pitch(arc-sec)
30
Yaw(arc-sec)
X-axis：20, Y-axis：25
Orthogonality(arc-sec)
±10
Payload(kg)
9
Stage orientation
Horizontal
Note：All specifications can be designed according to customer demand.
1110
(1351)
1040
X-Axis +Direction
Y-Axis +Direction

---

MM99TE07-1701
Linear Motor System
96
97
Customized
3.28  MLA series
 Integration of high-precision TMN torque motor. 
 With excellent flatness(X-Y-theta 0.01 mm).
 Water cooling design, reduce thermal deformation.
 XY Stage low center of gravity design.
 Can be equipped with ironless or ironcore motor.
3.28.1  Industry applications
Wafer cutting, the glass substrate testing equipment, wafer bonding.
3.28.2  Performance specifications
Table3-27   LMX2C-F23F43-300-300+BS-5-170+TMN93EH product specification
Stage type
LMX2C-F23F43-300-300+BS-5-170+TMN93EH
Motor Type
Ironcore (/Ironless) motor & HIWIN AC Servo motor
Stroke(mm)
X-axis：362, Y-axis：390
Peak Force(N)/Continuous Force(N)
X-axis：2082/764, Y-axis：5496/2252
Repeatability(µm)
±0.5(with HIWIN solution)
Accuracy(µm)
±1(after error mapping)
Max. Acceleration(m/s2)
10(with payload)
Max. Velocity(m/s)
1(with payload)
Payload(kg)
Z-axis：50, A-axis：30
Stage orientation
Horizontal
Torque Motor Type
TMN93EH
Peak Torque(Nm)/Continuous Torque(Nm) 45/15
Max. Velocity(rpm)
300(220V)
Repeatability(arc-sec)
±2.5
Accuracy(arc-sec)
±25
Inertia of rotation parts(kgm2)
0.052
Note：All specifications can be designed according to customer demand.
1610
1415
1638.6
X-Axis +Direction
Y-Axis +Direction
Z-Axis +Direction
3.29  MLB series
　Multi-axis simultaneously motion.
　Good working efficiency.
　High stiffness honeycomb beam design.
　High acceleration and deceleration motion.
　With excellent settling time.
　Can be used with automated pick and place conveying mechanism.
　Can be equipped with ironless or ironcore motor.
3.29.1  Industry applications
Precision component assembly applications, electronic components plug-in equipment.
3.29.2  Performance specifications
Table3-28   LMX8C-SA11F13-264-632 product specification
Stage type
LMX8C-SA11F13-264-632
Motor Type
Ironcore (/Ironless) motor
Stroke(mm)
X-axis：264, Y-axis：632
Peak Force(N)/Continuous Force(N)
X-axis：289/121, Y-axis：1380/510
Repeatability(µm)
X-axis：±1, Y-axis：±2(with HIWIN solution)
Accuracy(µm)
X-axis：±3, Y-axis：±5(after error mapping)
Max. Acceleration(m/s2)
X-axis：20, Y-axis：30(with payload)
Max. Velocity(m/s)
X-axis：1, Y-axis：1(with payload)
Horizontal Straightness(µm)
±10
Orthogonality(arc-sec)
±10
Payload(kg)
1
Stage orientation
Horizontal
Note：All specifications can be designed according to customer demand.
1340
1580
1388
X3-Axis +Direction
X1-Axis +Direction
X2-Axis +Direction
X4-Axis +Direction
Y4-Axis +Direction
Y2-Axis +Direction
Y1-Axis +Direction
Y3-Axis +Direction

---

MM99TE07-1701
Linear Motor System
98
99
Customized
3.30  ALA series
　Using non-contact air bearing.
　Without maintenance.
　High positioning accuracy.
　Not easily influenced by environmental temperature.
　With high-precision and large-size vacuum chuck.
　With passive vibration suppressing system.
　Integrated electronic control system.
　Equipped with ironless motor.
3.30.1  Industry applications
Glass substrate exposure Application, white testing equipment, wafer defect detection equipment.
3.30.2  Performance specifications
Table3-29   LMAP-CC8CB8-700-800+BS-2-50 product specification
Stage type
LMAP-CC8CB8-700-800+BS-2-50
Motor Type
Ironless motor
Stroke(mm)
X-axis：700, Y-axis：800, Z-axis：50
Peak Force(N)/Continuous Force(N)
X-axis：580/145, Y-axis：780/195, Z-axis：HIWIN 1KW(220V)
Repeatability(µm)
X-axis：±0.5, Y-axis：±0.5, Z-axis：±2(with HIWIN solution)
Accuracy(µm)
X-axis：±1.5, Y-axis：±1.5, Z-axis：±6(after error mapping)
Max. Acceleration(m/s2)
X-axis：2.5, Y-axis：4(with payload 10 kg), Z-axis：2(with payload 
200 kg)
Max. Velocity(m/s)
X-axis：0.3, Y-axis：0.3(with payload 10 kg) , Z-axis：0.05(with 
payload 200 kg)
Vertical Straightness(µm)
X-axis：±2, Y-axis：±2, Z-axis：±10
Horizontal Straightness(µm)
X-axis：±1, Y-axis：±1, Z-axis：±2
Orthogonality(arc-sec)
XY-axis：±5
Payload(kg)
XY-axis：10, Z-axis：200
Stage orientation
Horizontal
Note：All specifications can be designed according to customer demand.
2154
1868.5
1604
Y-Axis +Direction
Z-Axis +Direction
X-Axis +Direction
3.31  ALB series
   Using non-contact air bearing.
   Without maintenance.
   High positioning accuracy.
   Not easily influenced by environmental temperature.
   With high-precision and large-size vacuum chuck.
   Z direction jitter 100 nm.
   Vertical straightness up to ±1 µm.
   Equipped with ironless motor.
3.31.1  Industry applications
Glass substrate exposure Application, white testing equipment, wafer defect detection equipment.
3.31.2  Performance specifications
Table3-30   LMAP-CC8CB8-250-250 product specification
Stage type
LMAP-CC8CB8-250-250
Motor Type
Ironless motor
Stroke(mm)
X-axis：250, Y-axis：250
Peak Force(N)/Continuous 
Force(N)
X-axis：780/195, Y-axis：580/145
Repeatability(µm)
±0.75(with HIWIN solution)
Accuracy(µm)
±1.5(after error mapping)
Max. Acceleration(m/s2)
2(with payload)
Max. Velocity(m/s)
0.25(with payload)
Vertical Straightness(µm)
±1
Horizontal Straightness(µm)
±2
Orthogonality(arc-sec)
±3
Payload(kg)
15
Stage orientation
Horizontal
Note：All specifications can be designed according to customer demand.
1180
1100
486
X-Axis +Direction
Y-Axis +Direction

---

MM99TE07-1701
Linear Motor System
100
101
Drives
3.32  ALC series
　Using non-contact air bearing.
　Without maintenance.
　High positioning accuracy.
　High load capacity of up to 680 kg.
　Vertical straightness up to ±3 µm.
　Equipped with ironless motor.
3.32.1  Industry applications
Large-size glass substrate detection equipment
3.32.2  Performance specifications
Table3-31   LMAP-CFC-1-2350 product specification
Stage type
LMAP-CFC-1-2350
Motor Type
Ironless motor
Stroke(mm)
2320
Peak Force(N)/Continuous Force(N)
2736/684
Repeatability(µm)
±0.5 (with HIWIN solution)
Accuracy(µm)
±2(after error mapping)
Max. Acceleration(m/s2)
2(with payload)
Max. Velocity(m/s)
0.7(with payload)
Vertical Straightness(µm)
±4
Horizontal Straightness(µm)
±3
Payload(kg)
680
Stage orientation
Horizontal
Note：All specifications can be designed according to customer demand.
3620
1118.5
357.5
+Direction
4.1 HIWIN D1 servo motor drive
　Digital drive
　Vector control
　Lightening human, machine interface
　100-240Vac power input
　Support various pulse wave formats
　Support analog or digital optical scales
Motion
Controller
DC24V
LM STAGE
Drive
PC
CN1
CN3 CN2 CN4
Main Power
Option
1
4
3
2
5
6
Pulse signal etc.
Limit signals
CN2
CN3
4  Drive

---

MM99TE07-1701
Linear Motor System
102
103
Drives
4.2 HIWIN D1-N servo motor drive
Motion
Controller
DC24V
LM STAGE
PC
CN1
CN3 CN2
CN4
Option
7
10
9
11
Pulse signal etc.
Limit signals
X4
X3
X9
X2
X1
X5
X10/X11
X6
Drive
Main Power
8
12
　Current vector control
　Best for driving linear motors, shaft motors and torque motors
　100-240VAC power input
　Supports STP / DIR, CW / CCW, A / B pulse formats
       (differential / single ended interace)
　upports ±10V voltage or digital commands for velocity or 
       force/ torque modes
　PDL general motion language
　Supports analog and digital encoder and resolver
Name
Speciﬁcation
Connector
Description
RS-232communication 
cable
LMACR21D
D-sub 
connector 
and CN1
D-Sub9PIN to RJ-11
Regenerative resistor
050100700001
Rated power 100W, instant power 500W
D1 Drive connector 
accessories kit bag
D1-CK1
All connectors (not included CN3)
All connectors (also included CN3)
EMC accessories kit bag
D1-EMC1
Single phase power
D1-EMC2
Three phase power
Heat sink
D1-H1
Standard
D1-H2
Small type
Digital Hall sensor
LMAHS
Suitable for LMS series, single-ended signal
LMAHC
Suitable for  LMCA,LMCB and LMCC series, single-ended signal
LMAHC2
Suitable for  LMCD and LMCE series, single-ended signal
Analog Hall sensor
LMAHSA-D
Suitable for  LMS series, differential signal
LMAHCA-D
Suitable for  LMCA,LMCB and LMCC series, differential signal
Table4-1   Drive peripheral accessories
Note
Note
4.3 D1 related accessories
3
10
4
Note：Please contact us for hall sensor.

---

MM99TE07-1701
Linear Motor System
104
105
Drives
4.4.1  D1 related cables
Name
Speciﬁcation
Connector
Description
Control signal
cables
LMACK30R
CN2
To motion controller (about 3 meters long)
Limit switch 
extension cord
LMACKS
Motor power 
supply cables and 
over-temperature 
signal cables
LMACSD
Motor 
power 
connector 
(U.V.W)
LMACSL
LMACST
LMACSK
LMACSF
Drive connectors (3M)
Model: 10126-3000VE
Suitable for linear motor positioning stages
Suitable for LMS series linear motors，LMC series linear motors: LMC-
EFE、LMC-EFF
Suitable for TMS、TMN、TMY series torque motors (not include over-
temperature signal)
Suitable for LMC series linear motors: A, B, C, D, E, EFC LMT series linear 
motors: A, B, C
Suitable for LMSA series linear motors
D-Sub9 Pin to discrete wires
Interconnect to discrete cables and over-temperature connector
Intercontec to discrete cables
Suitable for LMCF motors
Note
Note
9W4S to discrete cables and over-temperature connector
9W4S to discrete cables and over-temperature connector
9W4S to discrete cables and over-temperature connector
Table4-2   Control signals, limit signals, motor power cables
Note
Note
Note
Note
Note
Note
Note
Note
Note
Note
4.4 Cables and connectors
6
1
5
12
2
Drive
Speciﬁcation
Connector
Description
HIWIN 
D1-XX-S2 
series
LMACEY
CN3
For Renishaw digital optical scale, motor over-temperature signal.
LMACEZ
Renishaw digital optical scale, motor over-temperature signal, digital Hall 
component signals.
LMACEC
Renishaw digital optical scale, motor over-temperature signal.
LMACEJ
Renishaw analog optical scale, motor over-temperature signal, digital Hall
HIWIN 
D1-XX-S3 
series
LMACEAW
LMACEAV
HIWIN 
D1-XX-S8 
series
LMACEAA
Jena for analog encoder, motor over-temperature signal, suitable for TMS 
series torque motors.
LMACEAM
Jena for analog encoder, motor over-temperature signal, Hall component 
signals.
HIWIN 
D1-XX-SR 
series
LMACEAD
HIWIN 
D1-XX-DR 
series
LMACEAU
Intercontec
Model no.：ASTA876NN0085200A000
Intercontec
Model no.：ASTA876NN0085200A000
Intercontec
Model no.：ASTA876NN0085200A000
Intercontec
Model no.：ASTA876NN0085200A000

03
04
05
06
07
08
09
10
Cable 
length (m)
3
4
5
6
7
8
9
10
Motor over-temperature connector
Motor over-temperature connector
Motor over-temperature connector
Motor over-temperature connector
For position feedback D-SUB 15 female connector
For position feedback D-SUB 15 female connector
Digital Hall component D-SUB 9 female connector
Digital Hall component D-SUB 9 female connector
Drive connector (3M) 
Model no.：10120-3000VE
Drive connector (3M) 
Model no.：10120-3000VE
Drive connector (3M) 
Model no.：10120-3000VE
Drive connector (3M) 
Model no.：10120-3000VE
Drive connector (3M) 
Model no.：10120-3000VE
Renishaw digital optical scale, 
motor over-temperature signal.
Renishaw digital optical scale, motor 
over-temperature signal, digital Hall 
component signals.
Single Resolver extension cable, includes over-temperature signal.
Dual Resolver extension cable, includes over-temperature signal.
Table4-3   Position feedback cables
Note
Note
Note
Note
Note
Note
Note
Note
Note
Note
component signals.

---

MM99TE07-1701
Linear Motor System
106
107
Drives
4.4.2  Pin assignments of D1 
Signal
D-SUB 15Pin
female 
connector
Color
(051400300063)
D-SUB 20Pin
male 
connector
5V
7
Brown
3
0V
2
White
2
A+
14
Green
4
A-
6
Yellow
5
B+
13
Blue
6
B-
5
Red
7
Z+
12
Violet
8
Z-
4
Grey
9
Inner Shield
15
Inner shield
20
Case
-
Outer shield
1
Signal
2Pin  
female 
connector
Color
(051400300133)
T+
1
Brown
14
T-
2
Blue
15
Signal
D-SUB 9Pin
female 
connector
Color
(051400100075)
5V
1
Brown
3
Hall A
2
White
11
Hall B
3
Grey
12
Hall C
4
Yellow
13
0V
5
Green
10
Shield
Case
Shield
1
Signal
D-SUB 15Pin
female 
connector
Color
(051400300063)
D-SUB 20Pin
male 
connector
5V
4
Brown
3
0V
12
White
2
Sin(+)
9
Green
16
Sin(-)
1
Yellow
17
Cos(+)
10
Blue
18
Cos(-)
2
Red
19
Z+
3
Violet
8
Z-
11
Grey
9
Inner Shield
15
Inner shield
20
Case
 -
Outer shield
1
Signal
2Pin 
female 
connector
Color 
(051400100133)
T+
1
Brown
14
T-
2
Blue
15
Signal
D-SUB 9Pin
female 
connector
Color 
(051400100075)
5V
1
Brown
3
Hall A
2
White
11
Hall B
3
Grey
12
Hall C
4
Yellow
13
0V
5
Green
10
Shield
Case
Shield
1
LMACEZ 
LMACEY (No Hall component)
Signal
D-SUB 15Pin
female 
connector
Color 
(051400300069)
D-SUB 20Pin
male 
connector
5V
7
Brown
3
0V
2
White
2
A+
14
Green
4
A-
6
Yellow
5
B+
13
Blue
6
B-
5
Red
7
Z+
12
Violet
8
Z-
4
Gray
9
Encoder Alarm
3
Pink
18
Inner
15
Inner shield
20
Outer
Case
Outer shield
1
Signal
2Pin 
female 
connector
Color 
(051400100133)
T+
1
Brown
14
T-
2
Blue
15
Signal
D-SUB 9Pin
female 
connector
Color
5V
1
Brown
3
Hall A
2
White
11
Hall B
3
Grey
12
Hall C
4
Yellow
13
0V
5
Green
10
Shield
Case
Shield
1
LMACEAV 
LMACEAW (No Hall component)
LMACEJ 
LMACEC (No Hall component)
Signal
Round connector
17Pin 
8-10-0090
Female 
connector
Color 
(051400300069)
SCSI 20Pin  
Male 
connector
Z+
13
Grey
12
Z-
14
Pink
13
Sin1+
2
Green
16
Sin1-
3
Yellow
17
COS1+
9
Blue
18
COS1-
10
Red
19
VREF+
1
Brown
11
VREF-
8
White
3
Inner
12
Inner shield
15
Outer
Metal
housing
Outer shield
1/Case
T+ 
11
White/Green
14
T-
12
Brown/Green
15
+5V
5
Violet
9
0V
6
Black
10 
Function
Signal
Round connector
17Pin 
8-10-0090
Female 
connector
Color 
(051400300069)
SCSI 20Pin  
Male 
connector
Resolver1
(20/115)
Vref+
1
Brown
11
4
White/Yellow
Vref-
7
White
3
8
Yellow/Brown
SIN+
2
Green
16
SIN-
3
Yellow
17
COS+
9
Blue
18
COS-
10
Red
19
Resolver2
(24/114)
SIN+
13
Black
4
SIN-
14
Violet
5
COS+
15
Grey
6
COS-
16
Pink
7
Inner Shield
12
Inner shield
15
Outer Shield
Case
Outer shield
1/Case
Temperature
T+
11
Brown/Green
14
T-
12
White/Green
15 
LMACEAD
LMACEAU
Function
8-10-0090
(Female)
JENA
Signal
Color
(051400300069)
SCSI 20
(Male)
mega-fabs D1
Signal
Power
4
5V
Blue
3
+5Vdc
5
5V
Blue
-
-
6
0V
White
2
Signal Gnd
Incremental signals
2
U2-
Red
19
Cos(-)
3
U1-
Brown
17
Sin(-)
9
U2+
Black
18
Cos(+)
10
U1+
Green
16
Sin(+)
Origin signal
1
U0-
Pink
9
/X
8
U0+
Grey
8
X
6
0V
Inner shield
20
Signal Gnd
Case
Shield
Outer shield
1
Frame Gnd
Temperature
11
T+
Violet
14
[IN5] Motemp
12
T-
Yellow
15
Signal Gnd
Hall sensor
13
Vcc
Blue
3
+5Vdc
14
HallA
Brown/Green
11
HA
15
HallB
White/Yellow
12
HB
16
HallC
White/Green
13
HC
17
GND
White
10
Signal Gnd
LMACEAM 
LMACEAA (No Hall component)

---

MM99TE07-1701
Linear Motor System
108
109
Drives
Signal
Pin
Color
Wire pair
Color
Pin
Signal
Frame Ground
1
Brown
1a
8a
Blue
14
[Out2]
Signal Ground
2
Brown/White
1b
8b
Blue/White
15
[Out3]
Enable [IN1]
3
Red
2a
9a
Light blue
16
Encoder A In/Out
GP Input [IN2]
4
Red/Black
2b
9b
Light blue /Black
17
Encoder /A In/Out
GP Input [IN3]
5
Orange
3a
10a
Purple
18
Encoder B In/Out
GP Input [IN4]
6
Orange/Black
3b
10b
Purple /White
19
Encoder /B In/Out
HS Input [IN6]
7
Green
6a
11a
Grey
20
Encoder X In/Out
HS Input [IN7]
8
Pink
4a
11b
Grey /Black
21
Encoder /X In/Out
HS Input [IN8]
9
Yellow
5a
12a
White/Red
22
+5 Vdc @ 400mA
HS Input [IN9]
10
Pink/Black
4b
12b
White/Blue
23
Siganl Ground
HS Input [IN10]
11
Yellow/Black
5b
13a
White
24
Analog Ref In (+)
GP Input [IN11]
12
Green/Black
6b
13b
White /Black
25
Analog Ref In (-)
[Out1]
13
Light green
7a
7b
Light green/Black
26
[IN12] GP Input
Shield
Case
LMACK30R
NOTE: Wire pair 1a and 1b represent diagonal.
NOTE: If connect wire set "L" to "+", can change wire set "OUT" output contact patterns.
Signal
Pin
Color
Wire set
Vcc
1
Yellow
+
GNb
9
Green
-
Negative limit signal output
3
Grey
1-OUT
* Reference notes
2
White
1-L
Positive limit signal output
5
Pink
2-OUT
* Reference notes
4
Brown
2-L
Origin signal output
7
Red
3-OUT
* Reference notes
6
Blue
3-L
LMACKS
4.5 D1-N related accessories
Name
Speciﬁcation
Connector
Description
USB 2.0A to Mini-B 
Cable (5m)
051700800514
Regenerative resistor
050100700001
Rated power 100W, instant power 500W
D1-N Drive connector 
accessories kit bag
D1-CK
All connectors 
EMC accessories kit bag
D1-N EMC2
Single phase power
D1-N EMC1
Three phase power
Table4-4   Drive peripheral accessories
9

---

MM99TE07-1701
Linear Motor System
110
111
Drives
4.5.1  D1-N related cables
Name
Speciﬁcation
Connector
Description
Control signal
cables
LMACKF
X6
Motor power 
supply cables and 
over-temperature 
signal cables
LMACSU
X3
LMACSV
LMACSM
LMACSN
LMACTD
LMACSZ
LMACTA
LMACTB
Suitable for LMC series linear motors: A, B, C, D, E, EFC LMT series linear 
motors: A, B, C, D
Suitable for LMC series linear motors:F
Suitable for LMT series linear motors:E
Suitable for LMFA series linear motors:
Suitable for LMFA series linear motors:
Suitable for LMFA series linear motors:
Suitable for LMSA motors
Table4-5  Control signals, limit signals, motor power cables
Note
Note
Note
Note
Note
Note
Note
Note
FMK3G
Note
Note
FMK3G
Suitable for LMC series linear motors: LMC-EFE、LMC-EFF
Both ends are scattered lines,suitable for HIWIN D1-N drive series.
Note
Note
Note
Note
Note
Note
Note
Note
LMFA0、LMFA1、 LMFA2、 LMFA31、LMFA31L、LMFA32、LMFA32L、LMFA41、
LMFA41L、LMFA42、LMFA42L、LMFA52、LMFA52L、LMFA62(round metal connector, wire diameter 
1.5mm
2)
LMFA33、LMFA33L、LMFA34、LMFA43 、LMFA43L、LMFA44、LMFA53、LMFA53L 、LMFA54、
LMFA62L 、LMFA63、LMFA64,includes KTY and PTC two sets of over-temperature signals.(round metal 
connector, wire diameter 2.5mm
2)
LMFA34L、LMFA44L、 LMFA54L、 LMFA63L,includes KTY and PTC two sets of over-temperature 
signals.(round metal connector, wire diameter 4.0mm
2)
11
7
Name
Speciﬁcation
Connector
Description
Motor power 
supply cables and 
over-temperature 
signal cables
LMACSC
X3
LMACSR
Suitable for LMFA series linear motors:LMFA64L,includes KTY and PTC two sets 
of over-temperature signals.(round metal connector, wire diameter 6.0mm
2)
Suitable for DD series direct drive motors: TMS、 TMN、 TMY,(not include over-
temperature signal)
Table4-5   Control signals, limit signals, motor power cables
Note
Note
Note
Note

---

MM99TE07-1701
Linear Motor System
112
113
Drives
Drive
Speciﬁcation
Connector
Description
Suitable for linear 
motors
LMACFC
LMACFD
LMACFA
LMACFH
LMACFL
LMACFG
Suitable for direct 
drive motors
LMACFE
LMACFJ
Table4-6   Position feedback cables
X10
X11
X12
For Renishaw digital optical scale,connector is the D-type connector,doesn't 
include Hall sensor signal.
For Renishaw digital optical scale,connector is the D-type connector, include 
Hall sensor signal.
Single Resolver encoder,with motor over-temperature signal,suitable for 
TMN motors.
Dual Resolveruencoder,with motor over-temperature signal,suitable for 
TMY、TMN□□A motors.
For Renishaw analog optical scale,connector is the D-type connector,doesn't 
include Hall sensor signal.
For Renishaw analog optical scale,connector is the D-type connector, include 
Hall sensor signal.
Jena for analog encoder, motor over-temperature signal, suitable for TMS、
TMNE motors.
Jena for analog encoder, motor over-temperature signal, hall sensor 
signals,suitable for TMNEH motors.
Note
Note
Note
Note
Note
Note
Note
Note
T-
T+
Note
Note
Note
Note
Note
Note
8
8      
4.5.2  Pin assignments of D1-N 
Signal
D-SUB 15Pin
female 
connector
Color
(051400300069)
X10HD-SUB 
15Pin
male 
connector
5V
7
Brown
5
8
Brown/Yellow
0V
2
White
15
9
White/Yellow
A+
14
Green
1
A-
6
Yellow
6
B+
13
Blue
2
B-
5
Red
7
Z+
12
Violet
3
Z-
4
Grey
8
Inner Shield
15
Inner shielding
15
Outer
Case
Outer shielding
Case
Signal
9Pin  
female 
connector
Color
(051400100075)
5V
1
Brown
5
Hall A
2
White
9
Hall B
3
Grey
10
Hall C
4
Yellow
11
0V
5
Green
15
Shield
Case
Shield
Case
LMACFD 
LMACFC (No Hall component)
Signal
D-SUB 15Pin
female 
connector
Color
(051400300069)
X11HD-SUB 
15Pin
male 
connector
5V
4
Brown
5
5
Brown/Yellow
0V
12
White
15
13
White/Yellow
Sin(+)
9
Green
1
Sin(-)
1
Yellow
6
Cos(+)
10
Blue
2
Cos(-)
2
Red
7
Z+
3
Violet
3
Z-
11
Grey
8
Inner Shield
15
Inner shielding
15
Outer
Case
Outer shielding
Case
Signal
D-SUB 9Pin
female 
connector
Color 
(051400100075)
5V
1
Brown
5
Hall A
2
White
9
Hall B
3
Grey
10
Hall C
4
Yellow
11
0V
5
Green
15
Shield
Case
Shield
Case
LMACEH 
LMACEA (No Hall component)
Function
JENA
Signal
17Pin female 
connector
Color
(051400300069)
X12 HD-SUB
15Pin female 
connector
Power
5V
4
Blue
5
5V
5
Blue
5
0V
6
White
15
Incremental 
signals
U2-
2
Red
7
U1-
3
Brown
6
U2+
9
Black
2
U1+
10
Green
1
Origin signal
U0-
1
Pink
8
U0+
8
Grey
3
Color
(051400100133)
Line number 
casung
Shield
Case
Inner shield
15
Temperature
T+
11
Purple
Brown
T+
T-
12
Yellow
Blue
T-
Color
(051400300063)
X10 HD-SUB
15Pin male 
connector
Hall sensor
Vcc
13
Blue
Blue
5
HallA
14
Brown/Green
Brown
9
HallB
15
White/Yellow
Yellow
10
HallC
16
White/Green
Green
11
GND
17
White
White
15
LMACFG 
LMACFL (No Hall component)

---

MM99TE07-1701
Linear Motor System
114
115
Signal
Round connector
17Pin 
8-10-0090
Female 
connector
Color 
(051400300108)
X12HD-
SUB 15Pin
female 
connector
5V
5
Brown
5
Brown/Green
0V
6
White
4
White/Green
Sin1+
2
Green
1
Sin1-
3
Yellow
6
COS1+
9
Blue
2
COS1-
10
Red
7
VREF+
1
Gray
11
VREF-
8
Pink
12
Z+
13
Black
13
Color 
(051400300138)
Line number 
casing
Z-
14
Violet
14
T+ 
11
Gray/Pink
Brown
T+
T-
12
Red/Blue
White
T-
Shield
Case
Shield
15
LMACFE
Signal
Round connector
17Pin 
8-10-0090
Female 
connector
Color 
(051400300108)
X12HD-
SUB 15Pin
female 
connector
Sin1+
2
Green
1
Sin1-
3
Yellow
6
COS1+
9
Brown
2
COS1-
10
White
7
Sin2+
13
Blue
3
Sin2-
14
Red
8
COS2+
15
Gray
9
COS2-
16
Pink
10
VREF+
1/4
Black
11
Color 
(051400300138)
Line number 
casing
VREF-
7/8
Violet
12
T+ 
11
Brown/Green
Brown
T+
T-
12
White/Green
White
T-
Shield
Case
Outer shielding
Case
LMACFJ
Signal
Pin
Color
Signal
Pin
Color
CWL
1
White
FG
21
Light blue
CCWL
2
White/Black
GND
22
Light blue/Black
CW+
3
Red
01+
23
Light green
CW-
4
Red/Black
01-
24
Light green /Black
CCW+
5
Yellow
02+
25
White/Red
CCW-
6
Yellow/Black
02-
26
White/Blue
I1
7
Green
03+
27
Red/White
I2
8
Green/Black
03-
28
Red/Blue
I3
9
Blue
PT+
29
Yellow/Red
I4
10
Blue/White
PT-
30
Yellow/Blue
I5
11
Brown
N/A
31
Green/White
I6
12
Brown/White
N/A
32
Light green /Blue
I7
13
Orange
A
33
Gray/Red
I8
14
Orange/Black
/A
34
Gray/Blue
I9
15
Gray
B
35
Pink/Red
I10
16
Gray/Black
/B
36
Pink/Blue
COM
17
Purple
Z
37
Light blue/Red
REF+
18
Pink
/Z
38
Light blue/Blue
REF-
19
Pink/Black
CZ
39
Light green /Red
DSF+
20
Violet/White
DSF-
40
Green/Blue
LMACKF
Appendix A: Motor Sizing
Motion velocity profile
1.   1/3-1/3-1/3 trapezoid profile
If the distance (X) and move time (T) have been 
given, the most common and efficient velocity profile 
for point-to-point motion is the “1/3-1/3-1/3” 
trapezoid curve because it provides the optimal 
move by minimizing the power required to complete 
the move. It breaks the time of the acceleration, 
Strokeing, and deceleration into three segments as 
shown below. 
Herein the parameters are described as motion 
equation. 
2.   1/2-1/2 triangle profile
If X and T are given, another common motion profile is 
the 1/2-1/2 triangle profile. The motion is divided into 
two parts, namely 
acceleration and deceleration. The second motion velo-
city profile is shown as follows.
Start Motor Sizing
The following contents describe how to choose proper 
motor according to speed, moving distance, and Payloading 
inertia. The basic process for sizing a motor is:
	 Decide motion profile and required parameters
	 Calculate peak and continuous force
	 Select motor
Symbols
X   : move distance (mm)
T   : move time (sec)
a   : acceleration (mm/s2)
V   : velocity (mm/s)
ML: Payloading (kg)
g   : gravitation acceleration (mm/s2)
Fp : peak force (N)
Fc : continuous force (N)
Fa : attraction force between stator and forcer (applicable for 
LMS, LMF series) (N)
Fi  : inertia force (N)
Kp : force constant (N/Arms)
Ip   : peak current (Arms)
Ie   : effective current (Arms)
Ic   : continuous current (Arms)
V0 : starting velocity (mm/s)
STEP 1 Decide motion velocity profile and required 
parameters
In order to determine the correct motor for a particular 
application it is necessary to be familiar with the motion 
equation.
Motion equation
Basic kinematics equations are described as follows: 
Where V is velocity, a is acceleration, T is move time and X is  
move distance.
You can choose two of the four parameters (V, a, T and X) as 
your designed parameters, then the last two parameters can 
be calculated by above equations.  

2
0
0
aT
2
1
T
V
X
aT
V
V
+
=
+
=
Vmax
V (m/sec)
T/3
T/3
T/3
 t(sec)

2
max
max
max
T
4.5X
3
T
V
a
)
3
T
2
V
3
T
V
3
T
2
V
X

Because
(   
T
X
1.5
V
=
=
×
+
×
+
×
=
×
=
Vmax
V (m/sec)
T/2
T/2
 t(sec)
2
max
max
T
4X
a
T
X
2
V
=
×
=

---

MM99TE07-1701
Linear Motor System
116
117
The peak current Ip and effective current Ie can be 
calculated by using motor force constant Kf.

STEP 3 Select motor by peak force and verify the 
current supply of motor 
From the HIWIN catalog, you can check the 
specifications of motor and choose an applicable 
motor by peak force, and then you can verify the 
current supply if it is fitted the specification as 
follows.  
Regarding effective and continuous current, the 
ratio of Ie/Ic had better be less than 0.7 to attain 
some margin.
The acceleration required in the first motion velocity profile is  
bigger than that in the second motion velocity profile; there-
fore, the required motor size is bigger. When choosing second 
motion velocity profile, the chosen motor size is smaller, ho-
wever, we need to verify the DC bus of driver is bigger enough, 
due to the higher velocity (Vmax).     
STEP 2 Determine peak force and effective force 
The peak force can be calculated by the follow equation
Where Fi is inertia force while Ff is friction force, and μ is 
friction factor.
In most cases, motions are cyclic point-to-point 
movements. Assuming a cyclic motion shown in the 
following profile with a pause time of t4 second, the 
effective force can be calculated as following formula:
3.   Some useful equations 
Vmax
V (m/sec)
T/2
T/2
 t(sec)
Vmax
V (m/sec)
T/3
T/3
T/3
 t(sec)
Triangle profile
1/3 -1/3-1/3 Trapezoid profile
V
a
t
T
X
1.5 ×

2
T
4.5X

2
T
4X

a
X

a
V
V
X
max
max
Vmax
Vmax
+
>
)
( if
T
X
2 ×
,  or 
a
X
×
c
f
e
e
p
f
p
p
I
K
F
I
I
K
F
I
<
=
<
=
(from specification of chosen motor)
(from specification of chosen motor)
f
e
e
f
p
p
K
F
I
K
F
I
=
=
(
)
f
i
a
L
L
p
F
F
µ
F
g
M
a
M
F
+
=
×
+
×
+
×
=
max
(
)
(
)
4
3
2
1
3
2
2
2
1
2
e
F
t
t
t
t
t
F
F
t
F
t
F
F
f
i
f
f
i
+
+
+
−
+
+
+
=
Vmax
V (m/sec)
t4
t3
t2
t1
 t(sec)
Linear Motor Sizing Example
For example, if Payload is 5 kg (moving mass of mechanism 
is 1 kg and payPayload is 4 kg), friction factor μ is 0.01 
,distance is 500 mm, move time is 400 ms and dwell time is 
350 ms. 
At first, we can calculate the Vmax, amax, Fp and Fe by the 
formulas described above (choose the first motion velocity 
profile and LMC series)
In this case, we can choose motor of type LMCA6 (p.48) which 
can provide up to 187(N )of peak force and continuous force 
62(N), and the force constant is 33.8 N/A(rms). Then the 
current supply of motor can be determined as follows

09  
%
70
%
89
.
68
%
100
8.1
24
.1
)
(8.1
)
(
24
.1
8.
33
92
.
41
)
(4.5
)
(
.2
8.
33
79
.
70
<
=
×
=
<
=
=
=
<
=
=
=
c
e
f
e
p
f
p
p
I
I
Arms
Arms
K
F
I
Arms
Arms
K
F
I
(
)
[
]
(N)
41.92
0.35
0.4
0.1333
0.49)
(70.3
0.49
0.49)
(70.3
F
(N)
70.79
0.49
70.3
0.01
9.81
5
14.06
5
µ
F
g
M
a
M
F
14.06 (m/sec2)
)
(0.4
0.5
4.5
T
X
4.5
a
1.875 (m/sec)
0.4
0.5
1.5
T
X
1.5
V
2
2
2
e
a
L
max
L
p
2
2
max
max
=
+
×
−
+
+
+
=
=
+
=
×
×
+
×
=
×
+
×
+
×
=
=
×
=
×
=
=
×
=
×
=

---

MM99TE07-1701
Linear Motor System
118
119
Appendix B: Sizing a Regen Resistor
1.  Gather required information
To calculate the power and resistance of the regen resistor 
requires information about the amplifier and the motor. 
For all applications, gather the following information:
	 Detail of motion profile, including acceleration and velocity
	 Amplifier model number
	 Applied line voltage to amplifier
	 Toque/force constant of the motor
	 Resistance (line-to-line) of the motor windings
For rotary motor applications, gather additional information
	 Payload inertia seen by the motor
	 Inertia of the motor
For linear motor applications, gather additional information
	 Moving mass
2.  Observe the properties of each deceleration during a com-
plete cycle of operation
For each deceleration during the motion cycle, determine:
	 Speed at the start of the deceleration
	 Speed at the end of the deceleration
	 Time over which the deceleration takes place
3.  Calculate energy returned for each deceleration
The energy returned during each deceleration can be 
calculated by the following formulas.
Rotary motor:
Edec (joules): Energy returned by the deceleration
Jt (kg m2 ): Payload inertia on the motor shaft plus the motor inertia 
       (radians /sec): Shaft speed at the start of deceleration
       (radians /sec): Shaft speed at the end of deceleration
Ie   : effective current (Arms)
Linear motor:
Edec (joules): Energy returned by the deceleration
Mt (kg): Moving mass
V1 (meters /sec): Velocity at the start of deceleration
V2 (meters /sec): Velocity at the end of deceleration
4.  Determine the amount of energy dissipated by the motor
Calculate the amount of energy dissipated by the motor 
due to current flow through the motor winding resistance 
using the following formula.
Ppower (watts): Power dissipated in the motor
Rwinding (ohm): Line to Line resistance of the motor coil
F	: Force need to decelerate the motor
       Nm for rotary applications
       N for linear applications
Kt: Torque constant for the motor
      Nm/Amp for rotary applications
       N/Amp for linear applications
Emotor = Pmotor Tdecel
Emotor (joules): Energy dissipated in the motor
Tdecel (seconds): Time of deceleration
5.	 Determine the amount of energy returned to the 
amplifier
Calculate the amount of energy that will be returned to the 
amplifier for each deceleration using the following formula
Ereturned = Edec-Emotor
Ereturned (joules): Energy returned to the amplifier
Edec (joules): Energy returned by the deceleration
Emotor (joules): Energy dissipated by the motor
6.	 Determine if energy returned exceeds amplifier capacity
Compare the amount of energy returned to the amplifier 
in each deceleration with the amplifier’s absorption 
capacity. The following formula is used to determine the 
energy that can be absorbed by the amplifier.
Wcapacity (joules): The energy that can be absorbed by the bus capacitor
C (farads): Bus capacitance 
Vregen(volts): Voltage at which the regen circuit turns on
Vmains(volts): Mains voltage (AC) applied to the amplifier 
7.	 Calculated energy to be dissipated for each deceleration
For each deceleration where the energy exceeds the 
amplifier’s capacity, using the following formula to 
calculate the energy that must be dissipated by the regen 
resistor.
Eregen = Ereturned _ Eamp
Eregen (joules): Energy that must be dissipated in the regen resistor 
Ereturned (joules): Energy delivered back to the amplifier from the motor
Eamp (joules): Energy that the amplifier will absorb
8.	 Calculate pulse power of each deceleration that exceeds  
amplifier capacity
For each deceleration where energy must be dissipated by 
the regen resistor, use the following formula to calculate 
the pulse power that will be dissipated by the regen 
resistor
Ppulse = Eregen / Tdecel   
Ppulse (watts): Pulse power
Eregen (joules): Energy that must be dissipated in the regen resistor
Tdecel (seconds): Time of deceleration 
9.	 Calculate resistance needed to dissipate the pulse power 
 Using the maximum pulse power from the previous 
calculation, calculate the resistance value of the regen 
resistor required to dissipate the maximum pulse power.
R = V2regen / Ppulse max  
R(ohms):Resistance
Ppulse max:The maximum pulse power
Vregen :The voltage at which the regen circuit turns on 
Choose a standard value of resistance less than the 
calculated value. The value must also be greater than 
the minimum regen resistor value specified by the 
amplifier supplier.
10.  Regen resistor sizing example
Gather required information
LM ROBOTS type:LMXL1L-S37L-1200-G200
Amplifier: mega-fabs D1
   DC bus capacitance: 1880uF
   Regen circuit turn on voltage: 390V
   Minimum resistance:15Ω
Moving mass: 86Kg (include payPayload 74 Kg)
Vmax: 2 m/s
Acceleration, deceleration: 5 m/s2
Power supply (AC) of driver: 220VAC 
Motor type:LMS37L
Force constant (Kf): 68N/A(rms)
Rwinding: 2 ohms(line-to-line)

Calculate regen resistor as following step:

Because the total value of selected resistance must be 
less than 844.77 ohms and the power capacity must be 
more than 180.05 watts, we choose two resistors and 
connect them in series, in each resistor the resistance 
is 68 ohms and power capacity is 100W. The total 
resistance value is 136 ohms and power capacity is 
200W. The resistance order number is 050100700001.
1880
51.98
51.98
72.02
72.02
844 77
180.05

---

MM99TE07-1701
Linear Motor System
120
121
Appendix C:Inquiry form,Mechanical System
Fields marked with asterisk (*) are required.
Date:　　　　　　　 
Customer name：_______________________________ Contact HIWIN：_______________________________
Inquiry No.：___________________________________
Business owners：_____________________________
Email：______________________________________
Tel.：_________________Fax.：_________________
*Industry/Application

___________________
Multi-forcers
□Yes,quantity：____________pcs
□No
*Operational environment
□Indoor, general 25℃ 
□Cleaning room, class：______
□Vacuum , _______
□Others 
Required 
measurement 
protocol
□Straightness(H)_______µm
□Straightness(V)_________µm
□Pitch_________arc-sec
□Yaw_________arc-sec
*Stage type
□Single □Dual axis Bridge 
□Gantry (single-driven) 
□Gantry (dual-driven)
□Others _________
*Cover
□No  □Metal cover  □Bellows
Cable chain
□No   □Horizontal     □Vertical
*Payload
□Mass：___kg
□Dimensions：___ mm
□Offset, X：___ mm,Y：___ mm,
Z：____ mm
*Movement
□Point to point movement    □Scanning
Drive
Firmware
version
□Latest version  
□Specific version：___________
Voltage □110V   □ 220V
□Other,_______ V
External force (N)
X-axis           Y-axis           Z-axis
_____             _____            _____
command
□Pulse 
formet
□STEP/DIR 
□CW/CCW □A/B
*Max. speed(m/s)
X-axis           Y-axis           Z-axis
_____             _____            _____
□Analog voltage command
*Max. acceleration(m/s²) X-axis           Y-axis           Z-axis
_____             _____            _____
□Bus
□mega-ulink
□EtherCAT
□Modbus
*Stroke(mm)
X-axis           Y-axis           Z-axis
_____             _____            _____
Wiring board 
included
□Yes (Please fill out appendix D)   □No
Repeatability(µm)
□Uni-dir.：___   □Bi-dir.：___
Software requirements □Yes (Please fill in the remarks column)   □No
Accuracy(µm)
________________________
Upper controller
□Specify
□Motion board
□Controller
□IPC 
 □PLC  
Encoder type(µm)
□Analog □Digital 
□Absolute：__________
Resolution：__________
□Customer provide
□HIWIN Design
□No 
Position trigger 
function
□Yes    □No
*Stage installation
□Horizon
Axis：______
□Vertical
Axis：_______
Distance
___________mm
Travel time
___________sec
Dwelling time
___________sec
□Hang
Axis：________
□Upside-down
Axis：________
Motion profile
Others
The information below is to be filled out by HIWIN or authorized agents.
Recommended specification:
FME0001-12
Appendix D:Inquiry form,Electric Control System
Fields marked with asterisk (*) are required.
Date:                          　 
*Power system
Input 
Voltage
□110V  □220V(Single phase) 
□220V(Three-phase)
□Other: ______V
□HIWIN design
Optional 
parts
□Socket
Input Voltage: ________V　
Quantity: ________
Connector
type
□H Type(Input current< 15A.) 
□T Type(Input current< 15A.)
□Bare Wire   
□Other: _______
□I/O 
terminal    
Input quantity______:
□NPN  □PNP  □Dry contact 
Output quantity______:
□NPN  □PNP  □Dry Contact
Output current : ________mA
□No
UPS
□Yes___KVA 
□No
*Control panel
□Wiring
Panel
Installation method
□Vertical □Horizontal
□Drawer-Type
Dimension(Unit: inch):
L:_____W:_____H:_____
HIWIN 
document
□Spare parts list(.pdf)　□N/A
Screen
□Touchscreen
Quantity: ______  Size: ______ inches
□Non-touchscreen
Quantity: ______  Size:______ inches
□No
□Electric 
Cabinet
Material type and Surface 
processing:
□Stainless Steel 
□Aluminum
□Coated □Non-Coated
Industrial 
specification
□Required safety approval: __________
Dimension(Unit: inch): 
□8U: L: 26”W: 19”H: 14”
□8U: L: 48”W: 19”H: 14”
□Other:______________
Customer wiring method:
□Customer wiring method 
□HIWIN Standard
Designated 
parts
□List of designated parts(.PDF)(.xls)
□HIWIN Design
□List of designated parts (Customer-
supplied )(.PDF)(.xls)
*Emergency 
stop mode
□Keep Motor power-off 
(Control power retains.)
□Keep Drive disable
(Control power retains.)
□HIWIN design
Alarm
□Stack light  □Buzzer 
□Safety Light Curtains
□Other: ________ □N/A
(Multiple choice are acceptable.)
Special requirements:
FME0001-12

---

MEMO
MEMO

---

MEMO

---

1. HIWIN is the registered trademark of HIWIN Mikrosystem Corp.. Please avoid buying the counterfeit 
goods that are from unknown sources to protect your rights.
2. Actual products may be different from the specifications and photos in this catalog, and the 
differences in appearances or specifications may be caused by, among other things, product 
improvements.
3. HIWIN will not sell or export those techniques and products restricted under the "Foreign Trade 
Act" and relevant regulations. Any export of restricted products should be approved by competent 
authorities in accordance with relevant laws, and shall not be used to manufacture or develop the 
nuclear, biochemical, missile and other military weapons.
Publication Date：May 2002, first edition
Print Date：January 2017, 7th edition 
Linear Motor System Technical Information
Copyright © HIWIN Mikrosystem Corp.

---

©2017 FORM MM99TE07-1701
(PRINTED IN TAIWAN)
Subsidiaries & R&D Centers
HIWIN Schweiz GmbH 
JONA, SWITZERLAND
www.hiwin.ch
info@hiwin.ch
HIWIN FRANCE
ECHAUFFOUR, FRANCE
www.hiwin.fr
info@hiwin.fr
HIWIN Srl
MILAN, ITALY
www.hiwin.it
info@hiwin.it
HIWIN SINGAPORE
SINGAPORE
www.hiwin.sg
info@hiwin.sg
HIWIN KOREA
SUWON, KOREA
www.hiwin.kr
info@hiwin.kr
HIWIN CHINA
SUZHOU, CHINA
www.hiwin.cn
info@hiwin.cn
Mega-Fabs Motion System, Ltd.
HAIFA, ISRAEL
www.mega-fabs.com
info@mega-fabs.com 
HIWIN GmbH
OFFENBURG, GERMANY
www.hiwin.de
www.hiwin.eu
info@hiwin.de
HIWIN JAPAN
KOBE‧TOKYO‧NAGOYA‧KYUSHU‧NAGANO‧ 
HIROSHIMA‧HOKURIKU, JAPAN
www.hiwin.co.jp
info@hiwin.co.jp
HIWIN USA
CHICAGO‧SILICON VALLEY, U.S.A. 
www.hiwin.com
info@hiwin.com
HIWIN s.r.o.
BRNO, CZECH REPUBLIC
www.hiwin.cz
info@hiwin.cz
The specifications in this catalog are subject to change without notification.
HIWIN MIKROSYSTEM CORP.
No.6, Jingke Central Rd., 
Taichung Precision Machinery Park, 
Taichung 40852, Taiwan
Tel: +886-4-23550110
Fax: +886-4-23550123
www.hiwinmikro.tw
business@hiwinmikro.tw