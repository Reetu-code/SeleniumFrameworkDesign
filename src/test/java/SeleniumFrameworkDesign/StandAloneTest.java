package SeleniumFrameworkDesign;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;

import java.time.Duration;
import java.util.List;

public class StandAloneTest {
    public static void main(String[] args) {


        String productName = "ZARA COAT 3";
        System.out.println("This is a standalone test.");

        WebDriver driver =  new ChromeDriver();
        driver.get("https://rahulshettyacademy.com/client");

        driver.manage().window().maximize();
        driver.manage().timeouts().implicitlyWait(java.time.Duration.ofSeconds(10));

        System.out.println( driver.getTitle());

        driver.findElement(By.id("userEmail")).sendKeys("RITUKUMARITECH@GMAIL.COM");
        driver.findElement(By.id("userPassword")).sendKeys("Reetu@123");
        driver.findElement(By.id("login")).click();


        List<WebElement> products = driver.findElements(By.cssSelector(".mb-3"));

        for (WebElement product : products) {
            System.out.println(product.findElement(By.cssSelector("h5")).getText());
        }

        WebElement prod = products.stream().filter(product-> product.findElement(By.cssSelector("h5")).getText().
                        equalsIgnoreCase(productName)).
                findFirst().orElse(null);

        if (prod != null) {
            prod.findElement(By.xpath("//div[@class='row']//div[2]//div[1]//div[1]//button[2]")).click();
            System.out.println("Added ZARA COAT 3 to cart");
        } else {
            System.out.println("Product not found");
        }

// System.out.println(prod);

        WebDriverWait wait =    new WebDriverWait(driver, Duration.ofSeconds(10));
        wait.until(ExpectedConditions.visibilityOfAllElementsLocatedBy(By.cssSelector("#toast-container")));

        // Wait for the loading spinner to disappear
        wait.until(ExpectedConditions.invisibilityOfElementLocated(By.cssSelector(".ngx-spinner-overlay")));

        driver.findElement(By.cssSelector(".btn.btn-custom[routerlink='/dashboard/cart']")).click();

       List<WebElement> cartProducts = driver.findElements(By.cssSelector(".cartSection h3"));
        boolean match = cartProducts.stream().anyMatch(cartProduct -> cartProduct.getText().equalsIgnoreCase(productName));

       System.out.println(match);

        Assert.assertTrue(match);

        driver.findElement(By.cssSelector(".totalRow button")).click();
        //List<WebElement> countryOptions = driver.findElements(By.cssSelector(".ta-results button"));

        driver.findElement(By.cssSelector("input[placeholder='Select Country']")).sendKeys("United States");
        wait.until(ExpectedConditions.visibilityOfAllElementsLocatedBy(By.cssSelector(".ta-results button")));
        driver.findElement(By.cssSelector(".ta-results button")).click();

        driver.findElement(By.cssSelector(".action__submit")).click();
            String orderConfirmationMessage = driver.findElement(By.cssSelector(".hero-primary")).getText();

            Assert.assertEquals (orderConfirmationMessage,"THANKYOU FOR THE ORDER." );


 driver.quit();
            }


        }
