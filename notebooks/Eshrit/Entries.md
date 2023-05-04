# Date: January 29

Our group finalised the project idea over the week and we began to work on the project proposal. The main agenda was to come up with a comprehensive block diagram.
We identified three main subsystems: RFID, Breathalyzer, and Data management. We shared multiple ideas to discuss feasibility, and evaluate pros and cons.
We all brought our different ideas, potential pairs of problems an solutions to the table and collaborated effectively to ensure each subsystem complemented the others and functioned well in the overall system. We made sure everyone understood their responsibilities and their duties towards each other. By the end we had a skeleton and a somewhat finished block diagram. Provided below is an image for our vision for the project.

<img width="1064" alt="Screen Shot 2023-05-03 at 10 25 14 PM" src="https://user-images.githubusercontent.com/117782788/236106130-9be7c6e8-d973-484e-ac13-b29f6471edc6.png">



# Date: February 1

We delved further into the problem and tried to identify more issues and ideas on how to tackle those issues. Essentially we thought more about expanding on the implementation of our subsystems and laid out an initial gameplan including the parts we would need and how the product we are delivering would actually be used in practice. We discussed the project idea on a more user friendly level. The project would include RFID-enabled wristbands/cards, a breathalyzer, a Raspberry Pi, and a microcontroller to measure the blood alcohol content (BAC) levels of users and encourage more responsible drinking.
Essentially TipsyTracker would remind users to get their BAC levels checked so they can be in control of their senses on a real scale analysis. The system would alert the host if a guest's BAC levels are above a certain threshold.
I carried forth discussions about the real time use cases and issues about device liquid safety and anticipating the problems for the device in real time such as what would we have the device do in case of system failure, and what would could cause our project to either malfunction or provide mismanaged data. Privacy is also a concern that we would have to tackle since we would be handling so much data about BAC levels.


# Date: February 3

We finalised the proposal and made small edits to it in accordance with the formatting of previous semesters. I assisted with finishing up the block diagram and making the high level requirements be more suitable to the overall success of our project instead of depending on the subsystem workings. We made plans of getting final inputs from the TA and making a submission for the project proposal a day before the deadline.

# Date: February 6th

I picked up the the RFID component and soldered it so that for our team meeting the following day, we can breadboard all components together and test them to see if they work before we proceed with the manafacturing process. Below is a picture of the component we used.

<img width="444" alt="Screen Shot 2023-05-03 at 10 26 50 PM" src="https://user-images.githubusercontent.com/117782788/236106309-d5788bac-68cf-49da-8b0f-7b1c4940f378.png">



# Date: February 7

We had made plans to breadboard the ordered components and were able to successfully breadboard the complete system design. This step was imperative to test the functionality of the various subsystems and identify any potential issues that needed to be resolved before proceeding with the manufacturing process. Akash made the decision to take the lead on making the PCB schematics with the incorporated parts.

Additionally, breadboarding the entire system helped the team to verify that all the components were correctly interconnected and that the system was working according to the expected standards. By utilizing the expertise of each team member, any problems encountered during testing were effectively addressed to ensure that the system operated as intended.

# Date: February 20

We decided to work on the design document and laid out a plan on how we would use the proposal as a basis and expand on the requirements and verification of the subsystems. In the course of the discussion, we carefully reviewed the current system design, identified areas that required clarification or more development, and discussed the implementation plan. Moreover, we identified potential issues that could arise during the manufacturing process. This comprehensive review allowed us to identify areas for improvement and confirm that the system design was well-documented and comprehended by all team members. This served as a valuable checkpoint regarding lower level understanding of the project. Akash also went over the updates of the PCB schematic. Sumedh, Akash and I at the end of the meeting came up with a more comprehensive division of labor which would be laid out in the schedule subsection of the design document.


# Date: February 21

Hashed out the final editings of the design document, I planned out the schedule and wrote it in the format that was suitable for submission along the lines with what my teammates and I went over in the previous meeting. Followed the plan of expanding the requirements and verification of the subsystems and finished that while concluding the brainstorming from the previous meeting on what verifications would conduct thorough checks for the workings of our subsystems. Prepared the design document for final submission and decided to submit it a day before the deadline.

# Date: February 27

Conducted a successful design review presentation where my teammates and I went over our design document with the Professors and some TAs. We got valuable feedback about a possible problem where our device could be provided with fake BAC values for a user when the air that they blow into the breathalyzer is not generated with enough pressure so that it comes from the lungs. To tackle this the Professor suggested the addition of a pressure sensor and we decided to go over the feasibility of this addition with the TA.

# Date: March 1

I picked up the the pressure sensor component and soldered it so that for our next team meeting, we can breadboard it and test to see if it works as expected before we proceed with the manafacturing process. Below is a picture of the pressure sensor we would be expermenting with.

<img width="495" alt="Screen Shot 2023-05-03 at 10 31 08 PM" src="https://user-images.githubusercontent.com/117782788/236106861-41236938-19de-4897-b9a6-d7d6e8734c9f.png">


# Date: March 6

Went over the setup of the website where users can register their information and how their BAC contents get updated with the latest measurements. Went over the functionality of the user getting a notification to test, testing within intervals setup by us and a  text broadcast in case of a subsystem failure which would indicate that the device is not working currently. This helped us discuss more ideas and features in case of subsystem failures. We also discussed the plan for soldering given the PCB. 


# Date: March 7

Headed over to the ECE lab to try and solder the first PCB since we needed to discuss the feasibility of soldering given some of the components were too small (0402 resistors, the diodes and capacitors). The soldering irons in the general area had tips that were too wide but in the special area with the finer soldering tips and the hot air I was able to solder the smaller components much more easily although it was still difficult. We then discussed problems even if I was able to get the components on. We could foresee some bridging issues due to the PCB having components that were too close and the components not having enough solder. We then moved to a newer PCB design which would incorporate through hole components. Below is are the images of the PCB and the PCB with some components soldered.

<img width="398" alt="PCB_1" src="https://user-images.githubusercontent.com/117782788/236100725-d1af80fe-4401-4d51-9d6e-44707d15eaa0.png">

<img width="398" alt="PCB_1_sol" src="https://user-images.githubusercontent.com/117782788/236102471-0a3ba6e1-1db4-4faa-8fe8-80c9480733c7.png">

# Date: March 14

We held a discussion with our TA and went over the feasibility of including the earlier discussed pressure sensor into our project. This was an idea we came back to as mentioned earlier so that the breath tests actually detect air from the lungs for BAC level checks rather than a user who can essentially cheat the breath test. We also briefly went over the design document and any other issues surrounding tipsy tracker and or how we can improve tipsy tracker. This is actually what brought back up the incorporation of a pressure sensor. The TA was for the inclusion of the pressure sensor and after the meeting Akash, Sumedh and I began our research regarding the pressure sensor that I had soldered earlier and how it would fit in with the other subsystems. 


# Date: March 20

Today we conducted the first of the two events that we planned to help with getting accurate BAC level measurements from the Tipsy Tracker device. We invited ten of our friends and made sure that they understood the purpose of the event. Our main objective was to gather accurate and consistent data while creating a relaxed and enjoyable atmosphere for our guests. To achieve this, we offered various snacks and beverages, games and activities to keep the participants engaged. Throughout the gathering, we emphasized the significance of the data collection process for the success of our project, stressing the role each person played in it.
During the event, our guests consumed alcohol and blew into our Arduino-based sensor and commercial breathalyzer at regular intervals. We carefully documented the readings from both devices, along with any contextual factors that could have influenced the results, such as the type and quantity of alcohol consumed and the duration between drinks. This enabled us to obtain valuable data to refine our device and algorithms and gain insights into the real-world conditions under which our device would be used. Below is the truncated image of our training data.

<img width="370" alt="Screen Shot 2023-05-03 at 11 26 53 PM" src="https://user-images.githubusercontent.com/117782788/236112506-f5228d32-da9f-4bd2-a49b-977b60e9acc2.png">

# Date: March 21

Today was when we revisited the idea of incorporating the pressure sensor in our project. To start our discussion, we conducted an extensive literature review on pressure sensors and their practical applications. This process helped us comprehend the underlying principles and technologies that govern the functioning of these sensors, which in turn, gave us the confidence to tackle potential issues that may arise.
In a meeting, we discussed several ideas, such as placing a cloth in front of the breathalyzer, creating an enclosure to detect differences in pressure, and covering the pressure sensor with paper to observe changes. We debated the pros and cons of each idea and took into account factors such as cost, implementation ease, and potential impact on the overall device performance.
However each method was not feasible to warrant inclusion of a pressure sensor

Reasons of failure:
1) Cloth failure: Provided inconsistent results which made differentiating changes in blowing pressure.
2) Enclosure to differentiate measurement of pressure: Sensor was not sensitive enough
3) Place a paper over the pressure sensor: Paper was not stable enough during a blow into the breathalyzer.

As a result we decided to move forward with the project without the inclusion of a pressure sensor.


# Date: March 22

Today we conducted the second of the two events that we plannedto help with getting accurate BAC level measurements from the Tipsy Tracker device. We would now be assessing the precision and accuracy of our calibrated system by comparing BAC level approximations with the BAC level readings from the commercial breathalyzer.
We again invited ten of our friends and conducted a series of tests during which each participant tested their BAC levels using Tipsy Tracker's breathalyzer and the commercial breathalyzer throughout the course of the event. Using this data we compounded it with the data gathered from the first event and looked for any obvious patterns or some sort of linear relationship between the two sensors and the two events. We then tried to figure out how we can map the arduino values to the model values keeping into account what the True BAC levels observed from the commerical breathalyzer showed. Below is the truncated image of our model data and how dissimilar it is from the true data.


<img width="363" alt="Screen Shot 2023-05-04 at 11 56 21 AM" src="https://user-images.githubusercontent.com/117782788/236273246-7b6c2e88-cce2-401b-a485-8271d9adb094.png">

# Date: March 23

Our team held a meeting and I picked up the newer version of the PCB which incorporated more spread out components and converted the surface mount components to through hole components. We also separated the components into different bags taking into account the values of resistors and capacitors to make the task of looking for components easier whilst soldering the PCB. I also printed out the schematic on paper so that while soldering I could cross-check this labeling. Below is an image of the physical board
<img width="434" alt="Screen Shot 2023-05-04 at 12 09 13 PM" src="https://user-images.githubusercontent.com/117782788/236276420-877dacf7-49ab-4948-b2b9-37e10be906b7.png">

# Date: March 24

Today we headed to the lab to knock off the soldering off some components. We were able to get the microcontroller soldered using the low temp solder and hot air. Once the microcontroller stabilized we added some more soldered using the fine tip soldering iron on each connection and it was verified by a TA as correct. 


<img width="307" alt="Screen Shot 2023-05-04 at 12 25 24 PM" src="https://user-images.githubusercontent.com/117782788/236281801-b2cb924a-3e07-4f28-a6a5-39db5c31fada.png">

# Date: March 25

We soldered 90% of the board adding the other components to the PCB and the sensors. Some surface mount components and a couple other components remained to be soldered. The USB to UART component used to program the microcontroller was almost impossible to solder. The replacement component could not be incorporated into our schematic. 

<img width="449" alt="Screen Shot 2023-05-04 at 12 28 10 PM" src="https://user-images.githubusercontent.com/117782788/236282395-e68930b3-49a5-43ae-9718-8331c41e3c16.png">

# Date: March 28

We held a brief team discussion about the feasibility of soldering and just the project in general with our TA Dushyant. During our meeting, we shared valuable tips and tricks, and brainstormed potential solutions to enhance our soldering process. Some of the suggestions included investing in high-quality soldering equipment like a soldering station with temperature control and a hot air rework station for surface-mount components. We also considered attending workshops or classes to further develop our soldering skills.


# Date: April 4th

At our recent team meeting, we collectively decided that creating an alternate PCB utilizing the development board would be an important step. This would provide us with a reliable backup plan in case any unexpected issues arise with our primary breathalyzer system, thereby ensuring the overall success and dependability of our project. This decision was made to minimize any risks associated with potential problems in our main breathalyzer system. Below is the image for the layout of the Development board PCB.

<img width="521" alt="Screen Shot 2023-05-04 at 1 36 09 PM" src="https://user-images.githubusercontent.com/117782788/236297577-a36d6dfb-d76b-4d75-830d-fb6824158d40.png">


# Date: April 8th





