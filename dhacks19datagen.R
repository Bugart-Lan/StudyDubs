library("rjson")
library("dplyr")
l_n = read.table(file = 'lastnames.tsv', sep = '\t', header = TRUE)
f_n = read.table(file = 'firstnames.tsv', sep = '\t', header = TRUE)

id <- seq(1, 100)

names = c()
for (i in 1:100){
  fn = l_n$name[floor(runif(1,min = 1, max = 100))]
  ln = f_n$name[floor(runif(1,min = 1, max = 100))]
  x = paste(ln, fn, sep = " ", collapse = NULL)
  names = c(names, x)

}
col1 <- data.frame(id, names)
fllist <- unlist(names[3:102])

gpa= c()
for (i in 1:100){
  grade = round(runif(1,min = 1.5, max = 4), 1)
  gpa = c(gpa, grade)
  
}
col2 <- data.frame(id, gpa)


auditory = c()
for (i in 1:100){
  grade = round(runif(1,min = 1, max = 5))
  auditory = c(auditory, grade)
  
}
col3 <- data.frame(id, auditory)

visual = c()
for (i in 1:100){
  grade = round(runif(1,min = 1, max = 5))
  visual = c(visual, grade)
  
}
col4 <- data.frame(id, visual)

audio = c()
for (i in 1:100){
  grade = round(runif(1,min = 1, max = 5))
  audio = c(audio, grade)
  
}
kinect = c()
for (i in 1:100){
  grade = round(runif(1,min = 1, max = 5))
  kinect = c(kinect, grade)
  
}
col5 <- data.frame(id, kinect)

merged <- left_join(col1, col2, "id")
merged2 <- left_join(col3, col4, "id")
merged3 <- left_join(merged, merged2, "id")
merged4 <- left_join(merged3, col5, "id")

jsodata <- toJSON(unname(split(merged4, 1:nrow(merged4))))
write(jsodata2, file = "studydubs.json")

write.csv(merged4, file = "studydubs.csv")

jsodata2 <- toJSON(as.list(unname(split(merged4, 1:nrow(merged4)))))
