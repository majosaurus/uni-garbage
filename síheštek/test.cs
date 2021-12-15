/*
 * Created by SharpDevelop.
 * User: martina.koutova
 * Date: 15-Dec-21
 * Time: 10:32
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;

namespace test
{
	class Program
	{
		public static void Main(string[] args)
		{
			//Hello world
			Console.WriteLine("Hello World!");
			string aFriend = "Bill";
			Console.WriteLine("Hello " + aFriend);
			//Console.WriteLine($"Hello {aFriend}" + aFriend); - C# 6 version and newer
			
			//Other data types
			double radius = 2.5;
			double area = (radius * radius) * Math.PI;
			Console.WriteLine(area);
			
			//If statements 
			int a = 5;
			int b = 6;
			if (a + b > 10)
			{
				Console.WriteLine("The answer is greater than 10.");
			}
			else
			{
				Console.WriteLine("The answer is not greater than 10.");
			}
			
			//While
			int counter = 0;
			while (counter < 10)
			{
				Console.WriteLine(counter);
				counter++;
			}
			
			//Do while
			int counter2 = 1;
			do
			{
				Console.WriteLine(counter2);
				counter2++;
			} while (counter2 < 11);
			
			//For
			for(int counter3 = 2; counter3 < 12; counter3++)
			{
  				Console.WriteLine(counter3);
			}
			
			int result = 0;
			for (int counter4 = 1; counter4 < 21; counter4++)
			{
    			if (counter4 % 3 == 0)
    			{
        			result += counter4;
    			}
			}
			Console.WriteLine(result);
			
			//Lists
			var names = new List<string> { "Maja", "Ana", "Felipe" };
			foreach (var name in names)
			{
  				Console.WriteLine($"Hello {name.ToUpper()}!");
			}
			
			//Fibonacci for cycle
			var fibonacciNumbers = new List<int> {1, 1};
			for(int fibcounter = 0; fibcounter < 18; fibcounter++)
			{
    			var previous = fibonacciNumbers[fibonacciNumbers.Count - 1];
    			var previous2 = fibonacciNumbers[fibonacciNumbers.Count - 2];
    			fibonacciNumbers.Add(previous + previous2);
			}
			foreach(var item in fibonacciNumbers)
    		Console.WriteLine(item);
			
			//Fibonacci while cycle
			var fibonacciNumbers = new List<int> {1, 1};
			while (fibonacciNumbers.Count < 20)
			{
    			var previous = fibonacciNumbers[fibonacciNumbers.Count - 1];
    			var previous2 = fibonacciNumbers[fibonacciNumbers.Count - 2];

    			fibonacciNumbers.Add(previous + previous2);
			}
			foreach(var item in fibonacciNumbers)
    		Console.WriteLine(item);
			
			Console.Write("Press any key to continue . . . ");
			Console.ReadKey(true);
		}
	}
}