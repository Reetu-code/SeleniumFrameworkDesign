package SeleniumFrameworkDesign;

import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.apache.commons.io.FileUtils;

import java.io.File;
import java.io.IOException;
import java.util.Set;
import java.util.Iterator;

public class MultiWindowTab {
        public static void main(String[] args) {
            System.out.println("This is a test for handling multiple windows and tabs.");

            WebDriver driver = new ChromeDriver();
            driver.get("https://rahulshettyacademy.com/angularpractice/");
            driver.manage().window().maximize();
            driver.manage().timeouts().implicitlyWait(java.time.Duration.ofSeconds(10));
            driver.switchTo().newWindow(WindowType.TAB);

            Set<String> handels = driver.getWindowHandles();
            Iterator<String> it = handels.iterator();
            String parentId = it.next();
            String childId = it.next();

            driver.switchTo().window(childId);
             driver.get("https://rahulshettyacademy.com/");
             System.out.println("Title of child window: " + driver.getTitle());

            String course =  driver.findElement(By.cssSelector("body > div:nth-child(2) > div:nth-child(4) > main:nth-child(3) > section:nth-child(2) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1) > div:nth-child(1) > h3:nth-child(2)")).getText();

             driver.switchTo().window(parentId);
             System.out.println("Title of parent window: " + driver.getTitle());
            WebElement name =  driver.findElement(By.cssSelector("input[name='name']"));
                                 name.sendKeys(course);
                         File file =   name.getScreenshotAs(OutputType.FILE);
            try {
                FileUtils.copyFile(file, new File("name1.png"));
            } catch (IOException e) {
                e.printStackTrace();
            }

            name.getRect().getDimension().getHeight();
            name.getRect().getDimension().getWidth();
             System.out.println("Height: " + name.getRect().getDimension().getHeight());
             System.out.println("Width: " + name.getRect().getDimension().getWidth());
            System.out.println("class: " + name.getRect().getClass());
             System.out.println("X: " + name.getRect().getX());
             System.out.println("Y: " + name.getRect().getY());
   // driver.quit();
// to get a screenshot of webelement
            /* File file = name.getScreenshotAs(OutputType.FILE);
             driver.quit();
         //   driver.get("https://rahulshettyacademy.com/"); */

        }
}
