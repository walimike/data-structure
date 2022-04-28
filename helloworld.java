public class HelloWorld {
    public static void main(string[], args){
// these are premitive data types
    int a = 5;
    long c = 400000;
    char g = 'edward';

    // Non premitive
    String name = "susan";
    System.out.printIn(name);
    addExclamation("Hello world")
    }

    // Creating methods
    public static void addExclamation(String s){
        System.out.printIn(s + '!');
    }

    // Java is a real Object oriented language
    //Creating an objects:
    Animal a = new Animal();
    String dog = a.iAmADog();

    public class Animal{
        public static String iAmADog(){
            return "I am a dog";
        }
    }
    //use void if u do not want to return a thing
}