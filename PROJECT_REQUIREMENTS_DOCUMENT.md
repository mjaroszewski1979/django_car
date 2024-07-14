## Project Requirements Document for Django Cars

### Unit Tests

#### Check Username View Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The view name must be resolved correctly for the check username URL. | When the URL for checking the username is resolved. | The resolved function should be htmx_views.check_username. | test_check_username_url_is_resolved
The check username view must handle POST requests correctly when the username already exists. | When a POST request is made to the check username URL with an existing username. | The response should have a status code of 200. The response content should be This username already exists. | test_check_username_post_existing_username
The check username view must handle POST requests correctly when the username is new. | When a POST request is made to the check username URL with a new username. | The response should have a status code of 200. The response content should be This username is available. | test_check_username_post_new_username

#### Add Car View Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The view name must be resolved correctly for the add car URL. | When the URL for adding a car is resolved. | The resolved function should be htmx_views.add_car. | test_add_car_url_is_resolved
The add car view must handle POST requests by anonymous users correctly. | When a POST request is made to the add car URL by an anonymous user. | The response should have a status code of 302. | test_add_car_post_anonymous_user
The add car view must handle POST requests by authenticated users correctly. | When a POST request is made to the add car URL by an authenticated user. | The response should have a status code of 200. | The context dictionary should include cars with the newly added car producer audi. The response should use the partials/car_list.html template. | test_add_car_post_authenticated_user

#### Delete Car View Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The view name must be resolved correctly for the delete car URL. | When the URL for deleting a car is resolved. | The resolved function should be htmx_views.delete_car. | test_delete_car_url_is_resolved
The delete car view must handle GET requests by anonymous users correctly. | When a GET request is made to the delete car URL by an anonymous user. | The response should have a status code of 302. | test_delete_car_get_anonymous_user
The delete car view must handle DELETE requests by authenticated users correctly. | When a DELETE request is made to the delete car URL by an authenticated user. The response should have a status code of 200. | The context dictionary should include cars with no cars left. The response should use the partials/car_list.html template. | test_delete_car_get_authenticated_user

#### Search Car View Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The view name must be resolved correctly for the search car URL. | When the URL for searching a car is resolved. | The resolved function should be htmx_views.search_car. | test_search_car_url_is_resolved
The search car view must handle POST requests by anonymous users correctly. | When a POST request is made to the search car URL by an anonymous user. | The response should have a status code of 302. | test_search_car_post_anonymous_user
The search car view must handle POST requests by authenticated users correctly. | When a POST request is made to the search car URL by an authenticated user. | The response should have a status code of 200. The context dictionary should include results with the car producer porshe. The response should use the partials/search_results.html template. | test_search_car_post_authenticated_user

#### Detail Car View Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------


