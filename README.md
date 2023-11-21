# Betting middleware API 

## Scope
a middleware layer for various books api's, should include
 - standardised common data model to represent a bet
 - adapter classes for each supported bookmakers api's 
 - POST methods to accept instances of the common data model, and a chosen bookmaker id, and return the correctly formatted request for the given API
 - GET methods to parse the unique response from the bookmakers API
 - async methods to get the outcome of the bet (this could potentially run as a seperate application if it's easier)
 - (optionally) a UI or dashboard to list all active bets as a timeline and bankroll details
 - email or push notifications for placing bets, and for payouts

 ## environment and stack 
 Prelim stack, will likely change
  - Poetry for package management
  - Streamlit for a lightweight UI
  - PushBullet for push notifications
