# Self-Painting-Bot

Dragging the Mouse 

Dragging means moving the mouse while holding down one of the mouse buttons. For example, you can move files between folders by dragging the folder icons, or you can move appointments around in a calendar app.

When you run this program, there will be a five-second delay ❶ for you to move the mouse cursor over the drawing program’s window with the Pencil or Brush tool selected. Then spiralDraw.py will take control of the mouse and click to put the drawing program in focus ❷. A window is in focus when it has an active blinking cursor, and the actions you take—like typing or, in this case, dragging the mouse—will affect that window. Once the drawing program is in focus, spiralDraw.py draws a square spiral pattern like

The distance variable starts at 200, so on the first iteration of the while loop, the first dragRel() call drags the cursor 200 pixels to the right, taking 0.2 seconds ❸. distance is then decreased to 195 ❹, and the second dragRel() call drags the cursor 195 pixels down ❺. The third dragRel() call drags the cursor –195 horizontally (195 to the left) ❻, distance is decreased to 190, and the last dragRel() call drags the cursor 190 pixels up. On each iteration, the mouse is dragged right, down, left, and up, and distance is slightly smaller than it was in the previous iteration. By looping over this code, you can move the mouse cursor to draw a square spiral.

You could draw this spiral by hand (or rather, by mouse), but you’d have to work slowly to be so precise. PyAutoGUI can do it in a few seconds!
