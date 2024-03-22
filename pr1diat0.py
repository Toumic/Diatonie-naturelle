# -*- coding: utf-8 -*-

# Développement diatonique élémentaire
# Version 1 : Calculer les modulations majeures
# pr0diat zéro

gnat = ['C','D','E','F','G','A','B']    # Notes diatoniques
gmaj = [1,1,0,1,1,1,0]                  # Formule majeure
gdeg = [0,1,2,3,4,5,6]                  # Degrés modal
nordiese = [' ','+','x','^','+^','x^']      # Altérations augmentées
subemol = [' ','°*','-*','*','°','-']       # Altérations diminuées
deg = 0
while deg < 7 :             # Lecture diatonique tonale de "gdeg"
    # Une tournée produit une tonalité modale de 7 notes
    nat = gdeg[deg]         # Degré tonal en question
    cri = gimj = gmod = maj = 0
    #
    while maj < 7 :   # Tonalité modale du degré
        #
        gmj = gmaj[maj]     # Forme majeure
        imaj = gmaj[nat]    # Forme modale
        gnt = gnat[nat]     # Forme tonale
        #print ("gmj,imaj,gnt ",gmj,imaj,gnt)
        cri = cri + gimj    # Tonalité cumulée
        gimj = imaj - gmj   # Calcul tonal PAS/PAS
        #print ("gimj,cri,gnt ",gimj,cri,gnt)
        cmod = gmod = cri
        #print ("gmod ",gmod,gnt)
        if gmod > 0 :
            imod = nordiese[cmod]
            #print ("imod+cmod",imod,cmod,gnt)
        if gmod < 0 :
            imod = subemol[cmod]
            #print ("imod-cmod",imod,cmod,gnt)
        if gmod == 0 :
            imod = subemol[cmod]
            #print ("imod,cmod ",imod,cmod,gnt)
        gmod = gmod + cri   # Transition tonale
        nat = nat + 1
        if nat > 6 : nat = 0
        maj = maj + 1 
        print ("imod,maj,gnt ",imod,maj,gnt)
        #
    print ("___",deg)
    deg = deg + 1
