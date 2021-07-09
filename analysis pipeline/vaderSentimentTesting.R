library('dplyr')
library('vader')
library('caret')
install.packages('vader')
tdata
tdata <- read.csv('testing-mentegy.csv')

  
#calculating the compound scores and assigning Yes if its a hate message and No if its not.

for( i in 1:length(tdata$text)) {
  score <- as.vector(get_vader(tdata$text[i])[2])
  if(as.double(score) > 0)
  { tdata$test[i] <- "No"}
  else
  {
    tdata$test[i] <- "Yes"
  }
 
} 

#Comparing the predicted scores with testing scores and accuracy is calculated

  tdata$test #prediction data
  tdata$Hate #available data
  
  confusionMatrix(as.factor(tdata$test),as.factor(tdata$Hate))