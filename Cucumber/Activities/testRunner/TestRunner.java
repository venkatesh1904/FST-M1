package testRunner;
import org.junit.runner.RunWith;
import io.cucumber.junit.Cucumber;
import io.cucumber.junit.CucumberOptions;

@RunWith(Cucumber.class)
@CucumberOptions(
        features = "src/test/Feature",
        glue = {"stepDefinition"}
)

public class TestRunner {
    //Nothing is written here

}
