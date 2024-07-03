# XOR_AI
### Most of this code is not my own. I have found a [video](https://www.youtube.com/watch?v=pauPCy_s0Ok&list=LL&index=12), by The Independent Code, that explains how a simple neural network works and the implementation of it.

### This project is meant to show case what I’ve learned by following their video.

This is an AI for solving an XOR gate. It is explained in the video why, but I also wish to show case this.
An XOR gate is a binary gate, that when given two inputs(both being 1 or 0), it will out put either 1 or 0. An XOR gate in particular has the following table.
(0,0) -> 0
(1,0) -> 1
(0,1) -> 1
(1,1) -> 0

The reason this was picked for an ai to try to solve is because the points with same outputs are not linearly separable. Making the solution to become a function that is non-linear. These interesting functions can be viewed as a 3d scatter plot.

![Scatterplot 1](https://github.com/TheFosh/XOR_AI/blob/main/table1_3D_Plot.png)

These are graphed by generating points over a 2d plane from (0,0) -> (1,1), then these points output a prediction value from the AI. This value is the z value of the plot to be able to visually see the functions generated.
These Images also have many variances since the AI originally starts with random parameters. This causes similar but different functions to be graphed when running the AI multiple times with the same points.

![Scatterplot 2](https://github.com/TheFosh/XOR_AI/blob/main/table2_3D_Plot.png)
![Scatterplot 3](https://github.com/TheFosh/XOR_AI/blob/main/table3_3D_Plot.png?raw=true)
