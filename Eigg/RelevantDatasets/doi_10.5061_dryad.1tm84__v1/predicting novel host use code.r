###This is the basic code used in Pearse and Altermatt (2013) Ecol. Lett.  in order to predict the novel host use
### of European moths on non-native host plants.  The code was developed in R version 2.10.1


##libraries & functions
library(ape)
library(vegan)
library(ROCR)
se<-function(x) sd(x, na.rm=T)/sqrt(length(x))
K_fold <- function(Nobs,K=5){
    rs <- runif(Nobs)
    id <- seq(Nobs)[order(rs)]
    k <- as.integer(Nobs*seq(1,K-1)/K)
    k <- matrix(c(0,rep(k,each=2),Nobs),ncol=2,byrow=TRUE)
    k[,1] <- k[,1]+1
    l <- lapply(seq.int(K),function(x,k,d) 
                list(train=d[!(seq(d) %in% seq(k[x,1],k[x,2]))],
                     test=d[seq(k[x,1],k[x,2])]),k=k,d=id)
   return(l)
}

##data
tr<-read.tree("plant_phylo_2010_11_30.tre")
plant<-read.table("plant_information.csv", header=TRUE, as.is=TRUE)
#oldmoth<-read.table("matrix_species_20101108.txt",header=TRUE, as.is=TRUE)  ##old data
moth<-read.table("matrix_species_20120901.txt",header=TRUE, as.is=TRUE)
moth[867,537]<-1
plant$species<-tolower(plant$species)
mothdat<-read.table("Lepidoptera_information.csv", header=T, as.is=T)
##culling full plant list to phylogeny.  This is getting rid of ferns
plant<-plant[which(plant$species %in% tr$tip.label),]
all(plant$species %in% tr$tip.label)
##should be TRUE
colnames(moth)<-tolower(colnames(moth))
a<-tolower(colnames(moth)) %in% plant$species
moth2<-moth[,a]
rownames(moth2)<-moth[,1]
moth<-moth2

##adding plants with no moths into matrix
eatplant<-plant$species[which(plant$species %in% colnames(moth2))]
noeatplant<-plant$species[-which(plant$species %in% eatplant)]
length(noeatplant)
##should be 1756
nullmat<-matrix(0,nrow(moth),length(noeatplant))
colnames(nullmat)<-noeatplant
moth<-cbind(moth,nullmat)
all(colnames(moth) %in% tr$tip.label)
all(plant$species %in% colnames(moth))

###this dataset is now ready for analysis
native<-plant[-which(plant$status == "ornamental_plant" | plant$status =="neophyte"),]
moth<-t(moth)
exotic<-plant[which(plant$status == "ornamental_plant" | plant$status =="neophyte"),]


###try using k-fold to estimate within-native parameters for logistic model
#separate data set
trmat<-cophenetic(tr)
trmat<-trmat/max(trmat)
mothnat<-moth[-which(rownames(moth)%in%exotic$species),]
mothnat[which(mothnat>1)]<-1
miss<-colnames(mothnat[,which(colSums(mothnat)==0)])
mothnat<-mothnat[,-which(colnames(mothnat)%in%miss)]
plantrange<-plant$raster_frequency_BW
names(plantrange)<-plant$species
K=5
set.seed(7402356)
kmoth<-K_fold(nrow(mothnat), K=K)
nhost<-apply(mothnat, 2,sum)
glist<-rep(NA, nrow(mothnat))
for(jjj in 1:nrow(mothnat)){
	mmm<-rownames(mothnat)[jjj]
	glist[jjj]<-plant$genus[which(plant$species==mmm)]
}
mothnatgen<-aggregate(x=mothnat, by=list(glist), FUN=mean)
mothnatgen[mothnatgen>0]<-1
mothnatgen<-mothnatgen[,-1]
ngenhost<-apply(mothnatgen,2,sum)
#nhost<-ngenhost
	
	


###run models for each K-fold
modlist<-list()
modlist_range<-list()
for(h in 1:K){
	print(paste("K-fold", h, "of", K))
	flush.console()
	train<-mothnat[kmoth[[h]]$train,]
	train<-t(train)
	train<-train[which(rowSums(train)>0),]
	test<-mothnat[kmoth[[h]]$test,]
	test<-t(test)
	test<-test[which(rownames(test)%in%rownames(train)),]
	mdistmat<-matrix(NA, nrow=ncol(test), ncol=nrow(train))
	rownames(mdistmat)<-colnames(test)
	colnames(mdistmat)<-rownames(train)
	print("estimating phylo distance")
	flush.console()
	for(i in 1:nrow(train)){
		mdat<-train[i,]
		m<-row.names(train)[i]
		hostpl<-names(mdat[-which(mdat==0)])
		hostdat<-trmat[which(row.names(trmat)%in% hostpl),]
		dmat<-matrix(NA, nrow=ncol(test), ncol=length(hostpl))
		row.names(dmat)<-colnames(test)
		if(length(hostpl)==1){
			pdist<-hostdat[which(names(hostdat)%in% colnames(test))]
			pdist<-pdist[which(duplicated(names(pdist))==F)]
			pdist<-pdist[colnames(test)]
			dmat[,1]<-pdist
			}
		if(length(hostpl)>1){
			for(j in 1:length(hostpl)){
				h1<-hostdat[j,]
				pdist<-h1[which(names(h1)%in% colnames(test))]
				pdist<-pdist[which(duplicated(names(pdist))==F)]
				pdist<-pdist[colnames(test)]
				dmat[,j]<-pdist
			}
		}
		dmin<-apply(dmat, 1, min)
		####Check that this matches up....
		mdistmat[,i]<-dmin
	}
	num_host<-rep(NA, nrow(test)*ncol(test))
	num_genhost<-rep(NA, nrow(test)*ncol(test))
	nhost_cor<-nhost[which(names(nhost)%in%rownames(test))]
	ngenhost_cor<-ngenhost[which(names(ngenhost)%in%rownames(test))]
	for(i in 1:length(nhost_cor)){
		nho<-rep(nhost_cor[i], ncol(test))
		num_host[((i-1)*ncol(test)+1):((i-1)*ncol(test)+ncol(test))]<-nho
	}	
	for(i in 1:length(ngenhost_cor)){
		nho<-rep(ngenhost_cor[i], ncol(test))
		num_genhost[((i-1)*ncol(test)+1):((i-1)*ncol(test)+ncol(test))]<-nho
	}	
	mothnam<-rownames(test)
	mothmoth<-rep(NA, nrow(test)*ncol(test))
	for(i in 1:length(mothnam)){
		mnam<-rep(mothnam[i], ncol(test))
		mothmoth[((i-1)*ncol(test)+1):((i-1)*ncol(test)+ncol(test))]<-mnam
	}
	plantplant<-rep(colnames(test), nrow(test))
	
	logdat<-data.frame(moth=mothmoth, plant=plantplant, real_int=as.numeric(t(test)), min_phylo=as.numeric(mdistmat), nhost=num_host, ngenhost=num_genhost)
	logdat$min_phylo[which(logdat$min_phylo=="Inf")]<-1000
	plran<-plantrange[as.character(logdat$plant)]
	logdat$BW_range<-plran
	print("running models in high heels")
	flush.console()
	mod1<-glm(real_int ~ min_phylo*nhost, data=logdat, family="binomial")
	mod2<-glm(real_int ~ min_phylo*ngenhost, data=logdat, family="binomial")
	#mod2<-glm(real_int ~ min_phylo*nhost+BW_range*min_phylo+BW_range*nhost, data=logdat, family="binomial")
	modlist[[h]]<-mod1
	modlist_range[[h]]<-mod2
}
logdat_nat<-logdat

modmat<-matrix(NA,nrow=length(modlist), ncol=length(modlist[[1]]$coeff))
modmatgen<-matrix(NA,nrow=length(modlist_range), ncol=length(modlist_range[[1]]$coeff))
###currently, this is sort of a wierd work around, where I am making an lm object from a previous model, but 
###replacing its coefficients with the averaged coefficients from the Kfolds
for(i in 1:length(modlist)){modmat[i,]<-modlist[[i]]$coeff}
for(i in 1:length(modlist_range)){modmatgen[i,]<-modlist_range[[i]]$coeff}
AveCoeff<-apply(modmat,2,mean)
AveCoeffgen<-apply(modmatgen,2,mean)
names(AveCoeff)<-names(modlist[[1]]$coeff)
modAve<-modlist[[1]]
modAve$coefficients<-AveCoeff

###create predictors for non-natives and use the previous model to predict interactions based
###on these values

##non-native interaction matrix
exint<-moth[which(rownames(moth)%in% exotic$species),]
exint<-exint[which(duplicated(rownames(exint))==F),]
exint[exint>0]<-1
exint<-exint[,-which(colnames(exint)%in%miss)]
mdistmat<-matrix(NA, nrow=nrow(exint), ncol=ncol(exint))
rownames(mdistmat)<-rownames(exint)
colnames(mdistmat)<-colnames(exint)
mothnat<-t(mothnat)
for(i in 1:nrow(mothnat)){
	m<-row.names(mothnat)[i]
	mdat<-mothnat[i,]
	hostpl<-names(mdat[-which(mdat==0)])
	hostdat<-trmat[which(row.names(trmat)%in% hostpl),]
	dmat<-matrix(NA, nrow=nrow(exint), ncol=length(hostpl))
	row.names(dmat)<-rownames(mdistmat)
	
	if(length(hostpl)==1){
		exdist<-hostdat[which(names(hostdat)%in% rownames(dmat))]
		exdist<-exdist[which(duplicated(names(exdist))==F)]
		exdist<-exdist[rownames(dmat)]
		dmat[,1]<-exdist
	}
	if(length(hostpl)>1){
		for(j in 1:length(hostpl)){
			h1<-hostdat[j,]
			exdist<-h1[which(names(h1)%in% rownames(dmat))]
			exdist<-exdist[which(duplicated(names(exdist))==F)]
			exdist<-exdist[rownames(dmat)]
			dmat[,j]<-exdist
		}
	}
	
	dmin<-apply(dmat, 1, min)	
	dmin<-dmin[rownames(mdistmat)]
	mdistmat[,i]<-dmin
	#print(paste(i, "AND", m))
}

nhost<-apply(mothnat, 1,sum)
num_host<-rep(NA, nrow(exint)*ncol(exint))
for(i in 1:length(nhost)){
	nho<-rep(nhost[i], nrow(exint))
	num_host[((i-1)*nrow(exint)+1):((i-1)*nrow(exint)+nrow(exint))]<-nho
}

mothnam<-colnames(exint)
mothmoth<-rep(NA, nrow(exint)*ncol(exint))
for(i in 1:length(mothnam)){
	mnam<-rep(mothnam[i], nrow(exint))
	mothmoth[((i-1)*nrow(exint)+1):((i-1)*nrow(exint)+nrow(exint))]<-mnam
}
plantplant<-rep(rownames(exint), ncol(exint))
	
logdat<-data.frame(moth=mothmoth, plant=plantplant, real_int=as.numeric(exint), min_phylo=as.numeric(mdistmat), nhost=num_host)
logdat$BW_range<-plantrange[logdat$plant]
logdat_nn<-logdat
###predict the natives model onto the nonnative plants
modpred<-prediction(predictions=predict(modAve, newdata=logdat), labels=logdat$real_int)
modperf<-performance(modpred, measure="tpr", x.measure="fpr")
modperf_all<-modperf
plot(modperf)
auc<-performance(modpred, measure="auc")
auc
# n=1000
# n_auc<-vector()
# for(i in 1:n){
	# print(i); flush.console()
	# randat<-logdat
	# randat$min_phylo<-sample(logdat$min_phylo)
	# randat$nhost<-sample(logdat$nhost)
	# n_modpred<-prediction(predictions=predict(modAve, newdata=randat), labels=randat$real_int)
	# auci<-performance(n_modpred, measure="auc")
	# n_auc[i]<-auci@y.values[[1]]
# }
# save(n_auc, file="rando_auc.Rdata")
###make a list of all predictions with real moth and plant names
logdat$predictions<-modpred@predictions[[1]]

logdat$mothname<-rep(NA, nrow(logdat))
for(i in 1:nrow(mothdat)){
	mm<-mothdat[i,]
	logdat$mothname[which(logdat$moth==mm$Lep_nr)]<-mm$Lep_name
}
realdat<-logdat[which(logdat$real_int==1),]

###Figure 1A ROC curve
jpeg(filename = "Fig1A_ROC_curve.jpeg", width = 6, height = 6, units = "in", 
	pointsize = 12, bg = "transparent", res = 600, restoreConsole = TRUE)
plot(modperf, colorize=F, lwd=3,xaxis.cex.axis=1.5, yaxis.cex.axis=1.5, cex.lab=1.5)
xs<-modperf@x.values[[1]]; ys<-modperf@y.values[[1]]
#polygon(y=c(ys,0), x=c(xs,1), col="light blue")
polygon(y=c(ys,order(ys)/length(ys)), x=c(xs,order(ys)/length(ys)), col="light green")
segments(x0=0,y0=0,x1=1,y1=1,lty="dashed", lwd=2)
dev.off()
###get values to make arrows to predictions of particular examples...did the drawing in Photoshop to get
###nice looking arrows.  

falsedat<-logdat[which(logdat$real_int==0),]
realdat<-logdat[which(logdat$real_int==1),]
##Eupethecia virginuata on Solidago canadensis/gigantea score = -2.363075
xval<-nrow(falsedat[which(falsedat$predictions>-2.363075),])/nrow(falsedat)
yval<-nrow(realdat[which(realdat$predictions>-2.363075),])/nrow(realdat)
##Dendrolimus_pini on pseudotsuga_menziesii:  score = -6.535287

xval<-nrow(falsedat[which(falsedat$predictions>-6.535287),])/nrow(falsedat)
yval<-nrow(realdat[which(realdat$predictions>-6.535287),])/nrow(realdat)

##Synanthedon_tipuliformis on ribes_aureum:  score= -3.300335
xval<-nrow(falsedat[which(falsedat$predictions>-3.300335),])/nrow(falsedat)
yval<-nrow(realdat[which(realdat$predictions>-3.300335),])/nrow(realdat)
##Calliteara_pudibunda on quercus_rubra:  score= -2.801016
xval<-nrow(falsedat[which(falsedat$predictions>-2.801016),])/nrow(falsedat)
yval<-nrow(realdat[which(realdat$predictions>-2.801016),])/nrow(realdat)
###model parameters
colnames(modmat)<-c("intercept", "min_phylo", "nhost", "min_phylo*nhost")
rownames(modmat)<-c("K_1", "K_2", "K_3", "K_4", "K_5")
modmat
AveCoeff
