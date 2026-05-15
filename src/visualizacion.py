"""
visualizacion.py - Mapa del Metro de Medellin en PNG.
Usa backend Agg, compatible con Codespaces sin display.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

POSICIONES = {
    "Niquia":(5,20),"Bello":(5,18),"Madera":(5,16),"Acevedo":(5,14),
    "Tricentenario":(5,12),"Caribe":(5,10),"Universidad":(5,8),"Hospital":(5,6),
    "Prado":(5,4),"Parque Berrio":(5,2),"San Antonio":(5,0),"Alpujarra":(5,-2),
    "Exposiciones":(5,-4),"Industriales":(5,-6),"Poblado":(5,-8),"Aguacatala":(5,-10),
    "Ayura":(5,-12),"Envigado":(5,-14),"Itagui":(5,-16),"La Estrella":(5,-18),
    "Suramericana":(3,0),"Estadio":(1,0),"Floresta":(-1,0),"Santa Lucia":(-3,0),
    "Trinidad":(-5,0),"San Javier":(-7,0),
    "Andalucia":(7,14),"Popular":(9,14),"Santo Domingo":(11,14),
    "Juan XXIII":(-9,2),"Vallejuelos":(-11,4),
    "Cisneros":(7,-6),"Oriente":(9,-7),"Miraflores":(11,-7.5),
    "Alejandro Echavarria":(13,-8),"Bicentenario":(15,-8.5),"Buenos Aires":(17,-9),
}

COLORES = {"A":"#00A651","B":"#F7941D","K":"#29ABE2","J":"#EC008C","T-A":"#8B4513"}

LINEAS = {
    "A":["Niquia","Bello","Madera","Acevedo","Tricentenario","Caribe","Universidad",
         "Hospital","Prado","Parque Berrio","San Antonio","Alpujarra","Exposiciones",
         "Industriales","Poblado","Aguacatala","Ayura","Envigado","Itagui","La Estrella"],
    "B":["San Antonio","Suramericana","Estadio","Floresta","Santa Lucia","Trinidad","San Javier"],
    "K":["Acevedo","Andalucia","Popular","Santo Domingo"],
    "J":["San Javier","Juan XXIII","Vallejuelos"],
    "T-A":["Industriales","Cisneros","Oriente","Miraflores","Alejandro Echavarria","Bicentenario","Buenos Aires"],
}

TRANSBORDOS = {"San Antonio","Acevedo","Industriales","San Javier"}

def dibujar_mapa(ruta_resaltada=None, nombre_archivo="docs/mapa_metro.png", titulo="Metro de Medellin"):
    fig, ax = plt.subplots(figsize=(18,26))
    ax.set_facecolor("#1a1a2e")
    fig.patch.set_facecolor("#1a1a2e")
    for linea, estaciones in LINEAS.items():
        color = COLORES[linea]
        for i in range(len(estaciones)-1):
            e1,e2 = estaciones[i],estaciones[i+1]
            if e1 in POSICIONES and e2 in POSICIONES:
                x1,y1 = POSICIONES[e1]
                x2,y2 = POSICIONES[e2]
                ax.plot([x1,x2],[y1,y2],color=color,linewidth=3,zorder=1)
    if ruta_resaltada and len(ruta_resaltada)>1:
        for i in range(len(ruta_resaltada)-1):
            e1,e2 = ruta_resaltada[i],ruta_resaltada[i+1]
            if e1 in POSICIONES and e2 in POSICIONES:
                x1,y1 = POSICIONES[e1]
                x2,y2 = POSICIONES[e2]
                ax.plot([x1,x2],[y1,y2],color="yellow",linewidth=6,zorder=2,alpha=0.8,linestyle="--")
    for estacion,(x,y) in POSICIONES.items():
        if estacion in TRANSBORDOS:
            ax.plot(x,y,'o',color="white",markersize=12,zorder=4)
            ax.plot(x,y,'o',color="#FFD700",markersize=8,zorder=5)
        else:
            ax.plot(x,y,'o',color="white",markersize=6,zorder=4)
        if ruta_resaltada and estacion in ruta_resaltada:
            ax.plot(x,y,'o',color="yellow",markersize=10,zorder=6)
        ax.annotate(estacion,(x,y),textcoords="offset points",xytext=(6,3),fontsize=7,color="white",zorder=7)
    leyenda = [mpatches.Patch(color=c,label=f"Linea {l}") for l,c in COLORES.items()]
    if ruta_resaltada:
        leyenda.append(mpatches.Patch(color="yellow",label="Ruta calculada"))
    ax.legend(handles=leyenda,loc="upper right",facecolor="#2d2d2d",labelcolor="white",fontsize=9)
    ax.set_title(titulo,color="white",fontsize=14,pad=15)
    ax.axis("off")
    plt.tight_layout()
    plt.savefig(nombre_archivo,dpi=150,bbox_inches="tight",facecolor=fig.get_facecolor())
    plt.close()
    print(f"Mapa guardado en: {nombre_archivo}")

if __name__ == "__main__":
    dibujar_mapa(nombre_archivo="docs/mapa_metro.png")
    dibujar_mapa(
        ruta_resaltada=["Niquia","Bello","Madera","Acevedo","Andalucia","Popular","Santo Domingo"],
        nombre_archivo="docs/mapa_ruta_ejemplo.png",
        titulo="Ruta: Niquia -> Santo Domingo"
    )
