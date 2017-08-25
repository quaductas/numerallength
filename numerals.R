library(ggplot2)

numsen<-read.csv('numerals_en.csv')

numsenwords<-read.csv('numerals_en_words.csv')

numsenhuge<-read.csv('numerals_en_1M.csv')

labelfn<-function(x){
  return(paste(as.character(x/1000),'K',sep=''))
}

# 0 to 1000
ggplot(numsen,aes(number,wordlen))+geom_point(col="steelblue")+theme_light()+
  labs(x="Number",y="Length of English numeral")+
  scale_x_continuous(breaks=seq.int(0,1000,200),minor_breaks = seq.int(0,1000,100))+
  scale_y_continuous(limits=c(0,28))

# 0 to 50, including numerals
ggplot(numsenwords[1:51,],aes(number,wordlen))+geom_point(col="steelblue")+
  geom_text(aes(label=numeral),angle=90,hjust=-0.1,vjust='middle')+theme_light()+
  labs(x="Number",y="Length of English numeral")+
  scale_y_continuous(limits=c(0,15),breaks=seq.int(0,15,5),minor_breaks = seq.int(0,15,1))
  
# 0 to 1M, takes ages to plot
pl<-ggplot(numsenhuge,aes(number,wordlen))+geom_point(col="steelblue")+theme_light()+
  labs(x="Number",y="Length of English numeral")+
  scale_x_continuous(breaks=seq.int(0,1000000,100000), labels = labelfn)

pl

# 0 to 1M, log scale, still takes ages
ggplot(numsenhuge,aes(number,wordlen))+geom_point(col="steelblue")+theme_light()+
  labs(x="Number (log scale)",y="Length of English numeral")+
  scale_x_log10(breaks=c(1,10,100,1000,10000,100000,1000000),minor_breaks=NULL,
                labels=c('1','10','100','1000','10K','100K','1000K'))+annotation_logticks(sides='b')
