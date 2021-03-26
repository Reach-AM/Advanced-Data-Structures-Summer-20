Public  class nodoSkip<T> {
	T elemento;
	nodoSkip<T> izq,der,arriba,abajo;
	….
	void setArriba(nodoSkip<T> nuevo){
		arriba=nuevo;
	}
	Void setAbajo(nodoSkip<T> nuevo){
		abajo=nuevo;
	}

}

Public class SkipList<T>{
	nodoSkip<T> cabeza,cola;
	Int cont;
	Int numlistas; //inicializado en 1
	
	Public boolean encuentra(T elem){
		nodoSkip<T> actual=busca(elem);
		If (actual.getElem().compareTo(elem)==0)
			Return True;
		Return False;
	}
		
	// Este método recibe un elemento y lo busca en la estructura de datos,
	// regresa el nodo de la lista de hasta abajo en donde se encuentra (si es
	//que se encuentra en la lista) o el nodo anterior si no se encuentra ahí
	private nodoSkip<T> busca(T elem){
		nodoSkip<T> actual=cabeza;
		Boolean termine=False;

		While (!termine){
while(actual.getDer().getElem()!=null 
         			&&actual.getDer().getElem().compareTo(elem)<=0)				actual=actual.getDer();
			If (actual.getAbajo()==null)
				termine=True;
			Else
actual=actual.getAbajo();
		}

		Return actual;

	}
  
####################################
############## Borrar ##############
####################################
  
Public void borra(T elem){
		nodoSkip<T> actual=busca(elem), ant, sig;
		If (actual.getElem().compareTo(elem)!=0)
			Return;
		while(actual!=null){
			ant=actual.getIzq();
			sig=actual.getDer();
			ant.setDer(sig);
			sig.setIzq(ant);
			actual=actual.getArriba();
		}
		//colapsar
		If (numlistas > floor(log(2+cont)/log(2)){
			cola=cola.getabajo();
			cabeza=cabeza.getabajo();
			actual=cabeza;
			While (actual!=null){
				actual.setArriba(null)
				actual=actual.getSiguiente();
			}
			numlistas--;
		}
		
	}

######################################
############## Insertar ##############
######################################
        
Private  void agregaLista(){
	nodoSkip<T> nuevo1=new nodoSkip(), nuevo2 = new nodoSkip();
	cabeza.setArriba(nuevo1);
	nuevo1.setAbajo(cabeza)
	cola.setArriba(nuevo2);
	nuevo2.setAbajo(cola);
	cabeza=cabeza.getArriba();
	cola=cola.getArriba();
	cabeza.setDerecha(cola); 
	cola.setIzquierda(cabeza);
	
	numlistas++;

}

Public void inserta( T elem) {
	nodoSkip<T> nuevo= new nodoSkip(elem), actual, temp;
	Int numVolados=1;
	actual=busca(elem);
temp = actual.getDer();
	actual.setDer(nuevo);
	nuevo.setDer(temp);
	nuevo.setIzq(actual);
	temp.setIzq(nuevo);
	cont++;
	while(Math.random()>0.5 && numVolados<=floor(log(2+cont)/log(2))){
		numVolados++;
		If (numVolados> numListas)
			agregaLista();
			
		while(actual.getArriba() == null){
			Actual = actual.getIzq();
}
Actual = actual.getArriba();
nuevo.setArriba(new nodoSkip(elem));
nuevo.getArriba().setAbajo(nuevo);
nuevo= nuevo.getArriba();
Temp = actual.getDer();
	actual.setDer(nuevo);
	nuevo.setDer(temp);
	nuevo.setIzq(actual);
	temp.setIzq(nuevo);
	}
}
