Public class minHeap<T> implements minheapADT<T>{

	Comparable<T> datos[];
	Int cont;
	//hacer el constructor y el expande
	Public void inserta(T elem){
		If (cont+1>=datos.length-1)
			expande();
		cont++;
		datos[cont]=elem;
		//ahora vamos a heapificar
		actual=cont;
		papa=cont>>1;
//CompareTo 
		while(papa!=0  && datos[actual].compareTo(datos[papa])<0){
			Comparable temp = datos[papa];
			datos[papa] = datos[actual];
			datos[actual] = temp;

			actual = papa;
			papa  >>= 1// es lo mismo que papa=papa>>1
}




Notas para borrar:
Casos de terminación
Ya no tiene hijos
Los hijos son mayores que yo
Aguas que puede ser que sólo tenga un hijo



Public T borraMin(){
	Int izq,der,min;
	If (cont<1)
		Throw new elementNOtFound();
	T res=datos[1];
	datos[1]=datos[cont--];
	actual=1;
	while(!termine){
		izq=actual<<1;//lo mismo que actual*2
		der=izq+1;//lo mismo que actual*2+1
		if(izq>cont) //si no tiene hijo izquierdo
			termine=true;
		else{//si tiene hijo izq
			min=izq;
			if(der>cont)
				termine=true
			else//tiene los dos hijos
				If (datos[der] < datos[izq])
					min=der
			if(!termine){
				T temp=datos[actual];
				datos[actual]=datos[min];
				datos[min]=temp;
				actual = min;
			}
				
		}//else	

	}//while


}
