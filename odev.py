import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#Girdilerin ve çıktıların tanımlanması
miktar=ctrl.Antecedent(np.arange(0,101,1),"miktar")
kirlilik=ctrl.Antecedent(np.arange(0,101,1),"kirlilik")
cins=ctrl.Consequent(np.arange(0,101,1),"cins")
yikamaZamani=ctrl.Consequent(np.arange(30,160,10),"yikamaZamani")
deterjanMiktari=ctrl.Consequent(np.arange(0,100,2.5),"deterjanMiktari")
suSicakligi=ctrl.Consequent(np.arange(35,72.5,2.5),"suSicakligi")
ustSepetPompaDevri=ctrl.Consequent(np.arange(2100,3500,100),"ustSepetPompaDevri")
altSepetPompaDevri=ctrl.Consequent(np.arange(2100,3500,100),"altSepetPompaDevri")

#Çıktı değerleri için üyelik fonksiyonlarının belirlenmesi (elle)

miktar["az"]=fuzz.trimf(miktar.universe,[0,0,35])
miktar["orta"]=fuzz.trimf(miktar.universe,[15,50,85])
miktar["cok"]=fuzz.trimf(miktar.universe,[65,100,100])

kirlilik["azKirli"]=fuzz.trimf(kirlilik.universe,[0,0,35])
kirlilik["ortaKirli"]=fuzz.trimf(kirlilik.universe,[15,50,85])
kirlilik["cokKirli"]=fuzz.trimf(kirlilik.universe,[65,100,100])

cins["hassas"]=fuzz.trimf(cins.universe,[0,0,35])
cins["karma"]=fuzz.trimf(cins.universe,[15,50,85])
cins["guclu"]=fuzz.trimf(cins.universe,[65,100,100])

yikamaZamani["cokKisa"]=fuzz.trimf(yikamaZamani.universe,[30,30,60])
yikamaZamani["kisa"]=fuzz.trimf(yikamaZamani.universe,[40,65,90])
yikamaZamani["orta"]=fuzz.trimf(yikamaZamani.universe,[70,95,120])
yikamaZamani["uzun"]=fuzz.trimf(yikamaZamani.universe,[100,125,150])
yikamaZamani["cokUzun"]=fuzz.trimf(yikamaZamani.universe,[130,160,160])

deterjanMiktari["cokAz"]=fuzz.trimf(deterjanMiktari.universe,[0,0,17.5])
deterjanMiktari["az"]=fuzz.trimf(deterjanMiktari.universe,[17.5,30,42.5])
deterjanMiktari["normal"]=fuzz.trimf(deterjanMiktari.universe,[32.5,50,67.5])
deterjanMiktari["cok"]=fuzz.trimf(deterjanMiktari.universe,[57.5,75,92.5])
deterjanMiktari["cokFazla"]=fuzz.trimf(deterjanMiktari.universe,[82.5,92.5,92.5])

suSicakligi["dusuk"]=fuzz.trimf(suSicakligi.universe,[35,35,50])
suSicakligi["normal"]=fuzz.trimf(suSicakligi.universe,[37.5,50,67.5])
suSicakligi["yuksek"]=fuzz.trimf(suSicakligi.universe,[55,72.5,72.5])

ustSepetPompaDevri["cokDusuk"]=fuzz.trimf(ustSepetPompaDevri.universe,[2100,2100,2400])
ustSepetPompaDevri["dusuk"]=fuzz.trimf(ustSepetPompaDevri.universe,[2300,2500,2700])
ustSepetPompaDevri["orta"]=fuzz.trimf(ustSepetPompaDevri.universe,[2600,2800,3000])
ustSepetPompaDevri["yuksek"]=fuzz.trimf(ustSepetPompaDevri.universe,[2900,3100,3300])
ustSepetPompaDevri["cokYuksek"]=fuzz.trimf(ustSepetPompaDevri.universe,[3200,3500,3500])

altSepetPompaDevri["cokDusuk"]=fuzz.trimf(altSepetPompaDevri.universe,[2100,2100,2400])
altSepetPompaDevri["dusuk"]=fuzz.trimf(altSepetPompaDevri.universe,[2300,2500,2700])
altSepetPompaDevri["orta"]=fuzz.trimf(altSepetPompaDevri.universe,[2600,2800,3000])
altSepetPompaDevri["yuksek"]=fuzz.trimf(altSepetPompaDevri.universe,[2900,3100,3300])
altSepetPompaDevri["cokYuksek"]=fuzz.trimf(altSepetPompaDevri.universe,[3200,3500,3500])

miktar.view()
kirlilik.view()
cins.view()
#bulanık kuralların belirlenmesi
kural1=ctrl.Rule(miktar["az"] | kirlilik["azKirli"] | cins["hassas"],yikamaZamani["cokKisa"])
kural2=ctrl.Rule(miktar["az"] | kirlilik["azKirli"] | cins["hassas"],deterjanMiktari["cokAz"])
kural3=ctrl.Rule(miktar["az"] | kirlilik["azKirli"] | cins["hassas"],suSicakligi["dusuk"])
kural4=ctrl.Rule(miktar["az"] | kirlilik["azKirli"] | cins["hassas"],ustSepetPompaDevri["cokDusuk"])
kural5=ctrl.Rule(miktar["az"] | kirlilik["azKirli"] | cins["hassas"],altSepetPompaDevri["cokDusuk"])

kural6=ctrl.Rule(miktar["az"] | kirlilik["cokKirli"] | cins["karma"],yikamaZamani["orta"])
kural7=ctrl.Rule(miktar["az"] | kirlilik["cokKirli"] | cins["karma"],deterjanMiktari["normal"])
kural8=ctrl.Rule(miktar["az"] | kirlilik["cokKirli"] | cins["karma"],suSicakligi["yuksek"])
kural9=ctrl.Rule(miktar["az"] | kirlilik["cokKirli"] | cins["karma"],ustSepetPompaDevri["dusuk"])
kural10=ctrl.Rule(miktar["az"] | kirlilik["cokKirli"] | cins["karma"],altSepetPompaDevri["cokYuksek"])

kural11=ctrl.Rule(miktar["orta"] | kirlilik["ortaKirli"] | cins["guclu"],yikamaZamani["orta"])                
kural12=ctrl.Rule(miktar["orta"] | kirlilik["ortaKirli"] | cins["guclu"],deterjanMiktari["normal"])
kural13=ctrl.Rule(miktar["orta"] | kirlilik["ortaKirli"] | cins["guclu"],suSicakligi["normal"])
kural14=ctrl.Rule(miktar["orta"] | kirlilik["ortaKirli"] | cins["guclu"],ustSepetPompaDevri["yuksek"])
kural15=ctrl.Rule(miktar["orta"] | kirlilik["ortaKirli"] | cins["guclu"],ustSepetPompaDevri["yuksek"])

kural16=ctrl.Rule(miktar["cok"] | kirlilik["cokKirli"] | cins["karma"],yikamaZamani["cokUzun"])
kural17=ctrl.Rule(miktar["cok"] | kirlilik["cokKirli"] | cins["karma"],deterjanMiktari["cokFazla"])
kural18=ctrl.Rule(miktar["cok"] | kirlilik["cokKirli"] | cins["karma"],suSicakligi["yuksek"])
kural19=ctrl.Rule(miktar["cok"] | kirlilik["cokKirli"] | cins["karma"],ustSepetPompaDevri["dusuk"])
kural20=ctrl.Rule(miktar["cok"] | kirlilik["cokKirli"] | cins["karma"],ustSepetPompaDevri["cokYuksek"])
#kuralların sonucunun belirlenmesi
kontrol=ctrl.ControlSystem([kural1,kural2,kural3,kural4,kural5,kural6,kural7,kural8,kural9,kural10,kural11,kural12,kural13,kural14,kural15,kural16,kural17,kural18,kural19,kural20])
kontrolbelirleme=ctrl.ControlSystemSimulation(kontrol)

#sonucun hesaplanması
kontrolbelirleme.input["miktar"]=90
kontrolbelirleme.input["kirlilik"]=98
kontrolbelirleme.input["cins"]=62
kontrolbelirleme.compute()
print(kontrolbelirleme.output[["yikamaZamani"],["deterjanMiktari"],["suSicakligi"],["ustSepetPompaDevri"],["altSepetPompaDevri"]])

#sonucun görsel oalrak gösterilmesi
yikamaZamani.view(sim=kontrolbelirleme)
deterjanMiktari.view(sim=kontrolbelirleme)
suSicakligi.view(sim=kontrolbelirleme)
ustSepetPompaDevri.view(sim=kontrolbelirleme)
altSepetPompaDevri.view(sim=kontrolbelirleme)
