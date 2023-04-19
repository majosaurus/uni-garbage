# cisla
2+3

# retezce
"den a noc"

# logicke hodnoty
5 < 10
5 == 1

# datove struktury

# vektor
# ciselny
cisla <- c(1,4,10,20)
cisla = c(1,4,10,20)
cisla

# string
slova = c("den", "noc", "poledne", "pulnoc")

# vsechny vektory musi byt stejneho typu
a = c(2,3,4)
b = c("den", "noc", "poledne", "pulnoc")
c = c(2, "den", 3)
d = c("2", "den", "3", "noc")
e = c("2", "3")
as.numeric(e)

# indexace polozek, pocita se od jednicky
a[1]
b[2:4]

# kdyz pouzijeme minus, odebira polozky
a[-2]
b[-1:-3]

# posledni tri polozky vektoru
tail(b, 3)
head(b, 3)

length_d = length(d)
d[c(length_d-2)]

# 
x = c(2)
x
y = c(4)
y
x+y
z = c(2,4)
u = c(6,8)
z+u

slova01 = c("den")
slova02 = c("noc")
slova01+slova02 # error

slova03 = c("rano", "poledne")
slova03
slova04 = c(slova01, slova02, slova03)
slova04
slova05 = c(slova01, slova02, slova03, x, y)
slova05

# nacteni a uprava textu

# scan - nacteni textu
hv_vrchlicky <- scan(file=file.choose(), what="char", sep="", encoding="UTF-8")
hv_vrchlicky

# pokud bychom chteli cely text v kuse, collapse je vlastne separator
hv_vrchlicky_celytxt = paste(hv_vrchlicky, collapse="@")
hv_vrchlicky_celytxt

# zjisteni slozky, kde jsem
getwd()
setwd()

# problemy - neslovni znaky
# neslovni znaky: \\W
# neslovni znaky: \\w

# nahrad neslovni znaky - ale v nekterych pripadech neumi ř, ť, ě apod., mne to funguje
gsub("\\W", "", hv_vrchlicky)

# zde vidime, co povazuje za neslovni znaky
unique(gsub("\\w", "", hv_vrchlicky))

hv_vrchlicky<-gsub("\\,|\\.|\\;|\\:|\\!|\\?|“|„|-|\\(|\\)|—|‚|‘|_|'|\\”|\\/|\\’
                  |\\[|\\]|\\<|\\>", "", hv_vrchlicky)

hv_vrchlicky<-hv_vrchlicky[hv_vrchlicky != ""]
hv_vrchlicky

# delka textu v tokenech
hv_vrchlicky_len = length(hv_vrchlicky)
hv_vrchlicky_len

# delka textu v typech
length(unique(hv_vrchlicky))

# TTR
TTR = length(unique(hv_vrchlicky))/hv_vrchlicky_len
TTR

# to ale neni ok - proc?
# musime to prevest na mala pismena
hv_vrchlicky_lc <- tolower(hv_vrchlicky)
TTR = length(unique(hv_vrchlicky_lc))/hv_vrchlicky_len
TTR

# vytvoreni abecedniho slovniku
hv_vrchlicky_dict = unique(hv_vrchlicky_lc)
hv_vrchlicky_dict = sort(unique(hv_vrchlicky_lc))
hv_vrchlicky_dict

# Jaccardova vzdalenost mezi preklady
# prunik a sjednoceni
b
d

intersect(b,d)
union(b,d)

# Jaccarduv index mezi slovnikem Nezvala a Vrchlickeho
hv_nezval <- scan(file=file.choose(), what="char", sep="", encoding="UTF-8")
hv_pokorny <- scan(file=file.choose(), what="char", sep="", encoding="UTF-8")

gsub("\\W", "", hv_nezval)
gsub("\\W", "", hv_pokorny)

hv_nezval<-gsub("\\,|\\.|\\;|\\:|\\!|\\?|“|„|-|\\(|\\)|—|‚|‘|_|'|\\”|\\/|\\’
                  |\\[|\\]|\\<|\\>", "", hv_nezval)
hv_pokorny<-gsub("\\,|\\.|\\;|\\:|\\!|\\?|“|„|-|\\(|\\)|—|‚|‘|_|'|\\”|\\/|\\’
                  |\\[|\\]|\\<|\\>", "", hv_pokorny)

# zmensi na mala pismena a odstran mezery
hv_nezval_lc<-tolower(hv_nezval[hv_nezval != ""])
hv_pokorny_lc<-tolower(hv_pokorny[hv_pokorny != ""])

# Jaccard - delka pruniku jedinecnych slov u Nezvala a u Vrchlickeho vydelena
# delkou sjednoceni unikatnich slov u Nezvala a Vrchlickeho
jd_vn = length(intersect(unique(hv_nezval_lc), unique(hv_vrchlicky_lc)))/length(union(unique(hv_nezval_lc), unique(hv_vrchlicky_lc)))
jd_vp = length(intersect(unique(hv_pokorny_lc), unique(hv_vrchlicky_lc)))/length(union(unique(hv_pokorny_lc), unique(hv_vrchlicky_lc)))
jd_np = length(intersect(unique(hv_nezval_lc), unique(hv_pokorny_lc)))/length(union(unique(hv_nezval_lc), unique(hv_pokorny_lc)))

jd_vn
jd_vp
jd_np

# vektor se vsemi delkami
havran_lens = c(length(hv_vrchlicky_lc), length(hv_nezval_lc), length(hv_pokorny_lc))
# pojmenovani polozek vektoru
names(havran_lens) = c("Vrchlicky", "Nezval", "Pokorny")
names(havran_lens)
havran_lens

havran_lens["Nezval"]
havran_lens["Pokorny"]

# usporadame od nejkratsi po nejdelsi
sort(havran_lens, decreasing=FALSE)

# vyhledani nejmensi/nejvetsi hodnoty /jmena polozky vektoru
max(havran_lens)
min(havran_lens)

min(names(havran_lens)) # nevrati nejkratsi text, ale nejkratsi jmeno
names(which.min(havran_lens))

# UKOL: vypocitejte procentualni hodnoty delek kratsich textu vzhledem k nejdelsimu textu
# napoveda: jednotlive hodnoty muzeme upravovat primo ve vektoru
f = c(1,2,3)
ff = 2*f
ff

nezval_perc = havran_lens["Nezval"]/havran_lens["Vrchlicky"]*100
pokorny_perc = havran_lens["Pokorny"]/havran_lens["Vrchlicky"]*100
nezval_perc
pokorny_perc

havran_lens/max(havran_lens)*100

which(havran_lens == max(havran_lens))

# vyhledavani v textu
jmena=c("Jan", "Jana", "Tom", "Petra", "Tom")
jmena=="Tom"

# cykly a podminky
for (slovo in jmena) {print(slovo)}

if (5 > 3) {print("Je to tak")
} else (print("Neni to tak"))

if (5 == 3) {print("Je to tak")
} else {print("Neni to tak")}

slovo = "Jana"
if (slovo %in% jmena)
{print(paste("Je tam", slovo))
  } else
  {print(paste("Neni tam", slovo))}

# delky slov
for (slovo in jmena)
{print(nchar(slovo))}

word_len = c()
for (slovo in jmena)
{word_len = append(word_len, nchar(slovo))
print(slovo)}
word_len

# UKOL: Z hv_vrchlicky vypiste slova, ktera maji jen jedno pismeno,
# udelejte jejich seznam, tj, kazde jen jednou
vrchlicky_len1 = c()
for (slovo in hv_vrchlicky)
{if (nchar(slovo) == 1) {vrchlicky_len1 = append(vrchlicky_len1, slovo)}}
unique(vrchlicky_len1)

# length = pocet polozek ve vektoru
# nchar = pocet pismen ve slove
# WTFFFFF

# pocet hledaneho vyrazu v textu
length(jmena[jmena=="Tom"])

length(hv_vrchlicky_lc[hv_vrchlicky_lc == "havran"])
length(hv_nezval_lc[hv_nezval_lc == "havran"])
length(hv_pokorny_lc[hv_pokorny_lc == "havran"])

# vytvoreni frekvencniho slovniku
table(hv_vrchlicky_lc)

f_slovnik_vrch = sort(table(hv_vrchlicky_lc), decreasing=TRUE)
f_slovnik_vrch
f_slovnik_nez = sort(table(hv_nezval_lc), decreasing=TRUE)
f_slovnik_pok = sort(table(hv_pokorny_lc), decreasing=TRUE)

f_slovnik_vrch_df = data.frame(f_slovnik_vrch)
f_slovnik_vrch_df
f_slovnik_nez_df = data.frame(f_slovnik_nez)
f_slovnik_pok_df = data.frame(f_slovnik_pok)



# zapisem do tab
write.table(f_slovnik_vrch_df, "Documents/freq_slov_vrch.csv", fileEncoding = "UTF-8")

vysledky = f_slovnik_vrch_df

# pokud chceme pridat novy sloupec, pouzivame cbind
# ale pokud je jiny pocet radku, musime pouzit merge
# by = 0 rika, ze se to ma zapisovat do radku vedle
vysledky = merge(vysledky, f_slovnik_nez_df, by = 0, all = TRUE, sort = FALSE)
vysledky = merge(vysledky, f_slovnik_pok_df, by = 0, all = TRUE, sort = FALSE)
vysledky

write.table(f_slovnik_vrch_df, "Documents/freq_slov_vrch.csv", fileEncoding = "UTF-8")

# Relativni frekvence
rel_freq_vrch = sort((table(hv_vrchlicky_lc)/length(hv_vrchlicky_lc))*100, decreasing = TRUE)
rel_freq_vrch
rel_freq_vrch = data.frame(rel_freq_vrch)

# delky slov
delky_slov_vrch = nchar(hv_vrchlicky_lc)
delky_slov_vrch
delky_slov_nez = nchar(hv_nezval_lc)
delky_slov_pok = nchar(hv_pokorny_lc)
max(delky_slov_vrch)
mean(delky_slov_vrch)
sd(delky_slov_vrch) # prumerny rozdil hodnot od prumeru, dal se odmocni, smerodatna odchylka
median(delky_slov_vrch) # neni ovlivnen extremy
table(delky_slov_vrch)
# modus
names(which.max(table(delky_slov_vrch)))

# obrazky
table(delky_slov_vrch)
plot(table(delky_slov_vrch))
barplot(table(delky_slov_vrch))
barplot(table(delky_slov_vrch), ylim = c(0,200), xlim = c(0,11))
barplot(table(delky_slov_vrch), ylim = c(0,200), xlim = c(0,11), xlab = "delky slov", ylab = "frekvence slov", 
        main = "distribuce delek slov")
barplot(table(delky_slov_vrch), ylim = c(0,200), xlim = c(0,11), xlab = "delky slov", ylab = "frekvence slov", 
        main = "distribuce delek slov", col = "#917FB3" )
barplot(table(delky_slov_vrch), ylim = c(0,200), xlim = c(0,11), xlab = "delky slov", ylab = "frekvence slov", 
        main = "distribuce delek slov", col = c("#2A2F4F", "#917FB3"))
barplot(table(delky_slov_vrch), ylim = c(0,200), xlim = c(0,11), xlab = "delky slov", ylab = "frekvence slov", 
        main = "distribuce delek slov", col = rainbow(11))

prum_delky_slov_vrch = mean(nchar(hv_vrchlicky_lc))
prum_delky_slov_nez = mean(nchar(hv_nezval_lc))
prum_delky_slov_pok = mean(nchar(hv_pokorny_lc))

prum_delky_slov = c(prum_delky_slov_vrch, prum_delky_slov_nez, prum_delky_slov_pok)

barplot(prum_delky_slov, xlim = c(0,4), ylim = c(0,5), xlab = "preklady", ylab = "prumerna delka slova", 
        main = "prumerne delky slov", col = "#FDE2F3", names.arg = c("Vrchlicky", "Nezval", "Pokorny"))

# boxplot
boxplot(delky_slov_vrch, ylab="delky slov", col = "#E5BEEC")
points(mean(delky_slov_vrch), col = "#2A2F4F")

# Pamatuje si nastaveni u obrazku z predchozich, pokud chci resetovat nastaveni:
dev.off()

# multigraf
data = list(delky_slov_vrch, delky_slov_nez, delky_slov_pok)
prumery = c(mean(delky_slov_vrch), mean(delky_slov_nez), mean(delky_slov_pok))
boxplot(data, ylab = "delky slov", names = c("Vrchlicky", "Nezval", "Pokorny"))
points(prumery, col = "red")

# popularni pro obrazky ggplot

# statisticke testovani rozdilu delek slov
# hypoteza: prumerna delka slova textu zaka 5. tridy bude mensi nez zaka 9. tridy
patak <- scan(file=file.choose(), what="char", sep="", encoding="UTF-8")
devatak <- scan(file=file.choose(), what="char", sep="", encoding="UTF-8")

patak<-gsub("\\,|\\.|\\;|\\:|\\!|\\?|“|„|-|\\(|\\)|—|‚|‘|_|'|\\”|\\/|\\’
                  |\\[|\\]|\\<|\\>", "", patak)
devatak<-gsub("\\,|\\.|\\;|\\:|\\!|\\?|“|„|-|\\(|\\)|—|‚|‘|_|'|\\”|\\/|\\’
                  |\\[|\\]|\\<|\\>", "", devatak)
patak_lc<-tolower(hv_nezval[hv_nezval != ""])
devatak_lc<-tolower(hv_pokorny[hv_pokorny != ""])

# UKOL: a) vytvorte vektory, v nichz budou delky slov u kazdeho textu
#       b) zjistete prumer, median a sd
patak_delky = nchar(patak_lc)
devatak_delky = nchar(devatak_lc)

mean(patak_delky)
mean(devatak_delky)
median(patak_delky)
median(devatak_delky)
sd(patak_delky)
sd(devatak_delky)

# empiricky testovatelna hypoteza - vztah mezi dvema promennymi
# s jakou pravdepodobnosti zamitame nulovou hypotezu, ackoliv plati?
# normalni rozdeleni
# testujeme pomoci Shapiro-Wilk test
# testujeme platnost H0, podle niz jsou data normalne rozdelena
norm <- c(rnorm(300, mean = 100, sd = 10))
round(norm, digit=2)
hist(norm)
plot(density(norm))

qqnorm(norm)
qqline(norm)

qqnorm(patak_delky)
qqline(patak_delky)

shapiro.test(patak_delky) # vysoce signifikantni, ze data normalne rozlozena nejsou
shapiro.test(devatak_delky)

# test delek
wilcox.test(patak_delky, devatak_delky) # NEsmime tam dat prumery!! potrebuje vsechna data

# korelace - je mezi velicinami nejaky vztah?
# vztah frekvence a delky slov
frek_delek = as.vector(table(delky_slov_nez))
delky = as.numeric(names(table(delky_slov_nez))) #numericky vektor

plot(delky, frek_delek)
abline(lm(frek_delek ~ delky))

# muzeme testovat, nejprve opet normalita
shapiro.test(frek_delek)
shapiro.test(delky)

# Pearsonuv korelacni koeficient
cor.test(frek_delek, delky, method = "pearson") # velmi silna zaporna korelace, p < 0.05

# neparametricke alternativy
cor.test(frek_delek, delky, method = "kendall")
cor.test(frek_delek, delky, method = "spearman")

# data frame
t=c(1:10)
u=c(101:110)
v=c(2,5,6,9,13,16,20,21,22,15)
df = data.frame(t,u,v)
df
df$t
max(df)
max(df$t)
sum(df$u)
df$t[4]
df$t[4:6]
# vyber jednotlivych bunek
df[1,1]
df[1,3]
# radky
df[3,1:3] # treti radek, 1. - 3. sloupec

plot(df$v)
plot(df$v, df$u)
n=c(df$t, df$u)
cor.test(df$t, df$v, method="kendall")

# nacteni tabulky ze souboru
data<-read.table(file=file.choose(), header = TRUE, sep="\t")
head(data)

data$Tokens

# sledujme vztah mezi delkou textu a proporci hapax legomen
plot(data$Tokens, data$hapax_perc)