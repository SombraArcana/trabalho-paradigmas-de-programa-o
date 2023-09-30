public class aula{
    Scanner teclado = new Scanner(System.in);
    System.out.print("Entre com valor do salário");
    double salario = teclado.nextDouble():
    if(salario < 1250){
        salario = salario * 1.10;
    }
    else {
        salario = salario * 1.15;
    }
    System.out.println("o valor do salário agora é:" + salario);
    teclado.close();
}