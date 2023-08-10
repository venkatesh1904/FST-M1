package examples;

import io.restassured.RestAssured;
import io.restassured.builder.RequestSpecBuilder;
import io.restassured.builder.ResponseSpecBuilder;
import io.restassured.response.Response;
import io.restassured.specification.RequestSpecification;
import io.restassured.specification.ResponseSpecification;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import java.util.HashMap;
import java.util.Map;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.lessThanOrEqualTo;

public class SpecificationTest {
    //Specifications
    RequestSpecification requestSpec;
    ResponseSpecification responseSpec;
    private Object petId;

    @BeforeClass
    public void setUp() {
        //Request Specification
        requestSpec = new RequestSpecBuilder()
                .setBaseUri("https://petstore.swagger.io/v2/pet")
                .addHeader("Content-Type","application/json")
                .build();

        //Response Specification
        responseSpec = new ResponseSpecBuilder()
                .expectStatusCode(200)
                .expectResponseTime(lessThanOrEqualTo(3000L))
                .expectBody("status", equalTo("alive"))
                .build();
    }

    @Test(priority = 1)
    public void postRequestTest() {

        Map<String, Object> reqBody = new HashMap<>();
        reqBody.put("id", 77232);
        reqBody.put("name", "Riley");
        reqBody.put("status", "alive");

        //Send POST Request
        Response response = given().spec(requestSpec).body(reqBody).when().post();

        //Extract petId from response
        petId = response.then().extract().path("id");

        //Assertions
        response.then().spec(responseSpec).body("name", equalTo("Riley"));

    }

    @Test(priority = 2)
    public void getRequestTest() {
        //Send GET Request
        given().spec(requestSpec).pathParam("petId", petId).
                when().get("/{petId}").
                then().spec(responseSpec).body("name", equalTo("Riley"));
    }


    @Test(priority = 3)
    public void deleteRequestTest() {
        //Send GET Request
        given().spec(requestSpec).pathParam("petId", petId).
                when().delete("/{petId}").
                then()
                .statusCode(200)
                .time(lessThanOrEqualTo(3000L))
                .body("message", equalTo("" +petId));
    }
}
