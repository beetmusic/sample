/*object high1{
	def math(x:Double,y:Double, f:(Double,Double)=>Double): Double = f(x,y);
	
	def main(args: Array[String]){
		val result = math(50,20,(x,y)=>x+y);
		println(result);
	}
}*/
object high1{
	def math(x:Double,y:Double, f:(Double,Double)=>Double): Double = f(x,y);
	
	def main(args: Array[String]){
		val result = math(50,20,_+_);
		println(result);
	}
}
