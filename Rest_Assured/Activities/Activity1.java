import io.restassured.response.Response;
import static io.restassured.RestAssured.given;
import io.restassured.http.ContentType;
import org.testng.annotations.Test;

import static org.hamcrest.CoreMatchers.equalTo;

public class Activity1 {
    // Set base URL
    final static String ROOT_URI = "https://petstore.swagger.io/v2/pet";

    @Test(priority=1)
    public void addNewPet() {
        // Create JSON request
        String reqBody = "{"
                + "\"id\": 85302,"
                + "\"name\": \"Pluto\","
                + " \"status\": \"alive\""
                + "}";

        Response response =
                given().contentType(ContentType.JSON) // Set headers
                        .body(reqBody) // Add request body
                        .when().post(ROOT_URI); // Send POST request

        // Assertion
        response.then().body("id", equalTo(85302));
        response.then().body("name", equalTo("Pluto"));
        response.then().body("status", equalTo("alive"));
    }

    @Test(priority=2)
    public void getPetInfo() {
        Response response =
                given().contentType(ContentType.JSON) // Set headers
                        .when().pathParam("petId", "85302") // Set path parameter
                        .get(ROOT_URI + "/{petId}"); // Send GET request

        // Assertion
        response.then().body("id", equalTo(85302));
        response.then().body("name", equalTo("Pluto"));
        response.then().body("status", equalTo("alive"));
    }

    @Test(priority=3)
    public void deletePet() {
        Response response =
                given().contentType(ContentType.JSON) // Set headers
                        .when().pathParam("petId", "85302") // Set path parameter
                        .delete(ROOT_URI + "/{petId}"); // Send DELETE request

        // Assertion
        response.then().body("code", equalTo(200));
        response.then().body("message", equalTo("85302"));
    }
}
