# healthiator
Easily compare medical costs across hospitals, tailored to your condition, insurance plan vs out-of-pocket payment with Healthiator. Uncover savings and take control of your healthcare journey.

## Inspiration
As a patient in the United States you do not know what costs you are facing when you receive treatment at a hospital or if your insurance plan covers the expenses. Patients are faced with unexpected bills and left with expensive copayments. In some instances patients would pay less if they cover the expenses out of pocket instead of using their insurance plan.

## What it does
Healthiator provides patients with a comprehensive overview of medical procedures that they will need to undergo for their health condition and sums up the total costs of that treatment depending on which hospital they go-to, and if they pay the treatment out-of-pocket or through their insurance. 
This allows patients to choose the most cost-effective treatment and understand the medical expenses they are facing. A second feature healthiator provides is that once patients receive their actual hospital bill they can claim inaccuracies. Healthiator helps patients with billing disputes by leveraging AI to handle the process of negotiating fair pricing. 

## How we built it
We used a combination of Together.AI and Fetch.AI. We have several smart agents running in Fetch.AI each responsible for one of the features. For instance, we get the online and instant data from the hospitals (publicly available under the Good Faith act/law) about the prices and cash discounts using one agent and then use together.ai's API to integrate those information in the negotiation part.

## Ethics
The ethics of the project was by far the most important and challenging part. The reason is that although our end purpose is to help people keep healthier by reducing the fear of surprise bills and actually making healthcare more affordable, we are aware that any wrong suggestions or otherwise violations of the user's privacy have significant consequences. Giving the user as much information as possible while keeping away from making clinical suggestions and false/hallucinated information was the most challenging part in our work.

## Challenges we ran into
Finding actionable data from the hospitals was one of the most challenging parts as each hospital has their own format and assumptions and it was not straightforward at all how to integrate them all into a single database. Another challenge was making various APIs and third parties work together in time.

## Accomplishments that we're proud of
Solving a relevant social issue. Everyone we talked to has experienced the problem of not knowing the costs they're facing for different procedures at hospitals and if their insurance covers it. While it is an anxious process for everyone, this fact might prevent and delay a number of people from going to hospitals and getting the care that they urgently need. This might result in health conditions that could have had a better outcome if treated earlier.

## What we learned
How to work with convex, fetch.api and together.api. 

## What's next for Healthiator
Getting more extensive user feedback and buidling a UI.