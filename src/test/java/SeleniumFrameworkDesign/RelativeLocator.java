package SeleniumFrameworkDesign;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;

import static org.openqa.selenium.support.locators.RelativeLocator.with;

public class RelativeLocator {

    public static void main(String[] args) {
        System.out.println("This is a test for relative locators.");

        WebDriver driver = new ChromeDriver();
        driver.get("https://rahulshettyacademy.com/angularpractice/");
        driver.manage().window().maximize();
        driver.manage().timeouts().implicitlyWait(java.time.Duration.ofSeconds(10));

        WebElement nameField = driver.findElement(By.cssSelector("input[name='name']"));
      System.out.println("Label above name field: " + driver.findElement(with(By.tagName("label")).above(nameField)).getText());

      // Find the email field and use relative locator to find the label below it
      WebElement emailField = driver.findElement(By.cssSelector("label[for='dateofBirth']"));
        System.out.println("Label below email field: " + driver.findElement(with(By.tagName("input")).below(emailField)).getText());

        driver.findElement(with(By.tagName("input")).below(emailField)).click();

     /*   WebElement checkBox = driver.findElement(By.id("exampleCheck1"));
        System.out.println( driver.findElement(with(By.tagName("label")).toLeftOf(checkBox)).getText());

         WebElement submitButton = driver.findElement(By.cssSelector("input[type='submit']"));
        System.out.println( driver.findElement(with(By.tagName("label")).toRightOf(submitButton)).getText()); */

      Assert.assertTrue(driver.findElement(By.cssSelector(".alert.alert-success.alert-dismissible")).getText().contains("Success!"));

    //  Assert.assertEquals(driver.findElement(By.cssSelector(".alert.alert-success.alert-dismissible")).getText(), "Success! The Form has been submitted successfully!.");


     WebElement checkB =  driver.findElement(By.cssSelector("label[for='exampleCheck1']"));
     driver.findElement(with(By.tagName("input")).toLeftOf(checkB)).click();

     WebElement text = driver.findElement(By.id("inlineRadio1"));
     System.out.println(driver.findElement(with(By.tagName("label")).toRightOf(text)).getText());  //label[for='inlineRadio1']
      driver.quit();

      
    }
}
