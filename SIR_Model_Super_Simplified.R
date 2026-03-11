#Reference : https://documents1.worldbank.org/curated/en/888341625223820901/pdf/An-Introduction-to-Deterministic-Infectious-Disease-Models.pdf
N <- 10000 #Total Population
B <- 0.5 #Transmission Rate
y <- 0.1 #recovery Rate (Inverse to the infectious period)
S <- 999
I <- 1
R <- 0
R_0 <- B/(y+miu) #Outbreak threshold
miu <- 0.16 #Natural mortality rate
delta <- miu * N #birth rate
dt <- 0.1
SG <-c()
IG <- c()
RG <- c()
tim <- 1:1000
for(t in 1:1000){
  dS <- delta - ((-B * S * I) / N) - (miu * S)
  dI <- ((B * S * I) / N) - ((y + miu) * I)
  dR <- (y * I) - (miu * R)
  S <- S + dS * dt
  I <- I + dI * dt
  R <- R + dR * dt
  SG[t] <- S
  IG[t] <- I
  RG[t] <- R
}

plot(tim, SG, type="l", col="blue", ylim=c(0, N), ylab="Population", xlab="Time")
lines(tim, IG, col="red")
lines(tim, RG, col="green")
legend("topright", legend=c("Susceptible","Infected","Recovered"), col=c("blue","red","green"), lty=1)
print("Outbreak Threshold : ")
print(R_0)


