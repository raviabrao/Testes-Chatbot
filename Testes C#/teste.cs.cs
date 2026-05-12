using System.Runtime.CompilerServices;
using Microsoft.VisualBasic;

int num1, num2;
string operacao;

Console.WriteLine("Insira o primeiro número a seguir: ");

num1 = Convert.ToInt32(Console.ReadLine());

// declaramos que a variável num1 é do tipo inteiro, e ela vai receber o valor
// digitado pelo usuário através do Console.ReadLine(), que além de ler a entreada,
// também converte o valor para de string para inteiro, usando o Convert.ToInt32().

Console.WriteLine("Insira o segundo número a seguir: ");

num2 = Convert.ToInt32(Console.ReadLine());

Console.WriteLine("Qual operação deseja realizar? \n\n1)Soma \n2)Subtração \n3)Multiplicação \n4)Divisão");

operacao = Console.ReadLine();

if (operacao == "1") 
{
    Console.WriteLine($"A soma de {num1} e {num2} é qeuivalente a: {num1 +num2}");
}
else if (operacao == "2") 
{
    Console.WriteLine($"A subtração de {num1} e {num2} é equivalente a: {num1 - num2}");
}
else if (operacao == "3") 
{
    Console.WriteLine($"A multiplicação de {num1} e {num2} é equivalente a: {num1 *num2}");
}
else if (operacao == "4") 
{
    Console.WriteLine($"A divisão de {num1} e {num2} e equivalente a: {num1 / num2}");
}
else
{
    Console.WriteLine("Opção inválida, tente novamente. ");
}