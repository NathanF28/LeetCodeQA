class Solution:
    def capitalizeTitle(self, title: str) -> str:
        liste = title.split(" ")
        for i in range(len(liste)):
            liste[i] = liste[i].lower()
            if len(liste[i]) > 2:
                liste[i] = liste[i][0].upper() + liste[i][1:]
        return " ".join(liste)        
        