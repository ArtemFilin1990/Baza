Technical guide No. 5
Bearing currents in modern 
AC drive systems
ABB drives

---

2   Bearing currents in modern AC drive systems | Technical guide No. 5

---

Technical guide No. 5 | Bearing currents in modern AC drive systems   3
Technical guide No. 5
Bearing currents in modern AC drive systems
© Copyright 2011 ABB. All rights reserved.
Specifications subject to change without notice. 
3AFE64230247 REV C EN 27.4.2011

---

4   Bearing currents in modern AC drive systems | Technical guide No. 5

---

Technical guide No. 5 | Bearing currents in modern AC drive systems   5
Contents
Chapter 1 - Introduction ............................................................................7
General  .............................................................................................7
Avoiding bearing currents  ..................................................................7
Chapter 2 - Generating bearing currents ...................................................8
High frequency current pulses  ............................................................8
Faster switching  ................................................................................9
How are HF bearing currents generated? .............................................9
Circulating current  ........................................................................9
Shaft grounding current .................................................................9
Capacitive discharge current ........................................................10
Common mode circuit ......................................................................10
Stray capacitances  ..........................................................................11
How does the current flow through the system? ................................12
Voltage drops ...................................................................................13
Common mode transformer ..............................................................14
Capacitive voltage divider .................................................................15
Chapter 3 - Preventing high frequency bearing current damage .............17
Three approaches ............................................................................17
Multicore motor cables .................................................................17
Short impedance path  .................................................................17
High frequency bonding connections  ...........................................18
Follow product specific instructions  ..................................................19
Additional solutions  .....................................................................19
Measuring high frequency bearing currents ........................................19
Leave the measurements to the specialists ........................................20
Chapter 4 - References ............................................................................21
Chapter 5 - Index .....................................................................................22

---

6   Bearing currents in modern AC drive systems | Technical guide No. 5

---

Technical guide No. 5 | Bearing currents in modern AC drive systems   7
Chapter 1 - Introduction
General 
Some new drive installations can have their  bearings fail only 
a few months after startup. Failure can be caused by  high fre-
quency currents, which flow through the  motor bearings.
While  bearing currents have been around since the advent 
of  electric motors, the incidence of damage they cause has 
increased during the last few years. This is because modern 
variable speed drives with their fast rising  voltage pulses and 
 high switching frequencies can cause  current pulses through 
the  bearings whose repeated discharging can gradually erode 
the  bearing races.
Avoiding bearing currents 
To avoid damage occurring, it is essential to provide proper 
 earthing paths and allow  stray currents to return to the  inverter 
frame without passing through the  bearings. The magnitude of 
the currents can be reduced by using  symmetrical motor cables 
or  inverter output filtering. Proper insulation of the  motor bearing 
construction breaks the  bearing current paths.

---

8   Bearing currents in modern AC drive systems | Technical guide No. 5
Chapter 2 - Generating bearing currents
High frequency current pulses 
Bearing currents come in several different guises. However, 
while modern motor design and manufacturing practices have 
nearly eliminated the  low frequency bearing currents induced by 
the asymmetry of the motor, the rapid switching in  modern AC 
drive systems may generate  high frequency (HF) current pulses 
through the  bearings. If the energy of these pulses is sufficiently 
high, metal transfers from the ball and the races to the lubricant. 
This is known as  electrical discharge machining or EDM. The 
effect of a single pulse is insignificant, but a tiny EDM pit is an 
incontinuity that will collect more pulses and expand into a typi-
cal  EDM crater. The switching frequency of modern AC drives is 
very high and the vast number of pulses causes the erosion to 
quickly accumulate. As a result, the  bearing may need replacing 
after only a short time in service.
High frequency bearing currents have been investigated by 
ABB since 1987. The importance of system design has been 
highlighted in the last few years. Each individual item involved, 
such as the motor, the  gearbox or the  drive controller, is the 
product of sophisticated manufacturing techniques and normally 
carries a favourable mean time between failure (MTBF) rate. It is 
when these components are combined and the installed system 
is looked upon as a whole, that it becomes clear that certain 
installation practices are required.
Figure 1: Bearing currents can cause “ bearing fluting”, a rhythmic 
pattern on the bearing’s  races.

---

Technical guide No. 5 | Bearing currents in modern AC drive systems   9
Faster switching 
Current  AC drive technology, incorporating insulated gate bipo-
lar transistors (IGBT), creates switching events 20 times faster 
than those considered typical ten years ago. Recent years have 
seen a rising number of  EDM-type bearing failures in  AC drive 
systems relatively soon after startup, within one to six months. 
The extent to which this occurs depends on the  AC drive system 
architecture and the installation techniques used.
 How are HF bearing currents generated?
The source of  bearing currents is the voltage that is induced 
over the  bearing. In the case of high frequency  bearing currents, 
this voltage can be generated in three different ways. The most 
important factors that define which mechanism is prominent, are 
the size of the motor and how the  motor frame and shaft are 
grounded. The electrical installation, meaning a suitable cable 
type and proper bonding of the protective conductors and the 
 electrical shield, plays an important role. Du/dt of the AC drive 
power stage components and the DC-link voltage level affect 
the level of bearing currents.
Circulating current 
In large  motors,  high frequency voltage is induced between the 
ends of the  motor shaft by the  high frequency flux circulating 
around the stator. This flux is caused by a net asymmetry of 
capacitive current leaking from the  winding into the  stator frame 
along the stator circumference. The voltage between the shaft 
ends affects the bearings. If it is high enough to overcome the 
impedance of the bearings’  oil film, a current that tries to com-
pensate the net flux in the  stator starts to flow in the loop formed 
by the shaft, the bearings and the  stator frame. This current is a 
circulating type of high frequency bearing current. 
Shaft grounding current 
The current leaking into the  stator frame needs to flow back to 
the  inverter, which is the source of this current. Any route back 
contains impedance, and therefore the voltage of the  motor 
frame increases in comparison to the source ground level. If the 
 motor shaft is earthed via the  driven machinery, the increase of 
the  motor frame voltage is seen over the bearings. If the voltage 
rises high enough to overcome the impedance of the drive-end 
bearing oil film, part of the current may flow via the drive-end 
bearing, the shaft and the driven machine back to the  inverter. 
This current is a shaft grounding type of high frequency bearing 
current. 
Generating bearing currents

---

10   Bearing currents in modern AC drive systems | Technical guide No. 5
Capacitive discharge current

In small  motors, the internal voltage division of the common 
mode voltage over the  internal  stray capacitances of the motor 
may cause  shaft voltages high enough to create high frequency 
bearing current pulses. This can happen if the  shaft is not earthed 
via the  driven machinery while the  motor frame is earthed in the 
standard way for protection. 
Common mode circuit
High frequency bearing currents are a consequence of the cur-
rent flow in the common mode circuit of the AC drive system.
A typical  three-phase sinusoidal power supply is balanced and 
symmetrical under normal conditions. That is, the vector sum of 
the three phases always equals zero. Thus, it is normal that the 
neutral is at zero volts. However, this is not the case with a  PWM 
switched three-phase power supply, where a dc voltage is con-
verted into three phase voltages. Even though the fundamental 
frequency components of the output voltages are sy mmetrical 
and balanced, it is impossible to make the sum of three output 
voltages instantaneously equal to zero with two possible output 
levels available. The resulting neutral point voltage is not zero. 
This voltage may be defined as a  common mode voltage source. 
It is measurable at the zero point of any load, eg. the star point 
of the motor  winding. 
Figure 2: This schematic shows the phase voltages of a typical  three 
phase PWM power supply and the average of the three, or  neutral point 
voltage, in a modern  AC drive system. The neutral voltage is clearly 
not zero and its presence can be defined as a  common mode voltage 
source. The voltage is proportional to the  DC bus voltage, and has a 
frequency equal to the  inverter switching frequency.
Generating bearing currents

---

Technical guide No. 5 | Bearing currents in modern AC drive systems   11
Figure 3: An example of the  common mode current at the  inverter output. 
The pulse is a superposition of several frequencies due to the different 
natural frequencies of the parallel routes of  common mode current.
Stray capacitances 
A capacitance is created any time two conductive components 
are separated by an insulator. For instance, the cable phase wire 
has capacitance to the PE-wire separated by PVC insulation, 
for example, and the motor  winding turn is insulated from the 
frame by enamel coating and slot insulation, and so has a value 
of capacitance to the  motor frame. The capacitances within a 
cable and especially inside the motor are very small. A small 
capacitance means high impedance for low frequencies, thus 
blocking the low frequency stray currents. However, fast rising 
pulses produced by modern power supplies contain frequencies 
so high that even small capacitances inside the motor provide a 
low impedance path for current to flow.
Any time one of the three  inverter outputs is changed from one 
of the possible potentials to another, a current proportional 
to this voltage change is forced to flow to earth via the earth 
capacitances of all the components of the output circuit. The 
current flows back to the source via the earth conductor and 
 stray capacitances of the  inverter, which are external to the 
three phase system. This type of current, which flows through 
the system in a loop that is closed externally to the system, is 
called  common mode current. 
Generating bearing currents

---

12   Bearing currents in modern AC drive systems | Technical guide No. 5
Figure 4: Simplified loop of the  common mode current of  a PWM  inverter 
and induction motor. The  inverter power supply acts as a  common mode 
voltage source (Vcm). Common mode current (CMC) flows through the 
 common mode cable and motor inductances, Lc Lm and through the  stray 
capacitances between the  motor  windings and  motor frame, combined 
to be Cm. From the  motor frame, the current proceeds through the 
factory earth circuit which has the inductance Lg. Lg is also fed  common 
mode current from the stray  cable capacitance Cc. The  inverter frame is 
connected to the factory earth and couples the  common mode current/
earth currents through stray  inverter to frame capacitances, combined 
as Cin, back to the  common mode voltage source.
How does the current flow through the system?

The return path of the leakage current from the  motor frame 
back to the  inverter frame consists of the  motor frame, cable 
shielding or PE-conductors and possibly steel or aluminium 
parts of the factory building structure. All these elements contain 
inductance. The flow of  common mode current through such 
inductance will cause a  voltage drop that raises the  motor frame 
potential above the source ground potential at the  inverter frame. 
This  motor frame voltage is a portion of the  inverter’s  common 
mode voltage. The  common mode current will seek the path of 
least impedance. If a high amount of impedance is present in 
the intended paths, like the PE-connection of the  motor frame, 
the  motor frame voltage will cause some of the  common mode 
current to be diverted into an unintended path, through the 
building. In practical installations a number of parallel paths 
exist. Most have a minor effect on the value of  common mode 
current or bearing currents, but may be significant in coping with 
EMC-requirements. 
Generating bearing currents

---

Technical guide No. 5 | Bearing currents in modern AC drive systems   13
Voltage drops

If the value of this inductance is high enough, the reactance at 
the upper range of typical  common mode current frequencies, 
50 kHz to 1 MHz, can support  voltage drops of over 100 volts 
between the  motor frame and the  inverter frame. If, in such a 
case, the  motor shaft is connected through a  metallic coupling 
to a  gearbox or other  driven  machinery that is solidly earthed 
and near the same earth potential as the  inverter frame, then it 
is possible, that part of the  inverter  common mode current flows 
via the motor bearings, the shaft and the driven machinery back 
to the  inverter.
Figure 5: A schematic presentation showing the circulating current 
and shaft grounding current, the latter resulting from high  motor frame 
voltage with superior  machine earthing.
If the shaft of the machinery has no direct contact to the ground 
level, current may flow via the gearbox or machine bearings. 
These bearings may be damaged before the motor bearings.
Figure 6: Source of circulating high frequency bearing current. Current 
leakage through distributed stator capacitances gives a non-zero current 
sum over the stator circumference. This leads to a net magnetising 
effect and flux around the  motor shaft. 
Generating bearing currents

---

14   Bearing currents in modern AC drive systems | Technical guide No. 5
Common mode transformer

The largest share of the motor’s  stray capacitance, is formed 
between the  stator  windings and the  motor frame. This capaci-
tance is distributed around the circumference and length of the 
 stator. As the current leaks into the stator along the coil, the 
high frequency content of the current entering the stator coil is 
greater than the current leaving.
This net current produces a high frequency  magnetic flux that 
will circulate in the  stator laminations, inducing an  axial voltage 
in the  shaft ends. If the voltage becomes large enough, a  high 
frequency circulating current can flow, internal to the motor, 
through the  shaft and both  bearings. The motor can, in this case, 
be thought of as a  transformer, where the  common mode current 
flowing in the  stator frame acts as a primary and induces the 
circulating current into the  rotor circuit or  secondary. This  bear-
ing current is considered to be the most damaging with typical 
peak values of 3 to 20 amps depending on the rated power of 
the motor, du/dt of the AC drive power stage components and 
DC-link voltage level. 
Figure 7: The high frequency  axial shaft voltage can be thought of as 
the resultant of a  transformer effect, in which the  common mode current 
flowing in the  stator frame acts as a  primary, and induces the  circulating 
current into the  rotor circuit or  secondary.
Another version of circulating bearing current occurs when, the 
current, instead of circulating completely inside the motor, flows 
via the  shaft and the bearings of the  gearbox or  driven machinery 
and in a structural element that is both external and common to 
the motor and the driven machine. The origin of the current is the 
same as in the current circulating inside the motor. An example of 
this “vagabond” circulating bearing current is shown in figure 8.
Generating bearing currents

---

Technical guide No. 5 | Bearing currents in modern AC drive systems   15
Generating bearing currents
Figure 8: “Vagabond” circulating bearing current, where the current loop 
is external to the motor.  
Capacitive voltage divider

Other  stray capacitances are also present in the motor, such as 
the capacitance between the  stator  windings and the  rotor, or 
that existing in the motor’s airgap between the  stator iron and the 
 rotor. The  bearings themselves may even have  stray capacitance. 
The existence of capacitance between the  stator  windings and 
the  rotor effectively couples the stator  windings to the  rotor 
iron, which is also connected to the  shaft and the bearing’s in-
ner races. Fast changes in the  common mode current from the 
 inverter can not only result in currents in the capacitance around 
the circumference and length of the motor, but also between the 
 stator  windings and the  rotor into the  bearings. 
Figure 9:  Common mode loop of  variable speed drive, showing  stator, 
 rotor and  bearing  stray capacitances.
The current flow into the  bearings can change rapidly, as this 
depends on the physical state of the  bearing at any one time. For 
instance, the presence of  stray capacitance in the  bearings is only 
sustained for as long as the  balls of the  bearings are covered in 
oil or grease and are non-conducting. This capacitance, where 

---

16   Bearing currents in modern AC drive systems | Technical guide No. 5
the  induced shaft voltage builds up, can be short-circuited if the 
 bearing voltage exceeds the threshold of its breakover value or 
if a “high spot” on a ball breaks through the oil film and makes 
contact with both  bearing  races. At very low speed, the  bearings 
have metallic contact since the  balls have not risen on an oil film.
Generally, the bearing impedance governs the voltage level at 
which the bearings start to conduct. This impedance is a non-
linear function of bearing load, temperature, speed of rotation 
and lubricant used, and the impedance varies from case to case.
Generating bearing currents

---

Technical guide No. 5 | Bearing currents in modern AC drive systems   17
Chapter 3 - Preventing high frequency 
bearing current damage
Three approaches

There are three approaches used to affect high frequency  bear-
ing currents: a proper cabling and earthing system; breaking the 
 bearing current loops; and damping the high frequency  common 
mode current. All these aim to decrease the bearing voltage to 
values that do not induce high frequency bearing current pulses 
at all, or damp the value of the pulses to a level that has no ef-
fect on bearing life. For different types of high frequency  bearing 
currents, different measures need to be taken. 
The basis of all  high frequency current mastering is the proper 
earthing system. Standard equipment earthing practices are 
mainly designed to provide a sufficiently low impedance connec-
tion to protect people and equipment against system frequency 
faults. A  variable speed drive can be effectively earthed at the 
high  common mode current frequencies, if the installation fol-
lows three practices: 
Multicore motor cables

Use only  symmetrical multicore motor cables. The earth (pro-
tective earth, PE) connector arrangement in the motor cable 
must be symmetrical to avoid  bearing currents at fundamental 
frequency. The symmetricity of the PE-conductor is achieved 
by a conductor surrounding all the phase leads or a  cable that 
contains a symmetrical arrangement of three phase leads and 
three earth conductors.
Figure 10: Recommended  motor cable with symmetrical core 
configuration.
Short impedance path 
Define a short, low impedance path for  common mode current 
to return to the  inverter. The best and easiest way to do this is to 
use  shielded motor cables. The  shield must be continuous and 
of good conducting material, ie, copper or aluminium and the 
connections at both ends need to be made with  360° termination.

---

18   Bearing currents in modern AC drive systems | Technical guide No. 5

Preventing high frequency bearing current damage
Figures 11a and 11b show  360° terminations for European and 
American cabling practices.
Figure 11 a: Proper  360° termination with European cabling practice. 
The shield is connected with as short a pigtail as possible to the PE 
terminal. To make a 360° high frequency connection between the EMC 
sleeve and the  cable shield, the outer insulation of the cable is stripped 
away.
Figure 11 b: Proper  360° termination with American cabling practice. 
An earthing bushing should be used on both ends of the  motor cable to 
effectively connect the earth wires to the  armour or  conduit.
High frequency bonding connections 
Add high frequency  bonding connections between the installa-
tion and known earth reference points to equalise the potential 
of affected items, using  braided straps of copper 50 - 100 mm 
wide;  flat conductors will provide a lower inductance path than 
round wires. This must be made at the points where discontinu-
ity between the earth level of the  inverter and that of the mo-
tor is suspected. Additionally it may be necessary to equalise 
the potential between the  frames of the motor and the driven 
 machinery to short the current path through the motor and the 
 driven machine bearings.

---

Technical guide No. 5 | Bearing currents in modern AC drive systems   19
Figure 12: HF bonding strap
Follow product specific instructions 
Although the basic principles of installations are the same, for 
different products suitable installation practices may differ. There-
fore, it is essential to carefully follow the installation instructions 
given in product specific manuals.
Additional solutions 
Breaking the  bearing current loops is achieved by insulating the 
bearing construction. The high frequency  common mode current 
can be damped by using  dedicated filters. As a manufacturer of 
both inverters and  motors,  ABB can offer the most appropriate 
solution in each case as well as detailed instructions on proper 
earthing and cabling practices.
Measuring high frequency bearing currents

Monitoring the bearing condition must be conducted with es-
tablished vibration measurements.
It is impossible to measure  bearing currents directly from a 
standard motor. But if high frequency bearing currents are 
suspected,  field measurements can be taken to verify the exist-
ence of suspected current loops. Measuring equipment needs 
to have wide bandwidth (minimum 10 kHz to 2 MHz) capable of 
detecting peak values of at least 150 to 200 A and RMS values 
at least down to 10 mA. The  crest factor of measured signals 
is seldom less than 20. The current may flow in unusual places, 
such as rotating shafts. Thus, special equipment and experienced 
personnel are needed. 
 ABB uses a specially designed, flexible, air-cored,  Rogowski-
type current sensor with dedicated accessories and has vast 
experience of over one thousand measured drives in different 
applications worldwide. 
Preventing high frequency bearing current damage

---

20   Bearing currents in modern AC drive systems | Technical guide No. 5
The most important measurement points are within the motor. 
During measurements, the motor speed needs to be at least 
10% of the nominal for the bearings to rise on the  oil film. As an 
example, basic measurements are shown in figure 13. Figure 14 
shows examples of measured current waveforms.  GTO (gate 
turn-off thyristor) inverters were used mainly in the 1980s and 
 IGBT inverters are used today. Note the different scale in the 
various graphs.
Figure 13: Basic measurements: A) circulating current measured with a 
jumper, B) shaft grounding current.
A) Circulating current
 GTO-inverter, 5 μs/div, 2 A/div 
IGBT-inverter, 5 μs/div, 2 A/div
B) Shaft grounding current
 GTO-inverter, 2 μs/div, 10 A/div 
IGBT-inverter, 5 μs/div, 500 mA/div
Figure 14: Examples of current waveforms at the measuring points 
shown in Figure 13.
Leave the measurements to the specialists
Since suitable commercial measurement equipment is not 
available on the market and specialised experience is needed 
to make the measurements and interpret the results, it is advis-
able that  bearing current measurements are made by dedicated 
personnel only.
Preventing high frequency bearing current damage

---

Technical guide No. 5 | Bearing currents in modern AC drive systems   21
Chapter 4 - References
1. Grounding and Cabling of the Drive System,

ABB Industry Oy, 3AFY 61201998 R0125
2. A New Reason for Bearing Current Damage in Variable  
Speed AC Drives 

by J. Ollila, T. Hammar, J. Iisakkala, H. Tuusa. EPE 97, 7th  
European Conference on Power Electronics and Applica-
tions, 8-10 September 1997. Trondheim, Norway.
3. On the Bearing Currents in Medium Power Variable 
Speed AC Drives 

by J. Ollila, T. Hammar, J. Iisakkala, H. Tuusa. proceedings 
of the IEEE IEDMC in Milwaukee, May 1997.
4. Minimizing Electrical Bearing Currents in Adjustable 
Speed Drive Systems 

by Patrick Link. IEEE IAS Pulp & Paper

Conference Portland, ME, USA. June 1998.
5. Instruction on Measuring Bearing Currents with a 
Rogowski Coil, ABB Industry Oy, 3BFA 61363602.EN.
6. Laakerivirta ja sen minimoiminen säädettyjen vaihto-
virtakäyttöjen moottoreissa,

I. Erkkilä, Automaatio 1999, 16.9.1999, Helsinki, Finland.  
(In Finnish).
7. High Frequency Bearing Currents in Low Voltage  

Asynchronous Motors,

ABB Motors Oy and ABB Industry Oy, 00018323.doc.
8. Bearing Currents in AC Drives

by ABB Industry Oy and ABB Motors Oy. Set of overheads  
in LN database “Document Directory Intranet” on  ABB_
FI01_SPK08/FI01/ABB
9. The Motor Guide

GB 98-12.
See also product specific installation manuals.

---

22   Bearing currents in modern AC drive systems | Technical guide No. 5
Chapter 5 - Index
Symbols
360° termination  17, 18
360° terminations  18
A
ABB  19
AC drive  9, 10
armour  18
axial shaft voltage  14, 15
axial voltage  14
B
balls  15, 16
bearing  8, 9, 15, 16
bearing current  9, 14, 20
bearing current loops  17, 19
bearing current paths  7
bearing currents  7, 9, 17, 19
bearing fluting  8
bearing races  7
bearings  7, 8, 14, 15, 16
bearing voltage  16
bonding connections  18
braided straps  18
C
cable  17
cable capacitance  12
cable shield  18
circulating current  14
common mode cable  12
common mode current  11, 12, 13, 
14, 15, 17, 19
common mode loop  15
common mode voltage  10, 12
conduit  18
crest factor  19
current pulses  7
D
DC bus voltage  10
dedicated filters  19
drive controller  8
driven machine  9, 18
driven machinery  10, 13, 14
E
earthing paths  7
EDM  9
EDM crater  8
electrical discharge machining  8
electrical shield  9
electric motors  7
F
field measurements  19
flat conductors  18
frame  18
G
gearbox  8, 13, 14
GTO (gate turn-off thyristor) invert-
ers  20
H
high frequency bearing currents  9
high frequency bearing voltage  9
high frequency circulating current  
14
high frequency current mastering  
17
high frequency current pulses  8
high frequency flux  9
high switching frequencies  7
I
IGBT inverters  20
induced shaft voltage  16
insulated gate bipolar transistors 
(IGBT)  9
internal voltage division  10
inverter  9, 11, 12, 13, 15, 17, 18
inverter frame  7, 13
inverter output filtering  7
inverter power supply  12
inverter switching frequency  10
L
low frequency bearing currents  8
M
machine  13
machinery  13, 18
magnetic flux  14
mean time between failure (MTBF)  
8
metallic coupling  13
modern drive systems  8
motor  8, 11, 12, 14, 15, 17, 18, 
19
motor bearing  7
motor cable  17, 18
motor frame  9, 10, 11, 12, 13, 14
motors  9, 10, 19
motor shaft  9, 13
motor windings  12

---

Technical guide No. 5 | Bearing currents in modern AC drive systems   23
N
neutral point voltage  10
O
oil film  9, 20
P
primary  14
PWM  10, 12
R
races  8, 16
Rogowski-type current sensor  19
rotor  14, 15
rotor circuit  14
S
secondary  14
shaft  10, 14, 15
shaft ends  14
shaft voltages  10
shield  17
stator  9, 14, 15
stator frame  9, 13, 14
stator laminations  14
stator windings  14, 15
stray capacitance  10, 11, 12, 14, 15
stray currents  7
symmetrical motor cables  7
symmetrical multicore motor cables  
17
T
three-phase sinusoidal power supply  
10
three phase power supply  10
transformer  14
V
variable speed drive  15, 17
voltage drop  12, 13
voltage pulses  7
W
winding  9, 10, 11, 12, 14, 15
Index

---

© Copyright 2011 ABB. All rights reserved. 
Specifications subject to change without notice.
For more information contact 
your local ABB representative or visit:
www.abb.com/drives
www.abb.com/drivespartners
3AFE64230247 REV C EN 27.4.2011 #15648
Contact us