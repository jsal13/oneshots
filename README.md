# One-Shots

A collection of one-shot campaigns.

This was an experiment to see how much of the process I could automate and still have a reasonable campaign.  **This project makes heavy use of AI generation.**

## Campaign Creation Pipeline

1. Create a folder in `./oneshots`, alongside the other oneshot campaigns.
2. Inside this newly created folder, create the folders `./acts`, `./data`, `./descriptions`.  You can also copy-paste an old oneshot's data.  (NOTE: We can automate this part with a justfile or something.)
3. Think of a setting or topic for the campaign.  Split this into approximately three acts (Beginning, Middle, End).
4. Use ChatGPT to create:
   1. The beginning description.
   2. The middle description.
   3. The end description.
   4. Two-or-so ambushes or fights with monsters.
   5. Four or five NPCs.
5. Edit the ChatGPT responses to be mroe consise and fit within a narrative whole.  Add or remove at will.
6. Chunk these responses into files in `./descriptions` and `./data` in the same way other oneshots have been doing it.  (See other folders for examples.)
7. Include these in `./act_X.qmd` for `X in 1, 2, 3`.  (See other folders for examples.)
8. Pull appropriate enemies from the `./bestiary` or create your own from a util script in `./util`.
9. Use Inkcarnate or the dungeon builder to generate the maps.
10. (????) Use (SOMETHING) to generate AI images of the enemies, or use standard enemy pictures.
11. Build the map for the players to see on Roll20 using the maps and the AI images.
12. Push to github and have actions build the page, or use quarto build locally.