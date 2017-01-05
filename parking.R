library(ggplot2)
library(reshape2)
bbi<-element_text(face="bold.italic", color="black")

x <- 1:200
y <- pnorm((1000/x-2), mean=15, sd=1)
text <- rep("", 200)


df <- data.frame(x,y, text)
df$text<-as.character(df$text)

df[52,3] <- "Length: 19.2 ft.\nCapacity: 52\nCoverage: 99%"
df[59,3] <- "Length: 16.9 ft.\nCapacity: 59\nCoverage: 48%"
df[68,3] <- "Length: 14.7 ft.\nCapacity: 68\nCoverage: 1%"

g2 <- subset(df, x==52|x==59|x==68)


delim_park <- ggplot(data=df, aes(x=x, y=y)) + geom_line() +
  labs(x="Capacity", y="Coverage", title="Delimited parking spaces:\nCapacity vs. Coverage") +
  scale_x_continuous(breaks=c(0, 50, 100, 200, 500, 1000)) +
  scale_y_continuous(breaks=c(0, .25, .5, .75, 1),
                     labels = c("0%", "25%", "50%", "75%", "100%")) +
  geom_point(data=g2, color="red", size=3) +
  geom_text(data=g2, label=g2$text, size=4,
            nudge_x = c(-12, -14, 14), nudge_y= c(-.08, 0,.06)) +
  theme(title=bbi, axis.text=element_text(size=12), axis.title=element_text(size=12))


leaders <- read.csv("~/Desktop/leaders.csv")

leader_park <- ggplot(data=leaders, aes(x=leaders, y=capacity)) + geom_point() +
  labs(x="Leaders", y="Capacity", title="Non-delimited parking spaces:\nLeaders vs. Capacity") +
  theme(title=bbi, axis.text=element_text(size=12), axis.title=element_text(size=12))
