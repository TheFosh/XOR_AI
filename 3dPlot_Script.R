> require(scatterplot3d)
table1 = read.table("plainOutput_01.txt", header = TRUE)
table2 = read.table("plainOutput_02.txt", header = TRUE)
table3 = read.table("plainOutput_03.txt", header = TRUE)

> scatterplot3d(table1[1:121,3:1],angle=140)

> scatterplot3d(table2[1:121,3:1],angle=50)

> scatterplot3d(table3[1:121,3:1],angle=230)