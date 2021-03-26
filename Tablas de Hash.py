Public interface Hasheable
{
	Public long hash();
}

Public class NodoHash<T extends Hasheable >{
	T elem;
	NodoHash<T> sig;
}



Public class TablaHash<T extends Haseable> {
	NodoHash<T> [] tabla;
	Int cont=0;
	Int Factor_de_carga; //regla de dedo es 70%

	TablaHash(){
		tabla=(T []) new Object[2];
		cont=0;
		Factor_de_carga= 2*0.7;

	}

	Private void expande()
{
	NodoHash<T> [] nuevaTabla= new NodoHash<T>[tabla.length*2] ;
	for(int i=0; i<tabla.length; i++){
		actual=tabla[i].getSig();
		while(actual!=null){
			pos=actual.getElem().hash()%nuevaTabla.length;
			if(nuevaTabla[pos]==null) //sentinela
				nuevaTabla[pos]=new NodoHash();
			nuevo=new NodoHash(actual.getElem());
			nuevo.setSig(nuevaTabla[pos].getSig());
			nuevaTabla[pos].setSig(nuevo);
			}
	}
	
	tabla=nuevaTabla;

}
Public void insert(T elem){
		If (cont+1 > factor_de_carga)
			expande();
int posicion = elem.hash() % tabla.length;
		NodoHash<T> nuevo = new NodoHash<T>(elem);
		if (tabla[posicion] == null)
			tabla[posicion] = new NodoHash<T>(null);

		NodoHash<T> actual = tabla[posicion];
		nuevo.setSig(actual.getSig());
		actual.setSig(nuevo);
cont++;
	}

} 	

Public T borra(T elem){
pos=elem.hash()%tabla.length;
NodoHash<T> actual = tabla[posicion];
If (tabla[posicion]==null)
	return null; //o lanzar exception. Por si no teníamos centinela
while(actual.getSig() != null && !actual.getSig().getElem().equals(elem))
	actual=actual.getSig();
if(actual.getSig()==null)
	return null;
cont--;
NodoHash<T> res=actual.getSig();
actual.SetSig(res.getSig());
return res.getElem();
//<3
}
