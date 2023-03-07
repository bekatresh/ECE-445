# Date: January 29
For the TipsyTracker Project Proposal, our group worked together closely to develop the block diagram that included the RFID subsystem, Breathalyzer measurement subsystem, and Data management subsystem. We had multiple brainstorming sessions where we shared our ideas, discussed the feasibility of different approaches, and evaluated the pros and cons of each subsystem.

We all shared our expertise and worked together to ensure that the different subsystems complemented each other and functioned effectively in the overall system. Each team member had a specific role to play, and we ensured that everyone had a clear understanding of their responsibilities.

# Date: February 1
Our group identified the problem of irresponsible drinking, which is a common issue, especially among university students, that leads to significant negative consequences, including deaths caused by excessive alcohol consumption. Our solution, TipsyTracker, is a comprehensive system that employs RFID-enabled wristbands/cards, breathalyzer devices, a Raspberry Pi server, and an ESP32 microcontroller to measure the blood alcohol content (BAC) levels of partygoers/patrons and encourage responsible drinking habits. TipsyTracker notifies guests about their BAC levels and sends reminders to them to check their levels, as well as alerts the host if a guest's BAC level exceeds a predetermined limit.

I specifically worked on identifying two subsystems. The Breathalyzer Measurement Subsystem, which involves the MQ-3 sensor, is responsible for measuring the BAC levels of partygoers/patrons by using a breathalyzer device. It is connected to the ESP32 microcontroller and communicates with the RFID identification subsystem to ensure that the test results are associated with the correct partygoer/patron. The Data Management Subsystem, powered by the Raspberry Pi server, is responsible for handling the communication between the device and the registration station and sending notifications to partygoers/patrons and the host. It hosts the necessary software and databases, handles data storage, analysis, and management, and sends reminders to partygoers/patrons at set intervals to test their BAC levels and notifies the host if necessary.

By working together as a group and collaborating effectively, we were able to develop a comprehensive solution that addresses the issue of excessive alcohol consumption and encourages responsible drinking habits. The TipsyTracker system is an effective solution to promote awareness and responsibility among partygoers and patrons.

# Date: February 3
During the development of the TipsyTracker project proposal, I assisted the group by editing and refining the document to ensure that it was clear, concise, and well-organized. I worked closely with the team members to ensure that the document was coherent and that the language used was appropriate for the intended audience.

In addition to editing the proposal, I also drew a visual aid to help illustrate the system architecture and explain how the different subsystems interacted with each other. The visual aid helped to clarify the system design and made it easier for team members to understand the overall concept of the TipsyTracker system

# Date: February 7

On February 7th, the TipsyTracker development team made significant progress by successfully breadboarding the entire system design. This was a crucial step in the development process as it enabled us to test the functionality of the different subsystems and identify any potential issues that needed to be addressed before moving forward with the manufacturing process.

Breadboarding the entire system also allowed the team to ensure that all components were properly connected and that the system was functioning as expected. By leveraging the expertise of each team member, we were able to address any issues that arose during testing and ensure that the system was operating as intended.


# Date: February 13
I am pleased to report that during the development of the TipsyTracker system, I was able to make significant progress on the Printed Circuit Board (PCB) schematic. Specifically, I was able to complete the first schematic for the PCB, which included important components such as the power input, 5V to 3.3V regulator, USB-to-UART converter, MQ-3 sensor, RFID sensors, and other key parts.

The power input section of the schematic was critical to ensure that the device was able to operate properly and that there were no issues with power delivery. The 5V to 3.3V regulator was important to provide the correct voltage for the components, and the USB-to-UART converter enabled the device to communicate with the Raspberry Pi server.

The MQ-3 sensor and RFID sensors were also critical components that allowed the system to measure BAC levels and identify partygoers/patrons accurately. Other parts, such as capacitors and resistors, were included to ensure proper signal conditioning and noise reduction.

Overall, the completion of the first schematic for the PCB was a significant milestone in the development of the TipsyTracker system. By leveraging my skills in PCB design and component selection, I was able to ensure that the system was well-designed and capable of meeting the requirements of the project.

# Date: February 15
I was able to make significant progress on the Printed Circuit Board (PCB) modeling and connections. Specifically, I was able to complete the modeling and line drawing of the PCB, which was a critical step in the development of the device.

The modeling and connections of the PCB were important because they enabled the team to visualize the physical layout of the device and ensure that all components fit correctly. I was able to create a detailed model of the PCB and ensure that all components were properly placed.

I helped to identify any potential issues or conflicts with the design, allowing the team to make any necessary adjustments before moving forward with the manufacturing process. This ensured that the device would function properly and meet the requirements of the project.

Overall, the completion of the first version of the PCB was a significant milestone in the development of the TipsyTracker system.

# Date: February 20
On February 20th, we started a discussion on the design document for the TipsyTracker system. This was an important step in the development process as it allowed us to ensure that all team members were on the same page regarding the system design and implementation.

During the discussion, we reviewed the current system design and identified any areas that needed clarification or further development. We also discussed the implementation plan and identified any potential issues that could arise during the manufacturing process. Through this discussion, we were able to identify areas of improvement and ensure that the system design was well-documented and understood by all team members.

# Date: February 21
We worked on refining the design document for the system. Specifically, we focused on adding more information about the requirements and verifications for all subsystems in the system, and I worked on adding a new power subsystem to the design.

I took the lead on adding detailed information about the functionality of each subsystem and the tests that would be used to verify that the subsystem was operating as intended (R and V).

By adding this additional information to the design document, we were able to ensure that all team members had a clear understanding of the requirements for each subsystem and the expected performance of the system as a whole. This allowed us to identify any potential issues or areas of improvement and make the necessary adjustments to ensure that the system would meet the requirements of the project.

# Date: February 24
I made significant progress in the development of the TipsyTracker system by ordering all the components needed for the PCB. This was a critical step in the manufacturing process, as it ensured that we had all the necessary parts to build the device.

To ensure that all the components were of high quality and met the requirements of the project, I carefully researched and selected each part. This involved evaluating different vendors and comparing prices to ensure that we were getting the best value for our money.

Once I had selected the components, I placed the order and worked closely with the team to ensure that the parts were delivered on time and in good condition. 

# Date: March 2

I successfully wrote the Arduino code for the MQ-3 and RFID sensors. This was a crucial step in the development process as it allowed us to test the functionality of the sensors and ensure that they were operating as intended.

The Arduino code that I wrote included logic for reading data from the MQ-3 and RFID sensors and processing the data for use in the TipsyTracker system. Additionally, I incorporated functionality for sending POST requests to a simple webserver that I wrote in Python. This feature enabled the system to send data to the webserver for storage and analysis, and allowed us to monitor the performance of the sensors in real-time.

The successful implementation of the Arduino code for the MQ-3 and RFID sensors, with the added functionality of sending post requests to a webserver, was a significant accomplishment in the TipsyTracker development process. My contribution to this milestone helped to move the project forward, and we are now one step closer to achieving our goal of creating an effective and reliable system for monitoring alcohol consumption.

# Date: March 5

I revamped the Python code to incorporate a web portal that allows for adding entries, viewing user history, and sending text messages about the BAC levels using Twilio. This was a crucial step in the development process as it allowed us to test the functionality of the web portal and ensure that it was operating as intended.

The revamped Python code includes a user-friendly web interface that allows hosts to add new entries and monitor the BAC levels of party-goers in real-time. The code also includes Twilio integration, allowing the system to send text messages to party-goers about their BAC levels and reminding them to check their levels at regular intervals.

Additionally, the code includes functionality for storing user history (during the party) to help hosts identify trends in alcohol consumption and make informed decisions about future events.

The successful implementation of the revamped Python code was a significant accomplishment in the TipsyTracker development process. By incorporating a user-friendly web portal and Twilio integration, the system is now more effective and easier to use than ever before. 

# Date: March 6
We discussed the plan for soldering the PCB, as well as went over my Arduino and Python code. This was an important step in the development process as it allowed us to prepare for the manufacturing phase and ensure that the code was properly reviewed and tested.

We also organized all of the components that were ordered for the PCB, ensuring that they were properly labeled and stored for easy access during the manufacturing process. This helped to streamline the process of assembling the PCB and reduce the risk of errors during manufacturing.

Additionally, we discussed the plan for soldering the PCB, identifying potential issues and developing a plan to mitigate these risks.

# Date: March 7
Initial note regarding developing PCB with larger resistors, backup dev board.

