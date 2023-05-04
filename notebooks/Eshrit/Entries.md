# Date: January 29

Our group finalised the project idea over the week and we began to work on the project proposal. The main agenda was to come up with a comprehensive block diagram.
We identified three main subsystems: RFID, Breathalyzer, and Data management. We shared multiple ideas to discuss feasibility, and evaluate pros and cons.
We all brought our different ideas, potential pairs of problems an solutions to the table and collaborated effectively to ensure each subsystem complemented the others and functioned well in the overall system. We made sure everyone understood their responsibilities and their duties towards each other. By the end we had a skeleton and a somewhat finished block diagram.

# Date: February 1

We delved further into the problem and tried to identify more issues and ideas on how to tackle those issues. Essentially we thought more about expanding on the implementation of our subsystems and laid out an initial gameplan including the parts we would need and how the product we are delivering would actually be used in practice. We discussed the project idea on a more user friendly level. The project would include RFID-enabled wristbands/cards, a breathalyzer, a Raspberry Pi, and a microcontroller to measure the blood alcohol content (BAC) levels of users and encourage more responsible drinking.
Essentially TipsyTracker would remind users to get their BAC levels checked so they can be in control of their senses on a real scale analysis. The system would alert the host if a guest's BAC levels are above a certain threshold.
I carried forth discussions about the real time use cases and issues about device liquid safety and anticipating the problems for the device in real time such as what would we have the device do in case of system failure, and what would could cause our project to either malfunction or provide mismanaged data. Privacy is also a concern that we would have to tackle since we would be handling so much data about BAC levels.


# Date: February 3

We finalised the proposal and made small edits to it in accordance with the formatting of previous semesters. I assisted with finishing up the block diagram and making the high level requirements be more suitable to the overall success of our project instead of depending on the subsystem workings. We made plans of getting final inputs from the TA and making a submission for the project proposal a day before the deadline.

# Date: February 6th

I picked up the the RFID component and soldered it so that for our team meeting the following day, we can breadboard all components together and test them to see if they work before we proceed with the manafacturing process.


# Date: February 7

We had made plans to breadboard the ordered components and were able to successfully breadboard the complete system design. This step was imperative to test the functionality of the various subsystems and identify any potential issues that needed to be resolved before proceeding with the manufacturing process. Akash made the decision to take the lead on making the PCB schematics with the incorporated parts.

Additionally, breadboarding the entire system helped the team to verify that all the components were correctly interconnected and that the system was working according to the expected standards. By utilizing the expertise of each team member, any problems encountered during testing were effectively addressed to ensure that the system operated as intended.

# Date: February 20th

We decided to work on the design document and laid out a plan on how we would use the proposal as a basis and expand on the requirements and verification of the subsystems. In the course of the discussion, we carefully reviewed the current system design, identified areas that required clarification or more development, and discussed the implementation plan. Moreover, we identified potential issues that could arise during the manufacturing process. This comprehensive review allowed us to identify areas for improvement and confirm that the system design was well-documented and comprehended by all team members. This served as a valuable checkpoint regarding lower level understanding of the project. Akash also went over the updates of the PCB schematic. Sumedh, Akash and I at the end of the meeting came up with a more comprehensive division of labor which would be laid out in the schedule subsection of the design document.


# Date: February 21st

Hashed out the final editings of the design document, I planned out the schedule and wrote it in the format that was suitable for submission along the lines with what my teammates and I went over in the previous meeting. Followed the plan of expanding the requirements and verification of the subsystems and finished that while concluding the brainstorming from the previous meeting on what verifications would conduct thorough checks for the workings of our subsystems. Prepared the design document for final submission and decided to submit it a day before the deadline.

# Date: February 27th

Conducted a successful design review presentation where my teammates and I went over our design document with the Professors and some TAs. We got valuable feedback about a possible problem where our device could be provided with fake BAC values for a user when the air that they blow into the breathalyzer is not generated with enough pressure so that it comes from the lungs. To tackle this the Professor suggested the addition of a pressure sensor and we decided to go over the feasibility of this addition with the TA.

# Date: March 1st

I picked up the the pressure sensor component and soldered it so that for our next team meeting, we can breadboard it and test to see if it works as expected before we proceed with the manafacturing process.

# Date: March 6th

Went over the setup of the website where users can register their information and how their BAC contents get updated with the latest measurements. Went over the functionality of the user getting a notification to test, testing within intervals setup by us and a  text broadcast in case of a subsystem failure which would indicate that the device is not working currently. This helped us discuss more ideas and features in case of subsystem failures. We also discussed the plan for soldering given the PCB. 


# Date: March 7th 

Headed over to the ECE lab to try and solder the first PCB since we needed to discuss the feasibility of soldering given some of the components were too small (0402 resistors, the diodes and capacitors). The soldering irons in the general area had tips that were too wide but in the special area with the finer soldering tips and the hot air I was able to solder the smaller components much more easily although it was still difficult. We then discussed problems even if I was able to get the components on. We could foresee some bridging issues due to the PCB having components that were too close and the components not having enough solder. We then moved to a newer PCB design which would incorporate through hole components. Below is are the images of the PCB and the PCB with some components soldered.

<img width="398" alt="PCB_1" src="https://user-images.githubusercontent.com/117782788/236100725-d1af80fe-4401-4d51-9d6e-44707d15eaa0.png">

<img width="351" alt="PCB_1_sol" src="https://user-images.githubusercontent.com/117782788/236102471-0a3ba6e1-1db4-4faa-8fe8-80c9480733c7.png">








