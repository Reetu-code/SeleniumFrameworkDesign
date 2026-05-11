package SeleniumFrameworkDesign;

import java.awt.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Stream;

public class ArrayToStream {

    public static void main(String[] args) {
        System.out.println("This is a test for converting an array to a stream.");
        ArrayList<String> names = new ArrayList<>();
        names.add("Ritu");
        names.add("Kumar");
        names.add("Selenium");
        names.add("Java");
        names.add("Reyansh");
        names.add("Rome");

        int count = 0;

        for(int i=0; i<names.size();i++){
            String actual = names.get(i);
            if(actual.startsWith("R")){
                count++;
            }
        }
        System.out.println(count);

        System.out.println("Now Stream is used to count the names starting with R");

        // same code using stream
        long d = Stream.of("Ritu", "Kumar", "Selenium", "Java", "Reyansh", "Rome").filter(name -> name.startsWith("R")).count();

        names.stream().filter(name -> name.startsWith("R")).forEach(System.out::println);
   /*    long c =  names.stream().filter(name -> name.startsWith("R")).count();
        System.out.println(c);
*/
// creating same test with map and filter
        Stream.of("Ritu", "Kumar", "Selenium", "Java", "Reyansh", "Rome").filter(name -> name.startsWith("R")).map(name -> name.toUpperCase()).forEach(System.out::println);

        // converting array to List and using it in stream
  List<String> name1 = Arrays.asList("Rekha", "Kumaran", "Sel", "Jeevan", "Reyanshi", "Roming");

  name1.stream().sorted().map(name -> name.toUpperCase()).forEach(System.out::println);

  // merging two arrays in one and sorting and printing
  Stream<String> newStream = Stream.concat(names.stream() , name1.stream());
  newStream.sorted().forEach(System.out::println);



    }



}
