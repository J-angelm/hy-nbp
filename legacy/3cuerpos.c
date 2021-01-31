#include <stdio.h>
#include <math.h>
#include <time.h>
#include "vector.h"

#define clear() printf("\033[H\033[J")

#define GS (6.67408E-11*1.988E30)						//Constante G por masa del sol
#define GT (6.67408E-11*5.9722E24)						//Constante G por masa de la tierra
#define GL (6.67408E-11*7.3476E22)						//Constante G por masa de la luna
#define h 0.1

double dy2(double t, double y, double y1);
struct vector aS(struct vector rST, struct vector rSL);
struct vector aT(struct vector rTS, struct vector rTL);
struct vector aL(struct vector rLS, struct vector rLT);
void solveEq(struct vector rS, struct vector rT, struct vector rL, struct vector vS, struct vector vT, struct vector vL);

int main(int argc, char **argv){
	printf("\tProblema de los 3 cuerpos\n\n");
	struct vector rS = {0, 0, 0};						//Vector de posicion del sol
	struct vector rT = {0, 1.5E11, 0};					//Vector de posicion de la tierra
	struct vector rL = {0, 1.50383E11, 3.449E7};			//Vector de posicion de la luna

	struct vector vS = {0, 0, 0};						//Vector de velocidad tangencial del sol
	struct vector vT = {-3E4, 0, 0};					//Vector de velocidad tangencial de la tierra
	struct vector vL = {-31020.62, 0, -91.81};			//Vector de velocidad tangencial de la luna
	solveEq(rS, rT, rL, vS, vT, vL);
	return 0;
}

struct vector aS(struct vector rST, struct vector rSL){		//Aceleracion del sol debido a la tierra y la luna
	struct vector ar = sumar_vector(kesc_vector(GT/pow(vabs(rST),2), norm_vector(rST)), kesc_vector(GL/pow(vabs(rSL),2), norm_vector(rSL)));
	return ar;
}

struct vector aT(struct vector rTS, struct vector rTL){		//Aceleracion de la tierra debido al sol y la luna
	struct vector ar = sumar_vector(kesc_vector(GS/pow(vabs(rTS),2), norm_vector(rTS)), kesc_vector(GL/pow(vabs(rTL),2), norm_vector(rTL)));
	return ar;
}

struct vector aL(struct vector rLS, struct vector rLT){		//Aceleracion de la luna debido al sol y la tierra
	struct vector ar = sumar_vector(kesc_vector(GS/pow(vabs(rLS),2), norm_vector(rLS)), kesc_vector(GT/pow(vabs(rLT),2), norm_vector(rLT)));
	return ar;
}

void solveEq(struct vector rS, struct vector rT, struct vector rL, struct vector vS, struct vector vT, struct vector vL){
	clock_t tl, ts;
	int segundos = 0, c = 10000;
	ts = clock()+CLOCKS_PER_SEC;
	
	FILE *archivo;
	archivo = fopen("Problema 3 cuerpos.xlsx","w");
	int i = 0, dia = 0, hr = 0, min = 0;
	double t;
	struct vector as, at, al, rST, rSL, rTS, rTL, rLS, rLT;
	for(t=0; t <= 3.1536E7; t+=h){
		if((ceil(t)/60) && (floor(t)/60) == i){
			min++;
			if((min/60) == 1){
				hr++;
				if((hr/24) == 1){
					dia++;
					hr = 0;
				}
				min = 0;
			}
			i++;
		}
		rST = dist_vector(rS, rT);				//Vector distancia entre sol y tierra
		rSL = dist_vector(rS, rL);				//Vector distancia entre sol y luna
		rTS = dist_vector(rT, rS);				//Vector distancia entre tierra y sol
		rTL = dist_vector(rT, rL);				//Vector distancia entre tierra y luna
		rLS = dist_vector(rL, rS);				//Vector distancia entre luna y sol
		rLT = dist_vector(rL, rT);				//Vector distancia entre luna y tierra
		as = aS(rST, rSL);
		at = aT(rTS, rTL);
		al = aL(rLS, rLT);
		int d = t;
		if((t == 0) || (d%c == 0) || (t == 3.1536E7)){
		      fprintf(archivo, "%lf \t %lf \t %lf \t %lf  \t %lf  \t %lf  \t %lf  \t %lf  \t %lf  \t %lf\n", t, rS.x, rS.y, rS.z, rT.x, rT.y, rT.z, rL.x, rL.y, rL.z);
		      c+10000;
		}
		if((tl=clock()) >= ts){
      		segundos++;
      		if(segundos%5 == 0){
      			clear();
      			printf("Tiempo total transcurrido %d dias %d horas %d minutos\n", dia, hr, min);
				printf("Posicion del Sol:"); mostrar_vector(rS); printf("Posicion de la Tierra:"); mostrar_vector(rT); printf("Posicion de la Luna:"); mostrar_vector(rL);
				printf("Velocidad del Sol:"); mostrar_vector(vS); printf("Velocidad de la Tierra:"); mostrar_vector(vT); printf("Velocidad de la Luna:"); mostrar_vector(vL);
		      }
		      ts = tl+CLOCKS_PER_SEC;
		}
		rS = sumar_vector(rS, kesc_vector(h, vS));			//Actualizacion de vectores de velocidad y posicion
		vS = sumar_vector(vS, kesc_vector(h, as));
		rT = sumar_vector(rT, kesc_vector(h, vT));
		vT = sumar_vector(vT, kesc_vector(h, at));
		rL = sumar_vector(rL, kesc_vector(h, vL));
		vL = sumar_vector(vL, kesc_vector(h, al));
	}
	fclose(archivo);
}
