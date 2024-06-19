# passwordGenerator
A python script that interacts with the user to generate a more secure and personalized password.

## Problem
[The 2013 Target Data Breach](https://www.commerce.senate.gov/services/files/24d3c229-4f2f-405d-b8db-a3a67f183883) proves the need for secure credentials. Page 4 of the analysis of the breach states "The attackers reportedly first gained access to Target's system by stealing credentials from an HVAC and refrigerations company..." Good password hygiene is the key to more secure credentials that could have saved the information of as many as 110 million Target customers as well as an $18.5 million settlement for the data breach.

The difficulties with password hygiene today is that random password generators create passwords that users forget, and users generate common passwords that are easily crackable by password cracking sources such as [RockYou](https://github.com/ohmybahgosh/RockYou2021.txt), [SecList](https://hackmd.io/@lewismk/r1j9NJfPs), [Rocktastic](https://labs.nettitude.com/blog/rocktastic/), [Weakpass](https://weakpass.com/download), and [Probable Wordlists](https://github.com/berzerk0/Probable-Wordlists). 

How can we better secure employee credentials (passwords) to defend against cyber-attacks?

## Solution
A python script that interacts with the user to generate a more secure and personalized password. Users remember passwords better when passwords are personalized to them and represent something that they care about. Passwords are more secure when they follow the structure of a passphrase and incorporate leet speech.

## Application
A business could incorporate this password generator into their onboarding process. When an employee obtains access to PII and SPII, the employee then becomes a security risk, as exemplified in the "Problem" section of this README. As part of the onboarding process, an employee can be assigned to interact with this script to generate a more secure password. The secure password consisting of 1-4 words with significant meaning to the employee will be easily memorable like a tagline or slogan. 2 minutes really could save an organization $18.5 million.

## Justification
Consider the following passwords and their security calculated by [security.org](https://www.security.org/how-secure-is-my-password/) then divided by each other for comparison:

`$8EHn4R@F9sPejC` -> Google Password Suggestion -> is a strong but forgettable password, although manageable with a password manager.

`running africa jordan` -> Plain Text Passphrase (hobby, song, athlete) -> is 2,733,333 times more secure than the Google Suggested Password - largely due to consisting of more characters - and is more memorable.

`runn!n9 @fr!c@ j0rd@n` -> Leet Speech Passphrase (hobby, song, athlete) -> is 26,666,666,666 times more secure than the Google Suggested Password and is more memorable. Despite consisting of the same amount of characters, it is still 9,756 times more secure than the Plain Text Passphrase (hobby, song, athlete) and is equally as memorable.

## Instructions:
"Write one word per prompt that represents a subject that is significant to you. For example: My favorite hobby is running. I could enter the word 'marathon' because it is my favorite race to run. Each word must be from a unique subject. Do not enter the subject itself. For example: My favorite hobby is running, but I would not enter the word 'running' or 'run' because it is surface level and easily crackable. Each prompt will have a suggested subject in the case that you can't think of one. Once all prompts are answered, a password will be output. Disclaimer: Word inputs and password outputs are NOT stored or recorded."

## Logical Flow:
Print instructions. -> Confirm that the user desires to continue. -> Pick a password length on a scale from 1-4 words. -> Prohibit numbers, special characters, or spaces? (because some systems don't allow those) -> Prompt for a word 1-4 times, depending on the previously determined length. -> Apply leet speech. -> Print password.
