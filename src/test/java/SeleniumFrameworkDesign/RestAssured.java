package SeleniumFrameworkDesign;

import io.restassured.response.Response;
import io.restassured.path.json.JsonPath;
import io.restassured.http.ContentType;
import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.greaterThan;
import static io.restassured.RestAssured.given;

class RestAssured {
    public static void main(String[] args) {
        System.out.println("This is a test for RestAssured API testing.");

  /*      Response response = RestAssured
                .get("https://reqres.in/api/users?page=2");
        System.out.println(response.getStatusCode());

*/



                io.restassured.RestAssured.baseURI = "https://jsonplaceholder.typicode.com";

                // GET with query param
                Response getResponse =
                        given()
                                .log().all()
                                .queryParam("postId", 1)
                                .when()
                                .get("/comments")
                                .then()
                                .log().all()
                                .statusCode(200)
                                .contentType(ContentType.JSON)
                                .body("size()", greaterThan(0))
                                .extract().response();

                System.out.println("GET response body:");
                getResponse.prettyPrint();

                // GET with path param
                Response singlePost =
                        given()
                                .log().all()
                                .pathParam("id", 1)
                                .when()
                                .get("/posts/{id}")
                                .then()
                                .statusCode(200)
                                .extract().response();

                System.out.println("Single post title: " + singlePost.jsonPath().getString("title"));

                // POST
                String postBody = "{\n" +
                        "  \"title\": \"foo\",\n" +
                        "  \"body\": \"bar\",\n" +
                        "  \"userId\": 1\n" +
                        "}";

                Response postResponse =
                        given()
                                .log().all()
                                .contentType(ContentType.JSON)
                                .header("Accept", "application/json")
                                .body(postBody)
                                .when()
                                .post("/posts")
                                .then()
                                .log().all()
                                .statusCode(201)
                                .body("title", equalTo("foo"))
                                .extract().response();

                System.out.println("POST response:");
                postResponse.prettyPrint();

                // PUT
                String putBody = "{\n" +
                        "  \"id\": 1,\n" +
                        "  \"title\": \"updated title\",\n" +
                        "  \"body\": \"updated body\",\n" +
                        "  \"userId\": 1\n" +
                        "}";

                Response putResponse =
                        given()
                                .log().all()
                                .contentType(ContentType.JSON)
                                .body(putBody)
                                .when()
                                .put("/posts/1")
                                .then()
                                .statusCode(200)
                                .extract().response();

                System.out.println("PUT response:");
                putResponse.prettyPrint();

                // PATCH
                String patchBody = "{\n" +
                        "  \"title\": \"patched title\"\n" +
                        "}";

                Response patchResponse =
                        given()
                                .log().all()
                                .contentType(ContentType.JSON)
                                .body(patchBody)
                                .when()
                                .patch("/posts/1")
                                .then()
                                .statusCode(200)
                                .extract().response();

                System.out.println("PATCH response:");
                patchResponse.prettyPrint();

                // DELETE
                Response deleteResponse =
                        given()
                                .log().all()
                                .when()
                                .delete("/posts/1")
                                .then()
                                .statusCode(200)
                                .extract().response();

                System.out.println("DELETE response:");
                deleteResponse.prettyPrint();

                // Extract JSON values
                JsonPath json = getResponse.jsonPath();
                int firstId = json.getInt("[0].id");
                System.out.println("First comment id: " + firstId);
            }
}
