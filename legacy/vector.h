/*Libreria Calculo Vectorial 1.0
*/
#ifndef _VECTOR
#define _VECTOR

#include <stdio.h>
#include <math.h>

struct vector{
    double x, y, z;
};

void mostrar_vector(struct vector v);
struct vector kesc_vector(double k, struct vector v);
struct vector sumar_vector(struct vector v, struct vector u);
struct vector dist_vector(struct vector v, struct vector u);
double p_punto(struct vector v, struct vector u);
double vabs(struct vector v);
struct vector norm_vector(struct vector v);



void mostrar_vector(struct vector v){
    printf("<%.2lfi + %.2lfj + %.2lfk>\n", v.x, v.y, v.z);
}

struct vector kesc_vector(double k, struct vector v){			// Escalar vector por k
    struct vector vr = {k*v.x, k*v.y, k*v.z};
    return vr;
}

struct vector sumar_vector(struct vector v, struct vector u){
	struct vector vr = {v.x+u.x, v.y+u.y, v.z+u.z};
	return vr;
}

struct vector dist_vector(struct vector v, struct vector u){
	struct vector vr = {u.x-v.x, u.y-v.y, u.z-v.z};
	return vr;
}

double p_punto(struct vector v, struct vector u){			// Producto punto v*u
    double r;
    return r = (v.x*u.x + v.y*u.y + v.z*u.z);
}

double vabs(struct vector v){
	return sqrt(pow(v.x,2) + pow(v.y,2) + pow(v.z,2));
}

struct vector norm_vector(struct vector v){
	struct vector vr = {v.x/vabs(v), v.y/vabs(v), v.z/vabs(v)};
	return vr;
}
#endif
