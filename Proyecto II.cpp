//Codigo del programa en c++
//Realizar una base de datos utilizando archivos.
//Al abrir el programa debe mostrar un menú con las siguientes opciones:Agregar producto, Buscar a un producto Modificar los datos de un producto
//Siguiendo ciertas restricciones que seran explicadas en la documentación externa.
//Aún asi en el menú principal del programa esta la opcción 4 la cual corresponde a dichas restrecciones.

//Comenzamos creando nuestra funcion princial la cual nos ayudara para abrir nuestro archivo con los productos.

#include <iostream>
#include <fstream>
#include <windows.h>
using namespace std;
int menu(){
	int x;//Creamos nuestra segunda funcion la cual consiste en guardar los datos en nuestro archivo
	system("cls");
	cout << "<<------Bienvenido------->>"<<endl<<endl;//Ahora creamos nuestra primera opciones del menu principal.
	cout << "1. Agregar Persona" << endl;
	cout << "2. Ver Personas" << endl;
	cout << "3. Buscar Personas" << endl;
	cout << "4. Modificar Personas" << endl;
	cout << "5. Salir " << endl;
	cout << "Opcion ";
	cin >> x;
	return x;
}

bool verifica(string ced){
	ifstream leer("Personas.txt", ios::in);
	string Nom;
	string Ced;
	float precio;
	string proveedor;
	int existencia;
	char estado;
	float descuento;
	leer >> Nom;
	while (!leer.eof()){
		leer>>Ced;
		leer>>precio;
		leer>>proveedor;
		leer>>existencia;
		leer>>estado;
		leer>>descuento;
		
		if(Ced == ced){
			cout << "¡¡¡Este codigo ya existe!!!";
			Sleep(1500);
			leer.close();
			return false;
		}
		leer>>Nom;
	}
	leer.close();
	return true;
}

void agregar (ofstream &es){
	system("cls");
	string Nom;
	string Ced;
	float precio;
	string proveedor;
	int existencia;
	char estado;
	float descuento;
	es.open("personas.txt", ios::out | ios::app);
	cout << "Nombre ";
	cin >> Nom;
	cout << "Codigo ";
	cin >> Ced;
	cout << "Precio ";
	cin >> precio;
	cout << "Proveedor ";
	cin >> proveedor;
	cout << "existencia ";
	cin >> existencia;
	cout << "Estado ";
	cin >> estado;
	cout << "Descuento ";
	cin >> descuento;
	if (verifica(Ced))
	es << Nom << " " << Ced << " " << precio << " " << proveedor << " " << existencia<< " " << estado << " " << descuento<< " " << "\n";
	es.close();
}

void verRegistros(ifstream &Lec){
	system("cls");
	string nom;
	string ced;
	float precio;
	string proveedor;
	int existencia;
	char estado;
	float descuento;
	Lec.open("Personas.txt", ios::in);
	cout<<"----Personas Registradas----"<< endl<<endl;
	Lec>>nom;
	while(!Lec.eof()){
		Lec>>ced;
		Lec>>precio;
		Lec>>proveedor;
		Lec>>existencia;
		Lec>>estado;
		Lec>>descuento;
		cout<<"Nombre------: "<<nom<<endl;
		cout<<"Codigo----: "<<ced<<endl;
		cout<<"Precio------: "<<precio<<endl;
		cout<<"Proveedor------: "<<proveedor<<endl;
		cout<<"Existencia----: "<<existencia<<endl;
		cout<<"Estado------: "<<estado<<endl;
		cout<<"Descuento------: "<<descuento<<endl;
		cout<<"--------------"<<endl;
		Lec>>nom;
	}
	Lec.close();
	system("pause");
}

void buscarPersona(ifstream &Lec){
	system("cls");
	Lec.open("Personas.txt", ios::in);
	string nom, ced, proveedor,cedaux;
	float precio,descuento;
	int existencia;
	char estado;
	bool encontrado = false;
	cout << "Digite el codigo: ";
	cin >> cedaux;
	Lec>>nom;
	while(!Lec.eof() && !encontrado){
		Lec>>ced;
        Lec>>precio;
		Lec>>proveedor;
		Lec>>existencia;
		Lec>>estado;
		Lec>>descuento;    
		if(ced == cedaux){
			cout << "Nombre-----: "<<nom<<endl;
			cout << "Codigo ----: "<<ced<<endl;
			cout << "Precio ----: "<<precio<<endl;
			cout << "Proveedor ----: "<<proveedor<<endl;
			cout << "Existencia ----: "<<existencia<<endl;
			cout << "Estado ----: "<<estado<<endl;
			cout << "Descuento ----: "<<descuento<<endl;
			cout << "----------------------"<<endl;
			encontrado = true;
		}
		Lec>>nom;
	}
	Lec.close();
	if(!encontrado)
	cout<<"Dato no encontrado"<<endl;
	system("pause");
}
void modificar(ifstream &Lec){
	system("cls");
	string nom;
	string ced;
	float precio;
	string proveedor;
	int existencia;
	char estado;
	float descuento;
	string cedaux;
	string nomaux;
	float precioux;
	string proveedorux;
	int existenciaux;
	char estadoux;
	float descuentoux;
	Lec.open("Personas.txt", ios::in);
	ofstream aux("auxiliar.txt", ios::out);
	if(Lec.is_open()){
		cout<<"Codigo ";
		cin>>cedaux;
		Lec>>nom;
		while(!Lec.eof()){
			Lec>>ced;
			Lec>>precio;
		Lec>>proveedor;
		Lec>>existencia;
		Lec>>estado;
		Lec>>descuento;   
			if(ced == cedaux){
				cout<<"Nuevo nombre ";
				cin>>nomaux;
				cout<<"Nuevo precio ";
				cin>>precioux;
				cout<<"Nuevo proveedor ";
				cin>>proveedorux;
				cout<<"Nueva existencia ";
				cin>>existenciaux;
				cout<<"Nuevo estado ";
				cin>>estadoux;
				cout<<"Nuevo descuento ";
				cin>>descuentoux;
				aux<<nomaux<<" "<<ced<< " " <<precioux << " " << proveedorux << " " <<existenciaux << " " <<estadoux << " " <<descuentoux << "\n";
			}else{
				aux<<nom<<" " <<ced<<"\n";
			}
			Lec>>nom;
			
		}
		Lec.close();
		aux.close();
	}else
	cout<<"Error"<<endl;
	remove("Personas.txt");
	rename("auxiliar.txt", "Personas.txt");
	
}
int main(){
	ofstream Esc;
	ifstream Lec;
	int op;
	do{
		system("cls");
		op = menu();
		switch(op){
			case 1: 
			    agregar(Esc);
			break;
			case 2:
				verRegistros(Lec);
			break;
			case 3:
				buscarPersona(Lec);
			break;
			case 4:
				modificar(Lec);
			break;
		}	
	} while(op != 4);
	
	return 0;
}



