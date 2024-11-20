"""Testing a screen class with TDD.

List of tests:
- A Screen class can be created with a specified width and height. 
- The screen is initialized with a blank screen (all cells are spaces). 
- The Shape class has a single method `draw_at(screen, x, y)` that draws the shape on the screen at the specified position.
- The default implementation of `draw_at` in the Shape class does nothing.
- The Rectangle class is a subclass of Shape and has a constructor that takes a width and height.
- The Rectangle class implements the draw_at method by drawing a rectangle of stars on the screen.
- When the cells to be drawn are outside the screen, the draw_at method should not draw them.
"""