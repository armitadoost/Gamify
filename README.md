# Gamify

Gamification is the integration of elements found in games – such as points and badges – into nongame activities. One example of gamification is students’ being awarded badges and points for completing exercises in online courses. This is done in order to encourage students to complete the exercises. Another example is supermarkets awarding points to customers for purchasing various items. This is done, in part, to induce the customers to purchase more items in order to gain more points.

This project implements a simulator for an app that encourages the user to exercise more by awarding “stars” to the user for exercising.

## The Project Rules
  - The user starts out with 0 health points, and 0 hedons
  - The user is always either running, carrying textbooks, or resting
  - Running gives 3 health points per minute for up to 180 minutes, and 1 health point per minute for every minute over 180 minutes that the user runs
  - Carrying textbooks always gives 2 health points per minute
  - Resting gives 0 hedons per minute
  - Both running and carrying textbooks give -2 hedons per minute if the user is tired and isn’t using a star
  - If the user is not tired, running gives 2 hedons per minute for the first 10 minutes of running, and -2 hedons per minute for every minute after the first 10
  - If the user is not tired, carrying textbooks gives 1 hedon per minute for the first 20 minutes, and -1 hedon per minute for every minute after the first 20
  - If a star is offered for a particular activity and the user takes the star right away, the user gets an additional 3 hedons per minute for at most 10 minutes
  - If three stars are offered within the span of 2 hours, the user loses interest, and will not get additional hedons due to stars for the rest of the simulatio
